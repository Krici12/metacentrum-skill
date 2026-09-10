# Datová úložiště

> Praktická příručka. Zdroj: `raw/metacentrum/data/` + `raw/metacentrum/computing/infrastructure/`
> (home/scratch/mount storages) + `raw/cesnet/object-storage-s3/`.

## Typy úložišť v MetaCentru

| Typ | Účel | Poznámka |
|-----|------|----------|
| **Scratch** | dočasná data **během** výpočtu | viz `pbs-qsub.md`; máš ho čistit, uklízí se ~14 dní |
| **Home** | data **mezi** joby (týdny–roky) | sdílené FS, mají omezenou kapacitu; pojmenované po městech |
| **S3 objektové úložiště** | velké/objemové >10 TB, dlouhodobé | CESNET, přes S3 protokol (samostatná sekce níže) |
| **NRP** | dlouhodobé publikování FAIR dat | národní repozitář, jinde |

> ⚠️ MetaCentrum úložiště **nejsou vhodná pro citlivá/medicínská data** či data
> pod NDA — pro ta je určen **SensitiveCloud** (samostatná služba).

## Home / frontend / mount storage

- Každý frontend má nativní home na storage serveru; z libovolného frontendu
  přistoupíš ke všem storages. Cesty tvaru `/storage/city/home/user`.
- Kvóty a limity: `raw/metacentrum/data/quotas.md`, `direct-access-storages.md`,
  `raw/metacentrum/computing/infrastructure/storages.md`.
- Sdílení dat / velké soubory / backup: `raw/metacentrum/data/data-sharing.md`,
  `large-data.md`, `metacentrum-backup.md`.

## S3 objektové úložiště (CESNET Data Storage)

Provozuje **Data Storage Department** (`docs.du.cesnet.cz`). Data v **bucketech**;
přístup přes virtuální organizace a skupiny. Vhodné pro sdílení mezi uživateli/
skupinami z různých institucí, automatické zálohy (mnoho nástrojů umí S3 nativně).

> **Není vhodné jako dlouhodobý veřejný repozitář** — pro to je NRP.

### Získání přístupu + nástroje

- `raw/cesnet/object-storage-s3/s3-getting-access.md`, `s3-features.md`,
  `s3-use-cases.md`.
- Klienti: **AWS CLI**, s3cmd, rclone, boto3 (Python), Cyberduck, WinSCP, s5cmd,
  CloudBerry… (kombinace v `raw/cesnet/object-storage-s3/`).

### AWS CLI — rychlý start

Konfigurace:
```bash
aws configure --profile test_user
# AWS Access Key ID / Secret Access Key (od správce storage)
# Default region name: us-east-1   <-- musíš vyplnit, jinak InvalidLocationConstraint
# Default output format: text|json|table
```

> Vždy používej `--endpoint-url` s konkrétním CESNET endpointem:
> např. `https://s3.cl2.du.cesnet.cz`.

```bash
EP="--profile test_user --endpoint-url https://s3.cl2.du.cesnet.cz"

aws s3 $EP mb s3://test1                     # create bucket
aws s3 $EP ls                                # list buckets
aws s3 $EP cp C:/data/file.zip s3://test1/   # upload
aws s3 $EP cp s3://test1/file.zip C:/data/   # download
aws s3 $EP rm s3://test1/file.zip            # delete
aws s3 $EP cp C:/data/dir s3://test1/dir/ --recursive   # upload dir
aws s3 $EP sync s3://test1/sync/ C:/data/sync           # sync down
```

Limity a tipy:
- Multipart upload jde **do 5 GB**; pro velké soubory používej `aws s3 cp`
  (sám dělá multipart), ne `s3api create-multipart-upload`.
- Bucket name: lowercase, číslice, `-`, `.`; začíná písmenem/číslicí; **bez `/`**
  (blokuje API přístup).
- Sdílení: **presign URLs** (`presign`), **bucket policies** (skupina/tenant,
  veřejné čtení), **versioning** (obnova starší verze objektu).
- Citlivá data: **client-side encryption** bucketů (správce ji nevidí).

### Další klienti

- **s3cmd** a **rclone**: `raw/cesnet/object-storage-s3/s3cmd.md`, `rclone.md`.
- **Python boto3**: `raw/cesnet/object-storage-s3/boto3.md`.

## Související

- Scratch v PBS jobech → `pbs-qsub.md`.
- Mount meta home v JupyterHub → `jupyterhub.md`.
