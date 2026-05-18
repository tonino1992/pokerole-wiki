---
title: Meteo e Scenario
category: Rule
tags: [weather, meteo, sunny, rain, sandstorm, hail, harsh_sunlight, typhoon, strong_winds, scenario, ambiente, environmental_challenges]
summary: "Le 7 Weather Conditions (Sunny, Harsh Sunlight, Rain, Typhoon, Sandstorm, Strong Winds, Hail) e le Environmental Challenges opzionali che modificano il campo di battaglia."
---

# Meteo e Scenario

## Descrizione Generale

> *"Pokémon, their Moves, and Abilities can be enhanced or diminished by Weather Conditions. Sunlight, Rain, Snow, and Sandstorms are important factors in the habitat of many Pokémon."*

La maggior parte dei combattimenti si svolge in ambienti selvaggi — foreste, vulcani, tundre, fondali marini — e il **meteo** e lo **scenario** non sono semplici sfondi decorativi. Le Weather Conditions potenziano o indeboliscono Moves, attivano Abilities e possono infliggere danno diretto ogni Round.

> *"Remember that most of the fights will be located in the wild. From forests and jungles to volcanoes and tundras and even underground or underwater. This turns the battlegrounds into a shifting scenario, not just an empty arena. Daytime and location can affect your chances of victory."*

Esistono **sette** condizioni meteo principali. Alcuni Pokémon possono evocarle tramite Moves speciali, e altri hanno la capacità innata di cambiarle a volontà tramite le loro Abilities.

> 💡 *"Make the scenario an important part of the fight. It can be the ally or the enemy of the players if you enable free battleground interaction."*

---

## Le 7 Weather Conditions

### ☀️ Sunny Weather (Tempo Soleggiato)

> *"A bright sunlight shines through the arena. It's hot, you feel thirsty and tired, the light is hurting your eyes."*

Tipico di **deserti, pianure e aree tropicali**.

| Effetto | Dettaglio |
|---|---|
| 🔥 **Fuoco potenziato** | Tutte le Moves di tipo [[Tipi_Pokemon\|Fuoco]] hanno **+1 dado** alla Damage Pool |
| 💧 **Acqua indebolita** | Tutte le Moves di tipo [[Tipi_Pokemon\|Acqua]] hanno il danno totale **ridotto di 1** |
| ❄️ **Anti-Freeze** | Nessuno può essere colpito dallo status [[Status_Conditions\|*Frozen*]] |

> 💡 Il Sunny Weather è il paradiso per i team Fuoco: le Moves guadagnano danno extra e gli avversari Acqua vengono indeboliti. Inoltre, alcune Moves curative (come *Synthesis*) diventano *Complete Heal* sotto il sole.

---

### 🔥 Harsh Sunlight Weather (Sole Bruciante)

> *"A harsh sunlight creates extreme heat through the battlefield, there is lava on the floor and some objects just burst into flames. You might need special equipment to go through this weather."*

Si trova **solo in aree vulcaniche**. Versione estrema del Sunny Weather.

| Effetto | Dettaglio |
|---|---|
| 🔥 **Fuoco potenziato** | Tutte le Moves di tipo Fuoco hanno **+1 dado** alla Damage Pool |
| 💧 **Acqua annullata** | Tutte le Moves di tipo Acqua **falliscono automaticamente** |
| 🎲 **Burn potenziato** | Aggiungi **+2 dadi** a qualsiasi tiro di Chance Dice per infliggere [[Status_Conditions\|*Burn*]] |
| ❄️ **Anti-Freeze** | Nessuno può essere colpito dallo status *Frozen* |
| 🚫 **Blocca altri meteo** | Le condizioni *Sunny*, *Rain*, *Sandstorm* e *Hail* **non possono essere attivate** con nessun mezzo |

> ⚠️ L'Harsh Sunlight è devastante per i team Acqua: le loro Moves **non funzionano affatto**. È una delle poche condizioni che blocca completamente un Tipo intero. Inoltre, impedisce di cambiare il meteo con Moves o Abilities normali.

---

### 🌧️ Rain Weather (Pioggia)

> *"A heavy downpour. You are soaking wet. There's deep puddles and it feels like this will grow into a raging storm any second."*

Comune in **foreste pluviali, rive di laghi e paludi**.

| Effetto | Dettaglio |
|---|---|
| 💧 **Acqua potenziata** | Tutte le Moves di tipo Acqua hanno **+1 dado** alla Damage Pool |
| 🔥 **Fuoco indebolito** | Tutte le Moves di tipo Fuoco hanno il danno totale **ridotto di 1** |
| 🩹 **Cure solari ridotte** | Le Moves che diventano *Complete Heal* con il Sunny Weather **curano solo 1 HP** |
| 🧊 **Anti-Burn facilitato** | **−3 successi necessari** per curare lo status [[Status_Conditions\|*Burn*]] |

