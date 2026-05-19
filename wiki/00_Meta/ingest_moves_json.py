import os
import json
import urllib.request
import urllib.parse
import time
import re

moves_dir = 'wiki/04_Moves_e_Abilities/Mosse'
os.makedirs(moves_dir, exist_ok=True)

print("Fase 1: Ottenimento lista mosse da GitHub...")
api_url = "https://api.github.com/repos/Willowlark/Pokerole-Data/git/trees/master?recursive=1"
try:
    req = urllib.request.Request(api_url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req)
    tree_data = json.loads(response.read().decode('utf-8'))
except Exception as e:
    print(f"Errore API GitHub: {e}")
    exit(1)

move_paths = [t['path'] for t in tree_data['tree'] if t['path'].startswith('v2.0/Moves/') and t['path'].endswith('.json')]
print(f"Trovate {len(move_paths)} mosse.")

# Pre-conta le mosse già presenti per il resume
existing_files = set(os.listdir(moves_dir))
skipped = 0

print(f"Fase 2: Download e Generazione Markdown... ({len(existing_files)} mosse già presenti, verranno saltate)")
for path in move_paths:
    url_path = urllib.parse.quote(path)
    raw_url = f"https://raw.githubusercontent.com/Willowlark/Pokerole-Data/master/{url_path}"
    
    try:
        req = urllib.request.Request(raw_url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        data = json.loads(response.read().decode('utf-8'))
    except Exception as e:
        print(f"Errore download {raw_url}: {e}")
        continue
        
    name = data.get("Name", "Unknown")
    move_type = data.get("Type", "Normal")
    power = data.get("Power", 0)
    category = data.get("Category", "Support")
    
    # Formatta Accuracy
    acc1 = data.get("Accuracy1", "")
    acc2 = data.get("Accuracy2", "")
    accuracy = "N/A"
    if acc1 and acc2:
        accuracy = f"{acc1} + {acc2}"
    elif acc1:
        accuracy = acc1
        
    # Formatta Damage
    dam1 = data.get("Damage1", "")
    dam2 = data.get("Damage2", "")
    damage = "N/A"
    if dam1 and dam2:
        damage = f"{dam1} + {dam2}"
    elif dam1:
        damage = f"{dam1} + {power}" if power else dam1
    elif power:
        damage = str(power)
        
    target = data.get("Target", "Foe")
    effect = data.get("Effect", "-")
    desc = data.get("Description", "")
    
    # Sanitize filename (remove slashes, colons, etc)
    safe_name = re.sub(r'[\\/*?:"<>|]', "", name).replace(" ", "_")
    md_filename = f"{safe_name}.md"
    md_path = os.path.join(moves_dir, md_filename)

    # Skip se già esiste (resume)
    if md_filename in existing_files:
        skipped += 1
        continue
    
    tags = ["move", move_type.lower(), category.lower()]
    
    md_content = f"""---
title: "{name}"
category: Move
tags: [{', '.join(tags)}]
---

# {name}
*{move_type} | {category}*

- **Accuracy:** {accuracy}
- **Damage:** {damage}
- **Target:** {target}
- **Effect:** {effect}

> {desc}
"""
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
        
    print(f"Generato {md_filename}")
    time.sleep(0.05) # Rate limit protection

total_generated = len(move_paths) - skipped
print(f"\nFase 2 Completata. Ingest Mosse terminato.")
print(f"  - Mosse totali nel database: {len(move_paths)}")
print(f"  - Mosse saltate (già presenti): {skipped}")
print(f"  - Mosse generate in questa sessione: {total_generated}")
print(f"  - File totali ora in {moves_dir}: {len(os.listdir(moves_dir))}")
