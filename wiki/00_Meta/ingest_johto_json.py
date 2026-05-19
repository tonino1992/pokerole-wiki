"""
Ingest Pokédex Johto (152-251) da Willowlark/Pokerole-Data JSON.
Genera 100 file Markdown in wiki/03_Pokedex/Johto/.
"""
import os, json, urllib.request, time, re

JOHTO_POKEMON = [
    (152, "Chikorita"), (153, "Bayleef"), (154, "Meganium"),
    (155, "Cyndaquil"), (156, "Quilava"), (157, "Typhlosion"),
    (158, "Totodile"), (159, "Croconaw"), (160, "Feraligatr"),
    (161, "Sentret"), (162, "Furret"),
    (163, "Hoothoot"), (164, "Noctowl"),
    (165, "Ledyba"), (166, "Ledian"),
    (167, "Spinarak"), (168, "Ariados"),
    (169, "Crobat"),
    (170, "Chinchou"), (171, "Lanturn"),
    (172, "Pichu"), (173, "Cleffa"), (174, "Igglybuff"),
    (175, "Togepi"), (176, "Togetic"),
    (177, "Natu"), (178, "Xatu"),
    (179, "Mareep"), (180, "Flaaffy"), (181, "Ampharos"),
    (182, "Bellossom"),
    (183, "Marill"), (184, "Azumarill"),
    (185, "Sudowoodo"),
    (186, "Politoed"),
    (187, "Hoppip"), (188, "Skiploom"), (189, "Jumpluff"),
    (190, "Aipom"),
    (191, "Sunkern"), (192, "Sunflora"),
    (193, "Yanma"),
    (194, "Wooper"), (195, "Quagsire"),
    (196, "Espeon"), (197, "Umbreon"),
    (198, "Murkrow"),
    (199, "Slowking"),
    (200, "Misdreavus"),
    (201, "Unown"),
    (202, "Wobbuffet"),
    (203, "Girafarig"),
    (204, "Pineco"), (205, "Forretress"),
    (206, "Dunsparce"),
    (207, "Gligar"),
    (208, "Steelix"),
    (209, "Snubbull"), (210, "Granbull"),
    (211, "Qwilfish"),
    (212, "Scizor"),
    (213, "Shuckle"),
    (214, "Heracross"),
    (215, "Sneasel"),
    (216, "Teddiursa"), (217, "Ursaring"),
    (218, "Slugma"), (219, "Magcargo"),
    (220, "Swinub"), (221, "Piloswine"),
    (222, "Corsola"),
    (223, "Remoraid"), (224, "Octillery"),
    (225, "Delibird"),
    (226, "Mantine"),
    (227, "Skarmory"),
    (228, "Houndour"), (229, "Houndoom"),
    (230, "Kingdra"),
    (231, "Phanpy"), (232, "Donphan"),
    (233, "Porygon2"),
    (234, "Stantler"),
    (235, "Smeargle"),
    (236, "Tyrogue"), (237, "Hitmontop"),
    (238, "Smoochum"),
    (239, "Elekid"),
    (240, "Magby"),
    (241, "Miltank"),
    (242, "Blissey"),
    (243, "Raikou"), (244, "Entei"), (245, "Suicune"),
    (246, "Larvitar"), (247, "Pupitar"), (248, "Tyranitar"),
    (249, "Lugia"),
    (250, "Ho-Oh"),
    (251, "Celebi"),
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

# ID noti per Pokémon fuori Johto (cross-gen evolution chains)
KNOWN_IDS = {
    # Kanto
    "Bulbasaur": "0001", "Ivysaur": "0002", "Venusaur": "0003",
    "Charmander": "0004", "Charmeleon": "0005", "Charizard": "0006",
    "Squirtle": "0007", "Wartortle": "0008", "Blastoise": "0009",
    "Zubat": "0041", "Golbat": "0042",
    "Clefairy": "0035", "Clefable": "0036",
    "Jigglypuff": "0039", "Wigglytuff": "0040",
    "Pikachu": "0025", "Raichu": "0026",
    "Oddish": "0043", "Gloom": "0044", "Vileplume": "0045",
    "Slowpoke": "0079", "Slowbro": "0080",
    "Scyther": "0123",
    "Chansey": "0113",
    "Jynx": "0124",
    "Electabuzz": "0125",
    "Magmar": "0126",
    "Eevee": "0133",
    "Onix": "0095",
    "Poliwag": "0060", "Poliwhirl": "0061", "Poliwrath": "0062",
    "Horsea": "0116", "Seadra": "0117",
    "Porygon": "0137",
    "Hitmonlee": "0106", "Hitmonchan": "0107",
}

md_dir = "wiki/03_Pokedex/Johto"
os.makedirs(md_dir, exist_ok=True)

RANK_ORDER = ["Starter", "Beginner", "Amateur", "Ace", "Pro", "Master", "Champion"]

def url_name(name):
    """Convert Pokemon name to URL-safe string for GitHub API."""
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
print("Fase 1: Download JSON Johto...")
all_data = {}
johto_id_map = {}  # name → DexID string

for poke_id, name in JOHTO_POKEMON:
    data = fetch_json(name)
    if data:
        all_data[name] = data
        johto_id_map[name] = data.get("DexID", f"{poke_id:04d}")
        print(f"  OK #{poke_id} {name}")
    else:
        print(f"  SKIP #{poke_id} {name}")
    time.sleep(0.15)

# Mappa nome → DexID completa (Johto + Kanto)
full_id_map = {**KNOWN_IDS, **johto_id_map}

# --- FASE 2: costruzione catene evolutive inverse ---
# evolves_from[name] = list of names that evolve INTO this pokemon
evolves_from = {}
for name, data in all_data.items():
    for evo in data.get("Evolutions", []):
        target = evo.get("To", "")
        if target:
            evolves_from.setdefault(target, []).append(name)

def get_chain_root(name, visited=None):
    """Risale alla radice della catena evolutiva."""
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
    """Genera la catena evolutiva completa dal root."""
    if visited is None:
        visited = set()
    if root in visited:
        return []
    visited.add(root)
    chain = [root]
    # Cerca evoluzione dal JSON (se presente)
    data = all_data.get(root, {})
    for evo in data.get("Evolutions", []):
        target = evo.get("To", "")
        if target and target not in visited:
            chain.extend(get_full_chain(target, visited))
    return chain

def build_evo_section(name):
    """Costruisce la sezione ## Correlati con la catena evolutiva."""
    root = get_chain_root(name)
    # Cerca anche pre-evoluzioni non Johto (es. Crobat da Golbat da Zubat)
    # Usa il root trovato
    chain = get_full_chain(root)
    if len(chain) <= 1 and name not in evolves_from:
        return ""  # nessuna evoluzione

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

for poke_id, name in JOHTO_POKEMON:
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
    tags = [name_tag, "johto"] + types_lower

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

print(f"\nFase 3 Completata. File generati: {generated}/100")
