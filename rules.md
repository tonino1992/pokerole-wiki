# Schema LLM Wiki: Pokérole IT/EN

Una base di conoscenza persistente, interconnessa e gestita dall'Intelligenza Artificiale per il sistema di gioco di ruolo Pokérole.
Basata sul pattern "LLM Wiki" (A. Karpathy), adattata con regole di traduzione rigide e formattazione semantica.

## 1. Scopo e Core Idea
Questa wiki è il livello di conoscenza lavorativa tra i manuali grezzi (PDF) e l'utente (Master/Giocatore). 
La maggior parte dei workflow costringe l'AI a riscoprire le stesse regole dai manuali ogni volta. Noi usiamo un approccio diverso: l'AI costruisce e mantiene questa Wiki in modo incrementale. I manuali originali rimangono la fonte di verità immutabile, ma la Wiki diventa il database strutturato in cui l'AI salva sintesi, statistiche, regole e collegamenti ipertestuali.

## 2. Architettura e Struttura Directory
Ci sono tre livelli fondamentali:
1. **Raw Sources (`raw/`)**: Documenti originali (PDF). Sono immutabili. L'AI li legge ma non li modifica mai.
2. **La Wiki (`wiki/01_` a `wiki/05_`)**: Pagine Markdown gestite e aggiornate dall'AI.
3. **Lo Schema (`rules.md`)**: Questo file, alla radice del progetto.

### Alberatura di Riferimento:
pokerole-wiki/                   # Radice del progetto
├── rules.md                     # Schema LLM Wiki (questo file)
├── raw/                         # Materiale grezzo in lettura (PDF sorgente)
└── wiki/                        # Contenuto della wiki
    ├── index.md                 # Indice generale (Table of Contents)
    ├── log.md                   # Registro append-only (Ingest, Query, Linting)
    ├── ingest_queue.md          # Coda ordinata degli ingest da fare
    ├── 00_Meta/                 # Script di ingestion, audit report, strumenti AI
    ├── 01_Regole_Base/          # Meccaniche core (Dadi, Combattimento, HP)
    ├── 02_Allenatori/           # Creazione PG, Attributes, Skills, Natures, Schede
    ├── 03_Pokedex/              # Pagine specifiche dei Pokémon e dei Tipi
    │   ├── Tipi/                # Es. Fuoco.md, Acqua.md
    │   └── Kanto/               # Es. 0001_Bulbasaur.md
    ├── 04_Moves_e_Abilities/    # Database Mosse e Abilità
    │   ├── Mosse/               # Es. Flamethrower.md, Tackle.md
    │   └── Tratti/              # Es. High_Critical.md, Recoil.md
    ├── 05_Strumenti_e_Oggetti/  # Pokeball, Hold Items, Cure
    └── assets/
        └── images/              # Immagini estratte dal PDF (decorative)

## 3. Principi Operativi
* L'umano è responsabile della fornitura dei testi, delle priorità e del giudizio.
* L'AI è responsabile di riassumere, strutturare, formattare (YAML), creare collegamenti e registrare le modifiche.
* Preferire l'aggiornamento di una pagina esistente rispetto alla creazione di un duplicato.
* Mantenere un linguaggio chiaro e utile.
* Ogni affermazione o dato numerico meccanico deve riflettere fedelmente la fonte `raw`.

## 4. Direttive Linguistiche e Glossario (Strict)
* **Lingua Base:** Scrivi tutto il testo descrittivo, la narrativa e le spiegazioni in **Italiano**.
* **Eccezioni di Traduzione (Parole Chiave in INGLESE):** NON DEVI MAI tradurre i seguenti termini meccanici. Devono rimanere rigorosamente in Inglese, in *corsivo* o con la Prima Lettera Maiuscola:
  - **Moves:** es. *Flamethrower*, *Tackle*.
  - **Abilities:** es. *Overgrow*, *Levitate*.
  - **Natures:** es. *Brave*, *Timid*, *Adamant*.
  - **Attributes:** *Vitality*, *Strength*, *Dexterity*, *Insight*, *Social*.
  - **Skills:** *Brawl*, *Channel*, *Evasion*, *Alert*, *Nature*.
  - **Stats:** *HP*, *Will*.
  - **Ranks:** *Starter*, *Beginner*, *Amateur*, *Ace*, *Pro*, *Master*, *Champion*.
  - **Status Ailments:** *Burn*, *Paralysis*, *Sleep*, *Poison*.
* **Elementi da TRADURRE in Italiano:**
  - **Tipi dei Pokémon:** Fire diventa *Fuoco*, Water diventa *Acqua* (es. Tipo [[Fuoco]]).
  - **Termini generici:** Allenatore (Trainer), Palestra (Gym), Medaglia (Badge).

## 5. Formattazione, Metadati e Template
Ogni file generato deve seguire regole semantiche per favorire il Retrieval.
* **Sistema di Dadi:** Usa "Dice Pool" o "Riserva di Dadi" (d6, Successo su 4, 5, 6).
* **Wikilink Semantici:** Usa le doppie parentesi quadre `[[Nome]]` per Moves, Abilities, Types o Attributes.

