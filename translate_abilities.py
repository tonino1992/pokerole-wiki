import os, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

ABIL_DIR = 'wiki/04_Moves_e_Abilities/Abilità'

# Translations: Italian flavor + effect per ability slug
# Format: slug -> (flavor_it, effect_it)
TRANSLATIONS = {
'Adaptability': (
    "Questo Pokémon si adatta facilmente all'ambiente circostante, spostandosi con disinvoltura su qualsiasi terreno.",
    "Ogni volta che questo Pokémon usa una mossa che infligge danno dello stesso Tipo, aggiungi 1 dado al Damage Pool di quell'attacco."
),
'Aerilate': (
    "Questo Pokémon non tocca mai il suolo: una corrente d'aria perpetua si avverte sempre intorno a lui.",
    "Le mosse di tipo Normale usate da questo Pokémon infliggono danno come se fossero di tipo Volante, applicando STAB, debolezze e resistenze di conseguenza. Aggiungi 1 dado di danno alle mosse di tipo Volante."
),
'Aftermath': (
    "Quando viene ferito o agitato, questo Pokémon si prepara ad esplodere. Se colpito abbastanza duramente, esploderà al contatto.",
    "Se questo Pokémon sviene a causa di un Non-Ranged Physical Attack, l'utilizzatore di quell'attacco subisce 2 Danno."
),
'Air_Lock': (
    "Il Pokémon si avvolge in un vuoto d'aria. Ogni particella di pioggia, sabbia e grandine resta sospesa immobile intorno a lui, persino il calore viene filtrato dal luogo.",
    "Annulla tutti gli effetti di una Condizione Meteo in campo. Se non ci sono condizioni meteo attive, non possono essere attivate da mosse o abilità. Se una è già attiva, non scompare ma non produce alcun effetto."
),
'Analytic': (
    "Questo Pokémon non agisce mai in modo avventato: si prende un momento per trovare la decisione migliore in ogni situazione.",
    "Se questo Pokémon ha un'Initiative inferiore a quella del bersaglio, aggiungi 1 dado a tutti i suoi Damage Pool."
),
'Anger_Point': (
    "Questo Pokémon si agita facilmente. Basta pochissima provocazione per farlo esplodere in una furia devastante.",
    "Se un avversario ottiene un Critical Hit su questo Pokémon, aumenta di 3 il suo attributo Strength."
),
'Anticipation': (
    "Questo Pokémon è sempre all'erta e raramente si rilassa. Se percepisce un potenziale pericolo, si innervosisce e inizia a tremare.",
    "Se un avversario conosce una mossa che infliggerebbe danno Letale o Super Effective contro questo Pokémon, avviserà il suo Allenatore."
),
'Arena_Trap': (
    "Il terreno intorno a questo Pokémon diventa morbido e difficile da attraversare. In pericolo, sprofonda il terreno creando una trappola di sabbia mobile.",
    "Tutti i Pokémon avversari a terra diventano Blocked: non possono fuggire né essere sostituiti finché questo Pokémon è in campo."
),
'Aroma_Veil': (
    "Questo Pokémon emana un profumo gradevole che aiuta a restare rilassati anche nelle situazioni più stressanti.",
    "L'utilizzatore e i suoi alleati nel raggio d'azione sono immuni agli effetti delle mosse: Taunt, Torment, Attract, Disable, Encore e Heal Block."
),
'Aura_Break': (
    "Chiunque emetta un'aura particolarmente maligna verrà purificato; chiunque abbia un'aura di purezza verrà corrotto avvicinandosi a questo Pokémon.",
    "Inverte gli effetti che le abilità [[Dark_Aura|Dark Aura]] e [[Fairy_Aura|Fairy Aura]] hanno sui loro utilizzatori. Se tali abilità aumenterebbero un Damage Pool, lo riducono invece."
),
'Bad_Dreams': (
    "Questo Pokémon trasferisce la sua malvagità attraverso il mondo dei sogni, seminando paura nella mente di chi dorme profondamente.",
    "Alla fine del Round, infligge 1 Danno a chiunque sia in campo con la Condizione di Stato Sleep."
),
'Ball_Fetch': (
    "Questo Pokémon è ossessionato dal gioco del «riporta la palla» e non si stanca mai di farlo.",
    "Ogni volta che lanci una Pokéball su un Pokémon selvatico, se il tiro di cattura fallisce, la Pokéball non si rompe — questo Pokémon la riporterà indietro alla fine della scena."
),
'Battery': (
    "La presenza di questo Pokémon crea un campo elettrico che ricarica dispositivi elettronici e fa sentire tutti più energici.",
    "Aumenta di 1 il Special di tutti i Pokémon alleati nel raggio d'azione. Tutti i Pokémon alleati ottengono 1 dado bonus al Damage Pool di tutte le loro mosse di tipo Special."
),
'Battle_Armor': (
    "La pelle di questo Pokémon è ricoperta da piastre di materiale estremamente resistente, come roccia, acciaio o esoscheletro.",
    "Se un avversario ottiene un Critical Hit su questo Pokémon, non ottiene dadi bonus per esso."
),
'Battle_Bond': (
    "Questo Pokémon forge un legame forte con chi affronta le battaglie più dure. Dopo una vittoria, un'ondata di potere emerge grazie all'amicizia.",
    "DOPO che un avversario viene sconfitto da questo Pokémon, se ha un punteggio di Loyalty pari a 5, cambia la sua Forma in \"Forma Battle-Bond\" (BBF) fino alla fine della scena o finché esso o il suo Allenatore sviene. Un solo Pokémon per gruppo può avere questa abilità. I Pokémon con questa abilità non possono tenere una Mega-Stone.\n\n**Effetti BBF:** aumenta di 2 i Limiti di Strength e Special; ridistribuisci i punti Rank su BBF come preferisci; aumenta di 1 il Power di una mossa a scelta; ripristina HP e Will completi e cura qualsiasi Condizione di Stato al cambio forma. In BBF, tutti i danni da combattimento subiti dal Pokémon vengono inflitti anche al suo Allenatore."
),
'Beast_Boost': (
    "Una soddisfazione malvagia cresce in questa creatura mentre semina distruzione, diventando sempre più feroce ad ogni avversario che cade.",
    "Se un avversario sviene a causa di un attacco di questo Ultra-Beast, aumenta di 1 il suo attributo con il Limite più alto. Possono essere aggiunti al massimo 3 punti in questo modo. Solo gli Ultra-Beast possono avere questa abilità. Beast Boost non può essere scambiata né copiata."
),
'Berserk': (
    "Questo Pokémon è solitamente calmo, ma quando la sua vita o quella di chi ama è in pericolo, la scarica di adrenalina lo trasforma in una bestia furiosa.",
    "Quando gli HP di questo Pokémon sono alla metà o meno, aumenta di 1 il suo attributo Special."
),
'Big_Pecks': (
    "Questo Pokémon tenace usa il suo becco per coprire i propri punti deboli.",
    "Questo Pokémon non può subire riduzioni alla sua Defense."
),
'Blaze': (
    "Il fuoco sul corpo di questo Pokémon brucia intensamente prima di spegnersi.",
    "Quando gli HP di questo Pokémon sono alla metà o meno, la Pain Penalization non riduce i successi ai tiri di danno delle sue mosse di tipo Fuoco, e ottengono 1 dado extra al Damage Pool."
),
'Bulletproof': (
    "L'armatura sul corpo di questo Pokémon lo protegge da proiettili e piccole esplosioni.",
    "Riduce di 1 tutti i danni provenienti da attacchi Special e Ranged Physical su questo Pokémon."
),
'Cheek_Pouch': (
    "Questo Pokémon è in grado di conservare cibo e oggetti nelle sue guance elastiche per consumarli in seguito.",
    "Questo Pokémon ripristina 2 HP ogni volta che mangia una bacca senza effetto di cura HP (es. Pecha Berry, Lum Berry)."
),
'Chlorophyll': (
    "Questo Pokémon sintetizza la luce solare per ricavare energia; se tenuto in un ambiente soleggiato raramente ha bisogno di mangiare.",
    "Se il meteo Sole è attivo, aumenta di 2 il Dexterity di questo Pokémon."
),
'Clear_Body': (
    "Questo Pokémon è perfettamente consapevole di tutto ciò che lo circonda: sorprenderlo è incredibilmente difficile.",
    "Gli altri Pokémon non possono aumentare né ridurre gli attributi di questo Pokémon. Questo Pokémon può ancora modificare i propri attributi autonomamente."
),
'Cloud_Nine': (
    "Questo Pokémon è naturalmente incline alla felicità, non importa se c'è il sole o la pioggia: non si sente mai triste.",
    "Annulla gli effetti delle Condizioni Meteo su questo Pokémon."
),
'Color_Change': (
    "Questo Pokémon può cambiare colore ed energia per mimetizzarsi nell'ambiente circostante.",
    "Quando questo Pokémon subisce danno, cambia temporaneamente il suo tipo in modo da corrispondere al tipo della mossa che lo ha colpito. L'effetto termina se il Pokémon viene rimosso dalla battaglia."
),
'Comatose': (
    "Per qualche ragione questo Pokémon dorme sempre e non riesce a svegliarsi. Eppure riesce a capire i comandi e a muoversi come se stesse sonnambulando.",
    "Il Pokémon ha permanentemente la Condizione di Stato Sleep ma è immune ai suoi effetti. Questo Pokémon non può ricevere altre Condizioni di Stato. Mosse e abilità che interessano i Pokémon addormentati hanno comunque effetto su di lui."
),
'Competitive': (
    "La determinazione di questo Pokémon cresce di fronte all'avversità. È sempre in competizione con chi lo circonda.",
    "La prima volta che un avversario riduce un attributo di questo Pokémon durante una battaglia, aumenta di 2 il suo Special."
),
'Compound_Eyes': (
    "Questo Pokémon ha una visione periferica che gli permette di localizzare i bersagli con grande precisione.",
    "Questo Pokémon ottiene 2 dadi bonus all'Accuracy Pool di qualsiasi mossa con Reduced Accuracy."
),
'Contrary': (
    "La maggior parte delle volte questo Pokémon vuole fare il contrario di ciò che gli si chiede. A volte si contraddice persino da solo.",
    "Se qualcosa ridurrebbe un attributo di questo Pokémon, lo aumenta invece. Se qualcosa aumenterebbe un attributo di questo Pokémon, lo riduce invece."
),
'Corrosion': (
    "Il veleno di questo Pokémon corrode metalli, legno e la maggior parte dei materiali organici e inorganici. Fare attenzione a non toccarlo!",
    "Ignora qualsiasi immunità del bersaglio al danno di tipo Veleno e/o all'inflizione delle Condizioni di Stato Poison e Badly Poison."
),
'Cotton_Down': (
    "Il cotone sul corpo di questo Pokémon viene continuamente perso. Può essere usato per fare bellissimi vestiti, ma è anche fastidioso camminarci sopra.",
    "Se questo Pokémon viene colpito da un Non-Ranged Physical Attack, riduce di 1 il Dexterity di tutti i Pokémon vicini (alleati e avversari, a discrezione dello Storyteller)."
),
'Cursed_Body': (
    "Questo Pokémon porta una maledizione dentro di sé. Fare un torto a questo Pokémon non è una buona idea.",
    "Ogni volta che questo Pokémon subisce danno da una mossa, tira 3 Chance Dice per Disable quella mossa. Possono essere disabilitate più mosse in questo modo."
),
'Cute_Charm': (
    "Che siano i suoi occhi brillanti o le sue guance rosee, le persone e gli altri Pokémon cercheranno sempre di conquistare il suo cuore.",
    "Se un avversario colpisce questo Pokémon con un Non-Ranged Physical Attack, tira 3 Chance Dice per far innamorare l'avversario (Condizione di Stato Love)."
),
'Damp': (
    "Questo Pokémon raccoglie l'umidità dell'aria intorno a sé. Accendere una scintilla o mantenere un fuoco acceso nelle sue vicinanze è quasi impossibile.",
    "Nessun alleato né avversario potrà usare le mosse Explosion o Self-Destruct nell'area circostante a questo Pokémon."
),
'Dancer': (
    "Quando qualcuno inizia a danzare, anche questo Pokémon danza. Esprime i suoi sentimenti e comunica attraverso piccoli passi di danza.",
    "Ogni volta che un Pokémon usa una mossa con la parola \"Dance\" nel nome (es. Dragon Dance, Petal Dance ecc.), questo Pokémon ottiene un'azione gratuita per usare la stessa mossa immediatamente dopo, riuscendo automaticamente (il danno va comunque tirato)."
),
'Dark_Aura': (
    "Una potente aura nera emana da questo Pokémon, avvolgendo il campo nell'oscurità e riempiendo il cuore di tutti di malvagità, egoismo e corruzione.",
    "Aggiunge 2 dadi a tutti i Damage Pool delle mosse di tipo Buio di tutti i Pokémon in campo. Questo effetto non si accumula. I Pokémon e gli Allenatori in campo non collaboreranno tra loro."
),
'Dauntless_Shield': (
    "La risoluta determinazione di questo Pokémon lo rende impervio al danno fisico grazie alla pura forza di volontà. La sua presenza può essere snervante.",
    "Ogni volta che questo Pokémon entra in battaglia, aumenta di 2 la sua Defense. Al di fuori della battaglia, questo Pokémon è immune al danno fisico."
),
'Dazzling': (
    "Le sue bellissime scaglie riflettono la luce come specchi: nessuno riesce a fare a meno di fermarsi quando le guarda.",
    "Gli avversari non possono usare mosse con Priority contro questo Pokémon."
),
'Defeatist': (
    "Questo Pokémon è pessimista per natura. Quando le cose si mettono male, sarà il primo ad arrendersi.",
    "Se questo Pokémon ha la metà o meno degli HP totali, tira la sua Loyalty ogni azione: se il tiro fallisce, riduce di 2 la sua Strength e il suo Special per quell'azione. Se riesce, può mantenere gli attributi invariati."
),
'Defiant': (
    "Questo Pokémon non cede mai: più la situazione si fa difficile, più il suo spirito combattivo cresce. Può però essere un po' ribelle.",
    "La prima volta che un avversario riduce un attributo di questo Pokémon durante una battaglia, aumenta di 2 la sua Strength."
),
'Delta_Stream': (
    "Le correnti d'aria soffiano attraverso l'intero campo di battaglia; i Pokémon potrebbero essere spazzati via se non sanno volare.",
    "Quando questo Pokémon entra in campo, avvia automaticamente gli effetti del meteo Strong Wind. Gli effetti terminano quando il Pokémon lascia la battaglia. (In caso di parità, il Pokémon con la Will più alta potrebbe mantenere il meteo dominante.)"
),
'Desolate_Land': (
    "Il sole brucia così forte da far arrossire la pelle. Tutta l'acqua evapora e ogni passo di questo Pokémon trasforma il suolo in lava fusa.",
    "Quando questo Pokémon entra in campo, avvia automaticamente gli effetti del meteo Harsh Sunlight. Gli effetti terminano quando il Pokémon lascia la battaglia. (In caso di parità, il Pokémon con la Will più alta potrebbe mantenere il meteo dominante.)"
),
'Disguise': (
    "Questo Pokémon indossa un travestimento convincente di un altro Pokémon. Se subisce danno, il travestimento si rompe, facendo sembrare che abbia ricevuto un colpo fatale.",
    "La prima volta che questo Pokémon riceverebbe danno durante una battaglia, quel danno viene ridotto a zero. Trappole sul campo, Condizioni Meteo e Condizioni di Stato non attivano questa abilità."
),
'Download': (
    "Questo Pokémon è in grado di scansionare e accedere ai dati digitali presenti nei computer, scaricando le informazioni dentro di sé. Troppi dati potrebbero farlo sentire pesante.",
    "Quando questo Pokémon entra in campo, scansionerà i suoi avversari e fornirà informazioni su di loro. Aumenterà poi di 1 il Strength o il Special, a discrezione dello Storyteller."
),
'Drizzle': (
    "Il cielo continuerà a piovere in un'apparente tempesta senza fine finché questo Pokémon lo vorrà.",
    "Quando questo Pokémon entra in campo, avvia automaticamente gli effetti del meteo Pioggia. Gli effetti terminano quando il Pokémon lascia la battaglia. (In caso di parità, il Pokémon con la Will più alta potrebbe mantenere il meteo dominante.)"
),
'Drought': (
    "La luce solare sarà abbagliante e il calore aumenterà in campo finché questo Pokémon lo vorrà.",
    "Quando questo Pokémon entra in campo, avvia automaticamente gli effetti del meteo Sole. Gli effetti terminano quando il Pokémon lascia la battaglia. (In caso di parità, il Pokémon con la Will più alta potrebbe mantenere il meteo dominante.)"
),
'Dry_Skin': (
    "La pelle di questo Pokémon richiede cure speciali, idratazione costante e protezione dal calore.",
    "Se il meteo Sole è attivo, questo Pokémon subisce 1 danno alla fine di ogni round. Gli attacchi di tipo Fuoco infliggono 1 danno aggiuntivo a questo Pokémon. Gli attacchi di tipo Acqua possono curare 1 HP a questo Pokémon invece di infliggere danno."
),
'Early_Bird': (
    "I Pokémon con questa abilità dormono poco e si svegliano con energia dopo pochissime ore di sonno.",
    "Il tempo in cui questo Pokémon resterebbe addormentato è ridotto della metà: deve ottenere solo 2 successi al tiro di Insight per svegliarsi in battaglia. Questo effetto non si applica alla mossa Rest."
),
'Effect_Spore': (
    "Sotto stress, questo Pokémon libera spore dal suo corpo che si disperdono nell'aria causando gravi allergie.",
    "Se colpito da un Non-Ranged Physical Attack, tira 3 Chance Dice per infliggere casualmente Poison, Paralysis o Sleep all'avversario."
),
'Electric_Surge': (
    "Questo Pokémon può circondarsi di un campo elettrico che riempie l'aria di tensione, tenendo tutti sul chi vive.",
    "Quando questo Pokémon entra in campo, avvia automaticamente gli effetti della mossa [[Electric_Terrain|Electric Terrain]]. (In caso di parità, il Pokémon con la Will più alta potrebbe mantenere il Terreno dominante.)"
),
'Emergency_Exit': (
    "Questo Pokémon effettua ritirate tattiche quando la situazione sfugge al controllo. Puoi costringerlo a combattere, ma non gli piacerà.",
    "Ogni volta che questo Pokémon raggiunge la metà o meno degli HP, si ritirerà nella sua Pokéball, mandando un alleato al suo posto. Se non ci sono alleati, la battaglia potrebbe terminare. Questo effetto non è influenzato da Blocked."
),
'Fairy_Aura': (
    "Una potente aura rosa emana da questo Pokémon, avvolgendo il campo in una luce brillante e riempiendo il cuore di tutti di pace, speranza e amore.",
    "Aggiunge 2 dadi a tutti i Damage Pool delle mosse di tipo Folletto di tutti i Pokémon in campo. Questo effetto non si accumula. I Pokémon e gli Allenatori in campo non attaccheranno l'utilizzatore di questa abilità."
),
'Filter': (
    "Questo Pokémon usa un campo energetico invisibile per filtrare le energie e le sostanze nocive.",
    "Se un avversario usa una mossa che infliggerebbe danno Super Effective a questo Pokémon, riduce di 1 il danno totale di quell'attacco."
),
'Flame_Body': (
    "Questo Pokémon può volontariamente incendiarsi senza subire danni. Gli oggetti che entrano in contatto con lui potrebbero prendere fuoco.",
    "Quando viene colpito da un Non-Ranged Physical Attack, tira 3 Chance Dice per infliggere Burn all'avversario."
),
'Flare_Boost': (
    "I Pokémon con questa abilità beneficiano del calore estremo prodotto dal fuoco. Potrebbe essere in qualche modo piromane.",
    "Se questo Pokémon riceve la Condizione di Stato Burn, aumenta di 2 il suo Special."
),
'Flash_Fire': (
    "Questo Pokémon è in grado di consumare altre fonti di fuoco e aggiungerle alle proprie. Camminare tra braci, fuoco, lava e inferno è per lui una passeggiata.",
    "La prima volta che questo Pokémon viene colpito da una mossa di tipo Fuoco, aggiunge 1 dado extra al Damage Pool delle sue mosse di tipo Fuoco fino alla fine della scena. Le mosse di tipo Fuoco non infliggono danno a questo Pokémon."
),
'Flower_Gift': (
    "I petali di questo Pokémon irradiano energia quando il sole splende intenso. L'energia irradiata fa sentire più forti chi gli sta intorno.",
    "Se il meteo Sole è attivo, aumenta di 2 la Strength e la Sp. Defense dell'utilizzatore e dei suoi alleati."
),
'Flower_Veil': (
    "Questo Pokémon fa crescere fiori nei giardini e vicino agli altri Pokémon per proteggerli dal male.",
    "L'utilizzatore e i suoi alleati non possono subire riduzioni agli attributi. L'utilizzatore e i suoi alleati non possono ricevere Condizioni di Stato. Le riduzioni di attributi e le Condizioni di Stato inflitte in precedenza rimangono."
),
'Fluffy': (
    "Il pelo di questo Pokémon è così soffice che potresti morire dall'emozione. È così morbido e coccoloso che invita all'abbraccio.",
    "Riduce di 2 il danno inflitto a questo Pokémon da tutti gli attacchi fisici. Aumenta di 2 il danno inflitto a questo Pokémon dagli attacchi di tipo Fuoco."
),
'Forecast': (
    "Questo Pokémon può assorbire gli elementi circostanti per adattarsi e sopravvivere anche in condizioni estreme.",
    "Il Tipo di questo Pokémon cambia in base al meteo attivo: Fuoco sotto il Sole, Acqua sotto la Pioggia, Ghiaccio sotto la Grandine e Roccia sotto la Tempesta di Sabbia."
),
'Forewarn': (
    "Quando questo Pokémon percepisce cattive intenzioni o un disastro imminente, avverte mentalmente il suo Allenatore. L'Allenatore deve effettuare un tiro di Insight per ricevere il messaggio.",
    "In battaglia, questo Pokémon avvisa della mossa più potente che uno degli avversari conosce. Lo Storyteller deve rivelarla all'Allenatore di questo Pokémon in segreto."
),
'Friend_Guard': (
    "Questo Pokémon è adorabile e risveglia l'istinto protettivo negli altri. Tutti i suoi alleati cercheranno sempre di proteggerlo.",
    "Se questo Pokémon viene colpito da una mossa effettuata da un alleato, riduce di 2 il danno subito."
),
'Frisk': (
    "Questo Pokémon riesce a vedere gli oggetti che gli altri portano con sé, anche se nascosti.",
    "Quando questo Pokémon entra in campo, lo Storyteller deve rivelare al suo Allenatore l'oggetto tenuto da uno degli avversari."
),
'Full_Metal_Body': (
    "Il corpo di questo Pokémon è un'armatura di metallo spesso: il suo rivestimento lucido non può essere offuscato. Guardarlo può abbagliare come il sole.",
    "Gli altri Pokémon non possono ridurre gli attributi di questo Pokémon. Questo Pokémon può ancora ridurre i propri attributi autonomamente."
),
'Fur_Coat': (
    "L'esterno soffice di questo Pokémon è morbido, ipoallergenico e funge anche da cuscino contro i colpi potenti.",
    "Riduce di 2 il danno inflitto a questo Pokémon da tutti gli attacchi fisici."
),
'Gale_Wings': (
    "Le ali di questo Pokémon sono progettate alla perfezione per cavalcare i venti più violenti senza sforzo.",
    "Aggiunge Priority a tutte le mosse di tipo Volante di questo Pokémon."
),
'Galvanize': (
    "Il corpo di questo Pokémon è circondato da correnti elettriche che lo rendono molto energico in tutto ciò che fa.",
    "Le mosse di tipo Normale usate da questo Pokémon infliggono danno come se fossero di tipo Elettro, applicando STAB, debolezze e resistenze di conseguenza. Aggiunge 1 dado extra di danno alle mosse di tipo Elettro."
),
'Gluttony': (
    "Questo Pokémon mangia tutto il giorno e non ha problemi a trovare fonti di cibo, dato che non è per niente schizzinoso.",
    "Questo Pokémon può mangiare qualsiasi tipo di cibo, medicine o erbe medicinali senza effetti negativi. Può mangiare le bacche tenute in qualsiasi momento della battaglia come azione gratuita."
),
'Gooey': (
    "Il muco appiccicoso di questo Pokémon si attacca a chiunque lo tocchi. Può diventare un bel fardello, ma è anche un ottimo collante naturale.",
    "La prima volta che un avversario colpisce questo Pokémon con un Non-Ranged Physical Attack, riduce di 1 il suo Dexterity."
),
'Gorilla_Tactics': (
    "I modi di questo Pokémon lasciano molto a desiderare: è rozzo e incivilito, e il suo unico approccio ai problemi è «Spacca tutto!»",
    "All'inizio della battaglia, scegli una mossa. Aumenta di 1 la Strength di questo Pokémon: potrà eseguire solo la mossa scelta, ma potrà Evadere ogni Round. L'effetto si azzera se il Pokémon viene richiamato."
),
'Grass_Pelt': (
    "Questo Pokémon ha un fitto manto erboso che protegge il suo corpo: anche se viene tagliato, ricresce in pochi giorni.",
    "Se gli effetti della mossa [[Grassy_Terrain|Grassy Terrain]] sono attivi, aumenta di 2 la Defense di questo Pokémon."
),
'Grassy_Surge': (
    "Questo Pokémon può circondarsi di un campo erboso che invita a rilassarsi e oziare al sole.",
    "Quando questo Pokémon entra in campo, avvia automaticamente gli effetti della mossa [[Grassy_Terrain|Grassy Terrain]]. (In caso di parità, il Pokémon con la Will più alta potrebbe mantenere il Terreno dominante.)"
),
'Gulp_Missile': (
    "Questo Pokémon è un cacciatore eccellente: quando si immerge in uno specchio d'acqua torna sempre con una preda. A volte usa la preda come arma...",
    "Se questo Pokémon usa le mosse [[Surf]] o [[Dive]], cambia forma dopo aver inflitto danno — \"Gulping Form\" se ha più della metà degli HP, \"Gorging Form\" se ne ha la metà o meno. Se viene colpito da un avversario in una di queste forme, infligge 2 dadi di danno con un effetto aggiuntivo. Dopodiché torna alla forma normale."
),
'Guts': (
    "Questo Pokémon osa fare ciò che nessun altro osa, e non perde facilmente la determinazione. Può essere un po' avventato.",
    "Mentre è affetto da una Condizione di Stato, aumenta di 2 la sua Strength."
),
'Harvest': (
    "Questo Pokémon produce naturalmente frutti commestibili in breve tempo; se nutrito con bacche, inizierà a farle crescere.",
    "Se questo Pokémon usa una bacca come oggetto tenuto durante un combattimento, la bacca ricrescerà entro la fine della giornata."
),
'Healer': (
    "Questo Pokémon ha poteri curativi e li usa senza esitazione per aiutare gli altri.",
    "Se un alleato in campo ha una Condizione di Stato, alla fine del Round questo Pokémon tira 3 Chance Dice per curarla."
),
'Heatproof': (
    "Questo Pokémon può resistere a temperature molto elevate senza problemi.",
    "La Condizione Burn 1 non infligge danno a questo Pokémon. Se viene colpito da un attacco di tipo Fuoco, il danno subito è ridotto di 2."
),
'Heavy_Metal': (
    "Il metallo che ricopre il corpo di questo Pokémon è così spesso da raddoppiarne facilmente il peso normale.",
    "Le mosse il cui danno è basato sul peso vengono modificate di conseguenza (peso raddoppiato)."
),
'Honey_Gather': (
    "Questo Pokémon produce il proprio miele: ogni giorno puoi ottenere un piccolo barile di miele di alta qualità.",
    "Un piccolo barile di miele può essere venduto fino a $100. Il miele attira i Pokémon selvatici e nutrirne uno lo rende felice."
),
'Huge_Power': (
    "Questo Pokémon possiede una fonte di Strength soprannaturale, al di là del suo aspetto fisico.",
    "Questo Pokémon ha un aumento permanente di 1 punto al suo attributo Strength."
),
'Hunger_Switch': (
    "Questo Pokémon diventa molto agitato quando ha fame: morde e si comporta male a meno che non gli si diano continuamente snack.",
    "Alla fine del Round, cambia la forma di questo Pokémon. Solo Morpeko può avere questa abilità. Non può essere copiata né scambiata."
),
'Hustle': (
    "Questo Pokémon fa tutto di fretta, risultando spesso approssimativo.",
    "Questo Pokémon riceve una Reduced Accuracy aggiuntiva e 2 dadi extra al Damage Pool per tutti i suoi attacchi fisici."
),
'Hydration': (
    "Il corpo di questo Pokémon assorbe l'acqua e ne usa l'umidità per mantenersi in salute.",
    "Se il meteo Pioggia è attivo, questo Pokémon cura qualsiasi Condizione di Stato alla fine del round."
),
'Hyper_Cutter': (
    "Gli artigli di questo Pokémon sono molto affilati e non possono essere smussati.",
    "Questo Pokémon non può subire riduzioni alla sua Strength per nessun motivo."
),
'Ice_Body': (
    "Il corpo di questo Pokémon è quasi congelato: si sente a casa quando le temperature sono sotto zero.",
    "Se il meteo Grandine è attivo, puoi ripristinare 1 HP a questo Pokémon alla fine del round. Questo Pokémon è immune al danno del meteo Grandine."
),
'Ice_Face': (
    "Il viso di questo Pokémon è ricoperto da un blocco di ghiaccio spesso che funge da protezione per il corpo. Se si rompe, avrà bisogno di temperature molto basse per riformarsi.",
    "Questo Pokémon ha 2 HP extra quando è in \"Ice Face Form\". Se il ghiaccio riceve 2 danni, cambia la forma del Pokémon in \"No-Ice Form\". Per ripristinare la \"Ice Face Form\", il Pokémon deve restare fuori un intero Round mentre il meteo Grandine è attivo."
),
'Ice_Scales': (
    "Il corpo di questo Pokémon è ricoperto da scaglie cristalline di ghiaccio, sempre fredde al tatto, che deflettono facilmente la maggior parte dei proiettili, dell'energia e della luce.",
    "Riduce di 2 il danno inflitto a questo Pokémon da tutti gli attacchi Special."
),
'Illuminate': (
    "Questo Pokémon produce luce naturalmente attraverso il suo corpo. Gli altri Pokémon si avvicinano curiosi quando la vedono.",
    "Aumenta la probabilità di incontri casuali con Pokémon selvatici. Se ci sono sfide ambientali con visibilità ridotta, questo Pokémon e i suoi alleati sono immuni agli effetti."
),
'Illusion': (
    "Questo Pokémon proietta un'illusione su se stesso per sembrare un'altra creatura che ha visto. L'illusione è indistinguibile dall'originale.",
    "Quando questo Pokémon entra in campo, assumerà l'aspetto di un altro Pokémon nel gruppo; riacquisterà la sua forma originale se subisce danno. Quando assume forma umana, non può parlare e la sua coda potrebbe restare visibile."
),
'Immunity': (
    "Questo Pokémon ha un sistema immunitario molto forte e si ammala raramente. Potrebbe persino mangiare cibo marcio senza conseguenze.",
    "Le Condizioni di Stato Poison e Badly Poison non infliggono danno a questo Pokémon."
),
'Imposter': (
    "Questo Pokémon può alterare rapidamente la propria struttura cellulare per trasformarsi in una copia di un altro essere.",
    "Non appena entra in battaglia, questo Pokémon subirà automaticamente gli effetti della mossa [[Transform]]."
),
'Infiltrator': (
    "Questo Pokémon è molto furtivo nei movimenti: è naturalmente più difficile da individuare degli altri.",
    "Le mosse scudo, Safeguard, Substitute, Light Screen e Reflect vengono ignorati da questo Pokémon."
),
'Innards_Out': (
    "Non avendo arti, questo Pokémon espelle i propri organi interni per usarli come membra o per difendersi. Disgustoso ma efficace.",
    "Se un attacco farebbe svenire questo Pokémon, infligge all'avversario un danno pari agli HP rimanenti che aveva."
),
'Inner_Focus': (
    "Questo Pokémon è estremamente serio e concentrato in tutto ciò che fa. Rimane calmo e non si tira mai indietro, anche quando viene gravemente ferito.",
    "Questo Pokémon non subisce Flinch e non può essere Intimidito (l'abilità Intimidate non ha alcun effetto contro questo Pokémon)."
),
'Insomnia': (
    "Questo Pokémon non ha bisogno di dormire: sarà sveglio qualunque sia l'ora.",
    "Questo Pokémon non è influenzato dalla Condizione di Stato Sleep."
),
'Intimidate': (
    "Questo Pokémon ha una presenza schiacciante che ispira sia paura che rispetto negli altri.",
    "Quando questo Pokémon entra in battaglia, riduce di 1 la Strength di tutti gli avversari nel raggio d'azione. Questo effetto dura finché il Pokémon è in campo. Riduce anche la probabilità di incontri casuali con Pokémon selvatici."
),
'Intrepid_Sword': (
    "Questo Pokémon audace non teme nessuna sfida: la sua forza aumenta grazie alla pura forza di volontà. La sua presenza può essere molto intimidatoria.",
    "Ogni volta che questo Pokémon entra in battaglia, aumenta di 2 la sua Strength. Al di fuori della battaglia, questo Pokémon può tagliare qualsiasi superficie."
),
'Iron_Barbs': (
    "Questo Pokémon è ricoperto da spigoli d'acciaio appuntiti che fanno male a chiunque li tocchi con poca attenzione.",
    "Ogni volta che questo Pokémon viene colpito da un Non-Ranged Physical Attack, tira 1 dado di danno contro l'attaccante."
),
'Iron_Fist': (
    "Le mani di questo Pokémon sono molto forti e pesanti: chiuse a pugno possono sfondare qualsiasi cosa.",
    "Aggiunge 1 dado al Damage Pool delle mosse basate sui pugni."
),
'Justified': (
    "Questo Pokémon ha un innato senso della giustizia: i soprusi lo faranno arrabbiare moltissimo.",
    "La prima volta che questo Pokémon viene colpito da un attacco di tipo Buio, o se ha assistito a qualcosa che ritiene ingiusto, aumenta di 1 la sua Strength."
),
'Keen_Eye': (
    "Questo Pokémon ha una vista eccezionale: localizzare oggetti piccoli o lontani sarà molto più facile.",
    "Questo Pokémon non può subire la rimozione di successi dai tiri di Accuracy tramite mosse, oggetti o abilità. Pain Penalization e difficoltà ambientali si applicano comunque."
),
'Klutz': (
    "Questo Pokémon non capisce come usare correttamente gli strumenti, finendo spesso per usarli in modi inaspettati.",
    "Gli oggetti tenuti non avranno alcun effetto su questo Pokémon."
),
'Leaf_Guard': (
    "Le foglie di questo Pokémon si espandono con il sole per coprire il suo corpo.",
    "Se il meteo Sole è attivo, questo Pokémon non può ricevere Condizioni di Stato. Le condizioni inflitte in precedenza rimangono."
),
'Levitate': (
    "Questo Pokémon levita per spostarsi senza toccare il suolo.",
    "Le mosse di tipo Terra e gli effetti legati al suolo non influenzano questo Pokémon. Se una mossa lo vincola al suolo, gli effetti vengono persi finché non è libero."
),
'Libero': (
    "Questo Pokémon ha sempre la mente in gioco. Privilegia una posizione difensiva e fa le migliori passaggi speciali quando attacca.",
    "Ogni volta che questo Pokémon usa una mossa, cambia prima il suo tipo in quello della mossa. Se la mossa è un attacco che infligge danno, applica il STAB appropriato."
),
'Light_Metal': (
    "Il materiale che ricopre il corpo di questo Pokémon è leggero come una piuma: pesa dal 50% al 75% in meno del normale.",
    "Le mosse il cui danno è basato sul peso vengono modificate di conseguenza (peso ridotto)."
),
'Lightning_Rod': (
    "Questo Pokémon attira fulmini ed elettricità verso di sé per potenziare la sua energia.",
    "Se qualcuno usa una mossa di tipo Elettro con bersaglio singolo, viene reindirizzata verso questo Pokémon; è immune al danno di tali mosse. La prima volta che viene colpito da una mossa di tipo Elettro, aumenta di 1 il suo Special."
),
'Limber': (
    "I muscoli di questo Pokémon sono incredibilmente flessibili ed elastici, facilitandone i movimenti, l'agilità e la grazia.",
    "Questo Pokémon non è influenzato dalla Condizione di Stato Paralysis."
),
'Liquid_Ooze': (
    "Questo Pokémon produce una melma pestilenziale e tossica nel suo corpo. Non tentare di mangiarla.",
    "Se colpito da una mossa che assorbe la sua energia vitale (Leech Seed, Dream Eater, Drain Punch, ecc.), infliggerà invece quel quantitativo come danno."
),
'Liquid_Voice': (
    "Le onde sonore della sua voce trasformano l'umidità nell'aria in acqua, evocando rugiada, pioggia e persino cascate dal nulla.",
    "Tutte le mosse basate sul suono usate da questo Pokémon sono considerate di tipo Acqua."
),
'Long_Reach': (
    "Questo Pokémon è in grado di attaccare attraverso le ombre di oggetti e avversari, mentre i bersagli reali subiscono il danno.",
    "Tutti gli attacchi di questo Pokémon sono considerati attacchi a distanza (Ranged)."
),
'Magic_Bounce': (
    "Questo Pokémon usa il controllo psichico sul suo avversario per farlo danneggiare indirettamente, facendolo sembrare magia.",
    "Tutte le mosse di supporto che prendono di mira questo Pokémon o il suo lato del campo vedranno i loro effetti reindirizzati verso l'avversario."
),
'Magic_Guard': (
    "Questo Pokémon è avvolto da una debole energia che blocca qualsiasi piccolo danno che possa venire.",
    "Questo Pokémon non subirà danno da Condizioni di Stato, Recoil, oggetti tenuti o Condizioni Meteo."
),
'Magician': (
    "Questo Pokémon eccelle nei semplici trucchi di magia che stupiscono gli altri, come far apparire e scomparire oggetti nelle vicinanze in un batter d'occhio.",
    "Questo Pokémon ruberà l'oggetto tenuto di un avversario che ha appena colpito."
),
'Magma_Armor': (
    "Il corpo di questo Pokémon è sempre caldo al tatto: può riscaldare una grande stanza semplicemente standoci e sopporta alte temperature.",
    "Questo Pokémon non è influenzato dalla Condizione di Stato Frozen."
),
'Magnet_Pull': (
    "Questo Pokémon può attivare un campo magnetico intorno a sé per attirare ogni tipo di metallo.",
    "Tutti i Pokémon di tipo Acciaio in campo diventano Blocked."
),
'Marvel_Scale': (
    "Le bellissime scaglie di questo Pokémon si induriscono quando il suo corpo è sotto stress.",
    "Se questo Pokémon ha una Condizione di Stato, aumenta di 2 la sua Defense."
),
'Mega_Launcher': (
    "I cannoni sul corpo di questo Pokémon gli permettono di sparare attacchi estremamente potenti.",
    "Aggiunge 2 dadi extra al Damage Pool o al Pool di Cura delle mosse con la parola chiave \"Pulse\" o \"Aura\" nel nome."
),
'Merciless': (
    "Una volta che questo Pokémon percepisce debolezza, inizia ad agire secondo la sua natura brutale. Può essere crudele se non tenuto sotto controllo.",
    "Se l'avversario è affetto da Poison o Badly Poison, tutte le mosse di questo Pokémon sono considerate Critical Hit. Questo Pokémon non si tratterrà nell'usare mosse con Lethal Damage, a discrezione dello Storyteller."
),
'Mimicry': (
    "Il corpo di questo Pokémon è perfetto per mimetizzarsi nel terreno. A volte si perde, ma lo troverai se qualche malcapitato gli cammina sopra.",
    "Se è attiva una mossa Terreno (es. Electric Terrain, Psychic Terrain ecc.), cambia il tipo principale di questo Pokémon in modo da corrispondere al Terreno attivo. Ripristina il tipo principale originale quando gli effetti del terreno terminano."
),
'Minus': (
    "Questo Pokémon ha una carica naturalmente negativa. Attrae la carica positiva e respinge quella negativa. Tende ad essere malinconico.",
    "Se un Pokémon alleato in campo ha l'abilità [[Plus]], aumenta di 2 il Special di questo Pokémon."
),
'Mirror_Armor': (
    "Il corpo di questo Pokémon è ricoperto da un'armatura lucida. Tale armatura respinge e rimanda indietro tutto ciò che cerca di indebolirlo.",
    "Tutti gli effetti che riducono gli attributi e che prendono di mira questo Pokémon o il suo lato del campo vengono reindirizzati verso l'avversario."
),
'Misty_Surge': (
    "Questo Pokémon può circondarsi di un campo nebbioso, stranamente silenzioso, che trasmette una sensazione di pace ma anche di solitudine.",
    "Quando questo Pokémon entra in campo, avvia automaticamente gli effetti della mossa [[Misty_Terrain|Misty Terrain]]. (In caso di parità, il Pokémon con la Will più alta potrebbe mantenere il Terreno dominante.)"
),
'Mold_Breaker': (
    "Questo Pokémon trova modi insoliti per raggiungere i propri obiettivi. È inventivo e aggira gli ostacoli.",
    "Se un Pokémon avversario ha un tipo, un'immunità o un'abilità che impedirebbe a questo Pokémon di attaccare con una certa mossa, viene ignorata."
),
'Moody': (
    "Questo Pokémon ha sbalzi d'umore piuttosto severi ed è spesso capriccioso. Speriamo sia solo una fase.",
    "Alla fine di ogni round, resetta gli attributi modificati da Moody, poi riduce di 1 un attributo casuale e aumenta di 1 un altro attributo casuale."
),
'Motor_Drive': (
    "Questo Pokémon assorbe l'elettricità e la immagazzina come energia per correre più veloce.",
    "La prima volta che questo Pokémon viene colpito da una mossa di tipo Elettro, aumenta di 1 il suo Dexterity. Questo Pokémon non riceve danno dalle mosse di tipo Elettro."
),
'Moxie': (
    "Questo Pokémon è naturalmente feroce e cerca di raggiungere una posizione di potere sconfiggendo i dominanti del branco.",
    "Se un avversario sviene a causa di un attacco di questo Pokémon, aumenta di 1 la sua Strength. Possono essere aggiunti al massimo 3 punti in questo modo."
),
'Multiscale': (
    "Questo Pokémon è ricoperto da due strati di scaglie dure: se uno strato viene danneggiato, viene eliminato e ricresce in seguito.",
    "Se questo Pokémon era a piena salute, riduce di 1 il danno di un attacco."
),
'Multitype': (
    "Tutte le energie che hanno creato l'universo scorrono crude attraverso questo Pokémon, che ne sfrutta quella più conveniente al momento.",
    "Questo Pokémon può cambiare liberamente il suo Tipo in qualsiasi momento. Questa abilità non può essere copiata, scambiata, modificata, ignorata o annullata in alcun modo."
),
'Mummy': (
    "Questo Pokémon maledirà chiunque osi fargli del male. La maledizione può durare generazioni e richiederà l'aiuto di un medium per essere rimossa.",
    "Quando questo Pokémon colpisce o viene colpito da un Non-Ranged Physical Attack, l'abilità dell'avversario viene cambiata in Mummy."
),
'Natural_Cure': (
    "Il corpo di questo Pokémon genera sostanze per auto-guarirsi, che possono essere usate per creare medicine.",
    "Alla fine del round, se questo Pokémon ha una Condizione di Stato, tira 3 Chance Dice per curarsi."
),
'Neuroforce': (
    "Il potere psichico di questo Pokémon è schiacciante e si percepisce anche solo standogli vicino. Sfrutta qualsiasi debolezza che trova nella tua mente.",
    "Questo Pokémon infligge 1 danno automatico con qualsiasi mossa che sia Super Effective contro un avversario."
),
'Neutralizing_Gas': (
    "Il Pokémon è circondato da un gas dal profumo dolce ma tossico. La maggior parte delle persone e dei Pokémon non riesce a fare a meno di fermarsi ad annusarlo.",
    "I Pokémon avversari nel raggio d'azione vedranno gli effetti delle loro abilità annullati finché questo Pokémon è in campo."
),
'No_Guard': (
    "Questo Pokémon si concentra nell'attaccare alla perfezione, ma sarà vulnerabile agli attacchi avversari poiché non si preoccupa di nient'altro che della sua precisione.",
    "Puoi dichiarare all'inizio del Round che questo Pokémon non effettuerà Evasion. In tal caso, tira tutte le mosse come se non avessero Reduced Accuracy."
),
'Normalize': (
    "Le azioni di questo Pokémon non sono mai impressionanti, sempre piatte e sembrano non riuscire mai ad essere eccezionali.",
    "Tutte le mosse conosciute da questo Pokémon sono considerate di tipo Normale. Applicando STAB, debolezze, immunità e resistenze di conseguenza. Aggiunge 1 dado di danno a tutte le mosse di tipo Normale."
),
'Oblivious': (
    "Questo Pokémon avrà raramente un'interazione sociale soddisfacente. È troppo preso da sé stesso per cogliere i segnali di ciò che ci si aspetta da lui.",
    "Questo Pokémon non è influenzato dalla Condizione di Stato Love. È immune agli effetti di mosse che ne influenzano i sentimenti, come Taunt, Charm, Captivate ecc."
),
'Overcoat': (
    "Questo Pokémon avrà un mantello protettivo intorno al corpo che gli permette di sopravvivere in condizioni meteorologiche estreme.",
    "Questo Pokémon non subirà danno dalle Condizioni Meteo."
),
'Overgrow': (
    "Quando questo Pokémon è ferito, farà crescere enormi piante sul suo corpo per difendersi. Queste piante sono molto forti, ma appassiscono rapidamente.",
    "Quando gli HP di questo Pokémon sono alla metà o meno, la Pain Penalization non riduce i successi ai tiri di danno delle sue mosse di tipo Erba, e ottengono 1 dado extra al Damage Pool."
),
'Own_Tempo': (
    "Questo Pokémon fa tutto al proprio ritmo e ignora la pressione degli altri. Il suo comportamento è riflessivo e calmo... forse troppo calmo.",
    "Questo Pokémon non è influenzato dalla Condizione di Stato Confused."
),
'Parental_Bond': (
    "Il Pokémon e il suo cucciolo sono molto legati e fanno tutto insieme. Il genitore è molto protettivo.",
    "Tutti i Damage Pool di questo Pokémon vengono tirati due volte. Scegli il risultato più alto per infliggere danno all'avversario."
),
'Pastel_Veil': (
    "Il Pokémon è circondato da un tenue bagliore dai colori pastello. Questa energia sembra pura e piena di innocenza. Incontaminabile e soprannaturale.",
    "L'utilizzatore e i suoi alleati nel raggio d'azione sono immuni a Poison e Badly Poison. Se la condizione era stata inflitta prima che questo Pokémon entrasse in campo, rimane."
),
'Perish_Body': (
    "Questo Pokémon maledice in silenzio chi lo ostacola. Condanna la loro anima a soffrire come lui ha sofferto. Evita questo Pokémon, altrimenti subirai la sua ira.",
    "Se questo Pokémon viene colpito da un Non-Ranged Physical Attack, l'avversario riceverà i suoi HP rimanenti come danno e sverrà dopo tre Round, a meno che non venga rimosso dalla battaglia."
),
'Pick_Up': (
    "Questo Pokémon raccoglie spesso oggetti e conserva un piccolo tesoro che potrebbe condividere con te.",
    "Se questo Pokémon era fuori dalla sua Pokéball, alla fine della scena vedi cosa ha trovato per te, a discrezione dello Storyteller."
),
'Pickpocket': (
    "Questo Pokémon ruba istintivamente dagli altri. Prende tutto quello che può quando le persone non guardano.",
    "Se questo Pokémon non ha un oggetto, ruberà l'oggetto tenuto dell'avversario che ha appena colpito con un Non-Ranged Physical Attack."
),
'Pixilate': (
    "Questo Pokémon sparge polvere fatata che porta pensieri felici nella mente. Tutto ciò che fa sembra incredibilmente adorabile.",
    "Le mosse di tipo Normale usate da questo Pokémon infliggono danno come se fossero di tipo Folletto. Applicando STAB, debolezze e resistenze di conseguenza. Aggiunge 1 dado extra di danno alle mosse di tipo Folletto."
),
'Plus': (
    "Questo Pokémon ha una carica naturalmente positiva. Attrae la carica negativa e respinge quella positiva. Ha sempre le guance rosse.",
    "Se un Pokémon alleato ha l'abilità [[Minus]], aumenta di 2 il Special di questo Pokémon."
),
'Poison_Heal': (
    "Questo Pokémon è immune a qualsiasi veleno e assimila quel veleno come fonte di energia.",
    "Se questo Pokémon viene avvelenato o fortemente avvelenato, curerà 1 HP alla fine di ogni round invece di subire danno. Il veleno verrà completamente assorbito dopo 3 Round."
),
'Poison_Point': (
    "Le spine e le scaglie appuntite di questo Pokémon rilasciano veleno che infetta chiunque le tocchi con forza. Indossare guanti quando lo si maneggia.",
    "Se questo Pokémon viene colpito da un Non-Ranged Physical Attack, tira 3 Chance Dice per avvelenare l'avversario (Poison)."
),
'Poison_Touch': (
    "Sostanze velenose grondano dal corpo di questo Pokémon: ti ammalerai gravemente se ti tocca.",
    "Se questo Pokémon colpisce l'avversario con un Non-Ranged Physical Attack, tira 2 Chance Dice per avvelenarlo (Poison)."
),
'Power_Construct': (
    "Piccole cellule si radunano intorno a questo Pokémon e vengono assorbite nel suo corpo. Cresce più grande e forte man mano che più cellule si uniscono.",
    "Alla fine del Round, se questo Pokémon ha la metà o meno degli HP, cambia la sua forma alla successiva (10% → 50% → 100%). Al cambio forma, rimuove le Condizioni di Stato e ripristina HP e Will completi. Non può essere copiata, scambiata né modificata. Solo Zygarde può avere questa abilità."
),
'Power_of_Alchemy': (
    "Questo Pokémon può assorbire l'essenza di tutto ciò che tocca, fondendosi con la composizione chimica e persino i geni dei rifiuti scartati.",
    "Per le successive 24 ore, il Pokémon copia l'abilità di un avversario svenuto. Possono essere copiate più abilità in questo modo, ma solo una può essere attiva in combattimento. (Alcune abilità non possono essere copiate, a discrezione dello Storyteller.)"
),
'Power_Spot': (
    "Questo Pokémon rilascia un'energia misteriosa che disturba l'elettronica e le bussole, ma che in qualche modo ti fa sentire molto energico.",
    "Aggiunge 1 dado extra ai Damage Pool delle mosse di un Alleato. Questo effetto non si accumula sullo stesso alleato se più Pokémon usano questa abilità."
),
'Prankster': (
    "Questo Pokémon avrà sempre un lampo di malizia negli occhi; nessuno nelle sue vicinanze sarà al sicuro dai suoi scherzi.",
    "Aggiunge Priority +1 a tutte le mosse di supporto di questo Pokémon."
),
'Pressure': (
    "Stare vicino a questo Pokémon è molto stressante e logorante; persino i più coraggiosi si sentiranno vacillare.",
    "Mentre questo Pokémon è in campo, riduce i Will Point totali di tutti gli avversari della metà, arrotondando per difetto."
),
'Primordial_Sea': (
    "La pioggia torrenziale lascia appena respirare, il campo si allaga rapidamente e si deve nuotare per restare a galla. Nessun fuoco può essere acceso in questi momenti.",
    "Quando questo Pokémon entra in campo, avvia automaticamente gli effetti del meteo Tifone. Gli effetti terminano quando il Pokémon lascia la battaglia. (In caso di parità, il Pokémon con la Will più alta potrebbe mantenere il meteo dominante.)"
),
'Prism_Armor': (
    "Il corpo di questo Pokémon è un'armatura incredibilmente resistente. Riesce a sopportare anche colpi che dovrebbero frantumarlo in pezzi.",
    "Annulla tutti i danni automatici di qualsiasi mossa Super Effective inflitta a questo Pokémon."
),
'Propeller_Tail': (
    "La coda di questo Pokémon gli permette di manovrare con molta facilità sott'acqua. Non ha problemi a fare improvvisi cambi di direzione per inseguire e catturare le prede.",
    "Ignora qualsiasi mossa o abilità che reindirizzerebbe le mosse di questo Pokémon verso un altro bersaglio (es. la mossa \"Follow Me\", l'abilità Lightning Rod ecc.)."
),
'Protean': (
    "Il corpo versatile di questo Pokémon gli conferisce abilità in praticamente tutto ciò che si propone di fare.",
    "Ogni volta che questo Pokémon usa una mossa, cambia prima il suo tipo in quello della mossa. Se la mossa è un attacco che infligge danno, applica il STAB appropriato."
),
'Psychic_Surge': (
    "Questo Pokémon può circondarsi di un campo psichico che fa fermare tutti, sentendo cose che non esistono.",
    "Quando questo Pokémon entra in campo, avvia automaticamente gli effetti della mossa [[Psychic_Terrain|Psychic Terrain]]. (In caso di parità, il Pokémon con la Will più alta potrebbe mantenere il Terreno dominante.)"
),
'Punk_Rock': (
    "Questo Pokémon ama la musica e i rumori forti. Improvvisa continuamente con la chitarra immaginaria e riesce facilmente a improvvisare un pezzo musicale dal nulla.",
    "Le mosse basate sul suono usate da questo Pokémon hanno 1 dado extra al Damage Pool. Le mosse basate sul suono infliggono 2 danni in meno a questo Pokémon."
),
'Pure_Power': (
    "Questo Pokémon sfrutta i suoi poteri psichici per muovere oggetti molte volte più grandi di lui.",
    "Questo Pokémon ha un aumento permanente di 1 punto al suo attributo Strength."
),
'Queenly_Majesty': (
    "La presenza di questo Pokémon impone soggezione e rispetto. Gli altri non hanno altra scelta che ubbidire; chi cerca di fregarlo sentirà la sua disapprovazione.",
    "Gli avversari non possono usare mosse con Priority contro questo Pokémon."
),
'Quick_Feet': (
    "Questo Pokémon sembra sempre di fretta. Sotto pressione si muoverà più veloce del normale.",
    "Mentre è affetto da una Condizione di Stato, aumenta di 2 il suo Dexterity. Il Pokémon può essere affetto da Paralysis, ma questa abilità ne impedisce gli effetti."
),
'Rain_Dish': (
    "Questo Pokémon immagazzina l'acqua piovana per bere e nutrirsi.",
    "Se il meteo Pioggia è attivo, puoi ripristinare 1 HP a questo Pokémon alla fine di ogni Round."
),
'Rattled': (
    "Quando questo Pokémon pauroso viene sorpreso o spaventato, si affretta ad allontanarsi dal pericolo.",
    "La prima volta che questo Pokémon viene colpito da un attacco di tipo Coleottero, Buio o Spettro, aumenta di 1 il suo Dexterity."
),
'Receiver': (
    "Questo Pokémon è abituato ad apprendere il comportamento tattico degli altri Pokémon con cui ha un legame.",
    "Se un alleato sviene in battaglia, questo Pokémon può copiare la sua abilità per le successive 24 ore. Può essere copiata solo un'abilità in questo modo. (Alcune abilità non possono essere copiate, a discrezione dello Storyteller.)"
),
'Reckless': (
    "Questo Pokémon si mette spesso in situazioni rischiose pur di ottenere ciò che vuole. Tende a rischiare la vita senza pensare alle conseguenze.",
    "Quando questo Pokémon usa una mossa con Recoil, aggiunge 2 dadi extra al Damage Pool di quella mossa."
),
'Refrigerate': (
    "Il corpo di questo Pokémon funziona come un congelatore: riesce a congelare le cose semplicemente toccandole.",
    "Le mosse di tipo Normale usate da questo Pokémon infliggono danno come se fossero di tipo Ghiaccio. Applicando STAB, debolezze e resistenze di conseguenza. Aggiunge 1 dado di danno alle mosse di tipo Ghiaccio."
),
'Regenerator': (
    "Il corpo di questo Pokémon si rigenera rapidamente dai danni: ferite che richiederebbero giorni per guarire migliorano in poche ore.",
    "Questo Pokémon può curarsi autonomamente fino a 4 Danni o fino a 2 Lethal Damage al giorno. Il Pokémon deve essere fuori dal combattimento per beneficiare di questo effetto."
),
'Ripen': (
    "Questo Pokémon riesce a maturare frutti e bacche in pochissimo tempo per renderli extra dolci e deliziosi: le bacche curative avranno gli effetti potenziati.",
    "Le mosse che usano bacche per effetti aggiuntivi avranno 2 dadi extra al Damage Pool (es. Natural Gift ecc.). Aumenta le proprietà curative delle bacche a discrezione dello Storyteller."
),
'Rivalry': (
    "Questo Pokémon è molto competitivo con gli altri per dimostrare la sua posizione di dominante nel branco, tuttavia cerca di conquistare il favore dei possibili compagni.",
    "Se questo Pokémon ha un avversario dello stesso sesso, aumenta di 1 la sua Strength. Se l'avversario è di sesso opposto, riduce di 1 la sua Strength."
),
'RKS_System': (
    "La fisiologia di questo Pokémon si trasforma in base al disco dati inserito nel suo RKS-drive. Esistono 17 dischi, uno per ogni Tipo (nessuno è di tipo Normale).",
    "Cambia il Tipo del Pokémon in modo da corrispondere al Disco nell'oggetto tenuto (es. un Disco Elettro rende questo Pokémon di tipo Elettro)."
),
'Rock_Head': (
    "La testa e il corpo di questo Pokémon sono così resistenti da non sentire quasi nulla. Attenzione: sbatte contro le cose senza nemmeno accorgersene.",
    "Questo Pokémon non subirà danno da Recoil."
),
'Rough_Skin': (
    "Usa protezioni sulle mani quando tocchi questo Pokémon. Il suo corpo è ricoperto da scaglie o spine appuntite che si conficcano nella pelle.",
    "Ogni volta che questo Pokémon viene colpito da un Non-Ranged Physical Attack, tira 1 dado di danno contro l'attaccante."
),
'Run_Away': (
    "Questo Pokémon è un maestro della fuga. Sarà difficile da catturare e riesce a passare anche per i buchi più piccoli.",
    "Questo Pokémon non può diventare Blocked. Può anche ottenere dadi bonus per fuggire da battaglie o prigionie, a discrezione dello Storyteller."
),
'Sand_Force': (
    "Questo Pokémon controlla le particelle di sabbia intorno al campo per potenziare i suoi attacchi.",
    "Se il meteo Tempesta di Sabbia è attivo quando questo Pokémon infligge danno con attacchi di tipo Terra, Acciaio o Roccia, aggiunge 1 dado extra al Damage Pool di quell'attacco. Il Pokémon è immune al danno del meteo Tempesta di Sabbia."
),
'Sand_Rush': (
    "Mentre la sabbia sferzante attraversa il campo di battaglia, questo Pokémon riesce a nuotarci come se fosse acqua.",
    "Se il meteo Tempesta di Sabbia è attivo, aumenta di 1 il Dexterity di questo Pokémon. Il Pokémon è immune al danno del meteo Tempesta di Sabbia."
),
'Sand_Spit': (
    "Questo Pokémon striscia nella sabbia del deserto mangiandone un po'; se viene colpito (o starnutisce) si scatena una tempesta di sabbia.",
    "Se questo Pokémon viene colpito da un Non-Ranged Physical Attack, avvia gli effetti del meteo Tempesta di Sabbia. L'effetto dura 4 round."
),
'Sand_Stream': (
    "Questo Pokémon può attivare una violenta tempesta di sabbia intorno a sé che durerà finché lo vorrà.",
    "Quando questo Pokémon entra in campo, avvia automaticamente gli effetti del meteo Tempesta di Sabbia. Gli effetti terminano quando il Pokémon lascia la battaglia. (In caso di parità, il Pokémon con la Will più alta potrebbe mantenere il meteo dominante.)"
),
'Sand_Veil': (
    "Il corpo di questo Pokémon si mimetizza facilmente con le particelle di sabbia nell'aria.",
    "Se il meteo Tempesta di Sabbia è attivo, aumenta di 1 l'Evasion di questo Pokémon. Il Pokémon è immune al danno del meteo Tempesta di Sabbia."
),
'Sap_Sipper': (
    "La dieta di questo Pokémon è strettamente vegetariana: adora in particolare la linfa dolce come nutrimento.",
    "La prima volta che questo Pokémon viene colpito da un attacco di tipo Erba, aumenta di 1 la sua Strength invece di subire danno. Le mosse di tipo Erba non infliggono danno a questo Pokémon."
),
'Schooling': (
    "Quando questo Pokémon è minacciato, chiama migliaia di alleati per creare un mostro incontrollabile. Più ci si trova vicino al mare, più arrivano in fretta.",
    "Solo Wishiwashi può avere questa abilità. Quando raggiunge la metà o meno degli HP, i suoi alleati arriveranno. All'arrivo, sostituisci il tuo Pokémon con Wishiwashi School-Form a HP pieni e aumenta il suo Rank a Pro. Alla fine della battaglia, ripristina Wishiwashi alla sua forma base.\n\n**Tempi di arrivo:** Mare/Fiume — fine del Round; Strada/Città — 2 Round; Grotta/Città — 3 Round; Deserto/Neve — 4 Round; Vulcano — 5 Round."
),
'Scrappy': (
    "Questo Pokémon non crede ai fantasmi.",
    "Questo Pokémon riesce a colpire i Pokémon di tipo Spettro con mosse di tipo Normale e Lotta, infliggendo danno normale. Applica le resistenze o le debolezze corrette al bersaglio se ha un tipo secondario."
),
'Screen_Cleaner': (
    "Questo Pokémon pulisce continuamente uno schermo invisibile; lo fa così bene che persino i veri schermi di vetro possono scomparire dopo che ha finito.",
    "Quando questo Pokémon entra in campo, rimuove qualsiasi barriera (es. Light Screen, Reflect, Aurora Veil ecc.) sia dal lato dell'utilizzatore che da quello dell'avversario."
),
'Serene_Grace': (
    "Questo Pokémon porta fortuna come se fosse benedetto dal cielo. La sua presenza è rasserenante e ti fa sentire calmo e pieno di gioia.",
    "Aggiunge 2 Chance Dice extra a tutti gli effetti secondari di questo Pokémon (es. se una mossa ha 3 Chance Dice per causare Flinch, con questo Pokémon ne tira 5)."
),
'Shadow_Shield': (
    "Quando è al massimo delle forze, il corpo spettrale di questo Pokémon non può essere toccato né trafitto da nulla; riesce persino ad attraversare i muri come se non ci fossero.",
    "Se questo Pokémon era a HP pieni, riduce di 2 il danno di un attacco. Questo effetto non può essere ignorato da mosse o abilità."
),
'Shadow_Tag': (
    "Questo Pokémon calpesta l'ombra dell'avversario, impedendogli di allontanarsi troppo.",
    "Tutti gli avversari diventano Blocked. I Pokémon di tipo Spettro sono immuni a questo effetto. I Pokémon con la stessa abilità sono immuni a questo effetto."
),
'Shed_Skin': (
    "Il corpo di questo Pokémon fa continuamente crescere nuova pelle e muta quella vecchia quando diventa troppo danneggiata.",
    "Alla fine del round, se questo Pokémon ha una Condizione di Stato, tira 3 Chance Dice per curarsi."
),
'Sheer_Force': (
    "Questo Pokémon è interessato solo a dimostrare la sua incredibile potenza in battaglia.",
    "Ogni volta che questo Pokémon usa un attacco con Chance Dice per un effetto aggiuntivo, puoi ignorare quei dadi e aggiungere 2 dadi al suo Damage Pool."
),
'Shell_Armor': (
    "Il guscio di questo Pokémon protegge i suoi punti vulnerabili dagli avversari.",
    "Se un avversario ottiene un Critical Hit su questo Pokémon, non otterrà i dadi di danno bonus per quell'attacco."
),
'Shield_Dust': (
    "Questo Pokémon genera continuamente granelli di polvere per schermarsi e proteggersi.",
    "Se questo Pokémon viene colpito da un attacco con Chance Dice per un effetto aggiuntivo, non sarà influenzato da tali effetti."
),
'Shields_Down': (
    "Il nucleo di questo Pokémon è protetto da uno scudo robusto; se lo scudo si rompe, il Pokémon inizia a comportarsi in modo frenetico.",
    "Solo Minior può avere questa abilità. Dopo aver raggiunto la metà o meno degli HP in battaglia, sostituisci Minior con Minior (Core) a HP pieni. Per riportarlo alla forma base, il nucleo deve essere liberato e poi riacciuffato dopo qualche giorno."
),
'Simple': (
    "La mente ingenua di questo Pokémon viene facilmente influenzata sia da sé stesso che dagli altri. Spesso trova modi per semplificare le cose.",
    "Se questo Pokémon subisce una riduzione di un attributo, riduce 1 punto in più. Se subisce un aumento di un attributo, aumenta 1 punto in più."
),
'Skill_Link': (
    "Questo Pokémon riesce a concatenare con perizia una raffica di attacchi. Ama anche la ripetizione e le sequenze.",
    "Aggiunge 2 dadi al tiro di Accuracy delle Azioni Successive."
),
'Slow_Start': (
    "Questo Pokémon è rimasto dormiente per migliaia di anni; i suoi movimenti sono pesanti e lenti. Scappa prima che scateni tutta la sua potenza.",
    "Durante i primi 5 Round di una battaglia, questo Pokémon andrà sempre per ultimo nell'ordine di Initiative. Dopo quei 5 Round, aumenta di 2 la sua Strength e il suo Dexterity e andrà sempre per primo. L'effetto si azzera se il Pokémon viene richiamato."
),
'Slush_Rush': (
    "Questo Pokémon è abituato a correre e cacciare sul terreno ghiacciato, spostandosi rapidamente nella neve durante le bufere.",
    "Se il meteo Grandine è attivo, aumenta di 1 il Dexterity di questo Pokémon. Il Pokémon è immune al danno del meteo Grandine."
),
'Sniper': (
    "Questo Pokémon si posiziona furtivamente in un punto vantaggioso per colpire i punti deboli dell'avversario.",
    "Se questo Pokémon ottiene un Critical Hit, riceverà 3 dadi bonus al Damage Pool dell'attacco invece dei normali 2."
),
'Snow_Cloak': (
    "La pelle di questo Pokémon si mimetizza bene con la neve e la grandine circostanti: è quasi invisibile.",
    "Se il meteo Grandine è attivo, aumenta di 1 l'Evasion di questo Pokémon. Il Pokémon è immune al danno del meteo Grandine."
),
'Snow_Warning': (
    "Questo Pokémon è in grado di richiamare una terribile grandinata a piacimento. La neve coprirà il campo e schegge di ghiaccio tagliente cadranno dal cielo.",
    "Quando questo Pokémon entra in campo, avvia automaticamente gli effetti del meteo Grandine. Gli effetti terminano quando il Pokémon lascia la battaglia. (In caso di parità, il Pokémon con la Will più alta potrebbe mantenere il meteo dominante.)"
),
'Solar_Power': (
    "Questo Pokémon è capace di sovraccaricarsi di energia solare, diventando più potente ma subendo anche un costo per il suo corpo.",
    "Se il meteo Sole è attivo, aumenta di 2 il suo Special. Se il meteo Sole è attivo, questo Pokémon subisce 1 danno alla fine del round."
),
'Solid_Rock': (
    "Il corpo di questo Pokémon è composto da roccia estremamente dura, che lo protegge da tutto, persino dalle proprie debolezze.",
    "Se questo Pokémon viene colpito da una mossa che infligge danno Super Effective, riduce di 1 il danno subito."
),
'Soul-Heart': (
    "Questo Pokémon è naturalmente premuroso e protettivo; se qualcuno che ama è in pericolo, la sua anima si irrobustisce grazie all'amore.",
    "Se un avversario sviene a causa di un attacco di questo Pokémon, aumenta di 1 il suo Special. Possono essere aggiunti al massimo 3 punti in questo modo."
),
'Soundproof': (
    "Il corpo di questo Pokémon è strutturato per proteggerlo dai rumori che potrebbero disturbare la sua pace e la sua concentrazione. Non ti sta ignorando: semplicemente non sente.",
    "Questo Pokémon è immune al danno e agli effetti di tutte le mosse basate sul suono."
),
'Speed_Boost': (
    "Questo Pokémon inizierà a manovrare a una velocità accelerata, muovendosi come se teletrasportasse da un posto all'altro.",
    "Alla fine del Round, aumenta di 1 il Dexterity di questo Pokémon. Possono essere aggiunti al massimo 3 punti in questo modo."
),
'Stakeout': (
    "Questo Pokémon controlla costantemente l'ambiente circostante, cercando possibili prede e attaccandole quando sono più vulnerabili.",
    "Ogni volta che un Pokémon avversario si ritira, questo Pokémon infliggerà 1 danno aggiuntivo con il suo primo attacco riuscito al sostituto."
),
'Stall': (
    "Questo Pokémon è indeciso e lascia sempre agire gli altri prima di decidere cosa fare.",
    "Questo Pokémon va sempre per ultimo nell'ordine di Initiative."
),
'Stalwart': (
    "Questo Pokémon ha un innato senso del dovere e della lealtà: una volta assegnato un compito, non si fermerà finché non sarà completato.",
    "Ignora qualsiasi mossa o abilità che reindirizzerebbe le mosse di questo Pokémon verso un altro bersaglio (es. la mossa \"Follow Me\", l'abilità Lightning Rod ecc.)."
),
'Stamina': (
    "Questo Pokémon non si stanca mai. Ritrova le forze quando si sente debole, anche quando mangia o dorme poco.",
    "La prima volta che questo Pokémon subisce danno in combattimento, aumenta di 1 la sua Defense e la sua Special Defense."
),
'Stance_Change': (
    "Questo Pokémon può cambiare forma diventando un potente scudo o una lama formidabile. I suoi attributi cambiano in base alla posizione scelta.",
    "Solo Aegislash può usare questa abilità. All'inizio del round, scegli una forma. In Spada può usare solo mosse di attacco. In Scudo, può usare solo mosse di supporto. Regola gli attributi in base al Rank e ai Limiti di ogni forma."
),
'Static': (
    "Il corpo di questo Pokémon è sempre pronto a scaricare una scintilla di elettricità statica al minimo contatto.",
    "Ogni volta che questo Pokémon viene colpito da un Non-Ranged Physical Attack, tira 3 Chance Dice per paralizzare l'avversario (Paralysis)."
),
'Steadfast': (
    "Questo Pokémon diventa ancora più affidabile quando l'avversità colpisce.",
    "La prima volta che questo Pokémon subisce Flinch, aumenta di 1 il suo Dexterity."
),
'Steam_Engine': (
    "Questo Pokémon funziona come una fornace a vapore: con un po' di fuoco e acqua riesce a muovere qualsiasi cosa a grande velocità. Ama anche mangiare carbone.",
    "La prima volta che questo Pokémon viene colpito da una mossa di tipo Fuoco o Acqua, aumenta di 3 il suo Dexterity."
),
'Steelworker': (
    "Questo Pokémon è in grado di modellare e mangiare l'acciaio, dando forma e un bordo più affilato a qualsiasi metallo che tocca.",
    "Gli attacchi di tipo Acciaio usati da questo Pokémon ottengono 1 dado extra al loro Damage Pool."
),
'Steely_Spirit': (
    "Questo Pokémon ha un comportamento ostinato la maggior parte del tempo. Se si mette in testa qualcosa lo porterà a termine. Irritante e al tempo stesso ispirante.",
    "Gli attacchi di tipo Acciaio usati da questo Pokémon e dai suoi alleati ottengono 1 dado extra al loro Damage Pool."
),
'Stench': (
    "Questo Pokémon può emettere un odore così sgradevole da respingere le persone e gli altri Pokémon.",
    "Riduce la probabilità di incontri casuali con Pokémon selvatici. Ogni volta che questo Pokémon viene colpito da un Non-Ranged Physical Attack, tira 1 Chance Dice per causare Flinch all'avversario."
),
'Sticky_Hold': (
    "Il corpo di questo Pokémon trasuda sempre sostanze adesive: se qualcosa si incolla, sarà molto difficile rimuoverlo.",
    "L'oggetto tenuto di questo Pokémon non può essere rimosso, rubato o scambiato da mosse o abilità."
),
'Storm_Drain': (
    "Questo Pokémon assorbe liquidi come una spugna, usandoli poi per aumentare la sua potenza e resistere più a lungo fuori dall'acqua.",
    "Se qualcuno usa una mossa di tipo Acqua con bersaglio singolo, viene reindirizzata verso questo Pokémon; è immune al danno di tali mosse. La prima volta che viene colpito da una mossa di tipo Acqua, aumenta di 1 il suo Special."
),
'Strong_Jaw': (
    "La mascella potente di questo Pokémon gli conferisce una forza di morso tremenda. I suoi denti riescono a lacerare quasi qualsiasi cosa.",
    "Se questo Pokémon usa una mossa con le parole chiave: Fang, Bite o Crunch, aggiunge 1 dado extra al Damage Pool di quella mossa."
),
'Sturdy': (
    "Il corpo di questo Pokémon è estremamente resistente ai danni: riesce a sopportare quasi qualsiasi cosa.",
    "La prima volta che questo Pokémon svenierebbe a causa di una mossa che infligge danno, resterà invece a 1 HP. Le Condizioni di Stato e il danno auto-inflitto lo faranno comunque svenire. Il Pokémon deve riposare per un'ora prima di beneficiare nuovamente di Sturdy."
),
'Suction_Cups': (
    "Le zampe di questo Pokémon contengono ventose che gli permettono di restare ancorato al posto. Riesce ad attaccarsi a qualsiasi superficie, persino a testa in giù.",
    "Questo Pokémon è immune agli effetti che forzano i cambi."
),
'Super_Luck': (
    "Questo Pokémon ha un'incredibile fortuna: gli accadono cose belle regolarmente.",
    "Aggiunge la proprietà \"High Critical\" a tutte le mosse di attacco di questo Pokémon. Se una mossa ha già High Critical, questo Pokémon avrà bisogno di 1 successo in più all'Accuracy roll per ottenere un Critical invece di 2."
),
'Surge_Surfer': (
    "Il campo magnetico di questo Pokémon gli permette di stare in piedi e surfare sulle correnti elettriche come se stesse fluttuando.",
    "Se Electric Terrain è attivo, aumenta di 2 il Dexterity di questo Pokémon."
),
'Swarm': (
    "Questo Pokémon entra in uno stato di mente alveare quando la sua vita è in pericolo, diventando più feroce e aggressivo.",
    "Quando gli HP di questo Pokémon sono alla metà o meno, la Pain Penalization non riduce i successi ai tiri di danno delle sue mosse di tipo Coleottero, e ottengono 1 dado extra al Damage Pool."
),
'Sweet_Veil': (
    "Il delizioso aroma di questo Pokémon stimolerà l'appetito di tutti i Pokémon nelle vicinanze.",
    "Questo Pokémon e i suoi alleati sono immuni alla Condizione di Stato Sleep. Aumenta la probabilità di incontri casuali con Pokémon selvatici."
),
'Swift_Swim': (
    "Questo Pokémon si muove più velocemente sull'acqua che sulla terra; persino una strada allagata da una pozzanghera gli permette di usare la massima velocità.",
    "Se il meteo Pioggia è attivo, aumenta di 2 il Dexterity di questo Pokémon."
),
'Symbiosis': (
    "Questo Pokémon ama formare una relazione benefica con qualsiasi alleato con cui fa squadra.",
    "Se un alleato perde o usa il suo oggetto tenuto, questo Pokémon gli passerà immediatamente il proprio come azione gratuita."
),
'Synchronize': (
    "Questo Pokémon può condividere il proprio umore, i propri sentimenti e le proprie sensazioni con gli altri, specialmente con chi gli ha causato dolore.",
    "Se un avversario infligge una Condizione di Stato a questo Pokémon, la stessa condizione viene inflitta all'avversario, a meno che non sia immune all'effetto."
),
'Tangled_Feet': (
    "Questo Pokémon si muove in modo molto strano e particolare quando è stordito o confuso; di solito questo va a suo vantaggio.",
    "Mentre questo Pokémon è Confused, aggiunge una Reduced Accuracy extra a tutte le mosse degli avversari che lo prendono di mira."
),
'Tangling_Hair': (
    "I capelli di questo Pokémon sono spessi e forti e ingarbugliamo facilmente chiunque si avvicini. Spazzolali due volte al giorno per tenerli setosi e lucenti.",
    "La prima volta che un avversario colpisce questo Pokémon con un Non-Ranged Physical Attack, riduce di 1 il suo Dexterity."
),
'Technician': (
    "Questo Pokémon è meticoloso e preciso in compiti che tutti gli altri svolgerebbero in modo approssimativo e senza cura.",
    "Aggiunge 1 dado al Damage Pool di tutte le mosse con Power 2 o inferiore."
),
'Telepathy': (
    "Questo Pokémon riesce a comunicare usando la telepatia. Può inviare messaggi ad altre menti, ma non può riceverne.",
    "Questo Pokémon non subirà danno dalle mosse eseguite dai suoi alleati."
),
'Teravolt': (
    "Dal corpo di questo Pokémon emerge una sfera di fulmini blu che impedisce ai suoi avversari di essere fuori portata: qualunque cosa faccia, li fulminierà.",
    "Se una mossa, un oggetto o un'abilità impedirebbe a questo Pokémon di prendere di mira un avversario o di infliggere un effetto, viene ignorata (es. un Pokémon con Immunity può essere avvelenato, un Pokémon con Levitate può essere colpito da mosse di tipo Terra)."
),
'Thick_Fat': (
    "Il corpo di questo Pokémon ha uno spesso strato di grasso che lo protegge dalle temperature estreme.",
    "Riduce di 1 il danno subito da mosse di tipo Fuoco e Ghiaccio."
),
'Tinted_Lens': (
    "Gli occhi simili a occhiali di questo Pokémon riescono a trovare il lato positivo in ogni situazione negativa, anche quando non ce n'è.",
    "Se un avversario ha una resistenza contro un attacco di questo Pokémon, quell'attacco infligge danno normale invece. Se l'avversario ha una doppia resistenza, l'attacco viene trattato come se avesse solo una resistenza."
),
'Torrent': (
    "Questo Pokémon accumula pressione per sparare getti d'acqua. Quando quella pressione non può essere contenuta, viene rilasciata in torrenti incontrollabili.",
    "Quando gli HP di questo Pokémon sono alla metà o meno, la Pain Penalization non riduce i successi ai tiri di danno delle sue mosse di tipo Acqua, e ottengono 1 dado extra al Damage Pool."
),
'Tough_Claws': (
    "Gli artigli di questo Pokémon sono così robusti da poter lacerare quasi qualsiasi cosa.",
    "Ogni volta che questo Pokémon usa un Non-Ranged Physical Attack, aggiunge 1 dado al suo Damage Pool."
),
'Toxic_Boost': (
    "Il sangue di questo Pokémon bolle e va in una furia potente ogni volta che viene affetto dal Veleno.",
    "Se questo Pokémon riceve la Condizione di Stato Poison o Badly Poison, aumenta di 2 la sua Strength."
),
'Trace': (
    "Questo Pokémon imita le caratteristiche speciali degli altri, facendole sembrare sue.",
    "Questo Pokémon copia l'abilità di un avversario casuale quando entra in campo. L'effetto termina se viene rimosso dalla battaglia. Alcune abilità (Flower Gift, Illusion, Imposter, Stance Change, Wonder Guard ecc.) non possono essere copiate."
),
'Triage': (
    "Questo Pokémon sente l'urgenza di curare i feriti ed è molto rapido nel medicare e fare nodi. Una competenza spesso usata per medicare istantaneamente le ferite.",
    "Aggiunge Priority +1 a tutte le mosse di supporto di questo Pokémon che curano HP o Condizioni di Stato."
),
'Truant': (
    "Questo Pokémon è estremamente pigro: non fa nemmeno il minimo sforzo e spesso bighellona anche nel pieno di una battaglia.",
    "Tira la Loyalty di questo Pokémon ogni altro turno, ottenendo almeno 2 successi. Se il tiro fallisce, questo Pokémon si rifiuta di agire. Se riesce, può agire normalmente."
),
'Turboblaze': (
    "Il Pokémon circonda tutto con una gigantesca sfera di fiamme vorticanti che impedisce ai suoi avversari di essere fuori portata: non c'è scampo al calore.",
    "Se una mossa, un oggetto o un'abilità impedirebbe a questo Pokémon di prendere di mira un avversario o di infliggere un effetto, viene ignorata (es. un Pokémon con Immunity può essere avvelenato, un Pokémon con Levitate può essere colpito da mosse di tipo Terra)."
),
'Unaware': (
    "Questo Pokémon è ignaro di molti dettagli dell'ambiente circostante: raramente nota ciò che accade intorno a lui.",
    "Questo Pokémon ignora qualsiasi aumento o riduzione degli attributi dell'avversario, sia quando attacca che quando subisce danno."
),
'Unburden': (
    "Questo Pokémon sta meglio quando non deve portare niente con sé. Ama potersi muovere senza restrizioni.",
    "La prima volta che questo Pokémon perde o usa il suo oggetto tenuto e non ne ha più uno, aumenta di 2 il suo Dexterity."
),
'Unnerve': (
    "Che sia il suo sguardo potente o la sua presenza minacciosa, gli altri vicino a questo Pokémon diventano così nervosi da perdere l'appetito.",
    "Gli avversari non possono consumare la loro bacca tenuta mentre questo Pokémon è in campo."
),
'Victory_Star': (
    "La presenza di questo Pokémon è un incredibile boost al morale. Chi ottiene il suo favore sarà guidato alla vittoria.",
    "Le mosse offensive di questo Pokémon e di tutti i suoi alleati ottengono la proprietà \"Never Miss\" finché questo Pokémon è in campo. Questa abilità non può essere scambiata né ceduta."
),
'Vital_Spirit': (
    "Questo Pokémon è incredibilmente attivo ed energico. Ha bisogno di attività e esercizio costanti o agirà in modo distruttivo. Non dorme mai.",
    "Questo Pokémon è immune alla Condizione di Stato Sleep."
),
'Volt_Absorb': (
    "Il corpo di questo Pokémon è praticamente una batteria sempre pronta a essere caricata al massimo.",
    "Ogni volta che questo Pokémon viene colpito da una mossa di tipo Elettro, puoi curare 1 HP invece di subire danno. Le mosse di tipo Elettro non infliggono danno a questo Pokémon."
),
'Wandering_Spirit': (
    "Questo Pokémon è uno spirito errante con un'espressione tormentata sul viso. Non risponde ai richiami e potrebbe perdersi fluttuando senza meta. Contatta un medium per guarirlo.",
    "Se questo Pokémon colpisce un avversario con un Non-Ranged Physical Attack, scambia la propria abilità con quella dell'avversario. Alcune abilità (Flower Gift, Illusion, Imposter, Stance Change, Wonder Guard ecc.) non possono essere scambiate, a discrezione dello Storyteller."
),
'Water_Absorb': (
    "Il corpo di questo Pokémon è composto per lo più di acqua: la immagazzina dentro di sé e la usa come nutrimento.",
    "Ogni volta che questo Pokémon viene colpito da una mossa di tipo Acqua, puoi curare 1 HP invece di subire danno. Le mosse di tipo Acqua non infliggono danno a questo Pokémon."
),
'Water_Bubble': (
    "Questo Pokémon è protetto da una bolla d'acqua. Stranamente, la bolla contiene acqua limpida invece di aria.",
    "Le mosse di tipo Fuoco infliggono 1 danno in meno a questo Pokémon. Questo Pokémon è immune alle Condizioni di Stato Burn 1 e Burn 2. Aggiunge 2 dadi extra al Damage Pool delle sue mosse di tipo Acqua."
),
'Water_Compaction': (
    "Il corpo di questo Pokémon assorbe acqua a una velocità sorprendente; si indurisce man mano che si asciuga rapidamente.",
    "La prima volta che questo Pokémon viene colpito da una mossa di tipo Acqua, aumenta di 2 la sua Defense invece di subire danno. Le mosse di tipo Acqua non infliggono danno a questo Pokémon."
),
'Water_Veil': (
    "Questo Pokémon è sempre bagnato e produce acqua per mantenersi umido. Grazie a questo, può stare lontano da un corpo d'acqua per molto tempo.",
    "Questo Pokémon è immune a qualsiasi Condizione di Stato Burn."
),
'Weak_Armor': (
    "Gli strati protettivi esterni di questo Pokémon possono staccarsi, permettendogli di muoversi più liberamente e agilmente.",
    "La prima volta che questo Pokémon viene colpito da qualsiasi attacco fisico, aumenta di 1 il suo Dexterity e riduce di 1 la sua Defense."
),
'White_Smoke': (
    "Questo Pokémon rilascia continuamente fumo bianco che lo rende difficile da vedere. Usa il fumo per mimetizzarsi.",
    "Gli avversari non possono ridurre gli attributi di questo Pokémon. Può però ridurre i propri attributi autonomamente."
),
'Wimp_Out': (
    "Questo Pokémon va in grande stress ogni volta che il suo esoscheletro si indebolisce: riesce a fuggire da qualsiasi situazione grazie alla sua viltà.",
    "Ogni volta che questo Pokémon raggiunge la metà degli HP totali, si ritirerà nella sua Pokéball, mandando un alleato al suo posto. Se non ci sono alleati, la battaglia potrebbe terminare. Questo effetto non è influenzato da Blocked."
),
'Wonder_Guard': (
    "Il corpo di questo Pokémon è protetto da un'incredibile aura soprannaturale. La maggior parte delle cose lo attraversa come se non ci fosse nulla.",
    "Questo Pokémon subisce danno solo dalle Condizioni di Stato e dalle mosse che infliggono danno Super Effective contro di lui. È immune al danno da Condizioni Meteo, trappole sul campo e altre fonti esterne."
),
'Wonder_Skin': (
    "La pelle di questo Pokémon è ricoperta da un sottile velo protettivo che indebolisce i pericoli.",
    "Riduce fino a 2 Chance Dice dagli avversari contro questo Pokémon (es. la mossa Ember ha 1 Chance Dice per infliggere Burn; contro questo Pokémon ne ha zero)."
),
'Zen_Mode': (
    "Sotto stress estremo, questo Pokémon sblocca le proprie capacità psichiche nascoste attraverso la meditazione. Tornerà normale il giorno dopo.",
    "Solo Darmanitan può usare questa abilità. Quando si trova alla metà o meno degli HP, cambia alla Forma Zen Mode alla fine del Round. Usa la sua Forma Zen Mode da quel momento in poi. Regola gli attributi in base al Rank e ai Limiti di ogni forma."
),
}


def make_file(slug, flavor, effect):
    display = slug.replace('_', ' ')
    tags = ['ability'] + [w.lower() for w in slug.replace('-', '_').replace('_', '-').split('-')]
    tags_str = ', '.join(f'"{t}"' for t in tags)
    content = f'''---
title: "{display}"
category: Ability
tags: [{tags_str}]
---

# {display}

*{flavor}*

**Effetto:** {effect}
'''
    path = os.path.join(ABIL_DIR, f'{slug}.md')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    return slug


ok, missing = 0, []
for slug, (flavor, effect) in TRANSLATIONS.items():
    make_file(slug, flavor, effect)
    ok += 1

# Check for files in dir not in TRANSLATIONS
for fname in os.listdir(ABIL_DIR):
    if fname.endswith('.md'):
        slug = fname[:-3]
        if slug not in TRANSLATIONS:
            missing.append(slug)

print(f'Aggiornati: {ok}  |  Non trovati nel dizionario: {len(missing)}')
for m in missing:
    print(f'  MANCANTE: {m}')
