#

CERIT-SC operates public clusters and a secure cluster (more information in the upcoming Secure cluster section). Public clusters include *kuba-cluster* (the largest one), *kubh-cluster* (HA cluster). The secure cluster includes the *kubas-cluster*.

## [Public clusters](#public-clusters)

### [kuba-cluster](#kuba-cluster)

The kuba-cluster consists of 39 nodes (currently 31 available) and features 22 NVIDIA A40, 6 NVIDIA A10, and 12 NVIDIA A100 (80GB variant) GPU accelerators. Four A100 cards are configured as MIG parts, resulting in 12x *10GB* and 8x *20GB* parts.

| 39x | |Nodes |
| Memory: |1024GB:
512GB:
1.5TB: |kub-b15, kub-b16
All remaining nodes apart from *kub-c*
8 HPC *kub-c* nodes |
| Disk: |2x 3.5TB SSD SATA:
8x 8TB NVME SSD:
60TB NVME SSD: |kub-a5 — kub-a25
kub-b1 — kub-b18
8 HPC *kub-c* nodes |
| GPU: |None:

2x NVIDIA A40 per node:
1x NVIDIA A40 per node:
 2x NVIDIA A10 per node:
2x NVIDIA A100 (80GB) per node:
1x NVIDIA H100 (PCIE/80GB):
1x NVIDIA L4:
1x NVIDIA H100 NVL (PCIE/94GB) per node: |kub-a5 — kub-a9, kub-b3, kub-b9, kub-b14, kub-b15, kub-b17

kub-a10 — kub-a14, kub-b12
kub-a15 — kub-a20, kub-a22 — kub-a24
kub-b1 — kub-b2, kub-b16
kub-b4 — kub-b8
kub-b10 — kub-b11
kub-b13
8 HPC *kub-c* nodes |
| Network: |2x 10Gbps Ethernet:
1x 100Gbps Infiniband:
1x 100Gbps Ethernet and 1x 200Gbps Infiniband: |All nodes
kub-b1 — kub-b18
8 HPC *kub-c* nodes |

#### [Storage](#storage)

Primary network storage consists of four head nodes each equipped with AMD EPYC 7302P, 256 GB RAM, 2x 10 Gbps NIC (failover only). It offers 500 TB of all-flash capacity using SSD drives only in a RAID 6-equivalent configuration. The filesystem used is IBM Spectrum Scale, which is exported via NFS version 3 to the Kubernetes cluster.

#### [Data Backup](#data-backup)

Storage is not backed up to another location, but file system snapshots are made daily. It is possible to restore deleted or overwritten data up to 14 days in the past.

### [kubh-cluster](#kubh-cluster)

The kubh-cluster consists of 6 nodes dispersed across three different locations (2 nodes in each location: University Campus Bohunice — UKB, University Computer Center — CPS — at Komenského náměstí, and Faculty of Informatics at Botanická), making it a suitable option for HA setups.

Affinities and antiaffinities are used to schedule Pods into same (or different) domains. When specifying the affinities, the *topologyKey* field is used by scheduler to determine the Pod placement. In our environment, use `cerit.io/region` as the value of the *topologyKey*. Current region values are `cerit.io/region: botanicka, cerit.io/region: komenskeho, cerit.io/region: kampus`.

| 6x | |Nodes |
| CPU: |2x AMD EPYC 7543 32-Core Processor
(in total 64 CPUs per node) | |
| Memory: |512GB | |
| Disk: |20TB NVME:
7TB NVME SSD: |kub-h1 — kub-h2
kub-h3 — kub-h6 |
| Network: |2x 10Gbps Ethernet: |All nodes |

#### [Storage](#storage-1)

Storage is provided only locally on each node.

#### [Data Backup](#data-backup-1)

Local storage is not backed up; it is up to the user to ensure backup.

## [Secure cluster](#secure-cluster)

### [kubas-cluster](#kubas-cluster)

The kubas-cluster consists of 10 nodes and features 5x NVIDIA A40, 2x NVIDIA A100 (80GB variant), 4x NVIDIA P100, 2x NVIDIA H100 (NVL 94GB variant), and on-demand 4x NVIDIA A100 GPU accelerators. Nodes *kub-cs1* and *kub-cs2* are physically located at a different site from the rest of the cluster; therefore, it is possible to create an HA setup in the secure cluster as well.

| 10x | |Nodes |
| CPU: |2x AMD EPYC 7543 32-Core Processor (in total 64 CPUs per node):
2x AMD EPYC 9454 48-Core Processor (in total 96 CPUs per node):
1x Intel(R) Xeon(R) CPU E5-2650 v4 @ 2.20GHz 24-Core Processor:
2x AMD EPYC 9454 48-Core Processor (in total 96 CPUs per node): |kub-as1 — kub-as6
kub-cs1, kub-cs2
kblack
kub-ds1, kub-ds2, kub-ds3 |
| Memory: |512GB:
1.5TB:
1.5TB:
512GB: |kub-as1 — kub-as6
kub-cs1, kub-cs2
kub-ds1, kub-ds2, kub-ds3
kblack |
| Disk: |2x 3.5TB SSD SATA:
60TB NVME SSD:
60TB NVME SSD:
1x 3.6TB SSD: |kub-as1 — kub-as6
kub-cs1, kub-cs2
kub-ds1, kub-ds2, kub-ds3
kblack |
| GPU: |1x NVIDIA A40 per node:
2x NVIDIA A100 (80GB) per node:
2x NVIDIA H100 NVL (94GB) per node:
4x NVIDIA P100:
1x NVIDIA H100 NVL (94GB) per node: |kub-as1 — kub-as5
kub-as6
kub-cs1, kub-cs2
kblack
kub-ds1, kub-ds2, kub-ds3 |
| Network: |2x 10Gbps Ethernet:
1x 100Gbps Ethernet:
1x 10Gbps Ethernet:
1x 10Gbps Ethernet: |kub-as1 — kub-as6
kub-cs1, kub-cs2
kblack
kub-ds1, kub-ds2, kub-ds3 |

#### [Storage](#storage-2)

Primary network storage consists of two head nodes each equipped with Intel(R) Xeon(R) Silver 4216 CPU @ 2.10GHz, 192 GB RAM, 1x 10 Gbps NIC. It offers 1700 TB of capacity using rotational drives only in a RAID 6 configuration. The filesystem used is IBM Spectrum Scale, which is exported via NFS version 3 to the Kubernetes cluster.

#### [Data Backup](#data-backup-2)

Storage is regularly backed up to a different storage in a different location.

![publicity banner](/_next/static/media/einfra_cerit-zapati.04hjcx2t12mah.svg)

### On this page
[Public clusters](#public-clusters)[kuba-cluster](#kuba-cluster)[Storage](#storage)[Data Backup](#data-backup)[kubh-cluster](#kubh-cluster)[Storage](#storage-1)[Data Backup](#data-backup-1)[Secure cluster](#secure-cluster)[kubas-cluster](#kubas-cluster)[Storage](#storage-2)[Data Backup](#data-backup-2)

![einfra banner](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fheader03.0ikyctvi6x5ki.png&w=384&q=75)
