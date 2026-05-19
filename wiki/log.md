# 📋 Pokérole Wiki — Log delle Operazioni

Registro cronologico append-only. Ogni operazione viene registrata con data, tipo e descrizione.

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
