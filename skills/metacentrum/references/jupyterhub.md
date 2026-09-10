# JupyterHub (hub.cloud.e-infra.cz)

> Praktická příručka. Zdroj: `raw/cerit/web-apps/jupyterhub.md`
> (CERIT-SC) + `raw/metacentrum/software/sw-list/jupyter.md`.

## Co to je

Multi-user platforma pro Jupyter Notebooky/Lab v e-INFRA CZ, běžící na
Kubernetes (CERIT-SC). URL: **https://hub.cloud.e-infra.cz** — přístup vyžaduje
platné členství v MetaCentru.

## Spuštění serveru

- `My Server` spustí default JupyterLab.
- Vlastní instance: `Add new server` + unikátní krátký popisný název.
- **Můžeš spustit víc instancí najednou** (různé obrazy).

### Výběr obrazu (image)

Poskytované typy: Simple Jupyter, **R** (RStudio), **TensorFlow / PyTorch**,
**Matlab**, folding (Colabfold/ESM Fold), **AI** obrazy (s integrovaným
Claude Code — LLM integrace viz `ai-as-a-service.md`), a vlastní custom obraz.

- Custom obraz: `repo/imagename:tag`, repozitář musí být **veřejný** (lze použít
  interní Harbor registr — `cerit.io`). Musí obsahovat celý jupyter stack —
  stavěj z oficiálních `jupyter/*` obrazů.
- Obrazy s GPU podporou jsou označené `...with GPU...`.

### Storage

- Default: persistentní úložiště v `/home/jovyan` (přežije respawn).
- MetaCentrum home: mountnout `/home/meta/{meta-username}` (jeden home na notebook).
  ⚠️ Vyber storage, kde home **máš** — jinak spawn selže (HTTP 500).

### Resource limity (hard limit)

| Resource | Garance | Max |
|----------|---------|-----|
| CPU | 1 | 32 |
| RAM | 4G | 256G |
| GPU | — | celá karta, nebo MIG (až 4× 10GB / 4× 20GB část A100) |

- Překročení CPU → throttling (zpomalí, nezabije). Překročení RAM → výpočet
  skončí chybou/zarazí se.
- GPU: funguje jen v obrazech s GPU podporou (řidiče atd.); MIG části jsou izolované.

## Automatické mazání neaktivních notebooků

Hodnocení probíhá 1× denně (průměr z 5-min segmentů za 24 h):

- **GPU** požadováno: po 2 dnech s využitím GPU **< 0.005** se instance smaže.
- **Bez GPU**: po 4 dnech s využitím CPU **< 0.1** se smaže.
- Před smazáním přijde e-mail (na preferovanou adresu účtu). Necháš-li to být,
  instance zmizí — ukládej si výsledky jinam.

## Správa

- `File → Hub Control Panel` (nebo `/hub/home`) — stop/delete, přidat server.
- Sdílení notebooku: `Hub Control Panel → Token → Request new API token`,
  přidej `?token=XXX` na URL končící `.../lab`. Token platí pro **všechny** tvé
  notebooky — opatrně. Příjemce musí být odhlášený (incognito).

## Spuštění jobu z notebooku (kubectl)

Náročnější části běž jako Kubernetes `Job` místo v notebooku:
- Nainstaluj `kubectl` do notebooku (curl z dl.k8s.io, `fakeroot` v RStudio obrazech).
- Získej názvy PVC: persistentní home → `kubectl get pvc`; meta home → porovnej
  storage z `df` s PVC končícími `-data-sshfs`.
- Job: image + script + resources + volumeMounts (připoj původní PVC) →
  template viz `kubernetes-rancher.md` (Job YAML).

## Různé

- **SSH do notebooku**: jen přes IPv6 síť (potřebuješ Edu VPN z IPv4 domova);
  obraz `Minimal NB with SSH access`, `ssh jovyan@<adresa>.dyn.cloud.e-infra.cz`;
  přidej svůj veřejný klíč do `/home/jovyan/.ssh/authorized_keys`.
- **Conda**: `conda create -n tenv --yes python=3.8 ipykernel nb_conda_kernels`,
  pak kernel `Kernel → Change Kernel`.
- **Expose lokální app**: `pip install git+https://github.com/CERIT-SC/flare`,
  pak `flare tunnel --port 8888 --name myapp` → `https://myapp.flare.cloud.e-infra.cz`.
- **Chyby**: HTTP 500 → špatně zvolený meta home (nemáš přístup) → přihlaš se
  znovu / zvol vlastní home. `ImagePullBackOff` → chybný název obrazu/repo.
  Spawn timeout 10 min → `Spawn failed: pod/... did not start in 600 seconds!`,
  pak `Relaunch server`.
- Podpora: **k8s@cerit-sc.cz**.

## Alternativa — MetaCentrum SW list Jupyter

Přehled Jupyter nasazení v rámci MetaCentra najdeš v
`raw/metacentrum/software/sw-list/jupyter.md`. Jupyter se dá spouštět i přes
**OnDemand** (`ondemand.md`) jako interaktivní aplikace.
