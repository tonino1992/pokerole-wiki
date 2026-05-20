# 📋 Pokérole Wiki — Log delle Operazioni

Registro cronologico append-only. Ogni operazione viene registrata con data, tipo e descrizione.

---

## [2026-05-20] ingest | pokédex-kalos-650-721
- **Tipo:** Bulk Ingest — Pokédex
- **Fonte:** JSON `Pokerole-Software-Development/Pokerole-Data` v2.0/Pokedex
- **File creati:** 72 schede Pokémon in `wiki/03_Pokedex/Kalos/` (#0650 Chespin → #0721 Volcanion)
- **Contenuto:** Type (IT), Abilities, Base HP, Statistiche (Attributes & Limits), Learnset per Rank, Catena Evolutiva, immagini ufficiali
- **Forme inline:** Meowstic (Forma Femminile) skippata (non presente nel dataset), Aegislash (Forma Lama), Mega Diancie, Hoopa (Forma Senza Catene), Zygarde (Forma 10% e 100%) — tutte come sezioni `##` nella pagina base
- **Script:** `wiki/00_Meta/ingest_kalos_json.py`, fix: `wiki/00_Meta/fix_kalos_missing.py`
- **Note:** Flabébé fetchata come "Flabebe" (senza accenti); Zygarde base = "Zygarde 50%"; DexID 0718F2 corretto a 0718.

---

## [2026-05-19] ingest | pokédex-johto-152-251
- **Tipo:** Bulk Ingest — Pokédex
- **Fonte:** `raw/POKEROLE COREBOOK 2.0 (2).pdf` (pp. 136-161) + JSON Willowlark/Pokerole-Data
- **File creati:** 100 schede Pokémon in `wiki/03_Pokedex/Johto/` (#0152 Chikorita → #0251 Celebi)
- **Contenuto:** Type (IT), Abilities, Base HP, Statistiche (Attributes & Limits), Learnset per Rank, Catena Evolutiva, immagini ufficiali
- **Script:** `wiki/00_Meta/ingest_johto_json.py`
- **Note:** Lore text in inglese dal JSON (fedele alla fonte PDF). Tipi tradotti in italiano.

---

## [2026-05-05] init | inizializzazione-wiki
- **Tipo:** Inizializzazione
- **Fonte:** `raw/POKEROLE COREBOOK 2.0 (2).pdf` (69.7 MB)
- **Azioni eseguite:**
  1. Scansione completa dell'indice (Table of Contents) del Corebook 2.0
  2. Creazione struttura directory Wiki (`00_Meta/`, `00_Raw_Sources/`, `01_Regole_Base/`, `02_Allenatori/`, `03_Pokedex/`, `04_Moves_e_Abilities/`, `05_Strumenti_e_Oggetti/`)
  3. Creazione sottocartelle regionali Pokédex (Kanto, Johto, Hoenn, Sinnoh, Unova, Kalos, Alola, Galar)
  4. Creazione sottocartelle Moves e Abilities
  5. Popolamento di `index.md` con mapping completo capitoli → cartelle Wiki + Wikilink To-Do
- **Prossimi Ingest identificati (Priorità Alta):**
  1. `[[Tirare_i_Dadi]]` — Dice Pool e meccanica base (p. 29)
  2. `[[Attributes_e_Skills]]` — I 5 Attributes e le Skills (pp. 23-26)
  3. `[[Come_Funziona_il_Combattimento]]` — Struttura del combattimento (pp. 44-49)
- **Note:** Nessun contenuto è stato ancora processato (ingest). L'index.md contiene solo Wikilink To-Do.

## [2026-05-09] ingest | tirare-i-dadi
- **Tipo:** Ingest
- **Fonte:** `raw/POKEROLE COREBOOK 2.0 (2).pdf` — p. 29
- **File creato:** `01_Regole_Base/Tirare_i_Dadi.md`
- **Contenuto:** Dice Pool (d6, successi su 4+), livelli di difficoltà (Troublesome → Almost Impossible), Critical Failure (3+ successi mancanti), esempi narrativi (Murkrow/Honchkrow).
- **Aggiornamenti:** `index.md` (rimosso marcatore 🔥), `ingest_queue.md` (segnato come completato).

## [2026-05-09] meta | creazione-ingest-queue
- **Tipo:** Meta / Organizzazione
- **File creato:** `wiki/ingest_queue.md`
- **Contenuto:** Coda ordinata di tutti gli ingest futuri, organizzata per priorità (Alta → Media → Bassa → Bulk). Aggiunta procedura di ingest sequenziale in `rules.md` (§9).

## [2026-05-09] ingest | attributes-e-skills
- **Tipo:** Ingest
- **Fonte:** `raw/POKEROLE COREBOOK 2.0 (2).pdf` — pp. 23-26
- **File creato:** `01_Regole_Base/Attributes_e_Skills.md`
- **Contenuto:** 5 Attributes fisici/mentali (*Strength, Vitality, Dexterity, Insight, Special*) con scala 1-6+; 5 Social Attributes (*Tough, Cool, Beauty, Clever, Cute*); 5 categorie di Skills (Fight, Survival, Contest, Knowledge, Extra) con dettaglio di ogni singola Skill.
- **Aggiornamenti:** `index.md` (segnato ✅), `ingest_queue.md` (segnato `[x]`).

## [2026-05-09] ingest | hp-e-will
- **Tipo:** Ingest
- **Fonte:** `raw/POKEROLE COREBOOK 2.0 (2).pdf` — pp. 26-27
- **File creato:** `01_Regole_Base/HP_e_Will.md`
- **Contenuto:** Health Points (calcolo: Base HP + *Vitality*), danno temporaneo e svenimento, Lethal Damage e morte. Will Points (calcolo: *Insight* + 2), spesa per ignorare Pain/Stress e rilanciare dadi, esaurimento, restrizioni d'uso, recupero.
- **Aggiornamenti:** `index.md` (segnato ✅), `ingest_queue.md` (segnato `[x]`).

## [2026-05-09] ingest | come-funziona-il-combattimento
- **Tipo:** Ingest
- **Fonte:** `raw/POKEROLE COREBOOK 2.0 (2).pdf` — pp. 44-49
- **File creato:** `01_Regole_Base/Come_Funziona_il_Combattimento.md`
- **Contenuto:** Struttura del combattimento (Initiative, Round, Turn, End of Round), Step-by-Step (Initiative → Accuracy → Evasion/Clash → Damage → Multiple Actions), Trainer Actions (Switch, Item, Cover, Enter the Fray, Run Away), Pain Penalizations, Fainting, Lethal Damage.
- **Aggiornamenti:** `index.md` (segnato ✅), `ingest_queue.md` (segnato `[x]`).

## [2026-05-09] ingest | ranking
- **Tipo:** Ingest
- **Fonte:** `raw/POKEROLE COREBOOK 2.0 (2).pdf` — pp. 30-31
- **File creato:** `01_Regole_Base/Ranking.md`
- **Contenuto:** 7 Ranks (*Starter* → *Champion*) con Achievement richiesti e Benefits. Regole per Pokémon selvatici con Rank superiore/inferiore. Tabella riassuntiva con Skill Limit, Max Target, punti Attribute/Social/Skill per ogni Rank.
- **Aggiornamenti:** `index.md` (segnato ✅), `ingest_queue.md` (segnato `[x]`).

## [2026-05-09] ingest | status-conditions
- **Tipo:** Ingest
- **Fonte:** `raw/POKEROLE COREBOOK 2.0 (2).pdf` — pp. 57-60 (pp. 61-62 illustrazioni)
- **File creato:** `01_Regole_Base/Status_Conditions.md`
- **Contenuto:** 10 Status Conditions: *Burn* (3 livelli, fino a Lethal), *Paralysis* (−2 Dex, 24h), *Frozen Solid* (5 HP ghiaccio), *Poison* (1 danno/Round), *Badly Poisoned* (1 Lethal/Round), *Sleep* (5 min), *Confused* (−1 successo, 5 Round), *Flinched* (1 azione), *Disabled* (blocca Move), *In Love* (metà danno). Regole stacking, immunità per Tipo, tabella riassuntiva.
- **Aggiornamenti:** `index.md` (segnato ✅), `ingest_queue.md` (segnato `[x]`).

## [2026-05-09] lint | revisione-status-conditions
- **Tipo:** Revisione / Approfondimento
- **File modificato:** `01_Regole_Base/Status_Conditions.md`
- **Motivo:** L'utente ha richiesto descrizioni più approfondite. La versione iniziale era troppo sintetica (solo tabelle riassuntive).
- **Modifiche:** Ogni status ora include citazione narrativa dal PDF, tabella meccaniche completa (immunità, effetto, resistenza, durata), note strategiche (💡), spiegazione dettagliata dell'escalation *Burn* 1→2→3, note su *Poison*/*Badly Poisoned* fuori dal combattimento. Aggiunta tabella riassuntiva finale con tutti i campi. File riscritto integralmente.

## [2026-05-16] ingest | strategie-di-combattimento
- **Tipo:** Ingest
- **Fonte:** `raw/POKEROLE COREBOOK 2.0 (2).pdf` — pp. 50-54
- **File creato:** `01_Regole_Base/Strategie_di_Combattimento.md`
- **Contenuto:** STAB (+1 dado bonus), Critical Hit (3+ successi extra = +2 dadi, 2+ per High-Critical), Effectiveness (riepilogo), Clash (*Strength*/*Special* + *Clash*, 1 volta/Round, 1 danno reciproco), Evasion (*Dexterity* + *Evasion*), Holding Action, Taking Cover (bonus DEF/SDEF da copertura), Low Accuracy Moves (−1/−2/−3 successi), Attribute Increase/Reduction (buff/debuff temporanei, no stacking, cap a 10), Holding Back (metà danno o danno regolare al posto di Lethal), Priority/Low Priority, Healing In-Battle (3 HP/Round limit, Complete Heal 5 HP, Will Point cost), Shield Moves (riducono danno fino a 0).
- **Aggiornamenti:** `index.md` (segnato ✅), `ingest_queue.md` (segnato `[x]`).

## [2026-05-16] ingest | azioni-multiple
- **Tipo:** Ingest
- **Fonte:** `raw/POKEROLE COREBOOK 2.0 (2).pdf` — p. 49
- **File creato:** `01_Regole_Base/Azioni_Multiple.md`
- **Contenuto:** Sistema delle Multiple Actions (regola opzionale): tabella successi richiesti (1ª=1, 2ª=2, 3ª=3, 4ª=4, 5ª=5), ordine di risoluzione (2ª+ dopo tutti gli altri, eccezione Evasion/Clash/Successive Actions), penalità cumulative (Pain Penalizations + Low Accuracy + Status), comportamento Pokémon senza ordini (max 1-2 azioni), esempio completo di Chuckie con 3 azioni simultanee, consigli strategici.
- **Aggiornamenti:** `index.md` (segnato ✅), `ingest_queue.md` (segnato `[x]`).

## [2026-05-16] ingest | meteo-e-scenario
- **Tipo:** Ingest
- **Fonte:** `raw/POKEROLE COREBOOK 2.0 (2).pdf` — pp. 55-57
- **File creato:** `01_Regole_Base/Meteo_e_Scenario.md`
- **Contenuto:** 7 Weather Conditions: *Sunny* (+1 dado Fuoco, −1 danno Acqua, no Frozen), *Harsh Sunlight* (+1 dado Fuoco, Acqua fallisce, +2 dadi Burn, blocca altri meteo), *Rain* (+1 dado Acqua, −1 danno Fuoco, −3 successi curare Burn), *Typhoon* (+1 dado Acqua, Fuoco fallisce, no Burn, blocca altri meteo), *Sandstorm* (1 danno/Round a non-Roccia/Terra/Acciaio, +1 SDEF Roccia), *Strong Winds* (+1 dado Volante, debolezze Volante neutralizzate, no Hazard/Barrier, blocca altri meteo), *Hail* (1 danno/Round a non-Ghiaccio, +1 DEF Ghiaccio). Environmental Challenges opzionali (Fog, Muddy, On Fire!, Electric Poles). Tabella riassuntiva comparativa.
- **Aggiornamenti:** `index.md` (segnato ✅), `ingest_queue.md` (segnato `[x]`).

## [2026-05-16] ingest | creazione-personaggio
- **Tipo:** Ingest
- **Fonte:** `raw/POKEROLE COREBOOK 2.0 (2).pdf` — pp. 18-20
- **File creato:** `02_Allenatori/Creazione_Personaggio.md`
- **Contenuto:** Guida completa alla creazione del Trainer: Concept (occupazione, personalità, obiettivo), 8 domande obbligatorie di Background, distribuzione punti Attribute (base 1 + extra per Età/Rank), Social Attributes, Skills (5 punti base, Skill Limit per Rank), tabella punti per Rank (*Starter*→*Professional*), tabella punti per Età (Kids/Teens/Adults/Seniors), calcolo HP e Will, compilazione Trainer Sheet (3 sezioni: Card, Attributes/Skills, Backpack), denaro iniziale $1.500, checklist rapida.
- **Aggiornamenti:** `index.md` (segnato ✅), `ingest_queue.md` (segnato `[x]`).

## [2026-05-16] ingest | scheda-allenatore
- **Tipo:** Ingest
- **Fonte:** `raw/POKEROLE COREBOOK 2.0 (2).pdf` — pp. 19-20
- **File creato:** `02_Allenatori/Scheda_Allenatore.md`
- **Contenuto:** Guida campo per campo alla Trainer Character Sheet. Trainer's Card Window (11 campi: immagine, Rank, nome, età, giocatore, concept, Nature/Confidence, denaro $1.500, HP, Will, Party). Attributes & Skills Window (5 campi: 4 Attributes base 1, 16 Skills in 4 categorie, 5 Social Attributes base 1, Achievements, Pokédex Info). Backpack Window (4 sezioni: Potion's Pocket, Small Pocket per uso in-battle, Main Pocket no-battle, Gym Badges). Tabelle per Età e Rank. Esempio compilazione Starter Teen. Checklist di compilazione.
- **Aggiornamenti:** `index.md` (segnato ✅), `ingest_queue.md` (segnato `[x]`).

## [2026-05-16] meta | riscrittura-indice
- **Tipo:** Meta / Organizzazione
- **File modificato:** `index.md`
- **Motivo:** Richiesta dell'utente di trasformare l'indice in "un vero e proprio indice per la wiki intera", abbandonando la formattazione a tabella di monitoraggio.
- **Modifiche:** Rimossa la sezione "Prossimi Ingest", rimossi i checkmark ✅ e la colonna "Fonte PDF". L'indice è ora una struttura pulita a elenchi puntati organizzata per categorie, adatta come Home Page definitiva della Wiki. Le funzionalità di tracking degli ingest restano delegate a `ingest_queue.md`.

## [2026-05-16] ingest | creazione-pokemon
- **Tipo:** Ingest
- **Fonte:** `raw/POKEROLE COREBOOK 2.0 (2).pdf` — pp. 21-22
- **File creato:** `02_Allenatori/Creazione_Pokemon.md`
- **Contenuto:** Guida alla creazione dello Starter e compilazione della Pokémon Character Sheet (28 campi). Spiegazione del controllo narrativo (gestito dallo Storyteller), scelta tramite l'icona Starter, limiti sulle Moves (massimo *Insight* + 2, Rank <= attuale). Spiegazione dettagliata delle 4 sezioni: Pokédex Window, Quick References, Attributes & Skills, Socials & Info. Valori iniziali (Social=1, Happiness/Loyalty=2).
- **Aggiornamenti:** `ingest_queue.md` (segnato `[x]`).

## [2026-05-16] ingest | natures
- **Tipo:** Ingest
- **Fonte:** `raw/POKEROLE COREBOOK 2.0 (2).pdf` — pp. 38-41
- **File creato:** `02_Allenatori/Natures.md`
- **Contenuto:** Sistema delle Nature per Umani e Pokémon. Spiegazione meccanica: umani possono agire contro natura spendendo Will Points, i Pokémon seguono l'istinto. Reward: agire secondo Natura fa recuperare Will Points. Statistica Confidence (Fiducia): impatto sociale e gestione stress. Tabella completa delle 25 Nature raggruppate per valore di Confidence decrescente (10 → 4), includendo parole chiave e descrizioni narrative di base. Regola sull'immutabilità della Natura umana vs potenziale cambiamento dei Pokémon tramite evoluzione.
- **Aggiornamenti:** `ingest_queue.md` (segnato `[x]`).

## [2026-05-16] ingest | happiness-e-loyalty
- **Tipo:** Ingest
- **Fonte:** `raw/POKEROLE COREBOOK 2.0 (2).pdf` — pp. 27-28
- **File creato:** `02_Allenatori/Happiness_e_Loyalty.md`
- **Contenuto:** Meccaniche per Happiness e Loyalty (scala da 0 a 5). Modificatori post-cattura: Loyalty scende dell'ammontare di Pain Penalizations inflitte, Happiness varia da 0 a 2 in base alla correttezza dello scontro. Tabella descrittiva per i livelli di Happiness (0: Miserable → 5: True Happiness) e per i livelli di Loyalty (0: Ostile → 5: Legame Assoluto). Test di Evoluzione: tiro sul Social Attribute più alto dell'Allenatore (richiesti 2 successi per evitare la perdita di 1 punto Loyalty a causa del drastico cambiamento). (Nota: La regola sui Will Points di pag. 27 era già stata unita in `HP_e_Will.md`).
- **Aggiornamenti:** `ingest_queue.md` (segnato `[x]`).

## [2026-05-16] ingest | creare-una-storia
- **Tipo:** Ingest
- **Fonte:** `raw/POKEROLE COREBOOK 2.0 (2).pdf` — pp. 32-37
- **File creato:** `02_Allenatori/Creare_una_Storia.md`
- **Contenuto:** Guida completa alla conduzione del gioco per GM e Giocatori. Formati di avventura (Pokémon Journey, Missions, Intrigue). Formati narrativi (Episodic, Chronicle, Storyteller Rotation). Le "13 Leggi dello Storytelling" per il GM (es. non giocare per vincere, privilegiare il dramma sulla meccanica, usare musica/tools). Trucchi per il GM (improvvisazione, incontri casuali, indizi di emergenza, rinforzo positivo). Doveri dei giocatori (Active Roleplay, ascoltare, lavorare in squadra, non focalizzarsi troppo sulle regole).
- **Aggiornamenti:** `ingest_queue.md` (segnato `[x]`).
## [2026-05-16] meta | integrazione-immagini
- **Tipo:** Meta / Contenuti Multimediali
- **Azioni eseguite:** 
  1. Utilizzato script Python (`fitz`) per estrarre immagini ad alta risoluzione dal manuale PDF (`type_effectiveness.png`, `trainer_sheet.png`, `pokemon_sheet.png`) salvate in `wiki/assets/images/`.
  2. Aggiornati i file `Tipi_Pokemon.md`, `Scheda_Allenatore.md` e `Creazione_Pokemon.md` includendo i percorsi relativi alle nuove immagini generate.
  3. Aggiunta una nuova direttiva ufficiale in `ingest_queue.md` per estrarre sistematicamente schede, icone e tabelle complesse come PNG durante i futuri ingest.

## [2026-05-16] ingest | pokedex-introduzione
- **Tipo:** Ingest
- **Fonte:** `raw/POKEROLE COREBOOK 2.0 (2).pdf` — pp. 88-89
- **File creato:** `03_Pokedex/Pokedex_Introduzione.md`
- **Contenuto:** Legenda dei campi del Pokédex (Name, Limits, Base HP, Starter Icon). Regole di lore e meccaniche per il Breeding (ereditarietà dello stadio base della madre, possibilità di tratti rari, focus sul roleplay e non sul grinding). Spiegazione delle Form Variations e Mega-Evoluzioni (consiglio di usare una scheda separata per ogni forma). Consigli per il GM sul World Building (iniziare in piccolo, evitare il railroading).
- **Aggiornamenti:** `ingest_queue.md` (segnato `[x]`).

## [2026-05-16] ingest | moves-introduzione
- **Tipo:** Ingest
- **Fonte:** `raw/POKEROLE COREBOOK 2.0 (2).pdf` — pp. 346-348
- **File creato:** `04_Moves_e_Abilities/Moves_Introduzione.md`
- **Contenuto:** Regole base delle Mosse (solo nel turno/Clash, una volta per round, limite mosse Insight+2, le Social non possono essere evase). Spiegazione strutturata di come leggere il blocco di una Mossa nel manuale. Estrazione tramite Python di 3 immagini referenziali (`moves_reading.png`, `moves_icons_1.png`, `moves_icons_2.png`) per coprire le legende visive per Categoria (Physical, Special, Support), Target (Battlefield, Area, ecc.), e Status/Effetti (Heal costa 1 Will, Chance Dice, High Crit, Block, ecc.). Inserimento delle immagini nella pagina.
- **Aggiornamenti:** `ingest_queue.md` (segnato `[x]`).

## [2026-05-16] ingest | equipaggiamento-base
- **Tipo:** Ingest
- **Fonte:** `raw/POKEROLE COREBOOK 2.0 (2).pdf` — p. 76
- **File creato:** `05_Strumenti_e_Oggetti/Equipaggiamento_Base.md`
- **Contenuto:** Istruzioni sulle necessità di base di un Trainer (Denaro, Cibo, Oggetti curativi, Attrezzatura da campeggio, Trasporti). Tabella del "Trainer Gear" con prezzi in PokéDollars (es. Pokédex a $5.000, Tende da $800-$2.500, Sacco a pelo, Fornello, ecc.). Consiglio di usare le abilità dei Pokémon per evitare acquisti inutili (es. usare Liane invece di comprare una corda). Nota di lore: gli oggetti ingombranti acquistati vengono forniti all'interno di Pokéball speciali per essere trasportati senza peso.
- **Aggiornamenti:** `ingest_queue.md` (segnato `[x]`).

## [2026-05-16] ingest | healing-items
- **Tipo:** Ingest
- **Fonte:** `raw/POKEROLE COREBOOK 2.0 (2).pdf` — pp. 77-79
- **File creato:** `05_Strumenti_e_Oggetti/Healing_Items.md`
- **Contenuto:** Catalogo completo degli oggetti curativi. Pozioni (in "Unità" da 2 a 14, con Max Potion e Full Restore bannate dalle competizioni per bypass dei limiti). Status Heals (Antidoti, Ice Heal, ecc.). Bacche curative (da consumare intere in natura). Erboristeria (Energy Root, Heal Powder, ecc.: cure potenti ma dal sapore terribile che riducono l'Happiness del Pokémon). Revive (frammenti di pietre magiche non creabili dai giocatori). Energy Drinks per il recupero fuori combattimento. Le tabelle non sono state estratte come immagini ma trascritte in Markdown per facilitare la ricerca e l'accessibilità.

## [2026-05-18] ingest | database-moves
- **Tipo:** Ingest / API Script
- **Fonte:** Database Ufficiale `Pokerole-Data` su GitHub (`v2.0/Moves/`)
- **Azioni eseguite:**
  1. Aggiornato `wiki/00_Meta/ingest_moves_json.py` con supporto **resume**: le mosse già presenti su disco vengono saltate automaticamente, permettendo di riprendere l'ingest senza riscrivere i file esistenti.
  2. Aggiunto import mancante `urllib.parse` per la codifica corretta degli URL con spazi e caratteri speciali.
  3. Eseguito lo script: 261 mosse già presenti saltate, **473 mosse generate in questa sessione**.
  4. Totale finale: **734 file Markdown** in `wiki/04_Moves_e_Abilities/Mosse/`, dalla A (Absorb) alla Z (Zippy Zap).
- **Formato file:** Ogni Move include frontmatter YAML (title, category, tags), intestazione con Tipo e Categoria, campi Accuracy / Damage / Target / Effect, e descrizione narrativa.
- **Aggiornamenti:** `ingest_queue.md` (segnato `[x]`).

## [2026-05-18] ingest | mosse-tratti-icons
- **Tipo:** Ingest / API Script
- **Fonte:** Database Ufficiale `Pokerole-Data` su GitHub
- **Azioni eseguite:**
  1. Scaricato master zip repository per ottenere tutti i file JSON delle mosse localmente.
  2. Generati 23 file Markdown esplicativi dentro `wiki/04_Moves_e_Abilities/Tratti/` corrispondenti ai vecchi "icon effects" (es. Lethal, Sound Based, Status Condition).
  3. Modificate tutte le 734 mosse esistenti, inserendo il campo `- **Traits:**` con Wikilink dinamici (es. `[[Status_Condition]] (Burn Chance Dice 1)`) tramite lettura di `Attributes` e `AddedEffects` nativi dei JSON originali.

## [2026-05-16] ingest | pokedex-kanto-json-revised
- **Tipo:** Ingest / API Script
- **Fonte:** Database Ufficiale `Pokerole-Data` su GitHub
- **Azioni eseguite:** 
  1. Aggiornate le regole in `ingest_queue.md`: vietati gli screenshot a pagina intera, obbligo di usare i Wikilink per mosse e abilità.
  2. Modificato lo script `wiki/00_Meta/ingest_kanto_json.py`: rimosso l'inserimento dell'immagine a fondo pagina e aggiunte le parentesi quadre (`[[Nome]]`) intorno alle Mosse e alle Abilità.
  3. Eliminati i vecchi file generati ed eliminate le vecchie immagini PNG a pagina intera dalla cartella assets.
  4. Rieseguito lo script per generare 151 file Markdown puri, perfetti e pronti per connettersi al database delle mosse futuro.
- **Aggiornamenti:** `ingest_queue.md` (segnato `[x]`).

## [2026-05-18] ingest | creazione-scheda-bulbasaur-base
- **Tipo:** Ingest / Creazione Personaggio
- **Fonte:** Regole di creazione da `wiki/02_Allenatori/Creazione_Pokemon.md` e statistiche da `wiki/03_Pokedex/Kanto/0001_Bulbasaur.md`
- **File creato:** `wiki/02_Allenatori/Scheda_Pokemon_Bulbasaur.md`
- **Contenuto:** Scheda personaggio compilata di un Bulbasaur base di Rank *Starter* pronto all'uso, con calcoli di HP, Will, Initiative, Evasion, Clash, attribuzione delle 5 starting Skill, scelta della natura *Docile* (Confidence 7), dell'abilità *Overgrow* e pre-calcolo dei dadi di precisione (Accuracy) e danno delle mosse di partenza (*Tackle* e *Growl*).
- **Aggiornamenti:** `wiki/index.md` (aggiunto link all'indice generale).

## [2026-05-18] ingest | riorganizzazione-schede-e-venusaur-ace
- **Tipo:** Ingest / Riorganizzazione e Creazione Personaggio
- **Fonte:** Regole di creazione da `wiki/02_Allenatori/Creazione_Pokemon.md` e statistiche da `wiki/03_Pokedex/Kanto/0003_Venusaur.md`
- **File creati:** `wiki/schede/Venusaur_Scheda.md` (Venusaur Ace Rank) e `wiki/schede/Bulbasaur_Scheda.md` (Bulbasaur Starter Rank, spostato per uniformità).
- **Contenuto:** 
  1. Creazione della nuova cartella dedicata `wiki/schede/` per raggruppare tutte le schede dei Pokémon.
  2. Compilazione della scheda personaggio per un Venusaur di Rank *Ace* pronto all'uso, con calcoli avanzati di HP (9), Will (6), Initiative (5), Evasion (6), Clash (5), Defense (4), Special Defense (4), attribuzione di 14 punti Skill e 6 punti Social extra, scelta della natura *Calm* (Confidence 8), dell'abilità *Overgrow* e pre-calcolo delle mosse *[[Tackle]]*, *[[Leech_Seed]]*, *[[Vine_Whip]]*, *[[Razor_Leaf]]*, *[[Synthesis]]*, *[[Solar_Beam]]*.
  3. Spostamento di Bulbasaur base nella cartella `schede/`.
- **Aggiornamenti:** `wiki/index.md` (aggiornati i link semantici all'indice generale).

## [2026-05-19] lint | audit-completo-e-pulizia-link

- **Tipo:** Lint / Manutenzione
- **Azioni eseguite:**
  1. **Audit completo:** Analizzati 933 file .md, 3.666 link validi, 521 link rotti identificati, 404 file orfani censiti.
  2. **Tratti mancanti creati (7):** `TerrainEffect.md`, `IgnoreShield.md`, `UserFaints.md`, `AlwaysCrit.md`, `Rampage.md`, `ResistedWithDefense.md`, `ResetTerrain.md` in `04_Moves_e_Abilities/Tratti/`. Risolti ~30 link rotti dalle mosse.
  3. **Duplicato Charge risolto:** Rinominato `Tratti/Charge.md` → `Tratti/Charge_Trait.md`. Aggiornate 15 mosse che referenziavano `[[Charge]]` come trait → `[[Charge_Trait]]`.
  4. **Pagine Tipo individuali create (18):** Generata cartella `03_Pokedex/Tipi/` con file per ogni tipo in italiano (Fuoco.md, Acqua.md, Erba.md, ecc.). Risolti ~30 link rotti dalle schede compilate.
  5. **Index.md ripulito:** 15 link a pagine non ancora create marcati con 🔥 e nota *(da creare)* per chiarezza.
  6. **Catene evolutive aggiunte:** Inserita sezione `## Correlati` con `### Catena Evolutiva` in 124 Pokémon Kanto, collegandoli ai loro compagni di linea evolutiva.
- **Link rotti residui:** ~300 link a Abilities mancanti (es. `[[Overgrow]]`, `[[Chlorophyll]]`). Richiedono ingest dedicato dal repository Pokerole-Data.
- **Script di audit:** Salvato in `00_Meta/audit_links.ps1` per futuri controlli.

## [2026-05-19] lint | riordino-struttura-progetto
- **Tipo:** Lint / Riorganizzazione
- **Azioni eseguite:**
  1. **Eliminati file temporanei dalla root:** `_extract_strat.txt` e `_extract_types.txt` (estratti PDF già ingestati, non più necessari).
  2. **Spostata `wiki/schede/Venusaur_Scheda.md`** in `wiki/02_Allenatori/` (posizione logicamente corretta).
  3. **Eliminata `wiki/schede/Bulbasaur_Scheda.md`** (file vuoto, placeholder) e rimossa la cartella `wiki/schede/`.
  4. **Aggiornato `rules.md` §2:** Alberatura di riferimento allineata alla struttura reale (`raw/` vs `00_Raw_Sources/`, `Mosse/` vs `Moves/`, `Tratti/` vs `Abilities/`, `Tipi/` vs `Tipi_Pokemon/`). Aggiunto `ingest_queue.md` e `assets/` all'alberatura.
  5. **Aggiornato `index.md`:** `[[Bulbasaur_Scheda]]` marcato come 🔥 *(da creare)*.
- **Stato post-riordino:** Struttura cartelle e `rules.md` ora coerenti tra loro.

## [2026-05-19] lint | audit-link-e-struttura-wiki
- **Tipo:** Lint / Audit strutturale
- **Strumento:** Analisi manuale + `audit_report_v2.txt`
- **Problemi trovati:**
  1. **Bug sintassi wikilink `\|`:** 35+ occorrenze in 13 file usavano `[[File\|Alias]]` invece del corretto `[[File|Alias]]`. Causa: backslash spurio generato da qualche script o editor.
  2. **Link tipo specifici via Tipi_Pokemon:** Pattern `[[Tipi_Pokemon|Fuoco]]` ecc. in Meteo_e_Scenario.md, Status_Conditions.md, Strategie_di_Combattimento.md. Sintatticamente validi ma non navigano alla pagina tipo individuale.
  3. **Template headings non aggiornati in rules.md:** I template prescritti (§5) non corrispondevano alle strutture reali dei file bulk-ingestati (Mosse, Pokédex, Tratti).
  4. **Link rotti non risolvibili ora:** ~440 link ad Abilities Pokémon non ancora create (Overgrow, Chlorophyll, ecc.); ~15 link a pagine future (Allenare_Pokemon, Catturare_Pokemon, ecc.) — tutti in `ingest_queue.md`.
  5. **File orfani:** ~280 file Mosse non referenziati da altri file — accettabile, sono database indicizzato alfabeticamente.
- **Azioni eseguite:**
  1. **Fix `\|` → `|`** in tutti e 13 i file interessati (replace globale sed).
  2. **Fix link tipo:** `[[Tipi_Pokemon|Fuoco]]` → `[[Fuoco]]` ecc. per tutti i 18 tipi in tutti i file di regole.
  3. **Aggiornato `rules.md` §5:** Template strutturali riscritti per riflettere la struttura reale di Mosse (compatto), Tratti (compatto), Pokédex (standard con `## Statistiche (Attributes & Limits)`, `## Mosse (Learnset)`, `## Correlati`).
- **Stato post-audit:** 0 file senza YAML frontmatter (esclusi index/log/queue). 0 occorrenze di `\|`. Link tipo specifici ora corretti. Link rotti residui tutti da ingest futuro.
- **Residui da risolvere (prossimi ingest):** Database Abilities (PDF pp. 434-472), Allenare_Pokemon, Catturare_Pokemon, Pokemon_Contests, ecc. (vedi `ingest_queue.md`).

## [2026-05-19] ingest | pokeball
- **Tipo:** Ingest
- **Fonte:** `raw/POKEROLE COREBOOK 2.0 (2).pdf` — pp. 69-71, 80
- **File creato:** `05_Strumenti_e_Oggetti/Pokeball.md`
- **Contenuto:** Meccaniche del Catch Roll (Dice Pool per tipo di Pokéball, bonus di condizione fino a +3 successi, successi richiesti per Rank da *Starter* a *Professional*), regola su Pokémon Svenuto (perdita bonus), cosa le Pokéball possono/non possono trasportare, Pokéball standard (Pokéball/Greatball/Ultraball/Masterball con prezzi), Pokéball speciali (Premier/Luxury/Cherish/UB/Dynamax/Master Ball), altri metodi per ottenere Pokémon (acquisto, adozione, scambio, rilascio) con regole su Happiness/Loyalty.
- **Aggiornamenti:** `index.md` (rimosso 🔥), `ingest_queue.md` (segnato `[x]`).

## [2026-05-19] ingest | pokemon-care-items
- **Tipo:** Ingest
- **Fonte:** `raw/POKEROLE COREBOOK 2.0 (2).pdf` — pp. 81-82
- **File creato:** `05_Strumenti_e_Oggetti/Pokemon_Care_Items.md`
- **Contenuto:** Cibo quotidiano (Dry Food Pack/Gourmet/High Performance con effetto Training Roll), Vitamine monouso (Protein/Iron/Calcium/Zinc/Carbos/PP Up/HP Up/Rare Candy — +1 Attribute o +2 Will/HP per un mese, non superano il Limit), regole di stacking, Grooming Kit/Costume/Accessory (+1 Confidence).
- **Aggiornamenti:** `index.md` (rimosso 🔥), `ingest_queue.md` (segnato `[x]`).

## [2026-05-19] ingest | held-items
- **Tipo:** Ingest
- **Fonte:** `raw/POKEROLE COREBOOK 2.0 (2).pdf` — pp. 84-85 (pp. 86-87 solo illustrazioni)
- **File creato:** `05_Strumenti_e_Oggetti/Held_Items.md`
- **Contenuto:** Regole generali Held Item (uno attivo per scena, no stacking stesso Attribute, esclusivi Pokémon, non in vendita). 17 oggetti Type Damage Boost (da Black Belt a Twisted Spoon, con rarità e tipo potenziato). 10 oggetti con effetti speciali: Eviolite (Defense/Sp.Def +1 non-evoluti), Quick Claw (Initiative +2), Life Orb (danno + recoil a tutti gli attacchi), Expert Belt (danno Super Effective), Wide Lens (Accuracy), Rocky Helmet (contrattacco fisico), King's Rock, Amulet Coin (×2 denaro), Lucky Egg (×2 vittorie per evoluzione), Razor Fang. 5 oggetti esclusivi per specie: Light Ball (Pikachu), Lucky Punch (Chansey/Blissey), Stick (Farfetch'd), Thick Club (Cubone/Marowak), Razor Claw.
- **Aggiornamenti:** `index.md` (rimosso 🔥), `ingest_queue.md` (segnato `[x]`).

## [2026-05-19] ingest | evolutionary-items
- **Tipo:** Ingest
- **Fonte:** `raw/POKEROLE COREBOOK 2.0 (2).pdf` — p. 83
- **File creato:** `05_Strumenti_e_Oggetti/Evolutionary_Items.md`
- **Contenuto:** Panoramica sui tre metodi evolutivi (livello, Happiness/Loyalty, influenza esterna). Pietre evolutive: Fire Stone/Thunder Stone/Water Stone a $5.000; Leaf Stone/Moon Stone/Sun Stone/Shiny Stone/Dusk Stone/Dawn Stone non in vendita. Trading Machine e il meccanismo di radiazione che scatena l'evoluzione. Evoluzione via Held Item (combinazione con Trading Machine). Regole generali sugli Held Item (uno attivo per scena, no stacking con mosse sullo stesso Attribute, non per umani, non in vendita — trovati in avventura).
- **Aggiornamenti:** `index.md` (rimosso 🔥), `ingest_queue.md` (segnato `[x]`).

## [2026-05-19] ingest | il-mondo-dei-pokemon
- **Tipo:** Ingest
- **Fonte:** `raw/POKEROLE COREBOOK 2.0 (2).pdf` — pp. 8-12, 14-16 (pp. 13, 17 solo illustrazioni)
- **File creato:** `06_Lore_e_Mondo/Il_Mondo_dei_Pokemon.md`
- **Contenuto:** Panoramica del mondo (differenze dalla realtà, ruolo dei Pokémon). Pocket Monsters e origine del nome. Evoluzione dei Pokémon (trigger: crescita, energia, cura, situazioni estreme). Vita nel mondo Pokémon (tecnologia ibrida, ruolo umano subordinato ai Pokémon). Interazione umani/Pokémon. 8 regioni con descrizione lore: Kanto, Johto, Hoenn, Sinnoh, Unova, Kalos, Alola, Galar. Lega Pokémon (licenze, autorità, Pokémon Center con struttura interna, Pokémon Gym e Gym Badge, requisito 8 badge per il Torneo). Elite Four e Champion (come si ottengono i titoli). 7 organizzazioni antagoniste: Team Rocket (Kanto/Johto), Team Aqua & Magma (Hoenn), Team Plasma (Unova), Team Flare (Kalos), Team Galactic (Sinnoh), Team Skull (Alola), Team Yell (Galar). Il Rivale. Diventare un Trainer (ruolo, aspirazioni, nota sulle armi come Plot Device).
- **Note:** Creata nuova cartella `wiki/06_Lore_e_Mondo/` per le sezioni di ambientazione e lore.
- **Aggiornamenti:** `index.md` (rimosso 🔥), `ingest_queue.md` (segnato `[x]`).

## [2026-05-19] ingest | introduzione
- **Tipo:** Ingest
- **Fonte:** `raw/POKEROLE COREBOOK 2.0 (2).pdf` — p. 7
- **File creato:** `01_Regole_Base/Introduzione.md`
- **Contenuto:** Definizione di GDR (analogia attore/giocattoli). Ruolo dello Storyteller (narratore, regista, non arbitro onnipotente — deve far divertire tutti). Cosa sono i Pokémon (flora/fauna di questo mondo, tra animali domestici e creature selvatiche). Ruolo del giocatore (creazione personaggio, non si è soli). I tre strumenti fondamentali: Immaginazione (fare l'impossibile nel gioco), Schede Personaggio (registrare capacità), Dadi (fortuna + abilità).
- **Aggiornamenti:** `index.md` (rimosso 🔥), `ingest_queue.md` (segnato `[x]`).

## [2026-05-19] ingest | catturare-pokemon
- **Tipo:** Ingest
- **Fonte:** `raw/POKEROLE COREBOOK 2.0 (2).pdf` — pp. 68-69 (pp. 69-71 già coperti da Pokeball.md)
- **File creato:** `06_Lore_e_Mondo/Catturare_Pokemon.md`
- **Contenuto:** Differenze tra Pokémon selvatici e allevati (adattamento vs sopravvivenza). Habitat (studio dell'ambiente, non si lancia a caso). Pokémon Speciali: Shiny (aspetto diverso, no cambio Tipo/Attributes), Forme Alternate (Tipo/Attributes/Abilities diverse), Varianti Regionali (adattamento ambientale multigenerazionale), Overgrown (+30-60% dimensioni, +1 Base HP, nascono così). Mosse e Abilità Nascoste (discrezione ST). Link alle meccaniche di cattura in Pokeball.md.
- **Aggiornamenti:** `index.md` (rimosso 🔥), `ingest_queue.md` (segnato `[x]`).

## [2026-05-19] ingest | allenare-pokemon
- **Tipo:** Ingest
- **Fonte:** `raw/POKEROLE COREBOOK 2.0 (2).pdf` — pp. 72-74 (p. 75 vuota)
- **File creato:** `06_Lore_e_Mondo/Allenare_Pokemon.md`
- **Contenuto:** Training Sessions (2h, una/giorno, bond-building). Rank Up: tiro Attribute/Social+Lore, tabella successi richiesti (Beginner 3 → Champion 48), limite Rank Trainer. Retrain: 3 successi, ridistribuisci Attribute/Skill/Mosse, Mosse esclusive perse per sempre. Pokémon disobbedienti (Rank superiore). Evoluzione tramite Vittorie (Fast 5, Medium 15, Slow 45), distribuzione bonus come Retrain. Overranking (blocco evoluzione → 1 Mossa Rank superiore, azzeramento Vittorie, max 1 Overrank; Forme Finali 20V). Limits (cap Attribute per specie, crescono con evoluzione, esempio Tyrogue→Hitmonlee). Insegnare/dimenticare Mosse (Retrain, limit Insight+2, Mosse esclusive perdute per sempre). Move Tutor. Day-Care Center (riduzione Vittorie a discrezione ST, well-behaved ≠ happy).
- **Aggiornamenti:** `index.md` (rimosso 🔥), `ingest_queue.md` (segnato `[x]`).

## [2026-05-19] ingest | pokemon-contests
- **Tipo:** Ingest
- **Fonte:** `raw/POKEROLE COREBOOK 2.0 (2).pdf` — pp. 63-67
- **File creato:** `06_Lore_e_Mondo/Pokemon_Contests.md`
- **Contenuto:** Cos'è un Pokémon Contest (talent show con Social Skills, no danni). Confidence/Stress: tabella stati emotivi (Full → Nervous → Freaking Out → Breakdown = squalifica). Struttura: Board, Contestants (max 8), Judges (preferenza segreta Attribute), Audience. 4 difficoltà (Normal 000/1succ → Master 000/4succ). 3 mazzi di carte: Reactions (Booing → Sheer Awe con Hearts e Confidence), Mishaps (imprevisti), Tricks (5 tipi per Social Attribute). Fasi dello show: Presentation Stage (tiro Social+ordine, 2 Trick Cards), Performance Runway (1d avanzamento, Social+Perform, Tricks prima del tiro per +1 Heart), Grand Finale (+5 Hearts al primo). Premi in denaro per 3 difficulty × 3 posti. 4 Coordinator Ranks (Normal→Super→Hyper→Master Coordinator) con requisiti ribbon e benefici Notoriety. 4 Notoriety Skills non re-trainabili: Fame, Supporters, Connections, Sponsors (scala 0→0k bi-settimanali).
- **Aggiornamenti:** `index.md` (rimosso 🔥), `ingest_queue.md` (segnato `[x]`).

## [2026-05-19] ingest | typeless-maneuvers
- **Tipo:** Ingest
- **Fonte:** `raw/POKEROLE COREBOOK 2.0 (2).pdf` — pp. 424-425
- **File creato:** `04_Moves_e_Abilities/Typeless_Maneuvers.md`
- **Contenuto:** Regole generali (no Clash, una/round, turno utente, uso in/fuori battaglia, Umani e Pokémon). 6 Manovre catalogate: Struggle (Dex+Brawl/Channel, Str/Spe+0), Grapple (Str+Brawl, Blocked con resistenza), Help Another (Accuracy come Chance Dice → +1 dado Alleato, max 6), Cover an Ally (copertura ranged in base alla taglia), Stabilize an Ally (Clever+Medicine, CPR su incosciente, Lethal riduce pool), Run Away (Dex+Athletic, esce dalla battaglia, fallisce se Blocked).
- **Aggiornamenti:** `index.md` (rimosso 🔥), `ingest_queue.md` (segnato `[x]`).

## [2026-05-19] ingest | max-moves
- **Tipo:** Ingest
- **Fonte:** `raw/POKEROLE COREBOOK 2.0 (2).pdf` — pp. 425-427
- **File creato:** `04_Moves_e_Abilities/Max_Moves.md`
- **Contenuto:** Regole Max Moves (solo Dynamax/Gigantamax, base deve essere Mossa Offensiva stesso Tipo, +2 Power, Added Effect sostituito, una/round, no Clash). Gigantamax Factor e G-Max Moves (personalizzabili, una sola per Pokémon, effetti extra per Rank: Beginner 1 → Master 6 personalizzabili). Lista 17 Max Moves per Tipo: potenziamento Alleati (Knuckle/Airstream/Quake/Ooze/Steelspike → +1 Attribute), indebolimento Nemici (Flutterby/Darkness/Wyrmwind/Phantasm/Strike → −1 Attribute), Meteo/Terrain (Lightning→Electric Terrain, Starfall→Misty Terrain, Flare→Sunny, Overgrowth→Grassy Terrain, Hailstorm→Hail, Rockfall→Sandstorm, Mindstorm→Psychic Terrain). Tabella G-Max Effect categories per Tipo.
- **Aggiornamenti:** `index.md` (rimosso 🔥), `ingest_queue.md` (segnato `[x]`).

## [2026-05-19] ingest | z-moves
- **Tipo:** Ingest
- **Fonte:** `raw/POKEROLE COREBOOK 2.0 (2).pdf` — pp. 428-430 (p. 431 vuota)
- **File creato:** `04_Moves_e_Abilities/Z-Moves.md`
- **Contenuto:** Lore origini Alola/Kahuna/Z-Crystals. Regole Z-Moves: entrambi tengono Z-Crystal + danza, una/giorno (extra costa 5 Will a Trainer e Pokémon), base stesso Tipo, Power = Base + Happiness + Loyalty, effetti base sostituiti, no Clash, no Lethal Damage, una Z-Crystal per party. Personalizzazione: effetti per Rank (Beginner 1 → Champion 6), singolo Target gratis, Attribute +/- = 1 Effetto, Status con Chance Dice, nome personalizzabile. Lista 18 Z-Moves con effetti di partenza suggeriti (da Savage Spin-Out/Bug a Hydro Vortex/Water). TM opzionali: dischi 000-000, richiede Training Session, Tipo libero, a discrezione ST.
- **Note extra:** Aggiunto Max Geyser (Water) a Max_Moves.md — era su p. 428, prima delle Z-Moves.
- **Aggiornamenti:** `index.md` (rimosso 🔥), `ingest_queue.md` (segnato `[x]`).

## [2026-05-19] ingest | strength-dexterity-chart
- **Tipo:** Ingest
- **Fonte:** `raw/POKEROLE COREBOOK 2.0 (2).pdf` — p. 432
- **File creato:** `04_Moves_e_Abilities/Strength_Dexterity_Chart.md`
- **Contenuto:** Strength Chart (Str 1-10 → capacità di sollevamento da 18 kg a 680 kg; +4 kg per punto Athletic; affetta da Pain Penalizations). Dexterity Chart (Dex 1-10 → velocità da 10 km/h a 160 km/h). Fling/Natural Gift (Tipo e Power da bacca, 17 sapori → 17 Tipi, Power 0-3). Secret Power/Nature Power (6 ambienti → effetti diversi: Paralysis, Flinch, −Accuracy, Sleep, Freeze, −Strength).
- **Aggiornamenti:** `index.md` (rimosso 🔥), `ingest_queue.md` (segnato `[x]`).

## [2026-05-19] ingest | faq-moves
- **Tipo:** Ingest
- **Fonte:** `raw/POKEROLE COREBOOK 2.0 (2).pdf` — p. 433
- **File creato:** `04_Moves_e_Abilities/FAQ_Moves.md`
- **Contenuto:** 15 FAQ ufficiali: Priority/cambio azione, estendere durate (ST discretion), no stack Attribute (solo con Abilities), aumentare danno Z/Max/G-Max (1 Effetto per dado), coesistenza Z+Max+G-Max (ST), Multiple Actions Evasion/Clash (eguaglia successi, ma conta come Azione), Evadere più volte (solo Double Team/Minimize), Ready to Fight (Switch e Switcher Moves), Pokémon svenuto → prossimo ready, range dinamico, target Alleato con mossa Foe (sì, raro ma utile), auto-danno (no), Out of Range (Fly/Dig, immunità), Ground su volanti (senza immunità sì), Dig da edifici (sì, dipende dal terreno), Protect/Wide Guard no stack.
- **Note extra:** Aggiornato `Strength_Dexterity_Chart.md` con le note Dexterity mancanti da p.433 (Athletic +2 km/h, Pain Penalizations camminare/strisciare, peso dimezza velocità).
- **Aggiornamenti:** `index.md` (rimosso 🔥), `ingest_queue.md` (segnato `[x]`).

## [2026-05-19] ingest | database-abilities
- **Tipo:** Ingest / Database
- **Fonte:** `raw/POKEROLE COREBOOK 2.0 (2).pdf` — pp. 434-472
- **File creati:** 258 file in `04_Moves_e_Abilities/Abilità/` (un file per Ability, A→Z)
- **Contenuto:** Tutte le Abilities del Corebook 2.0 con flavor text originale in inglese ed effetto meccanico completo. Include abilità base (Overgrow, Blaze, Torrent, ecc.), abilità Ultra-Beast (Beast Boost), abilità Leggendarie (Multitype, Power Construct, Battle Bond, ecc.), abilità dei Gigantamax (Hunger Switch, Shields Down), note speciali sulle Form-altering Abilities e le Curse Abilities.
- **Note:** I wikilink `[[NomeAbility]]` nelle schede Pokédex Kanto ora si risolvono correttamente verso questi file.
- **Aggiornamenti:** `index.md` (rimosso 🔥, aggiornato path cartella), `ingest_queue.md` (segnato `[x]`).

---

### sfide-avanzate
- **File:** `wiki/06_Lore_e_Mondo/Sfide_Avanzate.md`
- **Fonte:** PDF pp. 473-489
- **Contenuto:** Formati di avventura (Episode of the Week, Rival/Evil Team, League, Legends); Sistema dei Rivali (Attitudes, Relationships, Backgrounds, Unlike-Abilities x14); Pokémon League Challenge (Gym, Annual Tournament, Victory Road, Elite Four, Champion); Mega-Evolution (lore, regole: Mega-Stone + Key Stone, Final Stage, 1 Will Point, scena intera, possibile perdita controllo); Pokémon Leggendari (proprietà speciali, gestione narrativa); Legendary Ranking opzionale (Hero: +1 Attr min/limit, 1 Mossa, Heroic Ability; Guardian: HP+20, Max Attributes, All Z-Moves, x3 Abilities; Demi-God, God, Firstborn, Original One); BIG Leagues (Dynamax: Band+Stadium o Power Spot, HP+6, 3R o indefinito, immunità 6 effetti; Gigantamax: + Factor, HP+12)
- **Aggiornamenti:** `index.md` (rimosso 🔥), `ingest_queue.md` (segnato `[x]`).
