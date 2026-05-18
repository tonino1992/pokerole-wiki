import fitz
import os
import re

kanto_pokemon = [
    "Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard", 
    "Squirtle", "Wartortle", "Blastoise", "Caterpie", "Metapod", "Butterfree", 
    "Weedle", "Kakuna", "Beedrill", "Pidgey", "Pidgeotto", "Pidgeot", 
    "Rattata", "Raticate", "Spearow", "Fearow", "Ekans", "Arbok", 
    "Pikachu", "Raichu", "Sandshrew", "Sandslash", "Nidoran", "Nidorina", "Nidoqueen", 
    "Nidorino", "Nidoking", "Clefairy", "Clefable", "Vulpix", "Ninetales", 
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

os.makedirs(img_dir, exist_ok=True)
os.makedirs(md_dir, exist_ok=True)

doc = fitz.open(pdf_path)

# Kanto pages are 90 to 129 in the book. PDF is 0-indexed, so 89 to 128.
start_page = 89
end_page = 128

for page_idx in range(start_page, end_page + 1):
    page = doc[page_idx]
    text = page.get_text("text")
    
    # Find all pokemon present on this page
    found = []
    for pkmn in kanto_pokemon:
        # Avoid matching "Mew" inside "Mewtwo" using word boundaries
        # Handle special characters like Farfetch'd or Mr. Mime
        safe_pkmn = re.escape(pkmn)
        if re.search(r'\b' + safe_pkmn + r'\b', text, re.IGNORECASE):
            found.append(pkmn)
            
    if not found:
        print(f"Warning: No pokemon found on page {page_idx + 1}")
        continue
        
    print(f"Page {page_idx + 1}: Found {', '.join(found)}")
    
    # Render PNG
    img_filename = f"p{page_idx + 1}.png"
    img_path = os.path.join(img_dir, img_filename)
    page.get_pixmap(dpi=150).save(img_path)
    
    # Create Markdown
    safe_names = "_".join(found).replace(".", "").replace(" ", "_").replace("'", "")
    # Add page number to filename to keep order
    md_filename = f"P{page_idx + 1}_{safe_names}.md"
    md_path = os.path.join(md_dir, md_filename)
    
    tags = ", ".join([f"{p.lower().replace(' ', '_').replace('.', '')}" for p in found])
    
    md_content = f"""---
title: Pokédex - {', '.join(found)}
category: Pokedex
tags: [kanto, {tags}]
summary: "Schede Pokédex per: {', '.join(found)}"
---

# {', '.join(found)}

![Pokédex Page {page_idx + 1}](../../../assets/images/pokedex/kanto/{img_filename})

---

## Correlati
- [[Pokedex_Introduzione]] — Come leggere queste statistiche
"""
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)

print("Ingest completato!")
