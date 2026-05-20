"""
Ingest forme speciali (Mega, Primal, Alolan, Galarian, Hisuian, ecc.)
per Gen 1-4 (Kanto, Johto, Hoenn, Sinnoh).
Le forme vengono aggiunte nelle cartelle della regione del Pokémon base.
"""
import os, json, urllib.request, time

BASE_URL = "https://raw.githubusercontent.com/Pokerole-Software-Development/Pokerole-Data/master/v2.0/Pokedex"

TYPE_IT = {
    "Normal": "Normale", "Fire": "Fuoco", "Water": "Acqua",
    "Grass": "Erba", "Electric": "Elettro", "Ice": "Ghiaccio",
    "Fighting": "Lotta", "Poison": "Veleno", "Ground": "Terra",
    "Flying": "Volante", "Psychic": "Psico", "Bug": "Insetto",
    "Rock": "Roccia", "Ghost": "Spettro", "Dragon": "Drago",
    "Dark": "Buio", "Steel": "Acciaio", "Fairy": "Folletto",
}
RANK_ORDER = ["Starter", "Beginner", "Amateur", "Ace", "Pro", "Master", "Champion"]

# (file_url_name, base_pokemon_name, base_dex_id, base_poke_id_for_img, cartella, label)
SPECIAL_FORMS = [
    # ── KANTO ──────────────────────────────────────────────────────────────────
    # Mega
    ("Venusaur%20(Mega%20Form)",    "Venusaur",   "0003", 3,   "wiki/03_Pokedex/Kanto"),
    ("Charizard%20(Mega%20X%20Form)","Charizard", "0006", 6,   "wiki/03_Pokedex/Kanto"),
    ("Charizard%20(Mega%20Y%20Form)","Charizard", "0006", 6,   "wiki/03_Pokedex/Kanto"),
    ("Blastoise%20(Mega%20Form)",   "Blastoise",  "0009", 9,   "wiki/03_Pokedex/Kanto"),
    ("Beedrill%20(Mega%20Form)",    "Beedrill",   "0015", 15,  "wiki/03_Pokedex/Kanto"),
    ("Pidgeot%20(Mega%20Form)",     "Pidgeot",    "0018", 18,  "wiki/03_Pokedex/Kanto"),
    ("Alakazam%20(Mega%20Form)",    "Alakazam",   "0065", 65,  "wiki/03_Pokedex/Kanto"),
    ("Kangaskhan%20(Mega%20Form)",  "Kangaskhan", "0115", 115, "wiki/03_Pokedex/Kanto"),
    ("Pinsir%20(Mega%20Form)",      "Pinsir",     "0127", 127, "wiki/03_Pokedex/Kanto"),
    ("Gyarados%20(Mega%20Form)",    "Gyarados",   "0130", 130, "wiki/03_Pokedex/Kanto"),
    ("Aerodactyl%20(Mega%20Form)",  "Aerodactyl", "0142", 142, "wiki/03_Pokedex/Kanto"),
    ("Mewtwo%20(Mega%20X%20Form)",  "Mewtwo",     "0150", 150, "wiki/03_Pokedex/Kanto"),
    ("Mewtwo%20(Mega%20Y%20Form)",  "Mewtwo",     "0150", 150, "wiki/03_Pokedex/Kanto"),
    ("Gengar%20(Mega%20Form)",      "Gengar",     "0094", 94,  "wiki/03_Pokedex/Kanto"),
    ("Slowbro%20(Mega%20Form)",     "Slowbro",    "0080", 80,  "wiki/03_Pokedex/Kanto"),
    # Alolan
    ("Rattata%20(Alolan%20Form)",   "Rattata",    "0019", 19,  "wiki/03_Pokedex/Kanto"),
    ("Raticate%20(Alolan%20Form)",  "Raticate",   "0020", 20,  "wiki/03_Pokedex/Kanto"),
    ("Raichu%20(Alolan%20Form)",    "Raichu",     "0026", 26,  "wiki/03_Pokedex/Kanto"),
    ("Sandshrew%20(Alolan%20Form)", "Sandshrew",  "0027", 27,  "wiki/03_Pokedex/Kanto"),
    ("Sandslash%20(Alolan%20Form)", "Sandslash",  "0028", 28,  "wiki/03_Pokedex/Kanto"),
    ("Vulpix%20(Alolan%20Form)",    "Vulpix",     "0037", 37,  "wiki/03_Pokedex/Kanto"),
    ("Ninetales%20(Alolan%20Form)", "Ninetales",  "0038", 38,  "wiki/03_Pokedex/Kanto"),
    ("Diglett%20(Alolan%20Form)",   "Diglett",    "0050", 50,  "wiki/03_Pokedex/Kanto"),
    ("Dugtrio%20(Alolan%20Form)",   "Dugtrio",    "0051", 51,  "wiki/03_Pokedex/Kanto"),
    ("Meowth%20(Alolan%20Form)",    "Meowth",     "0052", 52,  "wiki/03_Pokedex/Kanto"),
    ("Persian%20(Alolan%20Form)",   "Persian",    "0053", 53,  "wiki/03_Pokedex/Kanto"),
    ("Geodude%20(Alolan%20Form)",   "Geodude",    "0074", 74,  "wiki/03_Pokedex/Kanto"),
    ("Graveler%20(Alolan%20Form)",  "Graveler",   "0075", 75,  "wiki/03_Pokedex/Kanto"),
    ("Golem%20(Alolan%20Form)",     "Golem",      "0076", 76,  "wiki/03_Pokedex/Kanto"),
    ("Grimer%20(Alolan%20Form)",    "Grimer",     "0088", 88,  "wiki/03_Pokedex/Kanto"),
    ("Muk%20(Alolan%20Form)",       "Muk",        "0089", 89,  "wiki/03_Pokedex/Kanto"),
    ("Exeggutor%20(Alolan%20Form)", "Exeggutor",  "0103", 103, "wiki/03_Pokedex/Kanto"),
    ("Marowak%20(Alolan%20Form)",   "Marowak",    "0105", 105, "wiki/03_Pokedex/Kanto"),
    # Galarian
    ("Meowth%20(Galarian%20Form)",  "Meowth",     "0052", 52,  "wiki/03_Pokedex/Kanto"),
    ("Farfetch%27d%20(Galarian%20Form)", "Farfetch'd", "0083", 83, "wiki/03_Pokedex/Kanto"),
    ("Mr.%20Mime%20(Galarian%20Form)",   "Mr. Mime",   "0122", 122, "wiki/03_Pokedex/Kanto"),

    # ── JOHTO ──────────────────────────────────────────────────────────────────
    # Mega
    ("Ampharos%20(Mega%20Form)",    "Ampharos",   "0181", 181, "wiki/03_Pokedex/Johto"),
    ("Steelix%20(Mega%20Form)",     "Steelix",    "0208", 208, "wiki/03_Pokedex/Johto"),
    ("Scizor%20(Mega%20Form)",      "Scizor",     "0212", 212, "wiki/03_Pokedex/Johto"),
    ("Heracross%20(Mega%20Form)",   "Heracross",  "0214", 214, "wiki/03_Pokedex/Johto"),
    ("Houndoom%20(Mega%20Form)",    "Houndoom",   "0229", 229, "wiki/03_Pokedex/Johto"),
    ("Tyranitar%20(Mega%20Form)",   "Tyranitar",  "0248", 248, "wiki/03_Pokedex/Johto"),
    # Galarian
    ("Slowpoke%20(Galarian%20Form)","Slowpoke",   "0079", 79,  "wiki/03_Pokedex/Johto"),
    ("Slowbro%20(Galarian%20Form)", "Slowbro",    "0080", 80,  "wiki/03_Pokedex/Johto"),
    ("Slowking%20(Galarian%20Form)","Slowking",   "0199", 199, "wiki/03_Pokedex/Johto"),
    ("Corsola%20(Galarian%20Form)", "Corsola",    "0222", 222, "wiki/03_Pokedex/Johto"),

    # ── HOENN ──────────────────────────────────────────────────────────────────
    # Mega
    ("Sceptile%20(Mega%20Form)",    "Sceptile",   "0254", 254, "wiki/03_Pokedex/Hoenn"),
    ("Blaziken%20(Mega%20Form)",    "Blaziken",   "0257", 257, "wiki/03_Pokedex/Hoenn"),
    ("Swampert%20(Mega%20Form)",    "Swampert",   "0260", 260, "wiki/03_Pokedex/Hoenn"),
    ("Gardevoir%20(Mega%20Form)",   "Gardevoir",  "0282", 282, "wiki/03_Pokedex/Hoenn"),
    ("Sableye%20(Mega%20Form)",     "Sableye",    "0302", 302, "wiki/03_Pokedex/Hoenn"),
    ("Mawile%20(Mega%20Form)",      "Mawile",     "0303", 303, "wiki/03_Pokedex/Hoenn"),
    ("Aggron%20(Mega%20Form)",      "Aggron",     "0306", 306, "wiki/03_Pokedex/Hoenn"),
    ("Medicham%20(Mega%20Form)",    "Medicham",   "0308", 308, "wiki/03_Pokedex/Hoenn"),
    ("Manectric%20(Mega%20Form)",   "Manectric",  "0310", 310, "wiki/03_Pokedex/Hoenn"),
    ("Sharpedo%20(Mega%20Form)",    "Sharpedo",   "0319", 319, "wiki/03_Pokedex/Hoenn"),
    ("Camerupt%20(Mega%20Form)",    "Camerupt",   "0323", 323, "wiki/03_Pokedex/Hoenn"),
    ("Altaria%20(Mega%20Form)",     "Altaria",    "0334", 334, "wiki/03_Pokedex/Hoenn"),
    ("Banette%20(Mega%20Form)",     "Banette",    "0354", 354, "wiki/03_Pokedex/Hoenn"),
    ("Absol%20(Mega%20Form)",       "Absol",      "0359", 359, "wiki/03_Pokedex/Hoenn"),
    ("Glalie%20(Mega%20Form)",      "Glalie",     "0362", 362, "wiki/03_Pokedex/Hoenn"),
    ("Salamence%20(Mega%20Form)",   "Salamence",  "0373", 373, "wiki/03_Pokedex/Hoenn"),
    ("Metagross%20(Mega%20Form)",   "Metagross",  "0376", 376, "wiki/03_Pokedex/Hoenn"),
    ("Latias%20(Mega%20Form)",      "Latias",     "0380", 380, "wiki/03_Pokedex/Hoenn"),
    ("Latios%20(Mega%20Form)",      "Latios",     "0381", 381, "wiki/03_Pokedex/Hoenn"),
    ("Kyogre%20(Primal%20Form)",    "Kyogre",     "0382", 382, "wiki/03_Pokedex/Hoenn"),
    ("Groudon%20(Primal%20Form)",   "Groudon",    "0383", 383, "wiki/03_Pokedex/Hoenn"),
    ("Rayquaza%20(Mega%20Form)",    "Rayquaza",   "0384", 384, "wiki/03_Pokedex/Hoenn"),
    # Forme Deoxys
    ("Deoxys%20(Attack%20Form)",    "Deoxys",     "0386", 386, "wiki/03_Pokedex/Hoenn"),
    ("Deoxys%20(Defense%20Form)",   "Deoxys",     "0386", 386, "wiki/03_Pokedex/Hoenn"),
    ("Deoxys%20(Speed%20Form)",     "Deoxys",     "0386", 386, "wiki/03_Pokedex/Hoenn"),

    # ── SINNOH ─────────────────────────────────────────────────────────────────
    # Mega
    ("Lopunny%20(Mega%20Form)",     "Lopunny",    "0428", 428, "wiki/03_Pokedex/Sinnoh"),
    ("Lucario%20(Mega%20Form)",     "Lucario",    "0448", 448, "wiki/03_Pokedex/Sinnoh"),
    ("Abomasnow%20(Mega%20Form)",   "Abomasnow",  "0460", 460, "wiki/03_Pokedex/Sinnoh"),
    ("Garchomp%20(Mega%20Form)",    "Garchomp",   "0445", 445, "wiki/03_Pokedex/Sinnoh"),
    ("Gallade%20(Mega%20Form)",     "Gallade",    "0475", 475, "wiki/03_Pokedex/Sinnoh"),
    # Forme Giratina / Shaymin / Rotom
    ("Giratina%20(Origin%20Form)",  "Giratina",   "0487", 487, "wiki/03_Pokedex/Sinnoh"),
    ("Shaymin%20(Sky%20Form)",      "Shaymin",    "0492", 492, "wiki/03_Pokedex/Sinnoh"),
    ("Rotom%20(Heat%20Form)",       "Rotom",      "0479", 479, "wiki/03_Pokedex/Sinnoh"),
    ("Rotom%20(Wash%20Form)",       "Rotom",      "0479", 479, "wiki/03_Pokedex/Sinnoh"),
    ("Rotom%20(Fan%20Form)",        "Rotom",      "0479", 479, "wiki/03_Pokedex/Sinnoh"),
    ("Rotom%20(Frost%20Form)",      "Rotom",      "0479", 479, "wiki/03_Pokedex/Sinnoh"),
    ("Rotom%20(Mow%20Form)",        "Rotom",      "0479", 479, "wiki/03_Pokedex/Sinnoh"),
]


