---
title: Strategie di Combattimento
category: Rule
tags: [stab, critical_hit, effectiveness, clash, evasion, priority, holding_back, healing, shield, cover, attributes, buff, debuff, low_accuracy, strategie, combattimento]
summary: "Tutte le strategie avanzate di battaglia: STAB, Critical Hit, Effectiveness, Clash, Evasion, Attribute Buffs/Debuffs, Low Accuracy, Holding Back, Priority, Healing in-Battle, Shield Moves, Taking Cover."
---

# Strategie di Combattimento

## Descrizione Generale

> *"It isn't always the strongest, the fastest, or the higher ranked Pokémon that wins the fight. How can you defeat an Onix with only the help of a tiny Pichu? Well, having a strategy can save the day!"*

In questa sezione sono raccolte tutte le **strategie e meccaniche avanzate** che separano un Allenatore principiante da un vero campione. Padroneggiare queste tecniche permette di sfruttare ogni vantaggio possibile, anche quando il Pokémon avversario sembra imbattibile.

---

## Same Type Attack Bonus (STAB)

> *"All Pokémon can control different Types of energy, but these energies will come out naturally stronger if they are from their own Type."*

Quando un Pokémon esegue un attacco il cui [[Tipi_Pokemon|Tipo]] **corrisponde** a uno dei suoi Tipi, ottiene il **Same Type Attack Bonus** (STAB).

| Campo | Dettaglio |
|---|---|
| **Effetto** | Aggiunge **+1 dado bonus** alla Damage Pool dell'attacco |
| **Quando si applica** | Quando il Tipo della Move corrisponde a uno dei Tipi del Pokémon che attacca |
| **Si cumula con** | *Super Effective*, *Critical Hit* e qualsiasi altro bonus al danno |

> 💡 Un Pokémon con doppio tipo beneficia di STAB per **entrambi** i suoi Tipi. Un Charizard (Fuoco/Volante) ottiene STAB sia su *Flamethrower* (Fuoco) che su *Air Slash* (Volante).

### Esempio

> Un Pokémon di tipo Erba che usa una Move di tipo Erba (es. *Razor Leaf*) aggiunge **1 dado extra** alla propria Damage Pool. Lo stesso Pokémon che usa una Move di tipo Normale (es. *Tackle*) **non** riceve il bonus.

---

## Critical Hit (Colpo Critico)

> *"To land a Critical Hit you have to score 3 more successes than what is required for your Accuracy Roll. If you do, you will add 2 dice to your Damage Pool."*

Il Critical Hit è un colpo devastante ottenuto quando l'Accuracy Roll supera ampiamente il minimo necessario.

| Campo | Dettaglio |
|---|---|
| **Requisito (Move normali)** | Ottenere **3 successi in più** del necessario nel tiro di Accuracy |
| **Requisito (Move *High-Critical*)** | Ottenere **2 successi in più** del necessario nel tiro di Accuracy |
| **Effetto** | Aggiunge **+2 dadi** alla Damage Pool |
| **Cumulabile con** | STAB, *Super Effective* e altri bonus al danno |

### Move *High-Critical*

Alcune Moves sono contrassegnate come *High-Critical*: hanno una soglia ridotta per ottenere il Critical Hit (**2 successi extra** invece di 3). Queste Moves sono particolarmente pericolose nelle mani di Pokémon con alta Accuracy.

### Esempio dal Manuale

> *Archen sta combattendo Amaura. Archen riesce a mettere a segno un Critical Hit con la Move* Crunch*.
> La Damage Pool di Archen sarà:*
>
> | Componente | Dadi |
> |---|---|
> | *Strength* di Archen | Valore Attribute |
> | Power di *Crunch* | Valore Move |
> | **Bonus Critical Hit** | **+2** |
> | − DEF di Amaura | Sottrazione |
>
> *Amaura rischia di subire una quantità di danno molto seria dall'attacco di Archen!*

> ⚠️ Il Critical Hit può trasformare qualsiasi attacco in un colpo potenzialmente letale. Combinato con STAB e *Super Effective*, può generare Damage Pool enormi.

---

## Effectiveness (Efficacia di Tipo)

