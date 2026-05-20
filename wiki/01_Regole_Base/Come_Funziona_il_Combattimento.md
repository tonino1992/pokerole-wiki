---
title: Come Funziona il Combattimento
category: Rule
tags: [combattimento, battle, initiative, round, turn, accuracy, damage, evasion, clash, trainer_actions, pain, lethal_damage, fainting, multiple_actions]
summary: "Struttura completa di un combattimento Pokémon: Initiative, Round, Turn, Accuracy, Damage, Evasion/Clash, azioni dell'Allenatore, Pain Penalizations e Lethal Damage."
---

# Come Funziona il Combattimento

## Descrizione Generale

Il combattimento tra Pokémon è lo sport principale nel mondo Pokémon. La Lega Pokémon si impegna a renderlo il più sicuro possibile nei match ufficiali, grazie a pozioni curative miracolose e assistenza sanitaria gratuita.

Un combattimento è diviso in **quattro fasi fondamentali**: Initiative, Round, Turns e End of the Round.

---

## Meccaniche Dettagliate

### Fase 1: Initiative

Si decide l'**ordine d'attacco**: chi agisce per primo e chi per ultimo.

> **Tiro di Initiative = 1d6 + *Dexterity* + [[Attributes_e_Skills|*Alert*]]**

Chi ottiene il risultato più alto agisce per primo. L'ordine resta **fisso** per tutta la durata del combattimento, salvo Moves con priorità che lo alterano temporaneamente.

### Fase 2: Round

Un Round dura circa **10 secondi**. All'interno di un Round, Pokémon e Allenatori eseguono le proprie azioni e attacchi. Il Round è composto da **Turns**.

- Un Pokémon veloce e con esperienza può eseguire più attacchi nello stesso Round.
- Un Pokémon di Rank basso potrebbe aver bisogno dell'intero Round per eseguire un solo attacco.

### Fase 3: Turn

Un Turn è la frazione del Round in cui un Pokémon usa la propria azione per eseguire una Move.

### Fase 4: End of the Round

Quando tutti i Pokémon hanno eseguito le proprie azioni, il Round termina.

- Gli Allenatori hanno la possibilità di compiere **un'azione** in questa fase.
- Alcune Moves e *Status Conditions* hanno effetti in questo momento.

---

## Battling Step by Step

### Step 1: Initiative
*"Pikachu, I choose you!"*

Tira 1 dado e aggiungi il tuo punteggio di Initiative (*Dexterity* + *Alert*). Chi ha il risultato più alto agisce per primo.

### Step 2: Use a Move
*"Pikachu, use Thunderbolt!"*

Durante il Turn del tuo Pokémon, ordina di usare una Move. Tira i dadi per l'**Accuracy** della Move per vedere se colpisce o manca. Ogni Move ha il suo tiro di Accuracy indicato nella sua voce.

### Step 2.5: Evasion/Clash (Opzionale)
*"Eevee, don't let it hit you!"*

L'avversario può tentare di **schivare** o **contrattaccare**:

| Reazione | Tiro | Effetto se eguaglia i successi dell'attaccante |
|---|---|---|
| **Evasion** | *Dexterity* + *Evasion* | Schiva l'attacco: nessun danno né effetti |
| **Clash** | *Strength*/*Special* + *Clash* | Entrambi i Pokémon subiscono **1 danno** (invece del danno regolare) |

> **Regole importanti per Evasion/Clash:**
> - Schivare e Clashare **conta come un'azione**.
> - Sia *Evasion* che *Clash* possono essere usati **una sola volta per Round**, ciascuno.
> - Il *Clash* richiede l'uso di una **Move con danno**.
> - Le Support Moves, le Moves che ignorano le difese e quelle con danno fisso **non possono essere Clashate**.
> - Il danno da Clash è influenzato da *Super Effective* e *Not Very Effective*.
> - Una Move usata per il Clash **non può essere ripetuta** nello stesso Round.

### Step 3: Damage

Se la Move ha colpito, si calcola il danno:

> **Damage Pool = *Strength*/*Special* + Power della Move − DEF/SDEF dell'avversario**

| Regola | Dettaglio |
|---|---|
| Ogni successo nel Damage Roll | Infligge **1 punto di danno** |
| Attacco andato a segno con 0 successi | Infligge comunque **1 danno minimo** |
| Bonus da *Super Effective* | Richiede almeno **1 successo** nel Damage Roll |

### Step 4: Next!
*"Eevee, Sand-Attack, now!"*

Il prossimo Pokémon nell'ordine di Initiative ha il suo Turn e segue gli Step 2 e 3.

### Step 5: Multiple Actions

Dopo che tutti i Pokémon hanno avuto la prima azione, chiunque può provare a usare un'altra Move nello stesso Round. Ogni azione oltre la prima richiede **successi aggiuntivi**:

| Azione | Successi Richiesti |
|---|---|
| 1ª Azione | 1 |
| 2ª Azione | 2 |
| 3ª Azione | 3 |
| 4ª Azione | 4 |
| 5ª Azione | 5 |

> Si possono eseguire fino a **5 azioni per Round**. L'ordine delle azioni extra segue l'ordine di Initiative originale.

> ⚠️ Se non hai abbastanza abilità, rischi un [[Tirare_i_Dadi|Critical Failure]].

> Quando un Pokémon agisce da solo (senza ordini), di solito non farà più di una o due azioni, anche se ne sarebbe capace.

---

## Trainer Actions (Azioni dell'Allenatore)

