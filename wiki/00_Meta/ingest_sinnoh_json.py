"""
Ingest Pokédex Sinnoh (387-493) da Willowlark/Pokerole-Data JSON.
Genera 107 file Markdown in wiki/03_Pokedex/Sinnoh/.
"""
import os, json, urllib.request, time

SINNOH_POKEMON = [
    (387, "Turtwig"), (388, "Grotle"), (389, "Torterra"),
    (390, "Chimchar"), (391, "Monferno"), (392, "Infernape"),
    (393, "Piplup"), (394, "Prinplup"), (395, "Empoleon"),
    (396, "Starly"), (397, "Staravia"), (398, "Staraptor"),
    (399, "Bidoof"), (400, "Bibarel"),
    (401, "Kricketot"), (402, "Kricketune"),
    (403, "Shinx"), (404, "Luxio"), (405, "Luxray"),
    (406, "Budew"), (407, "Roserade"),
    (408, "Cranidos"), (409, "Rampardos"),
    (410, "Shieldon"), (411, "Bastiodon"),
    (412, "Burmy"), (413, "Wormadam"), (414, "Mothim"),
    (415, "Combee"), (416, "Vespiquen"),
    (417, "Pachirisu"),
    (418, "Buizel"), (419, "Floatzel"),
    (420, "Cherubi"), (421, "Cherrim"),
    (422, "Shellos"), (423, "Gastrodon"),
    (424, "Ambipom"),
    (425, "Drifloon"), (426, "Drifblim"),
    (427, "Buneary"), (428, "Lopunny"),
    (429, "Mismagius"),
    (430, "Honchkrow"),
    (431, "Glameow"), (432, "Purugly"),
    (433, "Chingling"),
    (434, "Stunky"), (435, "Skuntank"),
    (436, "Bronzor"), (437, "Bronzong"),
    (438, "Bonsly"),
    (439, "Mime Jr."),
    (440, "Happiny"),
    (441, "Chatot"),
    (442, "Spiritomb"),
    (443, "Gible"), (444, "Gabite"), (445, "Garchomp"),
    (446, "Munchlax"),
    (447, "Riolu"), (448, "Lucario"),
    (449, "Hippopotas"), (450, "Hippowdon"),
    (451, "Skorupi"), (452, "Drapion"),
    (453, "Croagunk"), (454, "Toxicroak"),
    (455, "Carnivine"),
    (456, "Finneon"), (457, "Lumineon"),
    (458, "Mantyke"),
    (459, "Snover"), (460, "Abomasnow"),
    (461, "Weavile"),
    (462, "Magnezone"),
    (463, "Lickilicky"),
    (464, "Rhyperior"),
    (465, "Tangrowth"),
    (466, "Electivire"),
    (467, "Magmortar"),
    (468, "Togekiss"),
    (469, "Yanmega"),
    (470, "Leafeon"), (471, "Glaceon"),
    (472, "Gliscor"),
    (473, "Mamoswine"),
    (474, "Porygon-Z"),
    (475, "Gallade"),
    (476, "Probopass"),
    (477, "Dusknoir"),
    (478, "Froslass"),
    (479, "Rotom"),
    (480, "Uxie"), (481, "Mesprit"), (482, "Azelf"),
    (483, "Dialga"), (484, "Palkia"),
    (485, "Heatran"),
    (486, "Regigigas"),
    (487, "Giratina"),
    (488, "Cresselia"),
    (489, "Phione"), (490, "Manaphy"),
    (491, "Darkrai"),
    (492, "Shaymin"),
    (493, "Arceus"),
]

