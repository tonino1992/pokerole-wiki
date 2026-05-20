# 📋 Pokérole Wiki — Coda Ingest

Questo file traccia gli ingest da effettuare in ordine di priorità.
Quando l'utente chiede di "procedere con il prossimo ingest", l'AI deve:

1. Consultare questo file e individuare il primo elemento `[ ]` (non completato).
2. Aprire il PDF in `raw/` ed estrarre le pagine indicate.
3. Creare il file Wiki.
4. **[REGOLE IMMAGINI]** Se la pagina contiene tabelle, schede o icone, è possibile estrarle dal PDF come immagini (salvandole in `wiki/assets/images/`) **SOLO** come elemento decorativo o aggiuntivo per parti specifiche. **È severamente vietato inserire screenshot di intere pagine del manuale**. Le immagini **NON devono MAI sostituire i testi**. Il contenuto deve essere sempre trascritto/ingestato testualmente.
   - **[REGOLE IMMAGINI — POKÉDEX]** Per ogni scheda Pokédex (regioni Johto in poi), includere l'official artwork scaricato in `wiki/assets/images/pokemon/`. Il file è nominato `{id:03d}.png` (es. `152.png` per Chikorita). Inserire nel frontmatter `image: "assets/images/pokemon/{id:03d}.png"` e nel corpo, subito dopo la riga `# Nome (#XXXX)`, il tag: `<img src="../../assets/images/pokemon/{id:03d}.png" align="right" width="220" style="margin-left:20px;margin-bottom:8px;">`. Le immagini dei Pokémon di Kanto (001-151) sono già presenti in `wiki/assets/images/pokemon/` e tutte le 151 schede Kanto sono già state aggiornate con questo layout.
5. **[REGOLE COLLEGAMENTI]** Ogni volta che il testo menziona elementi chiave del gioco come nomi di Mosse, Abilità, o Tipi, questi devono essere inseriti come **Wikilink** (es. `[[Tackle]]`, `[[Overgrow]]`). Questo permette la corretta indicizzazione e navigazione quando il database relativo verrà popolato.
6. Aggiornare `index.md` e `log.md`.
7. Segnare l'elemento come `[x]` in questo file.

---

## Priorità Alta — Regole Base (`01_Regole_Base/`)

- [x] **Tirare_i_Dadi** — Dice Pool, successi, difficoltà, Critical Failure *(PDF p. 29)*
- [x] **Attributes_e_Skills** — I 5 Attributes (*Strength, Dexterity, Vitality, Insight, Special*), Social Attributes (*Tough, Cool, Beauty, Clever, Cute*), Skills (Fight, Survival, Contest, Knowledge, Extra) *(PDF pp. 23-26)*
- [x] **HP_e_Will** — Health Points, Base HP, Lethal Damage, Will Points e il loro utilizzo *(PDF pp. 26-27)*
- [x] **Come_Funziona_il_Combattimento** — Struttura di un turno, ordine d'azione, Accuracy, Damage *(PDF pp. 44-49)*
- [x] **Ranking** — Sistema dei Ranks (*Starter* → *Champion*), Achievement e Benefits *(PDF pp. 30-31)*
- [x] **Status_Conditions** — *Burn*, *Paralysis*, *Sleep*, *Poison*, *Freeze*, *Confusion* e altri *(PDF pp. 57-62)*
- [x] **Tipi_Pokemon** — I 18 Types e la tabella Effectiveness *(PDF pp. 42-43)*
- [x] **Strategie_di_Combattimento** — STAB, Critical Hit, Effectiveness, Clash *(PDF pp. 50-54)*
- [x] **Azioni_Multiple** — Multiple Actions in combattimento *(PDF p. 49)*
- [x] **Meteo_e_Scenario** — Weather Conditions e i loro effetti *(PDF pp. 55-56)*

---

## Priorità Media — Allenatori (`02_Allenatori/`)

