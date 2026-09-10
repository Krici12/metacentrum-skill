# Struktura repozitáře a pokrytí témat

## Co pokrýváme

Požadovaná témata a kde k nim v repozitáři najdeš syrový i zpracovaný obsah:

| Téma | raw/ (zdroj) | Skill reference |
|------|--------------|-----------------|
| **PBS Pro / qsub / fronty / walltime** | `raw/metacentrum/computing/` (resources, jobs, run-basic-job) | `references/pbs-qsub.md` |
| **Softwarové moduly** (module add/load/avail) | `raw/metacentrum/software/modules.md` | `references/software-modules.md` |
| **GPU uzly** | `raw/metacentrum/computing/gpu-comput/` (gpu-job, dgx, clusters, nvidia) | `references/gpu-nodes.md` |
| **JupyterHub** | `raw/cerit/web-apps/jupyterhub.md` + `raw/metacentrum/software/sw-list/jupyter.md` | `references/jupyterhub.md` |
| **OnDemand** | `raw/metacentrum/graphical/ondemand.md` | `references/ondemand.md` |
| **Kubernetes / Rancher** | `raw/cerit/platform/`, `raw/cerit/rancher/`, `raw/cerit/kubernetes/`, `raw/cerit/docker/` | `references/kubernetes-rancher.md` |
| **Datová úložiště** | `raw/metacentrum/data/` + `raw/cesnet/object-storage-s3/` (S3) | `references/data-storage.md` |
| **Autentizace** (Kerberos, SSH, účet) | `raw/metacentrum/access/` + `raw/einfra-account/access/` | `references/authentication.md` |
| **AI as a Service** (LLM chat/API, MCP, AI coding asistenti, DeepSite/DeepSec/n8n) | `raw/cerit/ai-as-a-service/` | `references/ai-as-a-service.md` |

## Strom repozitáře

```
.
├── README.md
├── SCRAPING.md              # jak re-scrapnout a udržovat
├── STRUCTURE.md             # tento soubor
├── .gitignore
├── raw/                     # syrový scrapnutý obsah (zrcadlo webu)
│   ├── metacentrum/         #   docs.metacentrum.cz
│   │   ├── access/          #     log-in, account, security/kerberos, security/connect-auth
│   │   ├── computing/
│   │   │   ├── infrastructure/  # frontends, storages, scratch, mount-storages
│   │   │   ├── jobs/            # email-notif, extend-walltime, job-arrays, job-tracking...
│   │   │   ├── resources/       # queues, resources, pbs-commands, qsub-compiler, fairshare
│   │   │   ├── gpu-comput/      # gpu-job, dgx, clusters, nvidia
│   │   │   ├── advanced, parallel-comput, run-basic-job, my-metacentrum
│   │   ├── data/            # types-of-storage, quotas, direct-access, large-data, backup
│   │   ├── graphical/       # ondemand, usegalaxy
│   │   └── software/        # modules, install-software, containers, sw-list/jupyter
│   ├── cerit/               # docs.cerit.io
│   │   ├── platform/        # overview, access, hw, technologies
│   │   ├── rancher/         # rancher, quotas, reqproj
│   │   ├── kubernetes/      # kubectl, ns, job, pvc, resources, expose, security
│   │   ├── docker/          # limitations, dockerfile
│   │   ├── ai-as-a-service/ # introduction, ai-api, chat-ai, mcp, llm-integration, deepsite, deepsec, ai-data-privacy, n8n-agents
│   │   └── web-apps/        # jupyterhub, binderhub
│   ├── cesnet/              # docs.du.cesnet.cz (datová úložiště)
│   │   └── object-storage-s3/  # s3-service, aws-cli, s3cmd, rclone, boto3, ...
│   └── einfra-account/      # docs.account.e-infra.cz
│       └── access/          # account, perun, mfa, orcid
├── .claude/skills/metacentrum/
│   ├── SKILL.md
│   └── references/          # praktické příručky (ručně psané z raw/)
│       ├── ai-as-a-service.md  ·  authentication.md  ·  data-storage.md
│       ├── gpu-nodes.md  ·  jupyterhub.md  ·  kubernetes-rancher.md
│       ├── ondemand.md  ·  pbs-qsub.md  ·  software-modules.md
└── scripts/
    ├── scrape.py            # hlavní scraper (MAP url→cesta)
    └── extract.py           # HTML → markdown extraktor
```

## Poznámky k pokrytí

- **PBS**: `resources/queues.md`, `resources/resources.md` a `jobs/*` kompletně
  pokrývají fronty, walltime (vč. `extend-walltime`), příkazy `qsub/qstat/qdel`,
  job arrays a modifikaci atributů.
- **GPU**: `gpu-comput/gpu-job.md` (parametr `ngpus`, `gpu_mem`), `dgx.md`
  (NVIDIA DGX H100), `clusters.md` + `nvidia.md`.
- **Storage**: MetaCentrum lokální disky (types-of-storage, quotas, scratch) +
  CESNET **S3 object storage** (objekty, bucket, aws-cli/s3cmd/rclone/boto3).
- **Auth**: MetaCentrum Kerberos/SSH login + e-INFRA CZ Account (Perun, MFA, ORCID).
- **Kubernetes**: CERIT-SC platforma + Rancher + kubectl/job/pvc/resources/expose/security.

## Co zatím NEpokrýváme (možné rozšíření)

- `docs.it4i.cz` (superpočítače) — jiný poskytovatel, mimo e-INFRA grid.
- `docs.nrp.eosc.cz` (National Data Repositories).
- `docs.platforms.cloud.e-infra.cz` (Compute Cloud / virtualizace).
- `docs.onedata.e-infra.cz` (Onedata).
- Detailní sub-stránky MetaCentrum (fields/chemistry/*, related/collgs/*, Galaxy, atd.)
  — verze pro úplnost lze přidat do `MAP`, když budou potřeba.