Le interazioni di Tipo sono trattate in dettaglio nella pagina [[Tipi_Pokemon]], ma ecco un riepilogo rapido di come influenzano il danno in battaglia:

| Situazione             | Effetto sul Danno       | Nota                                       |
| ---------------------- | ----------------------- | ------------------------------------------ |
| **Super Effective**    | **+1 danno** aggiuntivo | Richiede almeno 1 successo nel Damage Roll |
| **Not Very Effective** | **−1 danno** ricevuto   | Si applica sempre                          |
| **Doppia Debolezza**   | **+2 danno** aggiuntivo | Entrambi i Tipi del difensore sono deboli  |
| **Doppia Resistenza**  | **−2 danno** ricevuto   | Entrambi i Tipi del difensore resistono    |
| **Immunità**           | **0 danno**             | Non si applica alle Support Moves          |

> 💡 L'Effectiveness influenza anche il danno da **Clash**: il singolo punto di danno inflitto reciprocamente nel Clash è soggetto a *Super Effective* e *Not Very Effective*.

---

## Clash (Contrattacco)

> *"Some Pokémon are not dexterous enough to be constantly evading, but they can rely on their sheer power to fend off their foe's attacks by doing what we call a Clash."*

Il Clash è un'alternativa difensiva all'Evasion: invece di schivare, il Pokémon contrattacca con una propria Move di danno per deviare l'attacco avversario.

