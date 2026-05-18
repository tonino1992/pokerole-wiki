---
title: Azioni Multiple
category: Rule
tags: [multiple_actions, azioni, round, successi, turno, combattimento, evasion, clash, successive_actions, critical_failure]
summary: "Regole per eseguire più azioni nello stesso Round: tabella dei successi richiesti, ordine di risoluzione, eccezioni per Evasion/Clash, interazione con Pain Penalizations e Critical Failure."
---

# Azioni Multiple

## Descrizione Generale

> *"This is where you get fast and furious. You can abuse your speed and intellect to divide your attention and perform multiple tasks at the same time."*

Il sistema delle **Multiple Actions** (regola opzionale) permette a un Pokémon o a un Allenatore di compiere **più di un'azione** nello stesso Round. Non si limitano al combattimento: un Allenatore potrebbe tentare di leggere un libro mentre guida, o schivare un attacco mentre invia un messaggio.

> *"Maybe you want to read a book while driving a car, or maybe you want to catch a ball and kick your foe while dodging bullet seeds. I'm not saying that everything is possible, but you can at least try! Worst case scenario: You die."*

---

## Meccaniche Dettagliate

### Come Funzionano

Per ogni azione, si tira normalmente la **Dice Pool** appropriata. Tuttavia, ogni azione **oltre la prima** richiede successi aggiuntivi per essere completata.

### Tabella dei Successi Richiesti

| Azione nel Round | Successi Richiesti |
|---|---|
| **1ª Azione** | **1** successo |
| **2ª Azione** | **2** successi |
| **3ª Azione** | **3** successi |
| **4ª Azione** | **4** successi |
| **5ª Azione** | **5** successi |

> ⚠️ Si possono eseguire al massimo **5 azioni per Round**. Più azioni si tentano, più diventa rischioso: se non si hanno abbastanza dadi, si rischia un [[Tirare_i_Dadi|Critical Failure]].

### Ordine di Risoluzione

| Regola | Dettaglio |
|---|---|
| **1ª Azione** | Si risolve nel Turn normale, seguendo l'ordine di Initiative |
| **2ª Azione e successive** | Si possono eseguire **solo dopo** che tutti gli altri Pokémon hanno avuto la possibilità di agire |
| **Eccezioni** | Le azioni di *Evasion*, *Clash* e le **Successive Actions** possono essere eseguite fuori da questo ordine |

> 💡 Se un Pokémon compie molte azioni nello stesso Round, significa che si muove a velocità impressionante: *"Running, jumping, dodging and attacking in an impressive manner."*

### Penalità Cumulative

Le Multiple Actions diventano progressivamente più difficili, e le penalità si accumulano:

