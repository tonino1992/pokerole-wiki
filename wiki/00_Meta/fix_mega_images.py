"""
Inserisce i tag <img> nelle sezioni Mega/Primordiale/forma già presenti
nelle pagine base dei Pokémon (Johto, Hoenn, Sinnoh).
Le sezioni Kanto erano già corrette.
"""
import os, re

FORMS_DIR = "wiki/assets/images/pokemon/forms/"
IMG_TEMPLATE = '<img src="../../assets/images/pokemon/forms/{fname}" align="right" width="200" style="margin-left:16px;margin-bottom:8px;">'

# Mappa: parte del titolo della sezione → nome file in forms/
# Chiave: stringa che compare nel titolo ## dopo "Mega " o simili
FORM_IMG_MAP = {
    # Kanto (già ok, inclusi per completezza/verifica)
    "Mega Venusaur":        "venusaur-mega.png",
    "Mega Charizard X":     "charizard-mega-x.png",
    "Mega Charizard Y":     "charizard-mega-y.png",
    "Mega Blastoise":       "blastoise-mega.png",
    "Mega Beedrill":        "beedrill-mega.png",
    "Mega Pidgeot":         "pidgeot-mega.png",
    "Mega Alakazam":        "alakazam-mega.png",
    "Mega Kangaskhan":      "kangaskhan-mega.png",
    "Mega Pinsir":          "pinsir-mega.png",
    "Mega Gyarados":        "gyarados-mega.png",
    "Mega Aerodactyl":      "aerodactyl-mega.png",
    "Mega Mewtwo X":        "mewtwo-mega-x.png",
    "Mega Mewtwo Y":        "mewtwo-mega-y.png",
    "Mega Gengar":          "gengar-mega.png",
    "Mega Slowbro":         "slowbro-mega.png",
    # Johto
    "Mega Ampharos":        "ampharos-mega.png",
    "Mega Steelix":         "steelix-mega.png",
    "Mega Scizor":          "scizor-mega.png",
    "Mega Heracross":       "heracross-mega.png",
    "Mega Houndoom":        "houndoom-mega.png",
    "Mega Tyranitar":       "tyranitar-mega.png",
    # Hoenn
    "Mega Sceptile":        "sceptile-mega.png",
    "Mega Blaziken":        "blaziken-mega.png",
    "Mega Swampert":        "swampert-mega.png",
    "Mega Gardevoir":       "gardevoir-mega.png",
    "Mega Sableye":         "sableye-mega.png",
    "Mega Mawile":          "mawile-mega.png",
    "Mega Aggron":          "aggron-mega.png",
    "Mega Medicham":        "medicham-mega.png",
    "Mega Manectric":       "manectric-mega.png",
    "Mega Sharpedo":        "sharpedo-mega.png",
    "Mega Camerupt":        "camerupt-mega.png",
    "Mega Altaria":         "altaria-mega.png",
    "Mega Banette":         "banette-mega.png",
    "Mega Absol":           "absol-mega.png",
    "Mega Glalie":          "glalie-mega.png",
    "Mega Salamence":       "salamence-mega.png",
    "Mega Metagross":       "metagross-mega.png",
    "Mega Latias":          "latias-mega.png",
    "Mega Latios":          "latios-mega.png",
    "Kyogre Primordiale":   "kyogre-primal.png",
    "Groudon Primordiale":  "groudon-primal.png",
    "Mega Rayquaza":        "rayquaza-mega.png",
    # Sinnoh
    "Mega Lopunny":         "lopunny-mega.png",
    "Mega Lucario":         "lucario-mega.png",
    "Mega Abomasnow":       "abomasnow-mega.png",
    "Mega Garchomp":        "garchomp-mega.png",
    "Mega Gallade":         "gallade-mega.png",
}

def process_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    changed = False
    for section_title, img_fname in FORM_IMG_MAP.items():
        # Cerca il pattern: ## TitoloSezione (#...) seguito da una riga vuota e poi **Type:**
        # senza già avere un tag <img> subito dopo
        pattern = rf'(## {re.escape(section_title)}[^\n]*\n)\n(?!<img)'
        img_tag = IMG_TEMPLATE.format(fname=img_fname)
        replacement = rf'\1\n{img_tag}\n\n'
        new_content, n = re.subn(pattern, replacement, content)
        if n > 0:
            content = new_content
            changed = True
            print(f"  OK immagine: {section_title} in {os.path.basename(filepath)}")

    if changed:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

    return changed


# Esegui su tutte le cartelle già ingested
folders = [
    "wiki/03_Pokedex/Kanto",
    "wiki/03_Pokedex/Johto",
    "wiki/03_Pokedex/Hoenn",
    "wiki/03_Pokedex/Sinnoh",
]

updated = 0
for folder in folders:
    for fname in sorted(os.listdir(folder)):
        if not fname.endswith(".md"):
            continue
        fpath = os.path.join(folder, fname)
        if process_file(fpath):
            updated += 1

print(f"\nFile aggiornati: {updated}")