| Campo | Dettaglio |
|---|---|
| **Tiro** | *Strength*/*Special* + *Clash* |
| **Condizione di successo** | Ottenere **tanti successi quanti** il tiro di Accuracy dell'avversario |
| **Effetto (successo)** | Entrambi i Pokémon subiscono **1 solo danno** ciascuno (nessun Damage Roll) |
| **Effetto (fallimento)** | Il Pokémon subisce il danno pieno dell'attacco avversario |
| **Frequenza** | **Una sola volta per Round** |
| **Conta come** | **Un'azione** (le azioni successive richiedono successi extra per [[Come_Funziona_il_Combattimento|Multiple Actions]]) |

### Restrizioni del Clash

> ⚠️ **Non si possono Clashare:**
> - **Support Moves** (Moves non di danno)
> - **Moves che ignorano le difese**
> - **Moves con danno fisso** (*Set Damage*)

> ⚠️ La Move usata per il Clash **non può essere ripetuta** nello stesso Round. Se usi *Thunderbolt* per Clashare, non potrai usare *Thunderbolt* di nuovo fino al Round successivo.

### Quando preferire il Clash all'Evasion

> 💡 Il Clash è la scelta ideale per Pokémon con bassa *Dexterity* ma alta *Strength* o *Special*. Un Pokémon lento ma potente come Snorlax o Machamp può Clashare efficacemente anche quando non riuscirebbe mai a schivare.

> 💡 Il danno da Clash (1 punto per ciascun Pokémon) è soggetto alle regole di [[Tipi_Pokemon|Effectiveness]]: se il Tipo della Move usata nel Clash è *Super Effective* contro l'avversario, infliggerai +1 danno; se è *Not Very Effective*, il danno sarà ridotto.

---

## Evasion (Schivata)

> *"It is always a smart move to get away from danger."*

L'Evasion permette al Pokémon di schivare un attacco in arrivo, annullando completamente danno e effetti.

| Campo | Dettaglio |
|---|---|
| **Tiro** | *Dexterity* + *Evasion* |
| **Condizione di successo** | Ottenere **tanti successi quanti** il tiro di Accuracy dell'avversario |
| **Effetto (successo)** | L'attacco è completamente evitato: **nessun danno né effetto** |
| **Effetto (fallimento)** | Il Pokémon subisce il danno pieno dell'attacco avversario |
| **Frequenza** | **Una sola volta per Round** |
| **Conta come** | **Un'azione** |

> 💡 L'Evasion è più efficace del Clash nel prevenire il danno (0 danno vs. 1 danno per entrambi), ma richiede *Dexterity* alta. Pokémon veloci come Jolteon o Weavile eccellono nell'Evasion.

> ⚠️ Le *Pain Penalizations* e altre penalità riducono i successi anche nel tiro di Evasion.

---

## Holding Action (Trattenere l'Azione)

Quando un Pokémon dichiara di **trattenere la propria azione**, resta immobile osservando l'avversario.

| Campo | Dettaglio |
|---|---|
| **Effetto** | L'azione può essere usata in **qualsiasi momento** durante il Round |
| **Se entrambi i Pokémon trattengono l'azione** | Il Round finisce senza ulteriori azioni — *entrambe le parti si fissano guardinghe...* |

> 💡 Holding Action è una strategia psicologica: forza l'avversario a muoversi per primo, permettendoti di reagire alla sua scelta. Utile quando non conosci la Move che l'avversario intende usare.

---

## Taking Cover (Cercare Copertura)

> *"This action will help you resist damage against Ranged attacks depending on how much of your body is covered."*

Un Pokémon può ripararsi dietro un ostacolo per ridurre il danno da attacchi a distanza.

| Copertura del Corpo | Bonus DEF/SDEF vs. Attacchi a Distanza |
|---|---|
| **1/4** del corpo coperto | **+1** DEF/SDEF |
| **1/2** del corpo coperto | **+2** DEF/SDEF |
| **Copertura TOTALE** | La copertura **deve essere distrutta** prima di poter colpire il Pokémon |

> 💡 È possibile usare la manovra *"Cover an Ally"* per usare il corpo del proprio Pokémon come scudo per un alleato piccolo, oppure far coprire l'Allenatore da un Pokémon grande.

> ⚠️ La copertura può essere **distrutta** dopo aver subito alcuni colpi. La sua resistenza è a discrezione dello Storyteller.

---

## Low Accuracy Moves (Mosse a Bassa Precisione)

Alcune Moves potenti sono contrassegnate con un'icona di *Low Accuracy* che **rimuove successi** dal tiro di Accuracy.

| Icona | Effetto |
|---|---|
| Accuracy −1 | Rimuove **1 successo** dal tiro di Accuracy |
| Accuracy −2 | Rimuove **2 successi** dal tiro di Accuracy |
| Accuracy −3 | Rimuove **3 successi** dal tiro di Accuracy |

### Esempio dal Manuale

> *Pikachu cerca di attaccare Stunky con la Move* Thunder*, che ha Accuracy −2. Il suo tiro di Accuracy non ottiene abbastanza successi: il fulmine colpisce l'arena ma manca il bersaglio.*
>
> *Nel turno di Stunky, usa* Smokescreen*, che riduce l'Accuracy di Pikachu di un ulteriore punto. Al Round successivo, la penalità di Accuracy di Pikachu per* Thunder *sarà di −3 successi totali.*

> 💡 *"The power of some Moves might seem tempting, but you'll need a lot more than powerful moves to win your battles. If your foe is relying on powerful but inaccurate Moves, don't be scared — make their advantage become their disadvantage by Evading or Clashing."*

---

## Attributes: Increase & Reduction (Buff e Debuff)

> *"It is a valid strategy to reduce your foe's Attributes to get an advantage. If you combine this with increasing your own Pokémon Attributes, you will be on the right path to victory."*

Molte Moves non infliggono danno, ma **aumentano o riducono** gli Attributes di un Pokémon.

| Campo | Dettaglio |
|---|---|
| **Modifica possibile** | +1, +2 o +3 punti a un singolo Attribute (o −1, −2, −3) |
| **Durata** | **Temporanea**: fino alla fine della scena o finché il Pokémon viene ritirato dalla battaglia |
| **Stacking** | **Non si stackano** sullo stesso Attribute: si considera solo il **modificatore più alto** |
| **Limite massimo** | Un Attribute **non può superare 10** punti totali (compresi bonus temporanei) |
| **Limite minimo** | Un Attribute non può scendere sotto **1 punto** |

### Regola di Sostituzione (No Stacking)

I modificatori temporanei dello stesso segno **non si accumulano**: si tiene solo il più alto.

> *Un Shellder con DEF 5 usa* Withdraw *(+1 DEF), portando la DEF a 6. Poi usa* Iron Defense *(+2 DEF). La DEF diventa 7 (non 8): l'effetto di* Withdraw *è sostituito da quello di* Iron Defense*. Se* Iron Defense *viene usata di nuovo, la DEF resta 7.*

### Combinare Moves e Abilities

> *"Il tuo piccolo Snubbull rosa va in battaglia contro un aggressivo Tyranitar con* Strength *4. Fortunatamente, Snubbull ha l'Ability* Intimidate*, che riduce di 1 punto la* Strength *di tutti i nemici in raggio.*
>
> *Nel suo turno, Snubbull usa la Move* Charm*, che causa una riduzione ulteriore di 2 punti. Alla fine del turno di Snubbull, Tyranitar ha solo **1 punto** di* Strength*. Ora non sembra poi così minaccioso!"*

### Limite Massimo: Esempio

> *Il tuo Floatzel ha 4 punti di* Dexterity*. La sua Ability è* Swift Swim*, che aumenta la* Dexterity *di 2 punti durante la pioggia. Piove, e Floatzel usa la Move* Agility *(+2* Dexterity*). Floatzel finisce con 8 punti totali di* Dexterity*: 4 propri + 2 dall'Ability + 2 dalla Move.*

> ⚠️ *"It is illegal to go into an official match of the league with your Pokémon already buffed. You'll have to put it back into its Pokéball and let it out when the match begins."*

---

## Critical Hit — Tabella Riassuntiva Danno

Riepilogo di come STAB, Critical Hit ed Effectiveness si combinano nella Damage Pool:

| Componente | Dadi aggiunti/rimossi |
|---|---|
| **Attribute** (*Strength* o *Special*) | Valore dell'Attribute |
| **Power della Move** | Valore indicato nella Move |
| **STAB** | +1 dado |
| **Critical Hit** | +2 dadi |
| − **DEF/SDEF** dell'avversario | Sottratti dalla Pool |
| **Super Effective** | +1 danno al risultato (richiede ≥1 successo) |
| **Not Very Effective** | −1 danno al risultato |

> 💡 Nella situazione migliore possibile (STAB + Critical Hit + Super Effective + Doppia Debolezza), un attacco può generare un output di danno devastante. Pianifica le Moves del tuo team per massimizzare queste sinergie.

---

## Holding Back (Trattenere la Forza)

> *"Sometimes it will be more convenient to contain the full force of your Pokémon's attacks."*

In alcune situazioni è utile **limitare il danno** inflitto dal proprio Pokémon.

| Opzione | Effetto |
|---|---|
| **Deal Half Damage** | Tira il danno normalmente, ma infliggi solo **la metà** (arrotondata per difetto) |
| **Deal Regular instead of Lethal** | Se la Move infligge Lethal Damage, il danno diventa **danno regolare** |

### Quando usare Holding Back

- **Cattura:** Vuoi catturare un Pokémon selvatico senza farlo svenire.
- **Alleati in pericolo:** La Move colpisce un'area e potrebbe ferire i tuoi alleati.
- **Tornei ufficiali:** La Move preferita infligge Lethal Damage, bandito nei match di Lega.

> 💡 Il comando all'Allenatore è qualcosa come *"Restrain yourself!"* o *"Don't use full force!"* — il Pokémon capirà di doversi trattenere.

---

## Priority e Low Priority

> *"Many actions and Moves are quick and abrupt or slow and complex."*

Alcune Moves agiscono **fuori dall'ordine di Initiative** normale.

| Tipo | Effetto |
|---|---|
| **Priority** | Il Pokémon agisce **immediatamente**, anche se non è il suo turno |
| **Low Priority** | La Move ha effetto alla **fine del Round** |

### Regole di Priority

| Situazione | Risoluzione |
|---|---|
| Due Pokémon usano una Priority Move | La Move con **numero di Priority più alto** si risolve per prima |
| Stesso numero di Priority | Si segue l'ordine di **Initiative** |
| L'avversario reagisce a una Priority Move | Può cambiare la propria azione in un'**Evasion** o usare un'altra Priority Move |

> 💡 La Low Priority può sembrare uno svantaggio, ma può essere sfruttata tatticamente: l'avversario potrebbe non aspettarsi un attacco alla fine del Round, quando ha già usato la propria Evasion.

---

## Healing In-Battle (Cure in Combattimento)

Ci sono **tre modi** per curare un personaggio durante la battaglia:

| Metodo | Dettaglio |
|---|---|
| **Oggetti curativi** | Spray Potions, medicine. 1 unità di Pozione cura 1 danno; 2 unità curano 1 Lethal Damage |
| **Held Items** | Bacche (*Berries*) tenute dal Pokémon |
| **Moves curative** | Richiedono la spesa di **1 [[HP_e_Will|*Will Point*]]** se l'Accuracy Roll ha successo |

### Tipi di Moves Curative

| Tipo | Effetto |
|---|---|
| **Basic Heal** | Cura danno regolare pari a **3 HP** |
| **Complete Heal** | Cura danno regolare **e** Lethal Damage pari a **5 HP** |
| **Fixed Heal** | Cura fino a un quantitativo fisso (es. 2 danni) |
| **Fixed Complete Heal** | Cura fino a un quantitativo fisso di **Lethal Damage** |

### Limite di Cura per Round

> ⚠️ **Massimo 3 HP curati per Round** usando Pozioni, Bacche e la maggior parte delle Moves curative.
> L'eccezione è la **Complete Heal**: può curare fino a **5 HP per Round**.
> Anche *Max Potion* e *Full Restore* superano questo limite.

> 💡 *"Healing Moves are not infinite — your Pokémon's Will score can run out before recovering all of its HP. Always carry Potions!"*

> ⚠️ Gli umani **non possono usare Moves curative** direttamente, ma possono far usare ai propri Pokémon Moves su di loro. Gli umani non possono tenere *Held Items*, ma possono usare Bacche e medicine su sé stessi o sui propri Pokémon.

### Esempio dal Manuale

> *Il tuo Meganium sta combattendo e ha solo 2 HP su 9 totali. Usi* Grassy Terrain*, che cura 1 HP a fine Round. Corri in suo aiuto con una Pozione e applichi 3 unità (cura 3 HP), ma la cura di* Grassy Terrain *non avrà effetto questo Round perché il limite di 3 HP è già stato raggiunto.*
>
> *Qualche Round dopo, qualcuno attiva Sunny Weather. Meganium ha 5 HP e usa* Synthesis*, che con il Sole diventa una* Complete Heal *(5 HP). Ma Meganium ha subito solo 4 danni, quindi cura 4 HP e il punto restante va perso.*

---

## Shield Moves (Mosse Scudo)

> *"Unlike evading, Pokémon using these moves receive the attacks head-on with certainty that they'll come out practically unscathed. Shield Moves can reduce damage to zero."*

Alcune Moves sono contrassegnate come **Shield Moves**. A differenza dell'Evasion, il Pokémon **non schiva** ma blocca l'attacco direttamente.

| Campo | Dettaglio |
|---|---|
| **Effetto** | Varia da Move a Move, ma tutte proteggono da un attacco in arrivo |
| **Differenza dall'Evasion** | Il Pokémon riceve l'attacco frontalmente e lo annulla, anziché evitarlo |
| **Potenziale massimo** | Possono **ridurre il danno a 0** |

> 💡 Le Shield Moves sono ideali per Pokémon con bassa *Dexterity* che non possono contare sull'Evasion. Sono un'alternativa più sicura del Clash quando disponibili.

---

## Correlati

- [[Come_Funziona_il_Combattimento]] — Struttura del combattimento, Accuracy, Damage e Multiple Actions
- [[Tipi_Pokemon]] — Tabella completa delle interazioni di Tipo (Effectiveness)
- [[Tirare_i_Dadi]] — Dice Pool, successi e Critical Failure
- [[Attributes_e_Skills]] — Gli Attributes coinvolti nelle strategie di combattimento
- [[HP_e_Will]] — HP, Will Points e il loro ruolo nelle cure
- [[Status_Conditions]] — Gli Status Ailments che possono influenzare le strategie
- [[Azioni_Multiple]] — Regole per le Multiple Actions in combattimento
- [[Meteo_e_Scenario]] — Weather Conditions che potenziano certi Tipi e Abilities
- [[Ranking]] — Il Rank influenza la Skill Limit e le capacità in combattimento
