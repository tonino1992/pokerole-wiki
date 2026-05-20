import os
import urllib.request
import zipfile
import json
import re

# Percorsi
ZIP_URL = "https://github.com/Willowlark/Pokerole-Data/archive/refs/heads/master.zip"
ZIP_PATH = "raw/Pokerole-Data-master.zip"
JSON_DIR = "raw/Pokerole-Data-master/v2.0/Moves"
MOVES_DIR = "wiki/05_Mosse_e_Abilita/Mosse"
TRAITS_DIR = "wiki/05_Mosse_e_Abilita/Tratti"

# Crea directory
os.makedirs("raw", exist_ok=True)
os.makedirs(TRAITS_DIR, exist_ok=True)

# 1. Scarica ed estrai il database
if not os.path.exists(JSON_DIR):
    print("Download database Pokerole-Data in corso...")
    urllib.request.urlretrieve(ZIP_URL, ZIP_PATH)
    print("Estrazione in corso...")
    with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
        # Estrai solo la cartella Moves
        for file in zip_ref.namelist():
            if file.startswith("Pokerole-Data-master/v2.0/Moves/") and file.endswith(".json"):
                zip_ref.extract(file, "raw")
    print("Database estratto.")

# Dizionario per mappare le chiavi JSON a nomi standard per i file Tratto
TRAIT_MAP = {
    "HighCritical": "High_Critical",
    "DestroyShield": "Destroy_Shield",
    "IgnoreDefenses": "Ignore_Defenses",
    "Priority": "Priority",
    "NeverFail": "Never_Fail",
    "BlockDamagePool": "Block_Damage_Pool",
    "DoubleAction": "Double_Action",
    "Lethal": "Lethal",
    "SwitcherMove": "Switcher_Move",
    "AccuracyReduction": "Accuracy_Reduction",
    "Charge": "Charge",
    "PhysicalRanged": "Physical_Ranged",
    "MustRecharge": "Must_Recharge",
    "SoundBased": "Sound_Based",
    "SuccessiveActions": "Successive_Actions",
    "FistBased": "Fist_Based",
    "ShieldMove": "Shield",
    "Recoil": "Recoil",
    # Added Effects
    "Ailments": "Status_Condition",
    "StatChanges": "Stat_Changes",
    "Heal": "Heal",
    "AilmentHeal": "Ailment_Heal",
    "FixedDamage": "Fixed_Damage"
}

TRAIT_DESCRIPTIONS = {
    "High_Critical": "Questa mossa ha un'alta probabilità di infliggere un colpo critico.",
    "Destroy_Shield": "Distrugge le barriere come Protect o Detect.",
    "Ignore_Defenses": "Ignora le modifiche alle statistiche difensive del bersaglio.",
    "Priority": "Modifica l'ordine di iniziativa nel Round. Priority alte agiscono prima.",
    "Never_Fail": "Questa mossa non può essere evasa, ma può subire un Clash.",
    "Block_Damage_Pool": "Blocca o riduce i dadi danno in specifiche circostanze.",
    "Double_Action": "Richiede due azioni (o turni) per essere completata.",
    "Lethal": "Infligge Lethal Damage, che può essere fatale e richiede cure specifiche.",
    "Switcher_Move": "Forza la sostituzione del Pokémon avversario o scambia l'utilizzatore.",
    "Accuracy_Reduction": "Riduce temporaneamente l'Accuracy dell'utilizzatore o bersaglio.",
    "Charge": "L'utilizzatore deve caricare la mossa prima di poterla eseguire.",
    "Physical_Ranged": "Una mossa fisica che può essere effettuata a distanza.",
    "Must_Recharge": "L'utilizzatore deve riposare durante la prima azione del Round successivo.",
    "Sound_Based": "Mossa basata sul suono. Ignora i Substitute.",
    "Successive_Actions": "Colpisce più volte di fila. Spesso usata in combinazione con multi-hit.",
    "Fist_Based": "Mossa basata sui pugni. Beneficia dell'abilità Iron Fist.",
    "Shield": "Una mossa scudo. Usata consecutivamente, la sua Accuracy subisce penalità.",
    "Recoil": "L'utilizzatore subisce danni di contraccolpo pari ai danni inflitti.",
    "Status_Condition": "Infligge uno status alterato (es. Burn, Sleep, Paralysis).",
    "Stat_Changes": "Altera le statistiche (Attributes) in battaglia.",
    "Heal": "Cura l'utilizzatore o un alleato.",
    "Ailment_Heal": "Cura una Status Condition.",
    "Fixed_Damage": "Infligge un ammontare di danno fisso, ignorando le resistenze ordinarie."
}