> 💡 La pioggia non solo potenzia l'Acqua, ma rende anche molto più facile curare le *Burn*, e indebolisce le Moves di Fuoco. Team perfettamente bilanciati tra Acqua e Fuoco favoriscono sempre chi controlla il meteo.

---

### 🌊 Typhoon Weather (Tifone)

> *"A great torrent quickly floods the field, in just a matter of seconds everything is underwater and you struggle to stay afloat through the crashing waves around."*

Si trova **solo in mare aperto/sott'acqua**. Versione estrema della Rain.

| Effetto | Dettaglio |
|---|---|
| 💧 **Acqua potenziata** | Tutte le Moves di tipo Acqua hanno **+1 dado** alla Damage Pool |
| 🔥 **Fuoco annullato** | Tutte le Moves di tipo Fuoco **falliscono automaticamente** |
| 🧊 **Anti-Burn totale** | Nessuno può essere colpito dallo status [[Status_Conditions\|*Burn*]] |
| 🩹 **Cure solari annullate** | Le Moves che diventano *Complete Heal* con il Sunny Weather **non curano alcun HP** |
| 🚫 **Blocca altri meteo** | Le condizioni *Sunny*, *Rain*, *Sandstorm* e *Hail* **non possono essere attivate** |

> ⚠️ Il Typhoon è lo specchio dell'Harsh Sunlight: le Moves di Fuoco non funzionano affatto, e le cure solari sono completamente annullate. È l'ambiente più ostile per i Pokémon di tipo Fuoco.

---

### 🏜️ Sandstorm Weather (Tempesta di Sabbia)

> *"A raging wind is blowing sand all over. You can barely open your eyes, it's hard to breathe and little sharp rocks pierce your skin."*

Comune in **regioni aride e terre desolate**.

| Effetto | Dettaglio |
|---|---|
| 💥 **Danno a fine Round** | Infligge **1 danno** a tutti i Pokémon nel campo **che non siano** di tipo Roccia, Terra o Acciaio |
| 🛡️ **SDEF bonus** | **+1 punto** alla *Special Defense* di tutti i Pokémon di tipo **Roccia** nel campo |
| 🩹 **Cure solari ridotte** | Le Moves che diventano *Complete Heal* con il Sunny Weather **curano solo 1 HP** |

> 💡 Il Sandstorm è il meteo ideale per i team Roccia/Terra/Acciaio: sono immuni al danno periodico, e i Pokémon Roccia ottengono anche un bonus difensivo. Tutti gli altri subiscono un danno costante che li logora Round dopo Round.

> ⚠️ Il danno da Sandstorm si applica a **fine Round**, quindi anche un Pokémon appena entrato in campo lo subirà prima di poter agire nel Round successivo.

---

### 💨 Strong Winds Weather (Venti Forti)

> *"Strong wind currents lift and swirl everything in the air, from a tiny pebble to a giant truck. You are either being swept around or falling straight to the floor at a great speed."*

Si trovano **solo ad altezze elevate** nel cielo.

| Effetto | Dettaglio |
|---|---|
| 🕊️ **Volante potenziato** | Tutte le Moves di tipo Volante hanno **+1 dado** alla Damage Pool |
| ⚡ **Debolezze Volante annullate** | Le Moves di tipo Elettro, Ghiaccio e Roccia infliggono **danno neutro** ai Pokémon di tipo Volante (invece di *Super Effective*) |
| 🚫 **Hazard e Barriere annullate** | *Entry Hazards* (es. *Spikes*), *Barriers* (es. *Light Screen*) e *Block* **falliscono** |
| 🚫 **Blocca altri meteo** | Le condizioni *Sunny*, *Rain*, *Sandstorm* e *Hail* **non possono essere attivate** |

> 💡 I Strong Winds sono estremamente potenti per i team Volanti: non solo le Moves Volanti guadagnano danno, ma le tre classiche debolezze del tipo Volante (Elettro, Ghiaccio, Roccia) vengono **neutralizzate**, rendendo i Pokémon Volanti molto più resistenti.

---

### 🧊 Hail Weather (Grandine)

> *"Heavy ice shards are falling from the sky. It's cold, it's snowy and one of those ice pieces may fall right on your head."*

Tipico di **aree fredde e innevate**.

| Effetto | Dettaglio |
|---|---|
| 💥 **Danno a fine Round** | Infligge **1 danno** a tutti i Pokémon nel campo **che non siano** di tipo Ghiaccio |
| 🛡️ **DEF bonus** | **+1 punto** alla *Defense* di tutti i Pokémon di tipo **Ghiaccio** nel campo |
| 🩹 **Cure solari ridotte** | Le Moves che diventano *Complete Heal* con il Sunny Weather **curano solo 1 HP** |