TYPE_IT = {
    "Normal": "Normale", "Fire": "Fuoco", "Water": "Acqua",
    "Grass": "Erba", "Electric": "Elettro", "Ice": "Ghiaccio",
    "Fighting": "Lotta", "Poison": "Veleno", "Ground": "Terra",
    "Flying": "Volante", "Psychic": "Psico", "Bug": "Insetto",
    "Rock": "Roccia", "Ghost": "Spettro", "Dragon": "Drago",
    "Dark": "Buio", "Steel": "Acciaio", "Fairy": "Folletto",
}

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
    "Farfetchd": "0083",
    "Onix": "0095",
    "Lickitung": "0108",
    "Rhydon": "0112",
    "Chansey": "0113",
    "Tangela": "0114",
    "Horsea": "0116", "Seadra": "0117",
    "Mr. Mime": "0122",
    "Scyther": "0123",
    "Jynx": "0124",
    "Electabuzz": "0125",
    "Magmar": "0126",
    "Eevee": "0133",
    "Porygon": "0137",
    "Snorlax": "0143",
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
    "Sudowoodo": "0185", "Bonsly": "0438",
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
    # Hoenn
    "Treecko": "0252", "Grovyle": "0253", "Sceptile": "0254",
    "Torchic": "0255", "Combusken": "0256", "Blaziken": "0257",
    "Mudkip": "0258", "Marshtomp": "0259", "Swampert": "0260",
    "Poochyena": "0261", "Mightyena": "0262",
    "Zigzagoon": "0263", "Linoone": "0264",
    "Wurmple": "0265", "Silcoon": "0266", "Beautifly": "0267",
    "Cascoon": "0268", "Dustox": "0269",
    "Lotad": "0270", "Lombre": "0271", "Ludicolo": "0272",
    "Seedot": "0273", "Nuzleaf": "0274", "Shiftry": "0275",
    "Taillow": "0276", "Swellow": "0277",
    "Wingull": "0278", "Pelipper": "0279",
    "Ralts": "0280", "Kirlia": "0281", "Gardevoir": "0282",
    "Surskit": "0283", "Masquerain": "0284",
    "Shroomish": "0285", "Breloom": "0286",
    "Slakoth": "0287", "Vigoroth": "0288", "Slaking": "0289",
    "Nincada": "0290", "Ninjask": "0291", "Shedinja": "0292",
    "Whismur": "0293", "Loudred": "0294", "Exploud": "0295",
    "Makuhita": "0296", "Hariyama": "0297",
    "Azurill": "0298",
    "Nosepass": "0299",
    "Skitty": "0300", "Delcatty": "0301",
    "Sableye": "0302",
    "Mawile": "0303",
    "Aron": "0304", "Lairon": "0305", "Aggron": "0306",
    "Meditite": "0307", "Medicham": "0308",
    "Electrike": "0309", "Manectric": "0310",
    "Plusle": "0311", "Minun": "0312",
    "Volbeat": "0313", "Illumise": "0314",
    "Roselia": "0315",
    "Gulpin": "0316", "Swalot": "0317",
    "Carvanha": "0318", "Sharpedo": "0319",
    "Wailmer": "0320", "Wailord": "0321",
    "Numel": "0322", "Camerupt": "0323",
    "Torkoal": "0324",
    "Spoink": "0325", "Grumpig": "0326",
    "Spinda": "0327",
    "Trapinch": "0328", "Vibrava": "0329", "Flygon": "0330",
    "Cacnea": "0331", "Cacturne": "0332",
    "Swablu": "0333", "Altaria": "0334",
    "Zangoose": "0335", "Seviper": "0336",
    "Lunatone": "0337", "Solrock": "0338",
    "Barboach": "0339", "Whiscash": "0340",
    "Corphish": "0341", "Crawdaunt": "0342",
    "Baltoy": "0343", "Claydol": "0344",
    "Lileep": "0345", "Cradily": "0346",
    "Anorith": "0347", "Armaldo": "0348",
    "Feebas": "0349", "Milotic": "0350",
    "Castform": "0351", "Kecleon": "0352",
    "Shuppet": "0353", "Banette": "0354",
    "Duskull": "0355", "Dusclops": "0356",
    "Tropius": "0357", "Chimecho": "0358",
    "Absol": "0359",
    "Wynaut": "0360",
    "Snorunt": "0361", "Glalie": "0362",
    "Spheal": "0363", "Sealeo": "0364", "Walrein": "0365",
    "Clamperl": "0366", "Huntail": "0367", "Gorebyss": "0368",
    "Relicanth": "0369", "Luvdisc": "0370",
    "Bagon": "0371", "Shelgon": "0372", "Salamence": "0373",
    "Beldum": "0374", "Metang": "0375", "Metagross": "0376",
    "Regirock": "0377", "Regice": "0378", "Registeel": "0379",
    "Latias": "0380", "Latios": "0381",
    "Kyogre": "0382", "Groudon": "0383", "Rayquaza": "0384",
    "Jirachi": "0385", "Deoxys": "0386",
}

md_dir = "wiki/03_Pokedex/Sinnoh"
os.makedirs(md_dir, exist_ok=True)

RANK_ORDER = ["Starter", "Beginner", "Amateur", "Ace", "Pro", "Master", "Champion"]

def url_name(name):
    return name.replace(" ", "%20").replace(".", "%2E")

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

# --- FASE 1: download ---
print("Fase 1: Download JSON Sinnoh...")
all_data = {}
sinnoh_id_map = {}

for poke_id, name in SINNOH_POKEMON:
    data = fetch_json(name)
    if data:
        all_data[name] = data
        sinnoh_id_map[name] = data.get("DexID", f"{poke_id:04d}")
        print(f"  OK #{poke_id} {name}")
    else:
        print(f"  SKIP #{poke_id} {name}")
    time.sleep(0.15)

full_id_map = {**KNOWN_IDS, **sinnoh_id_map}

# --- FASE 2: catene evolutive inverse ---
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

# --- FASE 3: generazione Markdown ---
print("\nFase 3: Generazione file Markdown...")
generated = 0

for poke_id, name in SINNOH_POKEMON:
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
            slug_move = move_name.replace(" ", "_").replace("-", "_").replace("'", "")
            moves_by_rank.setdefault(rank, []).append(f"[[{slug_move}|{move_name}]]")

    moves_md = ""
    for rank in RANK_ORDER:
        if rank in moves_by_rank:
            moves_md += f"- **{rank}:** {', '.join(moves_by_rank[rank])}\n"

    evo_section = build_evo_section(name)

    name_tag = name.lower().replace(" ", "").replace("-", "").replace(".", "").replace("'", "")
    tags = [name_tag, "sinnoh"] + types_lower

    img_path = f"assets/images/pokemon/{poke_id:03d}.png"
    img_tag = f'<img src="../../assets/images/pokemon/{poke_id:03d}.png" align="right" width="220" style="margin-left:20px;margin-bottom:8px;">'

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

print(f"\nFase 3 Completata. File generati: {generated}/{len(SINNOH_POKEMON)}")
