# e-INFRA CZ / MetaCentrum — Dokumentace (zrcadlo)

Gitový repozitář se zdrojem pravdy pro **dokumentaci e-INFRA CZ / Metacentra**,
určený jako strojově čitelná referenční příručka — a zároveň **plugin marketplace
pro Claude Code** se skillem `metacentrum`.

- **naposledy scrapnuto:** 2026-09-10
- **zdroje:** [docs.e-infra.cz](https://docs.e-infra.cz) a návazné dokumentační weby e-INFRA CZ

## Instalace jako plugin (Claude Code)

Toto repo je zároveň **plugin marketplace** — instalace jedním příkazem:

```bash
claude plugin marketplace add Krici12/metacentrum-skill
claude plugin install metacentrum@metacentrum-skill
```

nebo interaktivně v Claude Code: `/plugin marketplace add Krici12/metacentrum-skill`
a poté `/plugin install metacentrum@metacentrum-skill`.

Po instalaci se skill `metacentrum` automaticky aktivuje, když se zeptáš na
cokoli o MetaCentru / e-INFRA CZ (PBS joby, GPU, kvóty, Kerberos, JupyterHub,
Kubernetes, S3, AI as a Service…).

## Autorství a licence obsahu

Skill v `skills/metacentrum/` je původní, ručně psaný kondenzát.

Obsah `raw/` je **zrcadlem veřejné dokumentace** provozované CESNET / MetaCentrum /
CERIT-SC ([docs.e-infra.cz](https://docs.e-infra.cz),
[docs.metacentrum.cz](https://docs.metacentrum.cz),
[docs.cerit.io](https://docs.cerit.io),
[docs.du.cesnet.cz](https://docs.du.cesnet.cz),
[docs.account.e-infra.cz](https://docs.account.e-infra.cz)) — slouží jen pro
vlastní strojově čitelné použití a sledování změn. **Není naším dílem**;
autorská práva patří příslušným provozovatelům. Pokud jste provozovatel a máte
námitky proti zrcadlení, otevřete issue.

## Co tu je

| Cesta | Obsah |
|-------|-------|
| `skills/metacentrum/` | Skill `metacentrum`: stručný `SKILL.md` + praktické příručky `references/<téma>.md` odvozené z `raw/`. |
| `.claude-plugin/` | Manifesty pluginu a marketplace (`plugin.json`, `marketplace.json`). |
| `raw/` | **Syrový** scrapnutý obsah (markdown) zrcadlící strukturu webu. Neupravuj ručně — zdroj pravdy pro re-scrap. |
| `scripts/` | Skripty pro scrapování (`scrape.py`, `extract.py`) a aktualizaci. |
| `SCRAPING.md` | Návod, jak obsah re-scrapnout a aktualizovat. |
| `STRUCTURE.md` | Mapa struktury webu a co kterou sekcí pokrýváme. |

## Proč `docs.e-infra.cz` není jediný zdroj

`docs.e-infra.cz` je **rozcestník**. Samotný obsah je hostovaný na e-INFRA rodině domén:

- **docs.metacentrum.cz** — grid MetaCentra: PBS/qsub, fronty, walltime, softwarové moduly, GPU uzly, Jupyter, OnDemand, Kerberos/SSH
- **docs.cerit.io** — Kubernetes/Rancher (CERIT-SC), JupyterHub, workflows, AI as a Service
- **docs.du.cesnet.cz** — datová úložiště (S3 object storage, RBD)
- **docs.account.e-infra.cz** — e-INFRA CZ účet / autentizace (Perun, MFA, ORCID)

Skripty scrapují z těchto domén a ukládají je podle jejich URL struktury.

## Rychlý start

```bash
# Celý obsah re-scrapnout (existující soubory nechá být, jen doplní/opraví chybějící)
python3 scripts/scrape.py

# Vynutit pře-scrapování všeho (až zdrojový web změní obsah)
python3 scripts/scrape.py --fresh
```

## Struktura skillu `metacentrum`

```
skills/metacentrum/
├── SKILL.md              # frontmatter + navigace k references/ (krátký)
└── references/
    ├── pbs-qsub.md       # PBS Pro: qsub, fronty, walltime, příkazy
    ├── software-modules.md
    ├── gpu-nodes.md
    ├── jupyterhub.md
    ├── ondemand.md
    ├── kubernetes-rancher.md
    ├── data-storage.md
    ├── authentication.md # Kerberos, SSH, e-INFRA CZ účet
    └── ai-as-a-service.md # LLM API/chat, AI coding asistenti
```

Více v [`STRUCTURE.md`](STRUCTURE.md) a [`SCRAPING.md`](SCRAPING.md).

## Jak tato repozitář funguje (workflow)

1. **Raw** vrstva = věrné zrcadlo webu, generované jen skripty.
2. **Skill zůstává ručně psaný** a odvozuje se z `raw/` — lidská kondenzace, ne přepis.
3. **Git diff** mezi scrapy ukáže, co se na webu změnilo (nové fronty, upravené limity, walltime atd.).
