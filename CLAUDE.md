# CLAUDE.md — Istruzioni Operative per Claude Code

Questo file viene letto automaticamente da Claude Code ad ogni sessione.
È la fonte di verità operativa per questo progetto. Il file `rules.md` contiene lo schema completo della wiki; questo file lo integra con le istruzioni pratiche per l'AI.

---

## Priorità Assoluta: Workflow Ingest

Quando l'utente dice "vai con il prossimo ingest" o formulazioni equivalenti:

1. **Leggere `wiki/ingest_queue.md`** — individuare il primo elemento con `[ ]`.
2. Se è un Pokédex bulk, eseguire lo script Python di ingest corrispondente (o crearne uno nuovo seguendo il pattern di `wiki/00_Meta/ingest_johto_json.py`).
3. Se è una sezione da PDF, aprire `raw/POKEROLE COREBOOK 2.0 (2).pdf` e leggere le pagine indicate.
4. Aggiornare `wiki/ingest_queue.md` segnando `[x]` sugli elementi completati.
5. Aggiornare `wiki/log.md` con entry cronologica di tipo `ingest`.

---

## Regole Pokédex Bulk (JSON da Willowlark/Pokerole-Data)

### Forme Alternative — REGOLA CRITICA
**Le Mega Evoluzioni, forme Primordiali, forme regionali (Alolan, Galarian, Hisuian) e qualsiasi altra forma alternativa NON devono essere create come file `.md` separati.**
Devono essere aggiunte come sezioni `##` in fondo alla pagina del Pokémon base (es. `## Mega Venusaur (#0003M1)`), con tipo, abilità, HP, statistiche e mosse.

### Immagini Pokédex
- Immagine nel frontmatter: `image: "assets/images/pokemon/{id:03d}.png"`
- Tag nel corpo (subito dopo `# Nome (#XXXX)`): `<img src="../../assets/images/pokemon/{id:03d}.png" align="right" width="220" style="margin-left:20px;margin-bottom:8px;">`
- Kanto (001-151): immagini già presenti.

### Template Pagina Pokémon
```
---
title: "Nome (#NNNN)"
category: Pokedex
tags: [nome, regione, tipo1, tipo2]
image: "assets/images/pokemon/NNN.png"
---

# Nome (#NNNN)

<img src="...">

*Categoria Pokédex*

**Type:** Tipo1 / Tipo2
**Abilities:** [[Ability1]], [[Ability2]], [[HiddenAbility]] *(Hidden)*
**Base HP:** N

> Descrizione Pokédex.

---

## Statistiche (Attributes & Limits)

| Attribute | Base / Limit |
|---|---|
| **Strength** | X/X |
| **Dexterity** | X/X |
| **Vitality** | X/X |
| **Special** | X/X |
| **Insight** | X/X |

---

## Mosse (Learnset)

- **Starter:** [[Mossa1]], [[Mossa2]]
- **Beginner:** ...

---

## Correlati

### Catena Evolutiva
- [[0001_Bulbasaur|Bulbasaur]]
- [[0002_Ivysaur|Ivysaur]]

---

## Mega Nome (#DexID)          ← SEZIONE per ogni forma alternativa

**Type:** ...
**Abilities:** ...
**Base HP:** N

| Attribute | Base / Limit |
...

### Mosse
...
```

---

## Regole Linguistiche (da `rules.md` §4)

- **Tutto il testo descrittivo in Italiano.**
- **NON tradurre mai:** nomi di Mosse, Abilità, Natures, Attributes (Strength, Dexterity, Vitality, Special, Insight), Skills, Ranks (Starter/Beginner/Amateur/Ace/Pro/Master/Champion), Status Ailments, termini meccanici (STAB, Critical Hit, ecc.).
- **Tradurre:** Tipi Pokémon (Fire→Fuoco, Water→Acqua, ecc.), termini generici (Trainer→Allenatore, ecc.).
- **Wikilink** per Mosse, Abilità, Tipi e Attributes: `[[NomeMossa]]`, `[[Overgrow]]`, `[[Fuoco]]`.

---

## File di Supporto da Aggiornare ad Ogni Ingest

- `wiki/ingest_queue.md` — segnare `[x]`
- `wiki/log.md` — aggiungere entry `## [YYYY-MM-DD] ingest | descrizione`
- `wiki/index.md` — aggiornare se necessario

---

## Stato Attuale Pokédex

| Generazione | Stato |
|---|---|
| Kanto (001-151) | ✅ Completato (con Mega/forme come sezioni) |
| Johto (152-251) | ✅ Completato |
| Hoenn (252-386) | ✅ Completato (con Mega/Primal/forme come sezioni) |
| Sinnoh (387-493) | ✅ Completato (con Mega/forme come sezioni) |
| Unova (494-649) | ⬜ Da fare |
| Kalos (650-721) | ⬜ Da fare |
| Alola (722-809) | ⬜ Da fare |
| Galar (810-898) | ⬜ Da fare |

**Script di ingest esistenti in `wiki/00_Meta/`:**
- `ingest_kanto_json.py`, `ingest_johto_json.py`, `ingest_hoenn_json.py`, `ingest_sinnoh_json.py`
- Pattern da seguire per le prossime generazioni: vedi `ingest_hoenn_json.py`
- Repository dati: `https://raw.githubusercontent.com/Pokerole-Software-Development/Pokerole-Data/master/v2.0/Pokedex/{Nome}.json`

---

## Riferimento Completo

Per lo schema completo della wiki (struttura directory, template dettagliati, workflow query, lint), leggere **`rules.md`** alla radice del progetto.