def fetch_json(url_encoded_name):
    url = f"{BASE_URL}/{url_encoded_name}.json"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        resp = urllib.request.urlopen(req, timeout=15)
        return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"  ERRORE fetch {url_encoded_name}: {e}")
        return None

def translate_type(t):
    return TYPE_IT.get(t, t)

def make_slug(name):
    return (name.replace(" ", "_").replace(".", "").replace("'", "")
               .replace("-", "_").replace("(", "").replace(")", ""))

def render_md(display_name, base_dex_id, base_poke_id, data, region_tag):
    dex_id = data.get("DexID", base_dex_id)
    types_raw = [data.get("Type1", "")]
    if data.get("Type2"):
        types_raw.append(data["Type2"])
    types_it = " / ".join(translate_type(t) for t in types_raw if t)
    types_lower = [t.lower() for t in types_raw if t]

    category = data.get("DexCategory", "Pokémon")
    desc = data.get("DexDescription", "")
    hp = data.get("BaseHP", 0)

    abs_list = []
    if data.get("Ability1"): abs_list.append(f"[[{data['Ability1']}]]")
    if data.get("Ability2"): abs_list.append(f"[[{data['Ability2']}]]")
    if data.get("HiddenAbility"): abs_list.append(f"[[{data['HiddenAbility']}]] *(Hidden)*")
    abilities_str = ", ".join(abs_list)

    str_val = f"{data.get('Strength', 0)}/{data.get('MaxStrength', 0)}"
    dex_val = f"{data.get('Dexterity', 0)}/{data.get('MaxDexterity', 0)}"
    vit_val = f"{data.get('Vitality', 0)}/{data.get('MaxVitality', 0)}"
    spe_val = f"{data.get('Special', 0)}/{data.get('MaxSpecial', 0)}"
    ins_val = f"{data.get('Insight', 0)}/{data.get('MaxInsight', 0)}"

    moves_by_rank = {}
    for move in data.get("Moves", []):
        rank = move.get("Learned", "Unknown")
        move_name = move.get("Name", "")
        if move_name:
            slug_m = move_name.replace(" ", "_").replace("-", "_").replace("'", "")
            moves_by_rank.setdefault(rank, []).append(f"[[{slug_m}|{move_name}]]")
    moves_md = ""
    for rank in RANK_ORDER:
        if rank in moves_by_rank:
            moves_md += f"- **{rank}:** {', '.join(moves_by_rank[rank])}\n"

    name_tag = display_name.lower().replace(" ", "").replace("-", "").replace(".", "").replace("'", "").replace("(","").replace(")","")
    tags = [name_tag, region_tag] + types_lower

    img_path = f"assets/images/pokemon/{base_poke_id:03d}.png"
    img_tag = f'<img src="../../assets/images/pokemon/{base_poke_id:03d}.png" align="right" width="220" style="margin-left:20px;margin-bottom:8px;">'

    return f"""---
title: "{display_name} (#{dex_id})"
category: Pokedex
tags: [{', '.join(tags)}]
image: "{img_path}"
---

# {display_name} (#{dex_id})

{img_tag}

*{category}*

**Type:** {types_it}
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

{moves_md}
---
"""

# --- ESECUZIONE ---
generated = 0
skipped = 0

for url_name, base_name, base_dex_id, base_poke_id, md_dir in SPECIAL_FORMS:
    # Ricava il display name dall'URL
    display_name = urllib.parse.unquote(url_name).replace("%27", "'") if False else \
        url_name.replace("%20", " ").replace("%27", "'").replace("%2E", ".")

    os.makedirs(md_dir, exist_ok=True)
    region_tag = md_dir.split("/")[-1].lower()

    data = fetch_json(url_name)
    if not data:
        skipped += 1
        print(f"  SKIP {display_name}")
        time.sleep(0.1)
        continue

    dex_id = data.get("DexID", base_dex_id)
    slug = make_slug(display_name)
    filename = f"{dex_id}_{slug}.md"
    filepath = os.path.join(md_dir, filename)

    content = render_md(display_name, base_dex_id, base_poke_id, data, region_tag)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    generated += 1
    print(f"  Creato {md_dir}/{filename}")
    time.sleep(0.12)

print(f"\nCompletato. Generati: {generated}, Saltati: {skipped}")
