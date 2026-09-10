# GPU uzly (MetaCentrum PBS)

> Praktická příručka. Zdroj: `raw/metacentrum/computing/gpu-comput/`
> (gpu-job.md, dgx.md, clusters.md, nvidia.md).

## Jak spustit GPU job

Stačí zadat **počet GPU karet** — scheduler job automaticky přesměruje do GPU fronty:

```bash
qsub -l select=1:ncpus=1:ngpus=2 ...
```

## GPU-related PBS resources

| Resource | Význam | Příklad |
|----------|--------|---------|
| `ngpus` | počet GPU karet (default `0`) | `select=1:ncpus=1:ngpus=1` |
| `gpu_mem` | **min.** paměť GPU karty | `select=1:ncpus=1:ngpus=1:gpu_mem=10gb` |
| `gpu_cap` | CUDA compute capability / architektura | viz níže |
| `cuda_version` | verze CUDA | `cuda_version=11.0` |

### Architektura GPU (`gpu_cap`)

- `gpu_cap=compute_70` → min. 7.0 architektura (dá 7.0–7.5 i 8.0, 9.0…)
- `gpu_cap=sm_72` → min. verze 7.2 v rámci architektury “Volta” (7.2–7.5, ne 8.0+)
- Lze kombinovat čárkově — **čárka = OR**:

```bash
qsub -l select=1:ngpus=1:gpu_cap="sm_65,compute_70":mem=4gb -l walltime=1:00:00
qsub -l 'select=1:ngpus=1:gpu_cap="sm_65,compute_70":mem=4gb' -l walltime=1:00:00
```

> Uvozovky kolem `gpu_cap` chraň před shellem (escape nebo celý `qsub` do single quotes).

## Systémové proměnné

- `CUDA_VISIBLE_DEVICES` — ID přidělených GPU karet. Pozor: CUDA nástroje je
  přemapují na virtuální ID 0,1,... (tj. hodnota `2,3` → CUDA vidí `0,1`).

## Monitoring využití GPU (po jobu)

```bash
qstat -fw job_ID | grep gpu
# resources_used.gpupercent      = 332   # souhrn využití GPU v % (může být >100, max 100*ngpus)
# resources_used.gpupowerusage   = 38.7  # energie na všech GPU [Wh]
# resources_used.gpumemmaxpercent= 149   # max špička GPU paměti v %
```

## GPU fronty a speciality

- Job s `ngpus>=1` sám zamíří do GPU fronty.
- `gpu_dgx@pbs-m1.metacentrum.cz` — joby vyžadující **≥4 GPU s NVLink** (NVIDIA DGX H100).
  Detaily viz `raw/metacentrum/computing/gpu-comput/dgx.md`.
- Skupina **iti** (Ústav teoretické informatiky ZČU) má vlastní GPU cluster
  `konos` — přímý odesílání do fronty `iti@pbs-m1.metacentrum.cz`.
- Přehled GPU uzlů a specifikací: `raw/metacentrum/computing/gpu-comput/clusters.md`
  a `nvidia.md`. Aktuální seznam front: https://my.metacentrum.cz/queues

## Související

- Základní resources (`mem`, `walltime`, `ncpus`) → `pbs-qsub.md`.
- GPU na Kubernetes/CERIT-SC (MIG, nodeSelector) → `kubernetes-rancher.md`.
