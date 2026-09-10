#

A complete list of storages can be found in table below:

## [Storage information](#storage-information)

| Server |Directory |Backup Class |Note |
| storage-brno2.metacentrum.cz |/storage/brno2/ |2 | |
| storage-brno11-elixir.metacentrum.cz |/storage/brno11-elixir/ |2 |dedicated to ELIXIR-CZ |
| storage-brno12-cerit.metacentrum.cz |/storage/brno12-cerit/ |2 | |
| storage-plzen1.metacentrum.cz |/storage/plzen1/ |2 | |
| storage-plzen2-zcu.metacentrum.cz |/storage/plzen2-zcu/ |3 |dedicated to ZČU groups |
| storage-plzen4-ntis.metacentrum.cz |/storage/plzen4-ntis/ |3 |dedicated to iti/kky groups |
| storage-praha2-natur.metacentrum.cz |/storage/praha2-natur/ |0 | |
| storage-praha6-fzu.metacentrum.cz |/storage/praha6-fzu/ |0 | |
| storage-praha5-elixir.metacentrum.cz |/storage/praha5-elixir/ |3 | |
| storage-budejovice1.metacentrum.cz |/storage/budejovice1/ |3 | |
| storage-liberec3-tul.metacentrum.cz |/storage/liberec3-tul/ |0 | |
| storage-pruhonice1-ibot.metacentrum.cz |/storage/pruhonice1-ibot/ |3 | |
| storage-vestec1-elixir.metacentrum.cz |/storage/vestec1-elixir/ |2 |also /storage/praha1/ |

## [Backup class description](#backup-class-description)

| Backup Class |Description |
| 0 |No backup. |
| 2 |Snapshot backups once a day. Backups are performed and stored on the same HW as primary data. This class provides protection against unintentional data removal. It does not protect against hardware failure of the storage. |
| 3 |Snapshot backups plus a backup copy. The copy resides on a different hardware. This class provides protection against unintentional data removal as well as hardware failures. |

Backup policy for storages

All storages are backed up once a day (normally between 6 a.m. and 7 a.m.), by snapshot backup. There backups are kept for 2 weeks. For a more complete understanding of how the data are backed up in MetaCentrum service, see [the corresponding chapter](../../data/metacentrum-backup).

💡
Tip

User data are moved from time to time when hardware is replaced. See [table of decommissioned storages](../../computing/infrastructure/decommissioned-storages) to track back where your old data have been moved to.

![publicity banner](/_next/static/media/einfra_meta-zapati.0m5s8338yq376.svg)

### On this page
[Storage information](#storage-information)[Backup class description](#backup-class-description)

![einfra banner](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fheader03.0ikyctvi6x5ki.png&w=384&q=75)