Gli Allenatori non sono semplici spettatori. Alla **fine di ogni Round**, hanno una breve opportunità di compiere **un'azione** scegliendo tra:

### Switching Pokémon (Scambiare Pokémon)
L'Allenatore può inviare e richiamare fino a **2 Pokémon**. È possibile richiamare un Pokémon in qualsiasi momento del Round, ma nei match ufficiali bisogna inviarne subito un altro o si concede la sconfitta.

> ⚠️ **Pokémon scambiato a metà Round:** Sarà stordito e disorientato, non potrà attaccare o schivare fino all'inizio del Round successivo. **Scambia alla fine del Round** per evitare questo.

### Use an Item (Usare un Oggetto)
L'Allenatore chiama il Pokémon vicino e applica il trattamento tirando:

> ***Clever* + *Medicine***

Il Pokémon non potrà attaccare, schivare o usare Moves per **un intero Round** durante l'applicazione. Se l'Allenatore è nella mischia (*Enter the Fray*), può applicare medicine senza fermare il Pokémon.

### Search for Cover (Cercare Copertura)
Nei combattimenti non ufficiali, l'Allenatore può cercare riparo tirando:

> ***Insight* + *Alert***

Questo garantisce la sicurezza finché la copertura resiste.

### Enter the Fray (Entrare nella Mischia)
L'Allenatore può decidere di partecipare attivamente al combattimento. Dal Round successivo tirerà la sua Initiative e avrà un Turn come tutti gli altri.

> ⚠️ **Conseguenze:** Non potrà dare ordini ai Pokémon (che agiranno seguendo le proprie [[Natures]]). Non potrà scambiare Pokémon né cercare copertura. Rischia ferite gravi. **Bandito nei match ufficiali della Lega.**

### Run Away (Fuggire)
L'Allenatore richiama i Pokémon e fugge tirando:

> ***Dexterity* + *Athletic*** VS ***Dexterity* + *Athletic*** dell'avversario

Se si ottengono più successi, la battaglia finisce. Essere bloccati impedisce la fuga.

---

## Damage, Fainting e Lethal Damage

### Danno e Guarigione Naturale
Ogni volta che si subisce un attacco, si riceve danno. Solo le resistenze di Tipo possono prevenirlo, e anche in quel caso si subisce almeno **1 danno**.

> **Guarigione naturale:** 1 HP ogni 8 ore.

### Fainting (Svenimento)
Subire danno uguale agli HP totali causa lo **svenimento**: non si può muovere né agire.

- Lo svenimento dura in media **8 ore**, dopo le quali il corpo guarisce 1 danno e il personaggio può riprendere conoscenza.
- Il *Revive* permette di recuperare in pochi secondi.
- Una Pozione cura il danno ma **non risveglia** il personaggio.
- Far svenire regolarmente i propri Pokémon **riduce la loro [[Happiness_e_Loyalty|Happiness e Loyalty]]**.

### Pain Penalizations (Penalità da Dolore)

Il danno subito causa penalità a tutti i tiri:

| Stato HP | Stato del Corpo | Penalità |
|---|---|---|
| **HP pieni** | Nessun dolore | Nessuna |
| **Metà HP** (arrotondato per difetto) | Il dolore ostacola i movimenti | **−1 successo** da ogni tiro |
| **1 HP rimanente** | Stai per svenire, tutto è sfocato | **−2 successi** da ogni tiro |

> **Tiri affetti:** Accuracy, Damage, tutti i Social Attributes, *Strength*, *Dexterity*, *Special*, *Insight*.
> **Tiri NON affetti:** *Vitality* e *Will*.

Le penalità vengono rimosse guarendo. In alternativa, si può spendere **1 [[HP_e_Will|*Will Point*]]** per ignorare 1 penalità per il resto della scena.

> Le Pain Penalizations possono essere assegnate anche **senza danno**: per esempio per esaurimento da esercizio, mancanza di cibo o sonno.

### Lethal Damage (Danno Letale) — Regola Opzionale

Se un personaggio svenuto continua a subire danno, questo diventa **Lethal Damage**. Alcune Moves possono infliggere Lethal Damage direttamente.

- Con 1 danno letale, si subisce **1 danno letale aggiuntivo ogni ora** senza cure.
- Le Moves con Lethal Damage sono **bandite dalla Lega**, ma un Pokémon può trattenersi per infliggere danno regolare.

> ⚠️ **Lethal Damage uguale agli HP totali = morte del personaggio.**

### Consigli per la Sicurezza

1. **Non risparmiare sugli oggetti curativi.** La vita dei Pokémon non ha prezzo.
2. **Insegna Moves curative** ai tuoi Pokémon, dando priorità alla sopravvivenza.
3. **Impara la Skill *Medicine*.** Quando le pozioni finiscono, saper creare rimedi è vitale.
4. **Schiva e cerca copertura.** Le battaglie hanno fiamme e raggi di energia ovunque.

---

## Correlati

- [[Tirare_i_Dadi]] — Dice Pool e Critical Failure
- [[Attributes_e_Skills]] — Gli Attributes e Skills usati nei tiri di combattimento
- [[HP_e_Will]] — HP, svenimento, Will Points per ignorare penalità
- [[Status_Conditions]] — Effetti degli Status Ailments a fine Round
- [[Strategie_di_Combattimento]] — STAB, Critical Hit, Super Effective e altre strategie
- [[Azioni_Multiple]] — Dettagli sulle Multiple Actions
- [[Ranking]] — Il Rank influenza le capacità in combattimento
- [[Tipi_Pokemon]] — Tabella Effectiveness per danno e Clash