> 💡 L'Hail è lo specchio del Sandstorm per il tipo Ghiaccio: danno periodico a tutti tranne ai Ghiaccio, che ottengono anche un bonus difensivo. Combinato con la resistenza naturale del Ghiaccio a sé stesso, rende i team Ghiaccio molto resistenti in questo meteo.

---

## Tabella Riassuntiva

| Weather | Tipo Potenziato (+1 dado) | Tipo Indebolito | Danno Periodico | Effetti Speciali |
|---|---|---|---|---|
| **Sunny** | Fuoco | Acqua (−1 danno) | — | No *Frozen* |
| **Harsh Sunlight** | Fuoco | Acqua (fallisce) | — | No *Frozen*, +2 dadi *Burn*, blocca altri meteo |
| **Rain** | Acqua | Fuoco (−1 danno) | — | −3 successi per curare *Burn*, cure solari ridotte |
| **Typhoon** | Acqua | Fuoco (fallisce) | — | No *Burn*, cure solari annullate, blocca altri meteo |
| **Sandstorm** | — | — | 1 danno a non-Roccia/Terra/Acciaio | +1 SDEF Roccia, cure solari ridotte |
| **Strong Winds** | Volante | — | — | Elettro/Ghiaccio/Roccia neutri vs Volante, no Hazard/Barrier, blocca altri meteo |
| **Hail** | — | — | 1 danno a non-Ghiaccio | +1 DEF Ghiaccio, cure solari ridotte |

---

## Environmental Challenges (Sfide Ambientali — Opzionale)

> *"You can add an extra layer of challenge into your battles if you take the environment into account. Official League Tournaments give each match one or two added challenges in the arenas."*

Oltre alle Weather Conditions, lo Storyteller può aggiungere **sfide ambientali** al campo di battaglia:

| Sfida | Categoria | Effetto |
|---|---|---|
| **Fog / Darkness** (Nebbia / Buio) | Visibilità Ridotta | Tutti i Pokémon subiscono **−1 Accuracy** (Reduced Accuracy) su tutte le Moves |
| **Muddy** (Fangoso) | Terreno Difficile | La mobilità di tutti i Pokémon è **dimezzata**. I Pokémon non possono uscire dal raggio di azione |
| **On Fire!** (In Fiamme) | Hazard Pericoloso | A fine di ogni Round, tira **3 Chance Dice** per infliggere [[Status_Conditions\|*Burn*]] a tutti nel campo. Se già in *Burn*, tira per **aumentare il livello** |
| **Electric Poles** (Pali Elettrici) | Elemento Potenziante | Tutti i Pokémon aggiungono **+1 dado** alla Damage Pool delle Moves di tipo Elettro. I Pokémon **non devono ricaricarsi** |

> 💡 *"Feel free to create your own."* — Lo Storyteller è incoraggiato a inventare le proprie sfide ambientali per rendere ogni battaglia unica e memorabile.

> 💡 Le Environmental Challenges si **sommano** alle Weather Conditions: un combattimento in un vulcano potrebbe avere sia *Harsh Sunlight* che *On Fire!*, creando un ambiente devastante per chiunque non sia di tipo Fuoco.

---

## Come Attivare e Cambiare il Meteo

| Metodo | Dettaglio |
|---|---|
| **Ambientale** | Il meteo è determinato dal luogo e dal momento del giorno (es. pioggia in una palude, sole nel deserto) |
| **Moves** | Alcune Moves speciali possono evocare una Weather Condition (es. *Sunny Day*, *Rain Dance*, *Sandstorm*, *Hail*) |
| **Abilities** | Alcune Abilities cambiano il meteo automaticamente quando il Pokémon entra in campo (es. *Drizzle*, *Drought*, *Sand Stream*, *Snow Warning*) |
| **Meteo estremo** | *Harsh Sunlight*, *Typhoon* e *Strong Winds* **bloccano** l'attivazione di *Sunny*, *Rain*, *Sandstorm* e *Hail* — solo condizioni naturali o Abilities leggendarie possono attivarli |

---

## Correlati

- [[Tipi_Pokemon]] — I Tipi potenziati o indeboliti da ciascun meteo
- [[Come_Funziona_il_Combattimento]] — Struttura del Round, fine del Round dove si applicano gli effetti del meteo
- [[Status_Conditions]] — *Burn* e *Frozen* interagiscono con il meteo
- [[Strategie_di_Combattimento]] — Healing in-Battle e le cure solari influenzate dal meteo
- [[HP_e_Will]] — Il danno periodico da Sandstorm e Hail riduce gli HP
- [[Attributes_e_Skills]] — *Special Defense* e *Defense* modificate dal meteo