### Metadati Avanzati (YAML Frontmatter)
Ogni pagina deve obbligatoriamente iniziare con questo blocco. I campi condizionali vanno inseriti se pertinenti:
---
title: [Titolo dell'elemento]
category: [Es. Move, Ability, Pokemon, Type, Rule]
tags: [tag_in_italiano, tag_in_inglese]
summary: [Una singola riga di riassunto. Es: "Mossa di tipo Fuoco ad alto danno con chance di Burn."]
# -- Campi Condizionali --
type: [Es. Fuoco - se è una mossa o un pokemon]
dice_pool: [Es. Dexterity + Channel - solo per Mosse]
power: [Es. 2 - solo per Mosse]
---

### Template Strutturali Obbligatori (Intestazioni)

**Mosse** (`04_Moves_e_Abilities/Mosse/`) — Formato compatto bulk:
```
# NomeMossa
*Tipo | Categoria*
- **Accuracy:** ...
- **Damage:** ...
- **Target:** ...
- **Traits:** [[Tratto1]], [[Tratto2]]
- **Effect:** descrizione effetto in italiano
> Flavour text in corsivo.
```

**Tratti** (`04_Moves_e_Abilities/Tratti/`) — Formato compatto:
```
# NomeTratti
Descrizione sintetica in italiano.
> Flavour text in corsivo.
```

**Pokémon** (`03_Pokedex/*/`) — Struttura standard:
```
# Nome (#NNNN)
*Specie Pokemon*
**Type:** ... | **Abilities:** [[Ab1]], [[Ab2]] *(Hidden)* | **Base HP:** N
> Lore quote.
## Statistiche (Attributes & Limits)   ← tabella Attribute / Base / Limit
## Mosse (Learnset)                     ← elenco per Rank
## Correlati
### Catena Evolutiva
```

**Regole** (`01_Regole_Base/`, `02_Allenatori/`):
`## Descrizione Generale`, `## Meccaniche Dettagliate`, `## Esempi`

## 6. Ingest Workflow
Quando l'utente aggiunge una nuova fonte grezza e ti chiede di processarla ("ingest"):
1. Leggi il testo fornito.
2. Genera il file o i file Markdown applicando le regole linguistiche, i template e lo YAML.
3. **Nomi File e Percorsi:** Usa estensione `.md`. Sostituisci spazi con `_`. Se è una Mossa/Abilità, il nome file DEVE essere in inglese (es. `wiki/04_Moves_e_Abilities/Mosse/Ember.md`).
4. **Azione Obbligatoria:** Indica il percorso completo all'inizio della tua risposta usando un code block: `Creazione file in: [percorso]`.
5. Fornisci le stringhe per aggiornare `index.md` (con una riga descrittiva) e `log.md`.
6. **Standard di Qualità Obbligatorio:** Ogni pagina deve contenere **tutto l'essenziale**, non solo un riassunto sintetico. Per ogni meccanica o elemento descritto, includere:
   - **Citazione narrativa** dal PDF (il flavour text originale, in corsivo e blockquote).
   - **Tabella meccaniche completa** con tutti i campi rilevanti (effetto, durata, resistenza, immunità, tiro richiesto).
   - **Note strategiche** (💡) con implicazioni pratiche per il gioco e consigli.
   - **Avvertenze** (⚠️) per le meccaniche pericolose o che hanno conseguenze gravi.
   - **Spiegazioni contestuali:** Non limitarsi a riportare i dati — spiegare *perché* una meccanica funziona in quel modo e *come* interagisce con le altre regole.


## 7. Query Workflow
Quando l'utente fa una domanda:
1. Leggi prima `index.md` per identificare le pagine rilevanti.
2. Sintetizza una risposta basandoti ESCLUSIVAMENTE sui contenuti della Wiki.
3. Cita le pagine specifiche usate.
4. Se l'informazione non c'è, dillo chiaramente invece di inventare/allucinare.
5. Se la risposta prodotta è di grande valore, offriti di salvarla come nuova pagina in `01_Regole_Base/`.

## 8. Lint e Manutenzione (Log)
Aggiorna il file `log.md` usando questo formato cronologico:
* `## [YYYY-MM-DD] ingest | aggiunta-mossa-flamethrower`
* `## [YYYY-MM-DD] query | risoluzione-dubbi-status-burn`
* `## [YYYY-MM-DD] lint | controllo-link-orfani`

Quando richiesto di fare "Linting", verifica:
* Contraddizioni tra le pagine.
* Pagine orfane (senza inbound links).
* Termini non tradotti correttamente (es. "Lanciafuoco" invece di *Flamethrower*).
* File mancanti di intestazione YAML.

## 9. Procedura Ingest Sequenziale
Quando l'utente chiede di "procedere con il prossimo ingest" (o formulazioni equivalenti), l'AI deve seguire questo workflow:

1. **Consultare `wiki/ingest_queue.md`**: Individuare il primo elemento con `[ ]` (non completato).
2. **Leggere il PDF sorgente**: Aprire `raw/POKEROLE COREBOOK 2.0 (2).pdf` ed estrarre le pagine indicate nell'elemento della coda.
3. **Creare il file Wiki**: Applicare tutte le regole linguistiche (§4), i template (§5) e lo YAML frontmatter (§5).
4. **Aggiornare i file di supporto**:
   - `wiki/index.md` — Rimuovere il marcatore 🔥 dalla voce e confermare il link.
   - `wiki/log.md` — Aggiungere un'entry cronologica di tipo `ingest`.
   - `wiki/ingest_queue.md` — Segnare l'elemento come `[x]`.
5. **Comunicare all'utente**: Riportare il percorso del file creato e un breve riassunto.

> **Regola Chiave:** Il file `wiki/ingest_queue.md` è la **fonte di verità** per l'ordine e lo stato degli ingest. Deve essere sempre tenuto aggiornato.