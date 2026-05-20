"""
Ingest Pokédex Hoenn (252-386) da Willowlark/Pokerole-Data JSON.
Genera 135 file Markdown in wiki/03_Pokedex/Hoenn/.
"""
import os, json, urllib.request, time, re

HOENN_POKEMON = [
    (252, "Treecko"), (253, "Grovyle"), (254, "Sceptile"),
    (255, "Torchic"), (256, "Combusken"), (257, "Blaziken"),
    (258, "Mudkip"), (259, "Marshtomp"), (260, "Swampert"),
    (261, "Poochyena"), (262, "Mightyena"),
    (263, "Zigzagoon"), (264, "Linoone"),
    (265, "Wurmple"), (266, "Silcoon"), (267, "Beautifly"),
    (268, "Cascoon"), (269, "Dustox"),
    (270, "Lotad"), (271, "Lombre"), (272, "Ludicolo"),
    (273, "Seedot"), (274, "Nuzleaf"), (275, "Shiftry"),
    (276, "Taillow"), (277, "Swellow"),
    (278, "Wingull"), (279, "Pelipper"),
    (280, "Ralts"), (281, "Kirlia"), (282, "Gardevoir"),
    (283, "Surskit"), (284, "Masquerain"),
    (285, "Shroomish"), (286, "Breloom"),
    (287, "Slakoth"), (288, "Vigoroth"), (289, "Slaking"),
    (290, "Nincada"), (291, "Ninjask"), (292, "Shedinja"),
    (293, "Whismur"), (294, "Loudred"), (295, "Exploud"),
    (296, "Makuhita"), (297, "Hariyama"),
    (298, "Azurill"),
    (299, "Nosepass"),
    (300, "Skitty"), (301, "Delcatty"),
    (302, "Sableye"),
    (303, "Mawile"),
    (304, "Aron"), (305, "Lairon"), (306, "Aggron"),
    (307, "Meditite"), (308, "Medicham"),
    (309, "Electrike"), (310, "Manectric"),
    (311, "Plusle"),
    (312, "Minun"),
    (313, "Volbeat"),
    (314, "Illumise"),
    (315, "Roselia"),
    (316, "Gulpin"), (317, "Swalot"),
    (318, "Carvanha"), (319, "Sharpedo"),
    (320, "Wailmer"), (321, "Wailord"),
    (322, "Numel"), (323, "Camerupt"),
    (324, "Torkoal"),
    (325, "Spoink"), (326, "Grumpig"),
    (327, "Spinda"),
    (328, "Trapinch"), (329, "Vibrava"), (330, "Flygon"),
    (331, "Cacnea"), (332, "Cacturne"),
    (333, "Swablu"), (334, "Altaria"),
    (335, "Zangoose"),
    (336, "Seviper"),
    (337, "Lunatone"),
    (338, "Solrock"),
    (339, "Barboach"), (340, "Whiscash"),
    (341, "Corphish"), (342, "Crawdaunt"),
    (343, "Baltoy"), (344, "Claydol"),
    (345, "Lileep"), (346, "Cradily"),
    (347, "Anorith"), (348, "Armaldo"),
    (349, "Feebas"), (350, "Milotic"),
    (351, "Castform"),
    (352, "Kecleon"),
    (353, "Shuppet"), (354, "Banette"),
    (355, "Duskull"), (356, "Dusclops"),
    (357, "Tropius"),
    (358, "Chimecho"),
    (359, "Absol"),
    (360, "Wynaut"),
    (361, "Snorunt"), (362, "Glalie"),
    (363, "Spheal"), (364, "Sealeo"), (365, "Walrein"),
    (366, "Clamperl"), (367, "Huntail"), (368, "Gorebyss"),
    (369, "Relicanth"),
    (370, "Luvdisc"),
    (371, "Bagon"), (372, "Shelgon"), (373, "Salamence"),
    (374, "Beldum"), (375, "Metang"), (376, "Metagross"),
    (377, "Regirock"), (378, "Regice"), (379, "Registeel"),
    (380, "Latias"), (381, "Latios"),
    (382, "Kyogre"),
    (383, "Groudon"),
    (384, "Rayquaza"),
    (385, "Jirachi"),
    (386, "Deoxys"),
]

# Traduzione tipi EN → IT
TYPE_IT = {
    "Normal": "Normale", "Fire": "Fuoco", "Water": "Acqua",
    "Grass": "Erba", "Electric": "Elettro", "Ice": "Ghiaccio",
    "Fighting": "Lotta", "Poison": "Veleno", "Ground": "Terra",
    "Flying": "Volante", "Psychic": "Psico", "Bug": "Insetto",
    "Rock": "Roccia", "Ghost": "Spettro", "Dragon": "Drago",
    "Dark": "Buio", "Steel": "Acciaio", "Fairy": "Folletto",
}

