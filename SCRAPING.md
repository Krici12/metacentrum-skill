# Scrapování a údržba

Tento soubor popisuje, jak `raw/` vzniká, jak ho re-scrapnout a jak ho udržovat
v git repozitáři tak, aby diffy mezi verzemi byly smysluplné.

## Jak raw/ vzniká

`raw/` je **syrové zrcadlo** dokumentace e-INFRA CZ. Nesmí se upravovat ručně —
mění se jen přes skripty. Jednotlivé domény se mapují na podstromy:

| Doména (zdroj) | Podstrom v `raw/` |
|----------------|-------------------|
| `docs.metacentrum.cz` | `metacentrum/` |
| `docs.cerit.io` | `cerit/` |
| `docs.du.cesnet.cz` | `cesnet/` |
| `docs.account.e-infra.cz` | `einfra-account/` |

Cesty uvnitř podstromu kopírují část URL po `/en/docs/` (např. URL
`docs.metacentrum.cz/en/docs/computing/resources/queues` →
`raw/metacentrum/computing/resources/queues.md`). Díky tomu:
- je snadné znovu scrapnout **jen jednu sekci**,
- git diff mezi dvěma scrapy ukáže, co se na webu přesně změnilo.

## Jak re-scrapnout

```bash
# Doplnit/opravit: existující soubory nechá být, stáhne chybějící a poškozené
python3 scripts/scrape.py

# Vynutit kompletní pře-scrap (po změnách na webu)
python3 scripts/scrape.py --fresh
```

Skript:
1. vezme seznam URL z `MAP` v `scripts/scrape.py`,
2. stáhne HTML (curl, User-Agent `Mozilla/5.0 (scrape; e-INFRA docs mirror)`),
3. `scripts/extract.py` převede hlavní článek na markdown,
4. uloží do `raw/<podstrom>/<cesta>.md`.

### Jak přidat novou stránku

1. Najdi URL v dokumentaci (např. přes navigaci na konkrétním docs webu).
2. Přidej dvojici `(url, raw-podstrom/cesta.md)` do `MAP` v `scripts/scrape.py`.
3. Spusť `python3 scripts/scrape.py` a zkontroluj vygenerovaný soubor.

## Pracovní postup při aktualizaci obsahu

1. `python3 scripts/scrape.py --fresh`
2. Zkontroluj git diff: `git diff --stat raw/`
3. Content changes v sekcích → aktualizuj příslušné `references/<téma>.md`.
4. Commit s popisem, co se změnilo (např. „new GPU cluster", „walltime limit 7d").

## Extrahování raw → skill (praktické příručky)

`raw/` je rozcestník pro ručně psané příručky. Při aktualizaci references:

- **Nepřepisuj HTML/původní text** — references mají být kondenzované, praktické:
  konkrétní příkazy, limity, poznámky, pitfalls.
- Vždy uveď **zdroj** (sekce v `raw/`), aby šlo dohledat detail.
- Konkrétní čísla (walltime limity, velikosti kvót, cesty k úložištím) ber
  z `raw/`, ale ověř, že se nezměnila — web se průběžně mění.

## Použité technologie

- Python 3 (jen standardní knihovna: `html.parser`, `urllib` není potřeba, používáme `curl`)
- `curl` pro stahování
- Žádné pip závislosti → skripty fungují všude kde je Python 3 + curl

## Licence obsahu

Veškerý scrapnutý obsah pochází z veřejné dokumentace e-INFRA CZ provozované
CESNET/MetaCentrem. Tento repozitář **nevytváří** obsah, jen ho zrcadlí pro
vlastní strojově čitelné použití. Před veřejným sdílením zkontroluj aktuální
licenční podmínky e-INFRA CZ a dodrž je.
