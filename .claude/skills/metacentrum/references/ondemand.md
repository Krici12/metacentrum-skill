# Open OnDemand (ondemand.metacentrum.cz)

> Praktická příručka. Zdroj: `raw/metacentrum/graphical/ondemand.md`.

## Co to je

Webové rozhraní pro přístup k MetaCentru prohlížečem: **https://ondemand.metacentrum.cz**.
Umožňuje:
- procházet **soubory** a úložiště,
- nahrávat/stahovat/soubory přesouvat/upravovat,
- spouštět **grafické aplikace** (Matlab, ANSYS, Jupyter notebook, RStudio server…),
- sestavovat a **spouštět batch joby**.

**Přihlášení**: akademickou identitou (jako webové služby e-INFRA CZ).
Podporované prohlížeče: Chrome, Firefox, Edge.

## Hlavní sekce

### Files
- Procházení storages; default `Home Directory` ukazuje na storage **brno2**.
- V menu jsou zkratky na 3 homes na různých storages.

### Jobs
- **Active jobs**: všechny tvé běžící/frontové joby na PBS (bez ohledu na to,
  jak byly odevzdány). Kliknutím zobrazíš detaily vč. umístění výstupních souborů.
- **Job composer**: GUI průvodce pro sestavení batch jobu.

### Clusters (shell access)
- CLI přístup k frontendům: `zuphux.metacentrum.cz`, `perian.metacentrum.cz`,
  `elmo.metacentrum.cz`. "Shell access" otevře SSH v prohlížeči.

### Interactive apps
- Všechny GUI aplikace a prostředí spouštěné jako **interaktivní job** na
  libovolném uzlu infrastruktury.
- ⚠️ Lokace domovského adresáře se může při každém spuštění lišit
  (`/storage/city_XY/home/user`) — ověř si cestu k datům.

### My Interactive Sessions
- Seznam tvých relací. Zavření záložky relaci **neztratí** — jde znovu spustit
  (klikem `Launch`, pokud neskončil vyhrazený čas).
- `View only` = sdílený **pouze-pro čtení odkaz** pro kolegu na živý desktop.

## Data directory

OnDemand si vytváří `~/ondemand` v domovském adresáři pro své soubory:
```text
~/ondemand/data/sys/dashboard/batch_connect/sys/bc_desktop/vmd/output/ONDEMAND_SESSION_ID
```
> `ONDEMAND_SESSION_ID` je **hash relace OnDemand, ne PBS job ID** (tvar např.
> `9a8b3f2b-0c6d-...`). Obsah `~/ondemand` můžeš kdykoli smazat; OnDemand ho
> vytvoří znovu.

## Tipy a pasti

- **RStudio**: default nastaven na `brno2` (kvůli problému home-on-any-storage);
  umístění lze přepsat v rozbalovací nabídce.
- **Kerberos ticket**: při dlouhém otevřeném sezení ticket vyprší — typická chyba
  `Key has expired @ dir_s_mkdir - /storage/brno2/home/user`.
  Obnova: **Help → Restart Web Server** (obyčejný reload nestačí).

## Související

- Jak funguje interaktivní job z CLI → `pbs-qsub.md`.
- Grafické aplikace obecně: `raw/metacentrum/software/graphical-access.md`.
