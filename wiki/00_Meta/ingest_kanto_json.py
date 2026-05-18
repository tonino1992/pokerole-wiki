import os
import re
import json
import urllib.request
import fitz
import time

kanto_pokemon = [
    "Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard", 
    "Squirtle", "Wartortle", "Blastoise", "Caterpie", "Metapod", "Butterfree", 
    "Weedle", "Kakuna", "Beedrill", "Pidgey", "Pidgeotto", "Pidgeot", 
    "Rattata", "Raticate", "Spearow", "Fearow", "Ekans", "Arbok", 
    "Pikachu", "Raichu", "Sandshrew", "Sandslash", "Nidoran (F)", "Nidorina", "Nidoqueen", 
    "Nidoran (M)", "Nidorino", "Nidoking", "Clefairy", "Clefable", "Vulpix", "Ninetales", 
    "Jigglypuff", "Wigglytuff", "Zubat", "Golbat", "Oddish", "Gloom", "Vileplume", 
    "Paras", "Parasect", "Venonat", "Venomoth", "Diglett", "Dugtrio", 
    "Meowth", "Persian", "Psyduck", "Golduck", "Mankey", "Primeape", 
    "Growlithe", "Arcanine", "Poliwag", "Poliwhirl", "Poliwrath", "Abra", "Kadabra", "Alakazam", 
    "Machop", "Machoke", "Machamp", "Bellsprout", "Weepinbell", "Victreebel", 
    "Tentacool", "Tentacruel", "Geodude", "Graveler", "Golem", "Ponyta", "Rapidash", 
    "Slowpoke", "Slowbro", "Magnemite", "Magneton", "Farfetch'd", "Doduo", "Dodrio", 
    "Seel", "Dewgong", "Grimer", "Muk", "Shellder", "Cloyster", 
    "Gastly", "Haunter", "Gengar", "Onix", "Drowzee", "Hypno", 
    "Krabby", "Kingler", "Voltorb", "Electrode", "Exeggcute", "Exeggutor", 
    "Cubone", "Marowak", "Hitmonlee", "Hitmonchan", "Lickitung", "Koffing", "Weezing", 
    "Rhyhorn", "Rhydon", "Chansey", "Tangela", "Kangaskhan", "Horsea", "Seadra", 
    "Goldeen", "Seaking", "Staryu", "Starmie", "Mr. Mime", "Scyther", "Jynx", 
    "Electabuzz", "Magmar", "Pinsir", "Tauros", "Magikarp", "Gyarados", 
    "Lapras", "Ditto", "Eevee", "Vaporeon", "Jolteon", "Flareon", 
    "Porygon", "Omanyte", "Omastar", "Kabuto", "Kabutops", "Aerodactyl", 
    "Snorlax", "Articuno", "Zapdos", "Moltres", "Dratini", "Dragonair", "Dragonite", 
    "Mewtwo", "Mew"
]

pdf_path = 'raw/POKEROLE COREBOOK 2.0 (2).pdf'
img_dir = 'wiki/assets/images/pokedex/kanto'
md_dir = 'wiki/03_Pokedex/Kanto'

os.makedirs(md_dir, exist_ok=True)

# 1. Map Pokemon to PDF pages using regex
print("Fase 1: Mappatura Pagine PDF...")
doc = fitz.open(pdf_path)
page_map = {}
for page_idx in range(89, 129):
    text = doc[page_idx].get_text("text")
    for pkmn in kanto_pokemon:
        search_name = pkmn.split(" (")[0] # Handle Nidoran
        safe_pkmn = re.escape(search_name)
        if re.search(r'\b' + safe_pkmn + r'\b', text, re.IGNORECASE):
            if pkmn not in page_map:
                page_map[pkmn] = page_idx + 1

# 2. Download JSON and Generate Markdown
print("Fase 2: Download JSON e Generazione Markdown...")
for pkmn in kanto_pokemon:
    # Format URL name (e.g. Nidoran (F) -> Nidoran_F or Nidoran F)
    # Looking at Willowlark repo, Farfetch'd is Farfetch'd.json, Mr. Mime is Mr. Mime.json, Nidoran (F) is Nidoran F.json
    url_name = pkmn.replace(" (F)", " F").replace(" (M)", " M").replace(" ", "%20")
    url = f"https://raw.githubusercontent.com/Willowlark/Pokerole-Data/master/v2.0/Pokedex/{url_name}.json"
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        data = json.loads(response.read().decode('utf-8'))
    except Exception as e:
        print(f"Errore download {pkmn} ({url}): {e}")
        continue

    # Extract Data
    dex_id = data.get("DexID", "000")
    name = data.get("Name", pkmn)
    types = [data.get("Type1", "")]
    if data.get("Type2"):
        types.append(data.get("Type2"))
    types_str = " / ".join(types)
    
    category = data.get("DexCategory", "Pokemon")
    desc = data.get("DexDescription", "")
    hp = data.get("BaseHP", 0)
    
    # Abilities
    abs_list = [f"[[{data.get('Ability1')}]]"] if data.get("Ability1") else []
    if data.get("Ability2"): abs_list.append(f"[[{data.get('Ability2')}]]")
    if data.get("HiddenAbility"): abs_list.append(f"[[{data.get('HiddenAbility')}]] *(Hidden)*")
    abilities_str = ", ".join([a for a in abs_list if a])
    
    # Moves
    moves_by_rank = {}
    for move in data.get("Moves", []):
        rank = move.get("Learned", "Unknown")
        moves_by_rank.setdefault(rank, []).append(f"[[{move.get('Name', '')}]]")
        
    moves_markdown = ""
    for rank in ["Starter", "Beginner", "Amateur", "Ace", "Pro"]:
        if rank in moves_by_rank:
            moves_markdown += f"- **{rank}:** {', '.join(moves_by_rank[rank])}\n"

    # Formatting attributes
    str_val = f"{data.get('Strength', 0)}/{data.get('MaxStrength', 0)}"
    dex_val = f"{data.get('Dexterity', 0)}/{data.get('MaxDexterity', 0)}"
    vit_val = f"{data.get('Vitality', 0)}/{data.get('MaxVitality', 0)}"
    spe_val = f"{data.get('Special', 0)}/{data.get('MaxSpecial', 0)}"
    ins_val = f"{data.get('Insight', 0)}/{data.get('MaxInsight', 0)}"

    # Write Markdown
    md_filename = f"{dex_id}_{name.replace(' ', '_').replace('.', '')}.md"
    md_path = os.path.join(md_dir, md_filename)
    
    tags = [name.lower().replace(" ", ""), "kanto"] + [t.lower() for t in types]
    
    md_content = f"""---
title: "{name} (#{dex_id})"
category: Pokedex
tags: [{', '.join(tags)}]
---

# {name} (#{dex_id})
*{category}*

**Type:** {types_str}
**Abilities:** {abilities_str}
**Base HP:** {hp}

> {desc}

---

## Statistiche (Attributes & Limits)

| Attribute | Base / Limit |
|---|---|
| **Strength** | {str_val} |
| **Dexterity** | {dex_val} |
| **Vitality** | {vit_val} |
| **Special** | {spe_val} |
| **Insight** | {ins_val} |

---

## Mosse (Learnset)

{moves_markdown}
"""
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
        
    print(f"Generato {md_filename}")
    time.sleep(0.1) # Be nice to Github API

print("Fase 2 Completata. Ingest JSON terminato.")
