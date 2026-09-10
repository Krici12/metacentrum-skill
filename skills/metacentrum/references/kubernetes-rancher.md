# Kubernetes / Rancher (CERIT-SC)

> Praktická příručka. Zdroj: `raw/cerit/platform/`, `raw/cerit/rancher/`,
> `raw/cerit/kubernetes/`, `raw/cerit/docker/`.

## Co to je

CERIT-SC provozuje Kubernetes platformu řízenou **Rancher GUI**. Slouží pro
kontejnerové úlohy (vedle PBS gridu). Dokumentace: `docs.cerit.io` →
`raw/cerit/`.

## Hardware (zkráceně)

- **kuba-cluster** (veřejný, největší, ~39 uzlů): GPU mj. NVIDIA A40, A10, A100
  (80GB), H100; uzly 512GB–1.5TB RAM; 500 TB all-flash síťové úložiště (IBM
  Spectrum Scale / NFSv3); denní snapshoty, obnova až 14 dní zpět.
- **kubh-cluster** (HA, 6 uzlů ve 3 lokalitách Brna): topologie `cerit.io/region`
  (`botanicka`, `komenskeho`, `kampus`); úložiště jen lokální, **bez zálohy**.
- **kubas-cluster** (secure/sensitive): GPU A40/A100/P100/H100; 1700 TB úložiště
  se zálohou na jiné místo.

Aktuální detaily si ověř v `raw/cerit/platform/hw.md` (počty uzlů se mění).

## První kroky

- Přihlas se do Rancher GUI — automaticky se vytvoří **Personal Project** a
  **Namespace**. Namespace vidíš pod `Project/Namespaces`.
- **Nové namespacy vytvářej v Rancher GUI** (`Create Namespace`), ne přes
  `kubectl` — kubectl-namespacy nebudou napojené na tvůj Project.
- Vyhni se obecným názvům jako `test`.

### kubectl

```bash
# stáhni kubeconfig z Rancher dashboardu, ulož do $HOME/.kube/config, chmod 700
chmod 700 $HOME/.kube/config
kubectl get pods
kubectl get ns
kubectl get pvc
```

## Resources (requests/limits)

- **CPU**: celé jednotky (`2`) nebo milli (`100m` = 0.1 CPU).
- **Memory**: `1Gi` = 1 GB; zahrnuje i `/dev/shm` a memory `emptyDir` volumy.
- **GPU**: celá karta `nvidia.com/gpu: 1`, nebo MIG část `nvidia.com/mig-1g.10gb: x`
  (10 GB) / `nvidia.com/mig-2g.20gb: x` (20 GB).
- Specifický GPU typ: `nodeSelector: nvidia.com/gpu.product: 'NVIDIA-A40'`
  (hodnoty: `NVIDIA-A10`, `NVIDIA-A100-80GB-PCIe`, `NVIDIA-A40`,
  `NVIDIA-H100-PCIe`, `NVIDIA-L4`).
- Min. GPU paměť: `nodeAffinity` s `operator: Gt` na `nvidia.com/gpu.memory`
  (hodnota jako **string** `'80000'`).
- **Zvýšení /dev/shm** (64 MB default, málo pro GPU/GUI): mount memory volume:

```yaml
volumes:
- name: dshm
  emptyDir: { medium: Memory, sizeLimit: 1Gi }
volumeMounts:
- name: dshm
  mountPath: /dev/shm
```

- POZOR: žádost must být ≤ kapacita **jednoho uzlu** (1000 CPU nikdy neprojde);
  requests/limits: mezi requests a limit přes nejsou garantované → eviction/throttle.

## Job (batch úloha)

Zjednodušený template (bezpečnostní kontext je nutný):

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: secure-job-name
spec:
  template:
    metadata:
      labels: { app: secure-job }
    spec:
      securityContext:
        fsGroupChangePolicy: OnRootMismatch
        runAsNonRoot: true
        seccompProfile: { type: RuntimeDefault }
      containers:
      - name: secure-container
        image: nginx:latest
        securityContext:
          allowPrivilegeEscalation: false
          capabilities: { drop: ["ALL"] }
          runAsUser: 1000
        resources:
          requests: { memory: "128Mi", cpu: "250m" }
          limits:   { memory: "256Mi", cpu: "500m" }
        volumeMounts:
        - name: config-volume
          mountPath: /etc/config
          readOnly: true
      restartPolicy: Never
      volumes:
      - name: config-volume
        configMap: { name: example-configmap }
```

Detaily: `runAsUser` dle obrazu, `restartPolicy` `Never`/`OnFailure`, labely
doporučené (síťové policy/monitoring je používají). Spustit: `kubectl apply -f job.yaml`.

## Další

- **Containery/Dockerfile**: `raw/cerit/docker/dockerfile.md` a `limitations.md`.
- **Expose služby**, security, certificates: `raw/cerit/kubernetes/expose.md`,
  `security.md`, `certificates.md`.
- **Persistent storage (PVC)**: `raw/cerit/kubernetes/pvc.md`.
- Rancher kvóty a žádost o projekt: `raw/cerit/rancher/quotas.md`, `reqproj.md`.
- Workflows (Argo, Nextflow, Snakemake, TES/WES): `raw/cerit/workflows/`.
- Podpora: **k8s@cerit-sc.cz**.

## Související téma

- MetaCentrum grid (PBS) je jiná služba než tento Kubernetes — nepleť `qsub`/joby
  dohromady. Rozdíly PBS vs K8s: PBS = dávkové fronty (`pbs-qsub.md`);
  K8s = trvalé/kontejnerové workloady.