# ID noti per Pokémon fuori Hoenn (cross-gen evolution chains)
KNOWN_IDS = {
    # Kanto
    "Bulbasaur": "0001", "Ivysaur": "0002", "Venusaur": "0003",
    "Charmander": "0004", "Charmeleon": "0005", "Charizard": "0006",
    "Squirtle": "0007", "Wartortle": "0008", "Blastoise": "0009",
    "Pikachu": "0025", "Raichu": "0026",
    "Clefairy": "0035", "Clefable": "0036",
    "Jigglypuff": "0039", "Wigglytuff": "0040",
    "Zubat": "0041", "Golbat": "0042",
    "Oddish": "0043", "Gloom": "0044", "Vileplume": "0045",
    "Slowpoke": "0079", "Slowbro": "0080",
    "Magnemite": "0081", "Magneton": "0082",
    "Onix": "0095",
    "Chansey": "0113",
    "Horsea": "0116", "Seadra": "0117",
    "Scyther": "0123",
    "Jynx": "0124",
    "Electabuzz": "0125",
    "Magmar": "0126",
    "Eevee": "0133",
    "Porygon": "0137",
    "Hitmonlee": "0106", "Hitmonchan": "0107",
    "Poliwag": "0060", "Poliwhirl": "0061", "Poliwrath": "0062",
    # Johto
    "Chikorita": "0152", "Bayleef": "0153", "Meganium": "0154",
    "Cyndaquil": "0155", "Quilava": "0156", "Typhlosion": "0157",
    "Totodile": "0158", "Croconaw": "0159", "Feraligatr": "0160",
    "Sentret": "0161", "Furret": "0162",
    "Hoothoot": "0163", "Noctowl": "0164",
    "Ledyba": "0165", "Ledian": "0166",
    "Spinarak": "0167", "Ariados": "0168",
    "Crobat": "0169",
    "Chinchou": "0170", "Lanturn": "0171",
    "Pichu": "0172", "Cleffa": "0173", "Igglybuff": "0174",
    "Togepi": "0175", "Togetic": "0176",
    "Natu": "0177", "Xatu": "0178",
    "Mareep": "0179", "Flaaffy": "0180", "Ampharos": "0181",
    "Bellossom": "0182",
    "Marill": "0183", "Azumarill": "0184",
    "Sudowoodo": "0185",
    "Politoed": "0186",
    "Hoppip": "0187", "Skiploom": "0188", "Jumpluff": "0189",
    "Aipom": "0190",
    "Sunkern": "0191", "Sunflora": "0192",
    "Yanma": "0193",
    "Wooper": "0194", "Quagsire": "0195",
    "Espeon": "0196", "Umbreon": "0197",
    "Murkrow": "0198",
    "Slowking": "0199",
    "Misdreavus": "0200",
    "Unown": "0201",
    "Wobbuffet": "0202",
    "Girafarig": "0203",
    "Pineco": "0204", "Forretress": "0205",
    "Dunsparce": "0206",
    "Gligar": "0207",
    "Steelix": "0208",
    "Snubbull": "0209", "Granbull": "0210",
    "Qwilfish": "0211",
    "Scizor": "0212",
    "Shuckle": "0213",
    "Heracross": "0214",
    "Sneasel": "0215",
    "Teddiursa": "0216", "Ursaring": "0217",
    "Slugma": "0218", "Magcargo": "0219",
    "Swinub": "0220", "Piloswine": "0221",
    "Corsola": "0222",
    "Remoraid": "0223", "Octillery": "0224",
    "Delibird": "0225",
    "Mantine": "0226",
    "Skarmory": "0227",
    "Houndour": "0228", "Houndoom": "0229",
    "Kingdra": "0230",
    "Phanpy": "0231", "Donphan": "0232",
    "Porygon2": "0233",
    "Stantler": "0234",
    "Smeargle": "0235",
    "Tyrogue": "0236", "Hitmontop": "0237",
    "Smoochum": "0238",
    "Elekid": "0239",
    "Magby": "0240",
    "Miltank": "0241",
    "Blissey": "0242",
    "Raikou": "0243", "Entei": "0244", "Suicune": "0245",
    "Larvitar": "0246", "Pupitar": "0247", "Tyranitar": "0248",
    "Lugia": "0249", "Ho-Oh": "0250",
    "Celebi": "0251",
}

md_dir = "wiki/03_Pokedex/Hoenn"
os.makedirs(md_dir, exist_ok=True)

RANK_ORDER = ["Starter", "Beginner", "Amateur", "Ace", "Pro", "Master", "Champion"]

def url_name(name):
    return name.replace(" ", "%20")

def fetch_json(name):
    raw_name = url_name(name)
    url = f"https://raw.githubusercontent.com/Willowlark/Pokerole-Data/master/v2.0/Pokedex/{raw_name}.json"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        resp = urllib.request.urlopen(req, timeout=15)
        return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"  ERRORE fetch {name}: {e}")
        return None

def translate_type(t):
    return TYPE_IT.get(t, t)

def make_slug(name):
    return name.replace(" ", "_").replace(".", "").replace("'", "").replace("-", "_")

def dex_link(dex_id, name):
    slug = make_slug(name)
    return f"[[{dex_id}_{slug}|{name}]]"

# --- FASE 1: scarica tutti i JSON ---
print("Fase 1: Download JSON Hoenn...")
all_data = {}
hoenn_id_map = {}

