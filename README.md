# e-INFRA CZ / MetaCentrum — Dokumentace (zrcadlo)

Gitový repozitář se zdrojem pravdy pro **dokumentaci e-INFRA CZ / Metacentra**,
určený jako strojově čitelná referenční příručka (pracovní podklad pro Claude Code,
LLM agenty a re-scrapování a diffování přes git).

- **naposledy scrapnuto:** 2026-09-10
- **licence obsahu:** viz `SCRAPING.md` (obsah pochází z veřejné dokumentace e-INFRA CZ)
- **zdroje:** [docs.e-infra.cz](https://docs.e-infra.cz) a návazné dokumentační weby e-INFRA CZ

## Co tu je

| Cesta | Obsah |
|-------|-------|
| `raw/` | **Syrový** scrapnutý obsah (markdown) zrcadlící strukturu webu. Neupravuj ručně — zdroj pravdy pro re-scrap. |
| `.claude/skills/metacentrum/` | Skill `metacentrum`: stručný `SKILL.md` + praktické příručky `references/<téma>.md` odvozené z `raw/`. |
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
.claude/skills/metacentrum/
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
