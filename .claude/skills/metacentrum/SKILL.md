---
name: metacentrum
description: >-
  Use when the user asks about Metacentrum, e-INFRA CZ, PBS job, qsub,
  batching, compute queues, walltime, softwarové moduly, module add/load,
  JupyterHub, Kubernetes Metacentrum, Rancher, GPU uzly, Kerberos login,
  SSH frontend, or datová úložiště S3. Covers practical specs, commands and limits.
---

# Metacentrum / e-INFRA CZ

Praktická referenční příručka pro práci s infrastrukturou **MetaCentrum** a
**e-INFRA CZ** (dávkové počítání PBS, moduly, GPU, JupyterHub, Kubernetes,
úložiště, autentizace). Obsah je kondenzací oficiální dokumentace.

## Kde najít co

| Téma | Soubor |
|------|--------|
| PBS Pro: qsub, fronty, walltime, příkazy, scratch | [`references/pbs-qsub.md`](references/pbs-qsub.md) |
| Softwarové moduly (`module add/load` atd.) | [`references/software-modules.md`](references/software-modules.md) |
| GPU uzly (PBS `ngpus`, DGX, MIG) | [`references/gpu-nodes.md`](references/gpu-nodes.md) |
| JupyterHub (hub.cloud.e-infra.cz) | [`references/jupyterhub.md`](references/jupyterhub.md) |
| Open OnDemand (webové rozhraní) | [`references/ondemand.md`](references/ondemand.md) |
| Kubernetes / Rancher (CERIT-SC) | [`references/kubernetes-rancher.md`](references/kubernetes-rancher.md) |
| Datová úložiště (home, scratch, S3 object storage) | [`references/data-storage.md`](references/data-storage.md) |
| Autentizace: Kerberos, SSH, e-INFRA CZ účet (Perun, MFA) | [`references/authentication.md`](references/authentication.md) |
| AI as a Service (LLM API, chat, AI coding asistenti) | [`references/ai-as-a-service.md`](references/ai-as-a-service.md) |

## Často hledané zkratky

- **PBS** = Portable Batch System → scheduler na MetaCentrum gridu.
- **Frontend** = přihlašovací server (`ssh user@tarkil.metacentrum.cz`, atd.).
- **qsub** = odevzdání jobu; **qstat** = stav; **qdel** = zrušení.
- **Moduly** = `module avail/load/add/list/unload/purge`.
- **JupyterHub** = `hub.cloud.e-infra.cz`; **OnDemand** = `ondemand.metacentrum.cz`.
- **Kubernetes** = CERIT-SC platforma řízená Rancherem (`hub.cloud.e-infra.cz`).
- **S3** = objektové úložiště CESNET (`docs.du.cesnet.cz`).
- **AIaaS** = on-premise LLM platforma e-INFRA CZ (`llm.ai.e-infra.cz`,
  `chat.ai.e-infra.cz`) — OpenAI-kompatibilní API, chat, AI coding asistenti.

Zdrojový materiál: `raw/` v kořeni repozitáře (syrový scrap oficiální dokumentace).
Pro detaily vždy ověř aktuální čísla (walltime limity, kvóty, fronty) v `references/`
a `raw/`, protože se mění.