| Tipo di Penalità | Effetto |
|---|---|
| **Successi aggiuntivi richiesti** | +1 per ogni azione oltre la prima (vedi tabella) |
| **[[Come_Funziona_il_Combattimento#Pain Penalizations\|Pain Penalizations]]** | Rimuovono successi dai tiri (−1 a metà HP, −2 a 1 HP) |
| **Low Accuracy** | Le Moves a bassa precisione [[Strategie_di_Combattimento#Low Accuracy Moves\|rimuovono ulteriori successi]] |
| **Altre penalità** | Qualsiasi altra penalità attiva (es. da [[Status_Conditions|Status Conditions]]) |

> ⚠️ Tutte queste penalità si **sommano tra loro**. Un Pokémon a metà HP (−1 successo) che tenta una 3ª azione (3 successi richiesti) con una Move a Low Accuracy −2, ha bisogno effettivamente di **6 successi** per completare l'azione con successo.

---

## Evasion e Clash come Azioni

Sia l'*Evasion* che il *Clash* contano come **un'azione** ai fini delle Multiple Actions:

| Azione Difensiva | Dettaglio |
|---|---|
| **Evasion** | Conta come un'azione. Se è la 2ª azione del Round, richiede 2 successi nel tiro di *Dexterity* + *Evasion* |
| **Clash** | Conta come un'azione. Se è la 2ª azione del Round, richiede 2 successi nel tiro di *Strength*/*Special* + *Clash* |

> 💡 Un Pokémon che attacca e poi schiva (2 azioni totali) avrà bisogno di 2 successi nel tiro di Evasion. Pianifica attentamente: schivare costa un'azione, ma subire danno causa Pain Penalizations che rendono tutto più difficile.

---

## Pokémon Senza Ordini

> *"When a Pokémon is acting on its own, they usually won't make more than one or two actions, even if they are capable of doing more."*

Un Pokémon che combatte **senza ordini** dell'Allenatore (ad esempio se l'Allenatore è svenuto, assente o ha scelto *Enter the Fray*) tenderà a essere conservativo, limitandosi a 1-2 azioni per Round anche se la sua Dice Pool gli permetterebbe di più. Il comportamento dipende dalla [[Natures|Nature]] del Pokémon.

---

## Esempio dal Manuale

> *Chuckie vuole cavalcare un Tauros selvatico e inviare un messaggio al Professor Oak con le sue scoperte. Sale in groppa al Pokémon quando scopre che i Tauros selvatici non gradiscono essere cavalcati. Improvvisamente, una freccia vola nell'aria verso di lui.*
>
> *Chuckie, essendo un uomo di scienza, decide che informare il Professor Oak è più importante, ma tiene anche alla propria vita. Decide di fare tutto contemporaneamente.*

### Le 3 Azioni di Chuckie

| # | Azione | Dice Pool | Successi Richiesti | Risultato |
|---|---|---|---|---|
| **1ª** | Restare in sella al Tauros | *Dexterity* + *Athletic* | **1** | ✅ Il Tauros si scuote violentemente, ma Chuckie resta in sella |
| **2ª** | Schivare la freccia | *Dexterity* + *Evasion* | **2** | ✅ Si sposta agilmente dalla traiettoria della freccia |
| **3ª** | Inviare il messaggio a Prof. Oak | *Clever* + *Science* | **3** | ✅ Il Professor Oak ha ricevuto il messaggio! |

> 💡 Questo esempio mostra che le Multiple Actions non sono solo per il combattimento: qualsiasi combinazione di azioni è possibile, purché si abbiano abbastanza successi. Chuckie aveva punteggi alti in *Dexterity*, *Evasion*, *Clever* e *Science*, il che gli ha permesso di superare anche la soglia della 3ª azione.

---

## Consigli Strategici

> 💡 **Non esagerare.** Ogni azione extra oltre la prima aumenta il rischio di Critical Failure. Se il tuo Pokémon ha una Dice Pool bassa, è meglio concentrarsi su un'azione efficace piuttosto che tentarne tre mediocri.

> 💡 **La 2ª azione è la più comune.** Nella pratica, la combinazione più frequente è attaccare e poi schivare (o viceversa), per un totale di 2 azioni. La 3ª azione è fattibile solo per Pokémon di Rank alto con Dice Pool ampie.

> 💡 **Rank e Multiple Actions.** I Pokémon di [[Ranking|Rank]] più alto hanno Skills più elevate, il che significa Dice Pool più grandi e maggiore capacità di gestire le Multiple Actions. Un Pokémon *Champion* con Skills al massimo può tentare 3-4 azioni con relativa sicurezza.

> ⚠️ **Il rischio del Critical Failure.** Tentare una 4ª o 5ª azione con una Dice Pool insufficiente può portare a un [[Tirare_i_Dadi|Critical Failure]] (3+ successi mancanti), con conseguenze potenzialmente disastrose.

---

## Correlati

- [[Come_Funziona_il_Combattimento]] — Struttura del Round e del Turn in cui le Multiple Actions si inseriscono
- [[Tirare_i_Dadi]] — Dice Pool, successi e rischio di Critical Failure
- [[Strategie_di_Combattimento]] — Evasion, Clash, Priority e altre strategie che interagiscono con le azioni
- [[Attributes_e_Skills]] — Gli Attributes e Skills che determinano la grandezza della Dice Pool
- [[HP_e_Will]] — Pain Penalizations che riducono i successi disponibili
- [[Ranking]] — Il Rank influenza la Skill Limit e quindi la capacità di eseguire Multiple Actions
- [[Status_Conditions]] — Alcuni status (es. *Paralysis*, *Confused*) impattano i tiri per le Multiple Actions
- [[Natures]] — Influenzano il comportamento dei Pokémon senza ordini
