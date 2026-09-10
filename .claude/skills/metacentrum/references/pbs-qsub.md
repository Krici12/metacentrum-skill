# PBS Pro — qsub, fronty, walltime, scratch

> Praktická příručka pro dávkové počítání na MetaCentrum gridu.
> Zdroj: `raw/metacentrum/computing/` (run-basic-job, resources/queues,
> resources/resources, jobs/extend-walltime, jobs/*, infrastructure/scratch-storages).

## Úvod — základní koncept

MetaCentrum = distribuovaný grid Debian clusterů + storage serverů + **frontendů**
(přihlašovací servery). Scheduler je **PBS**. Frontendy jsou sdílené — **nejsou
pro těžké počítání**, jen pro přípravu dat, správu jobů a lehké kompilace.

```
ssh user@tarkil.metacentrum.cz   # přihlašovací frontend (vyber nejbližší umístění)
```

## Základní příkazy PBS

| Příkaz | Význam |
|--------|--------|
| `qsub` | odevzdat job |
| `qstat` | stav jobů (`Q`=queued, `R`=running, `F`=finished) |
| `qdel jobID` | zrušit job |
| `qmove` | přesunout job do jiné fronty |
| `pbsnodes` | stav uzlů a jejich vlastnosti |
| `qextend jobID +walltime` | prodloužit walltime běžícího jobu |
| `qstat -u user` | tvé joby (běžící + frontové) |
| `qstat -x -u user` | tvé joby i skončené |
| `qstat -q` / `qstat -Q` | seznam front a vlastnosti |
| `qstat -fw jobID` | detailní info vč. GPU usage |

> **Kerberos**: od února 2026 všechny PBS příkazy při chybějícím Kerberos
> ticketu vyzvou k zadání hesla (viz `authentication.md`).

## 4 základní zdroje (resources)

| Zdroj | Výchozí | Formát | Poznámka |
|-------|---------|--------|----------|
| `ncpus` | `1` | `ncpus=2` | počet CPU |
| `mem` | `400MB` | `mem=10gb` | velikost RAM |
| `walltime` | `24:00:00` | `hh:mm:ss` | max. délka běhu |
| `scratch_XY` | žádný | `scratch_local=10gb` | scratch dir, **musíš zadat** (typ i velikost) |

Příklad:
```bash
qsub -l select=1:ncpus=1:mem=10gb:scratch_local=100gb -l walltime=1:00:00 script.sh
qsub -I -l select=1:ncpus=1:mem=1gb -l walltime=1:00:00          # interaktivní job
```

## Fronty

- **Výchozí fronta:** `default@pbs-m1.metacentrum.cz` — job jde tam, pokud
  neurčíš jinak; scheduler ho automaticky zařadí podle walltime a počtu GPU.
- Vlastní frontu zadáš `qsub -q <název_fronty>`.

Důležité specifické fronty:

| Fronta | Použití |
|--------|---------|
| `elixircz@pbs-m1.metacentrum.cz` | hardware vyhrazený členům ELIXIR |
| `gpu_dgx@pbs-m1.metacentrum.cz` | joby ≥4 GPU s NVLink (`dgx`) |
| `uv18@pbs-m1.metacentrum.cz` | joby >100 CPU NEBO >500 GB RAM |
| `gpu_long` | dlouhé výpočty na GPU (v příkladu max walltime 336:00:00, vyžaduje ≥1 GPU) |

Info o frontách:
```bash
qstat -q                 # list front
qstat -Q -f gpu_long@pbs-m1.metacentrum.cz   # detail vybrané fronty
qsub -q queue@server     # konkrétní server
qsub -q @server          # výchozí fronta na daném serveru
```

## Walltime a jeho prodloužení

- Formát `hh:mm:ss`, maximum závisí na frontě (některé GPU fronty až `336:00:00` = 14 dní).
- Prodloužení běžícího jobu: `qextend jobID 01:00:00`
- `qextend` má **kvótu**: max **20× za 30 dní** A celkem **1440 CPU-hodin za 30 dní**.
  - CPU-hodiny ≠ walltime hodiny: prodloužíš-li job na 8 CPU o 1 h, ubere se 8 CPU-hodin.
  - Stav fondu: `qextend info`
  - Celek nad kvótu: domluv se s podporou `meta@cesnet.cz`. Array joby `qextend` neprodlouží.

## Scratch úložiště

Scratch je dočasné úložiště pro běh jobu. **Není výchozí** — pro batch job musíš
zadat typ i velikost. Lokace je v proměnné `$SCRATCHDIR`.

| Typ | PBS resource | Poznámka |
|-----|--------------|----------|
| Lokální disk | `scratch_local=10gb` | na každém uzlu, `/scratch/USER/job_JOBID` — výchozí volba |
| SSD | `scratch_ssd=1gb` | ultra rychlý, menší, ne na všech uzlech `/scratch.ssd/...` |
| Sdílený | `scratch_shared=10gb` | síťový, sdílený mezi uzly clusteru `/scratch.shared/...` |
| V RAM | `scratch_shm=true` | nejrychlejší, data nepřežijí konec jobu, max = velikost `mem` |
| Multijob (v přípravě) | `multijob=brno` / `multijob=plzen` | **perzistentní** napříč joby, `/scratch.multijob-[brno\|plzen]/USER/`, jen některé uzly |

> `scratch_shm` je boolean — velikost je určena parametrem `mem` (pamatuj na to).

- `SCRATCHDIR` **není zapisovatelný** — čistí se jen obsah: `rm -rf $SCRATCHDIR/*`.
- Job by si měl scratch uklidit sám (`clean_scratch`); jinak se automaticky smaže
  zhruba po **14 dnech** (dříve při nedostatku místa).
- BeeGFS paralelní FS: `scratch_shared` + `cl_bee=True`, vhodné pro velké/početné
  soubory, paralelní I/O, joby přes více uzlů, array joby s mezivýsledky
  (přístupné i jako `scratch.multijob-brno`).
- **Multijob scratch** (uvádí se v září/říjnu 2026): perzistentní scratch pro
  navazující nezávislé joby nad stejnými daty — odpadá opakované kopírování
  velkých dat na začátku/konci každého jobu. Fast varianta (`multijob=[brno|plzen]`)
  + chystaná globální (pomalá) varianta.

## Ukázkový batch skript (template)

```bash
#!/bin/bash
#PBS -l walltime=0:30:00
#PBS -l select=1:ncpus=1:mem=1gb:scratch_local=1gb
#PBS -N my_job

module load python          # načti moduly

cp ${PBS_O_WORKDIR}/input.txt $SCRATCHDIR
cd $SCRATCHDIR
python my_script.py input.txt output.txt

cp output.txt ${PBS_O_WORKDIR}/
clean_scratch                # uklid
```

Odevzdání a sledování:
```bash
qsub test.sh                # -> 18411451.pbs-m1.metacentrum.cz
qstat -xu user
qdel 18411451.pbs-m1.metacentrum.cz
```

Výstup: `jobname.o<jobID>` (STDOUT) a `jobname.e<jobID>` (STDERR — čti nejdřív při chybě)
v adresáři, odkud se job odevzdával (`$PBS_O_WORKDIR`).

## Další užitečné resources (výběr)

```bash
# konkrétní CPU vendor / výkon
-l select=1:ncpus=1:cpu_vendor=amd
-l select=1:ncpus=1:spec=4.8          # třída výkonu SPEC CPU2017

# OS / cluster / lokalita
-l select=1:ncpus=1:os=debian11
-l select=1:ncpus=1:cluster=halmir    # nebo cl_halmir=True / False
-l select=1:ncpus=1:brno=True         # fyzická lokalita (brno, praha, plzen, ...)

# MPI / OpenMP
-l select=3:ncpus=2:mpiprocs=2        # 6 MPI procesů, 2 sdílejí 1 vnode

# licence
-l matlab=1

# vlastní cesty pro výstup
-o /custom/path/out   -e /custom/path/err
```

Pozn.: v PBS jde každý resource zadat jen jednou — pro vyloučení více clusterů
použij `cl_adan=False:cl_halmir=False`, ne opakovaný `cluster=^...`.

## Související témata

- GPU joby → `gpu-nodes.md`
- Moduly → `software-modules.md`
- Prodloužení/konec jobů: `raw/metacentrum/computing/jobs/`
- Interaktivní/grafické aplikace → OnDemand `ondemand.md`
