# Softwarové moduly (module system)

> Praktická příručka. Zdroj: `raw/metacentrum/software/modules.md`
> + `software/install-software.md`, `software/containers.md`, `software/sw-list/jupyter.md`.

## Princip

Všechny aplikace v MetaCentru jsou zabalené do **modulů**. Modul nastaví správné
prostředí (PATH, LD_LIBRARY_PATH, závislosti). **Software musíš nejdřív
načíst modulem** — jinak příkaz nenajdeš.

## Hledání modulů

```bash
module avail                 # všechny dostupné (bez verzí) — dlouhé, mezerník = posun
module avail intel           # vše začínající na "intel"
module avail *intel*         # wildcard doprostřed
module avail intelcdk/       # verze v adresáři modulu (koncové "/" je důležité)
module avail intelcdk --indepth   # všechny + podrobněji
module avail intelcdk -a          # + aliasy
```

## Načítání a odebírání

```bash
module load intelcdk             # default verze (obvykle nejnovější/nejstabilnější)
module add intelcdk              # totéž
module load intelcdk/17.1        # konkrétní verze

module unload matlab/9.9         # odeber (aliasy: module del / module rm)
module purge                     # odeber VŠE
module list                      # co je načteno
module display intelcdk/17.1     # detail: nastavované proměnné
```

> **`module purge` odstraní i `metabase/1`** (automaticky načtený modul, který
> zpřístupňuje utility jako `qextend`, `clean_scratch`, `check-local-quota`).
> Po purgu se doporučuje znovu: `module purge && module add metabase/1`.

### Klíčové proměnné nastavované moduly

- `PATH` — cesta k binárce (povinná)
- `LD_LIBRARY_PATH` — knihovny pro linker
- `LIBRARY_PATH` — knihovny

## Konflikty mezi moduly

Načítání mnoha modulů najednou může konfliktovat (např. dvě verze Pythonu).
Pokud konflikt nastane, **omezte rozsah modulu na subshell** — závorky vytvoří
subshell, po jeho ukončení se modul automaticky odebere:

```bash
(module add python/3.8.0-gcc; python)      # po skončení subshellu modul pryč
(module add python/3.8.0-gcc-rab6t; python)
```

Chyba konfliktu (typická):
```
ERROR:150: Module '...' conflicts with the currently loaded module(s) '...'
```

## Verze a varianty

Modulů je víc kopií lišících se verzí, kompilátorem a funkcemi. Příklad TensorFlow:
`tensorflow/1.3.0-cpu`, `tensorflow/1.5.0-gpu-python3`, ... → vždy **zvol variantu
`gpu`** pro GPU výpočty.

## Modulefile (jak se modul definuje)

Textový soubor v adresářích z `$MODULEPATH`:
```tcl
#%Module1.0
set basedir /software/gsl/1.16/gcc
prepend-path PATH ${basedir}/bin
prepend-path LD_LIBRARY_PATH ${basedir}/lib
```

- Podporované moduly se dodávají i přes **containery** (Singularity/Apptainer)
  — viz `raw/metacentrum/software/containers.md`.
- Vlastní software si můžeš nainstalovat do domovského adresáře; pro
  nestandardní instalaci nastav `$MODULEPATH` odpovídajícím způsobem.

## Související

- Spuštění jobu s moduly → `pbs-qsub.md` (template skriptu s `module load`).
- Python/R/Matlab konkrétně: `raw/metacentrum/software/fields/*` a `sw-list/jupyter.md`.