- [x] **Creazione_Personaggio** — Guida passo-passo per creare un Trainer *(PDF pp. 18-20)*
- [x] **Scheda_Allenatore** — Come compilare la Trainer Character Sheet *(PDF pp. 19-20)*
- [x] **Creazione_Pokemon** — Come creare un Pokémon iniziale *(PDF pp. 21-22)*
- [x] **Natures** — Le Natures e il sistema di *Confidence* *(PDF pp. 38-41)*
- [x] **Happiness_e_Loyalty** — Felicità, Lealtà e impatto meccanico *(PDF pp. 27-28)*
- [x] **Creare_una_Storia** — Consigli per lo Storyteller *(PDF pp. 32-37)*

---

## Priorità Media — Pokédex Intro e Moves Intro

- [x] **Pokedex_Introduzione** — Legenda statistiche Pokédex *(PDF pp. 88-89)*
- [x] **Moves_Introduzione** — Legenda icone effetto, leggere una Move *(PDF pp. 346-348)*

---

## Priorità Bassa — Strumenti e Oggetti (`05_Strumenti_e_Oggetti/`)

- [x] **Equipaggiamento_Base** — Lo zaino dell'Allenatore *(PDF p. 76)*
- [x] **Healing_Items** — Pozioni, Antidoti, Revive *(PDF pp. 77-79)*
- [x] **Pokeball** — Tipi di Pokéball e meccaniche di cattura *(PDF pp. 69-71, 80)*
- [x] **Pokemon_Care_Items** — Oggetti per cura e crescita *(PDF pp. 81-82)*
- [x] **Evolutionary_Items** — Pietre evolutive *(PDF p. 83)*
- [x] **Held_Items** — Oggetti tenuti in combattimento *(PDF pp. 83-87)*

---

## Priorità Bassa — Sezioni Extra

- [x] **Il_Mondo_dei_Pokemon** — Ambientazione, regioni, Lega *(PDF pp. 8-17)*
- [x] **Introduzione** — Cos'è un GDR, ruolo dello Storyteller *(PDF p. 7)*
- [x] **Catturare_Pokemon** — Habitat, Pokéball *(PDF pp. 68-71)*
- [x] **Allenare_Pokemon** — Training Sessions ed Evoluzione *(PDF pp. 72-75)*
- [x] **Pokemon_Contests** — Gare di bellezza *(PDF pp. 63-67)*
- [x] **Typeless_Maneuvers** — Manovre senza tipo *(PDF p. 424)*
- [x] **Max_Moves** — Max Moves (Dynamax) *(PDF pp. 425-427)*
- [x] **Z-Moves** — Z-Moves *(PDF pp. 428-431)*
- [x] **Strength_Dexterity_Chart** — Tabella riassuntiva *(PDF p. 432)*
- [x] **FAQ_Moves** — FAQ sulle Moves *(PDF p. 433)*
- [x] **Sfide_Avanzate** — Rivali, Mega-Evolution, Leggendari *(PDF pp. 473-489)*

---

## Bulk Ingest — Pokédex e Database Moves/Abilities

> Questi ingest sono massivi e verranno affrontati per blocchi tematici solo dopo le sezioni prioritarie.

- [x] **Pokédex Kanto** (001-151) *(PDF pp. 90-129)*
- [x] **Pokédex Johto** (152-251) *(PDF pp. 130-161)*
- [x] **Pokédex Hoenn** (252-386) *(PDF pp. 162-201)*
- [x] **Pokédex Sinnoh** (387-493) *(PDF pp. 202-232)*
- [x] **Pokédex Unova** (494-649) *(PDF pp. 233-273)*
- [ ] **Pokédex Kalos** (650-721) *(PDF pp. 274-293)*
- [ ] **Pokédex Alola** (722-809) *(PDF pp. 294-317)*
- [ ] **Pokédex Galar** (810-898) *(PDF pp. 318-345)*
- [x] **Database Moves** (per Type) *(PDF pp. 349-423)*
- [x] **Database Abilities** *(PDF pp. 434-472)*