for poke_id, name in HOENN_POKEMON:
    data = fetch_json(name)
    if data:
        all_data[name] = data
        hoenn_id_map[name] = data.get("DexID", f"{poke_id:04d}")
        print(f"  OK #{poke_id} {name}")
    else:
        print(f"  SKIP #{poke_id} {name}")
    time.sleep(0.15)

# Mappa nome → DexID completa (Hoenn + Kanto + Johto)
full_id_map = {**KNOWN_IDS, **hoenn_id_map}

# --- FASE 2: costruzione catene evolutive inverse ---
evolves_from = {}
for name, data in all_data.items():
    for evo in data.get("Evolutions", []):
        target = evo.get("To", "")
        if target:
            evolves_from.setdefault(target, []).append(name)

def get_chain_root(name, visited=None):
    if visited is None:
        visited = set()
    if name in visited:
        return name
    visited.add(name)
    parents = evolves_from.get(name, [])
    if not parents:
        return name
    return get_chain_root(parents[0], visited)

def get_full_chain(root, visited=None):
    if visited is None:
        visited = set()
    if root in visited:
        return []
    visited.add(root)
    chain = [root]
    data = all_data.get(root, {})
    for evo in data.get("Evolutions", []):
        target = evo.get("To", "")
        if target and target not in visited:
            chain.extend(get_full_chain(target, visited))
    return chain

def build_evo_section(name):
    root = get_chain_root(name)
    chain = get_full_chain(root)
    if len(chain) <= 1 and name not in evolves_from:
        return ""

    lines = ["## Correlati\n", "### Catena Evolutiva"]
    for member in chain:
        did = full_id_map.get(member)
        if did:
            lines.append(f"- {dex_link(did, member)}")
        else:
            lines.append(f"- {member}")
    return "\n".join(lines)

# --- FASE 3: genera i file Markdown ---
print("\nFase 3: Generazione file Markdown...")
generated = 0

for poke_id, name in HOENN_POKEMON:
    data = all_data.get(name)
    if not data:
        print(f"  SKIP {name} (dati mancanti)")
        continue

    dex_id = data.get("DexID", f"{poke_id:04d}")
    types_raw = [data.get("Type1", "")]
    if data.get("Type2"):
        types_raw.append(data["Type2"])
    types_it = " / ".join(translate_type(t) for t in types_raw if t)
    types_lower = [t.lower() for t in types_raw if t]

    category = data.get("DexCategory", "Pokémon")
    desc = data.get("DexDescription", "")
    hp = data.get("BaseHP", 0)

    # Abilità
    abs_list = []
    if data.get("Ability1"): abs_list.append(f"[[{data['Ability1']}]]")
    if data.get("Ability2"): abs_list.append(f"[[{data['Ability2']}]]")
    if data.get("HiddenAbility"): abs_list.append(f"[[{data['HiddenAbility']}]] *(Hidden)*")
    abilities_str = ", ".join(abs_list)

    # Statistiche
    str_val = f"{data.get('Strength', 0)}/{data.get('MaxStrength', 0)}"
    dex_val = f"{data.get('Dexterity', 0)}/{data.get('MaxDexterity', 0)}"
    vit_val = f"{data.get('Vitality', 0)}/{data.get('MaxVitality', 0)}"
    spe_val = f"{data.get('Special', 0)}/{data.get('MaxSpecial', 0)}"
    ins_val = f"{data.get('Insight', 0)}/{data.get('MaxInsight', 0)}"

    # Mosse per rank
    moves_by_rank = {}
    for move in data.get("Moves", []):
        rank = move.get("Learned", "Unknown")
        move_name = move.get("Name", "")
        if move_name:
            slug_move = move_name.replace(" ", "_").replace("-", "_").replace("'", "")
            moves_by_rank.setdefault(rank, []).append(f"[[{slug_move}|{move_name}]]")

    moves_md = ""
    for rank in RANK_ORDER:
        if rank in moves_by_rank:
            moves_md += f"- **{rank}:** {', '.join(moves_by_rank[rank])}\n"

    # Catena evolutiva
    evo_section = build_evo_section(name)

    # Tag
    name_tag = name.lower().replace(" ", "").replace("-", "").replace(".", "").replace("'", "")
    tags = [name_tag, "hoenn"] + types_lower

    # Immagine
    img_path = f"assets/images/pokemon/{poke_id:03d}.png"
    img_tag = f'<img src="../../assets/images/pokemon/{poke_id:03d}.png" align="right" width="220" style="margin-left:20px;margin-bottom:8px;">'

    # Filename
    slug_name = make_slug(name)
    filename = f"{dex_id}_{slug_name}.md"
    filepath = os.path.join(md_dir, filename)

    md = f"""---
title: "{name} (#{dex_id})"
category: Pokedex
tags: [{', '.join(tags)}]
image: "{img_path}"
---

# {name} (#{dex_id})

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

{evo_section}
"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(md)

    generated += 1
    print(f"  Creato {filename}")

print(f"\nFase 3 Completata. File generati: {generated}/{len(HOENN_POKEMON)}")