# 2. Crea le pagine per i tratti
print("Generazione file dei Tratti...")
for trait_key, trait_name in TRAIT_MAP.items():
    desc = TRAIT_DESCRIPTIONS.get(trait_name, "Dettaglio dell'effetto della mossa.")
    content = f"""---
title: "{trait_name.replace('_', ' ')}"
category: Trait
---

# {trait_name.replace('_', ' ')}

{desc}

> Le mosse con questo tratto applicano meccaniche speciali durante il combattimento.
"""
    with open(os.path.join(TRAITS_DIR, f"{trait_name}.md"), "w", encoding="utf-8") as f:
        f.write(content)

# 3. Analizza le mosse locali e aggiunge i Traits
print("Aggiornamento Mosse...")
files = [f for f in os.listdir(MOVES_DIR) if f.endswith('.md')]

for filename in files:
    filepath = os.path.join(MOVES_DIR, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if "- **Traits:**" in content:
        continue # Già processato

    # Trova il file JSON corrispondente (es. "Water_Sport.md" -> "Water Sport.json")
    # Ci sono alcune differenze di escaping, ad esempio Nidoran, ma le mosse non hanno problemi
    base_name = filename.replace('.md', '')
    # Tenta di trovare il json
    json_name = base_name.replace('_', ' ') + ".json"
    json_path = os.path.join(JSON_DIR, json_name)
    
    if not os.path.exists(json_path):
        # Fallback case sensitive
        candidates = [f for f in os.listdir(JSON_DIR) if f.lower() == json_name.lower()]
        if candidates:
            json_path = os.path.join(JSON_DIR, candidates[0])
        else:
            print(f"JSON non trovato per {filename}")
            continue

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    traits = []

    # Processa Attributes
    if "Attributes" in data:
        for attr, val in data["Attributes"].items():
            t_name = TRAIT_MAP.get(attr, attr)
            if val is True:
                traits.append(f"[[{t_name}]]")
            elif isinstance(val, (int, str)):
                traits.append(f"[[{t_name}]] ({val})")

    # Processa AddedEffects
    if "AddedEffects" in data:
        for eff, details in data["AddedEffects"].items():
            t_name = TRAIT_MAP.get(eff, eff)
            # Dettagli (es. Burn, -1 Defense, ecc.)
            mods = []
            if isinstance(details, dict):
                # Caso StatChanges (es. {"Target": "Foe", "Stat": "Defense", "Stages": -1})
                if eff == "StatChanges":
                    stat = details.get("Stat", "")
                    stages = details.get("Stages", "")
                    if stat and stages:
                        mods.append(f"{stat} {stages}")
                # Caso Ailments (è una lista a volte)
                # Lasciamo che il loop dopo gestisca le liste se esistono
            
            # Gestione specifica di Ailments che è un array di dict
            if eff == "Ailments" and isinstance(details, list):
                for ail in details:
                    ail_type = ail.get("Type", "").replace("1", "").replace("2", "").replace("3", "")
                    chance = ail.get("ChanceDice", "")
                    if chance:
                        mods.append(f"{ail_type} Chance Dice {chance}")
                    else:
                        mods.append(ail_type)
            
            if eff == "Heal" and isinstance(details, dict):
                perc = details.get("Percentage", "")
                if perc:
                    mods.append(f"{int(float(perc)*100)}%")

            if mods:
                traits.append(f"[[{t_name}]] ({', '.join(mods)})")
            else:
                traits.append(f"[[{t_name}]]")

    if not traits:
        continue # Nessun tratto da aggiungere

    traits_line = f"- **Traits:** {', '.join(traits)}"
    
    # Inserisci sotto Target
    content = re.sub(r'(- \*\*Target:\*\* [^\n]+)', r'\1\n' + traits_line, content)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("Aggiornamento Mosse Completato!")
