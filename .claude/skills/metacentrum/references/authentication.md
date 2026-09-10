# Autentizace: Kerberos, SSH, e-INFRA CZ účet

> Praktická příručka. Zdroj: `raw/metacentrum/access/` (log-in, account,
> security/kerberos, security/connect-auth) + `raw/einfra-account/access/`
> (account, perun, mfa, orcid).

## Dvě úrovně přihlašování — nezaměňovat

1. **e-INFRA CZ / MetaCentrum účet** = pro služby (přihlášení na webové služby,
   registrace). Spravuje se v Perun / User Profile.
2. **Kerberos + SSH** = pro ne-webové služby (PBS, frontendy, storage, git...).
   MetaCentrum grid vyžaduje Kerberos ticket pro bezheslový SSH přístup.

## e-INFRA CZ účet

- Účet se vytvoří automaticky při registraci do první služby. Otevřeno členům
  akademické komunity ČR (výzkumné účely).
- Registrace → např.: MetaCentrum grid/cloud/K8s přes
  https://metavo.metacentrum.cz (registration), OwnCloud/konference přes signup.e-infra.cz.
- Přihlášení webových služeb: **home organization account** (univerzitní
  přihlašování) nebo e-INFRA CZ login/heslo.
- Správa účtu, hesel, obnova: **e-INFRA CZ User Profile** → https://profile.e-infra.cz
- Session/členství spravuje **Perun** (https://perun.e-infra.cz) — stav účtu,
  členství ve skupinách, dostupné zdroje.
- **MFA**: doporučeno zapnout (viz `einfra-account/access/mfa.md`).
- ORCID propojení: `einfra-account/access/orcid.md`.

### Povinné potvrzení veřejně-zdrojových výstupů

Při použití zdrojů **e-INFRA CZ** musí publikace obsahovat potvrzení, např. EN:
> "This work was supported by the Ministry of Education, Youth and Sports of the
> Czech Republic through the e-INFRA CZ (ID:90254)."

V RIV zadej "e-INFRA CZ research infrastructure" (LRI code 90254).

## SSH + Kerberos (MetaCentrum grid)

Cíl: přihlásit se **jednou**, pak bez hesla všude (frontendy, compute uzly, storage).

### Linux (Debian/Ubuntu)

```bash
sudo apt install krb5-user ssh-krb5
# config wizard zruš (Ok/Next), nastaví se ručně:

sudo scp user@skirit.ics.muni.cz:/etc/krb5.conf /etc/

# ~/.ssh/config:
#   GSSAPIAuthentication yes
#   GSSAPIDelegateCredentials yes
#   GSSAPIKeyExchange yes      # MacOS: tento řádek VYnech

kinit user@META               # získat ticket (zadáš heslo)
klist                          # kontrola platných ticketů
```

Ticket platí **24 h** (v příkladu); s renew možností až **7 dnů**:
```bash
kinit -r 7d USER@META
```

Pak: `ssh user@skirit.ics.muni.cz` bez hesla.

> **Tip**: pokud se nepřihlásíš, zkus synchronizovat hodiny: `ntpdate tik.cesnet.cz`
> (Kerberos je citlivý na časové rozdíly).

### Windows

- MIT Kerberos (KFW); zkopíruj `/etc/krb5.conf` jako
  `C:\ProgramData\MIT\Kerberos5\krb5.ini` (pozor na příponu `.ini` — ulož s uvozovkami).
- Ticket přes MIT Kerberos GUI → už žádné heslo v PuTTY.
- **WSL**: postupuj jako Linux.

### Poznámky

- PBS příkazy od února 2026 vyzvou k zadání hesla, chybí-li ticket (viz `pbs-qsub.md`).
- `connect-auth.md` — další bezheslové připojení / certifikáty:
  `raw/metacentrum/access/security/connect-auth.md`.

## Související

- První přihlášení k PBS jobům → `pbs-qsub.md`.
- Přihlášení přes OnDemand (web, žádný Kerberos v prohlížeči) → `ondemand.md`.
- JupyterHub SSH (z IPv6, eduvpn) → `jupyterhub.md`.
