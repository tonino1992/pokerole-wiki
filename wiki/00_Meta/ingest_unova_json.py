"""
Ingest Pokédex Unova (494-649) da Pokerole-Data JSON.
Genera 156 file Markdown in wiki/03_Pokedex/Unova/.
Le forme speciali vengono aggiunte come sezioni ## nella pagina base.
"""
import os, json, urllib.request, time, re

BASE_URL = "https://raw.githubusercontent.com/Pokerole-Software-Development/Pokerole-Data/master/v2.0/Pokedex"

UNOVA_POKEMON = [
    (494, "Victini"),
    (495, "Snivy"), (496, "Servine"), (497, "Serperior"),
    (498, "Tepig"), (499, "Pignite"), (500, "Emboar"),
    (501, "Oshawott"), (502, "Dewott"), (503, "Samurott"),
    (504, "Patrat"), (505, "Watchog"),
    (506, "Lillipup"), (507, "Herdier"), (508, "Stoutland"),
    (509, "Purrloin"), (510, "Liepard"),
    (511, "Pansage"), (512, "Simisage"),
    (513, "Pansear"), (514, "Simisear"),
    (515, "Panpour"), (516, "Simipour"),
    (517, "Munna"), (518, "Musharna"),
    (519, "Pidove"), (520, "Tranquill"), (521, "Unfezant"),
    (522, "Blitzle"), (523, "Zebstrika"),
    (524, "Roggenrola"), (525, "Boldore"), (526, "Gigalith"),
    (527, "Woobat"), (528, "Swoobat"),
    (529, "Drilbur"), (530, "Excadrill"),
    (531, "Audino"),
    (532, "Timburr"), (533, "Gurdurr"), (534, "Conkeldurr"),
    (535, "Tympole"), (536, "Palpitoad"), (537, "Seismitoad"),
    (538, "Throh"), (539, "Sawk"),
    (540, "Sewaddle"), (541, "Swadloon"), (542, "Leavanny"),
    (543, "Venipede"), (544, "Whirlipede"), (545, "Scolipede"),
    (546, "Cottonee"), (547, "Whimsicott"),
    (548, "Petilil"), (549, "Lilligant"),
    (550, "Basculin"),
    (551, "Sandile"), (552, "Krokorok"), (553, "Krookodile"),
    (554, "Darumaka"), (555, "Darmanitan"),
    (556, "Maractus"),
    (557, "Dwebble"), (558, "Crustle"),
    (559, "Scraggy"), (560, "Scrafty"),
    (561, "Sigilyph"),
    (562, "Yamask"), (563, "Cofagrigus"),
    (564, "Tirtouga"), (565, "Carracosta"),
    (566, "Archen"), (567, "Archeops"),
    (568, "Trubbish"), (569, "Garbodor"),
    (570, "Zorua"), (571, "Zoroark"),
    (572, "Minccino"), (573, "Cinccino"),
    (574, "Gothita"), (575, "Gothorita"), (576, "Gothitelle"),
    (577, "Solosis"), (578, "Duosion"), (579, "Reuniclus"),
    (580, "Ducklett"), (581, "Swanna"),
    (582, "Vanillite"), (583, "Vanillish"), (584, "Vanilluxe"),
    (585, "Deerling"), (586, "Sawsbuck"),
    (587, "Emolga"),
    (588, "Karrablast"), (589, "Escavalier"),
    (590, "Foongus"), (591, "Amoonguss"),
    (592, "Frillish"), (593, "Jellicent"),
    (594, "Alomomola"),
    (595, "Joltik"), (596, "Galvantula"),
    (597, "Ferroseed"), (598, "Ferrothorn"),
    (599, "Klink"), (600, "Klang"), (601, "Klinklang"),
    (602, "Tynamo"), (603, "Eelektrik"), (604, "Eelektross"),
    (605, "Elgyem"), (606, "Beheeyem"),
    (607, "Litwick"), (608, "Lampent"), (609, "Chandelure"),
    (610, "Axew"), (611, "Fraxure"), (612, "Haxorus"),
    (613, "Cubchoo"), (614, "Beartic"),
    (615, "Cryogonal"),
    (616, "Shelmet"), (617, "Accelgor"),
    (618, "Stunfisk"),
    (619, "Mienfoo"), (620, "Mienshao"),
    (621, "Druddigon"),
    (622, "Golett"), (623, "Golurk"),
    (624, "Pawniard"), (625, "Bisharp"),
    (626, "Bouffalant"),
    (627, "Rufflet"), (628, "Braviary"),
    (629, "Vullaby"), (630, "Mandibuzz"),
    (631, "Heatmor"), (632, "Durant"),
    (633, "Deino"), (634, "Zweilous"), (635, "Hydreigon"),
    (636, "Larvesta"), (637, "Volcarona"),
    (638, "Cobalion"), (639, "Terrakion"), (640, "Virizion"),
    (641, "Tornadus"), (642, "Thundurus"),
    (643, "Reshiram"), (644, "Zekrom"),
    (645, "Landorus"),
    (646, "Kyurem"),
    (647, "Keldeo"),
    (648, "Meloetta"),
    (649, "Genesect"),
]

# Forme speciali Unova: (url_encoded, sezione_titolo, img_fname_o_None)
UNOVA_FORMS = {
    "Audino":       [("Audino%20(Mega%20Form)",           "Mega Audino",                  "audino-mega.png")],
    "Darumaka":     [("Darumaka%20(Galarian%20Form)",     "Darumaka (Forma Galar)",        None)],
    "Darmanitan":   [
        ("Darmanitan%20(Zen%20Form)",          "Darmanitan (Forma Zen)",        None),
        ("Darmanitan%20(Galarian%20Form)",     "Darmanitan (Forma Galar)",      None),
        ("Darmanitan%20(Galarian%20Zen%20Form)", "Darmanitan (Forma Galar Zen)", None),
    ],
    "Yamask":       [("Yamask%20(Galarian%20Form)",       "Yamask (Forma Galar)",          None)],
    "Stunfisk":     [("Stunfisk%20(Galarian%20Form)",     "Stunfisk (Forma Galar)",        None)],
    "Tornadus":     [("Tornadus%20(Therian%20Form)",      "Tornadus (Forma Totem)",        None)],
    "Thundurus":    [("Thundurus%20(Therian%20Form)",     "Thundurus (Forma Totem)",       None)],
    "Landorus":     [("Landorus%20(Therian%20Form)",      "Landorus (Forma Totem)",        None)],
    "Kyurem":       [
        ("Kyurem%20(Black%20Form)",            "Kyurem Nero",                   None),
        ("Kyurem%20(White%20Form)",            "Kyurem Bianco",                 None),
    ],
    "Keldeo":       [("Keldeo%20(Resolute%20Form)",       "Keldeo (Forma Risoluta)",       None)],
    "Meloetta":     [("Meloetta%20(Pirouette%20Form)",    "Meloetta (Forma Piroetta)",     None)],
}

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
    "Bulbasaur":"0001","Ivysaur":"0002","Venusaur":"0003",
    "Charmander":"0004","Charmeleon":"0005","Charizard":"0006",
    "Squirtle":"0007","Wartortle":"0008","Blastoise":"0009",
    "Pikachu":"0025","Raichu":"0026",
    "Clefairy":"0035","Clefable":"0036",
    "Jigglypuff":"0039","Wigglytuff":"0040",
    "Zubat":"0041","Golbat":"0042",
    "Oddish":"0043","Gloom":"0044","Vileplume":"0045",
    "Slowpoke":"0079","Slowbro":"0080",
    "Magnemite":"0081","Magneton":"0082",
    "Onix":"0095",
    "Lickitung":"0108",
    "Rhydon":"0112","Chansey":"0113","Tangela":"0114",
    "Horsea":"0116","Seadra":"0117",
    "Mr. Mime":"0122","Scyther":"0123",
    "Jynx":"0124","Electabuzz":"0125","Magmar":"0126",
    "Eevee":"0133","Porygon":"0137","Snorlax":"0143",
    "Hitmonlee":"0106","Hitmonchan":"0107",
    "Poliwag":"0060","Poliwhirl":"0061","Poliwrath":"0062",
    # Johto
    "Chikorita":"0152","Bayleef":"0153","Meganium":"0154",
    "Cyndaquil":"0155","Quilava":"0156","Typhlosion":"0157",
    "Totodile":"0158","Croconaw":"0159","Feraligatr":"0160",
    "Pichu":"0172","Cleffa":"0173","Igglybuff":"0174",
    "Togepi":"0175","Togetic":"0176",
    "Marill":"0183","Azumarill":"0184",
    "Aipom":"0190","Yanma":"0193",
    "Espeon":"0196","Umbreon":"0197",
    "Murkrow":"0198","Slowking":"0199","Misdreavus":"0200",
    "Wobbuffet":"0202",
    "Gligar":"0207","Steelix":"0208",
    "Scizor":"0212","Heracross":"0214","Sneasel":"0215",
    "Slugma":"0218","Magcargo":"0219",
    "Swinub":"0220","Piloswine":"0221",
    "Corsola":"0222","Remoraid":"0223","Octillery":"0224",
    "Mantine":"0226","Skarmory":"0227",
    "Houndour":"0228","Houndoom":"0229","Kingdra":"0230",
    "Phanpy":"0231","Donphan":"0232",
    "Porygon2":"0233","Stantler":"0234","Smeargle":"0235",
    "Tyrogue":"0236","Hitmontop":"0237",
    "Smoochum":"0238","Elekid":"0239","Magby":"0240",
    "Miltank":"0241","Blissey":"0242",
    "Raikou":"0243","Entei":"0244","Suicune":"0245",
    "Larvitar":"0246","Pupitar":"0247","Tyranitar":"0248",
    "Lugia":"0249","Ho-Oh":"0250","Celebi":"0251",
    # Hoenn
    "Treecko":"0252","Grovyle":"0253","Sceptile":"0254",
    "Torchic":"0255","Combusken":"0256","Blaziken":"0257",
    "Mudkip":"0258","Marshtomp":"0259","Swampert":"0260",
    "Ralts":"0280","Kirlia":"0281","Gardevoir":"0282",
    "Roselia":"0315",
    "Carvanha":"0318","Sharpedo":"0319",
    "Numel":"0322","Camerupt":"0323",
    "Trapinch":"0328","Vibrava":"0329","Flygon":"0330",
    "Swablu":"0333","Altaria":"0334",
    "Lileep":"0345","Cradily":"0346",
    "Anorith":"0347","Armaldo":"0348",
    "Shuppet":"0353","Banette":"0354",
    "Duskull":"0355","Dusclops":"0356",
    "Absol":"0359","Wynaut":"0360",
    "Snorunt":"0361","Glalie":"0362","Froslass":"0478",
    "Bagon":"0371","Shelgon":"0372","Salamence":"0373",
    "Beldum":"0374","Metang":"0375","Metagross":"0376",
    "Latias":"0380","Latios":"0381",
    "Kyogre":"0382","Groudon":"0383","Rayquaza":"0384",
    "Jirachi":"0385","Deoxys":"0386",
    # Sinnoh
    "Turtwig":"0387","Grotle":"0388","Torterra":"0389",
    "Chimchar":"0390","Monferno":"0391","Infernape":"0392",
    "Piplup":"0393","Prinplup":"0394","Empoleon":"0395",
    "Budew":"0406","Roserade":"0407",
    "Cranidos":"0408","Rampardos":"0409",
    "Shieldon":"0410","Bastiodon":"0411",
    "Burmy":"0412","Wormadam":"0413","Mothim":"0414",
    "Ambipom":"0424",
    "Drifloon":"0425","Drifblim":"0426",
    "Buneary":"0427","Lopunny":"0428",
    "Mismagius":"0429","Honchkrow":"0430",
    "Chingling":"0433",
    "Bonsly":"0438","Mime Jr.":"0439","Happiny":"0440",
    "Munchlax":"0446","Riolu":"0447","Lucario":"0448",
    "Skorupi":"0451","Drapion":"0452",
    "Croagunk":"0453","Toxicroak":"0454",
    "Mantyke":"0458",
    "Snover":"0459","Abomasnow":"0460",
    "Weavile":"0461","Magnezone":"0462","Lickilicky":"0463",
    "Rhyperior":"0464","Tangrowth":"0465",
    "Electivire":"0466","Magmortar":"0467",
    "Togekiss":"0468","Yanmega":"0469",
    "Leafeon":"0470","Glaceon":"0471",
    "Gliscor":"0472","Mamoswine":"0473","Porygon-Z":"0474",
    "Gallade":"0475","Probopass":"0476",
    "Dusknoir":"0477",
    "Rotom":"0479",
    "Uxie":"0480","Mesprit":"0481","Azelf":"0482",
    "Dialga":"0483","Palkia":"0484","Heatran":"0485",
    "Regigigas":"0486","Giratina":"0487","Cresselia":"0488",
    "Phione":"0489","Manaphy":"0490",
    "Darkrai":"0491","Shaymin":"0492","Arceus":"0493",
}

RANK_ORDER = ["Starter", "Beginner", "Amateur", "Ace", "Pro", "Master", "Champion"]
IMG_FORM = '<img src="../../assets/images/pokemon/forms/{fname}" align="right" width="200" style="margin-left:16px;margin-bottom:8px;">'

md_dir = "wiki/03_Pokedex/Unova"
os.makedirs(md_dir, exist_ok=True)


def fetch_json(url_encoded_name):
    url = f"{BASE_URL}/{url_encoded_name}.json"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        resp = urllib.request.urlopen(req, timeout=15)
        return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"  ERRORE fetch {url_encoded_name}: {e}")
        return None

def url_enc(name):
    return name.replace(" ", "%20").replace("'", "%27")

def translate_type(t):
    return TYPE_IT.get(t, t)

def make_slug(name):
    return (name.replace(" ", "_").replace(".", "").replace("'", "")
               .replace("-", "_").replace("(", "").replace(")", ""))

def dex_link(dex_id, name):
    return f"[[{dex_id}_{make_slug(name)}|{name}]]"

def build_moves_md(data):
    moves_by_rank = {}
    for move in data.get("Moves", []):
        rank = move.get("Learned", "Unknown")
        mn = move.get("Name", "")
        if mn:
            slug_m = mn.replace(" ", "_").replace("-", "_").replace("'", "")
            moves_by_rank.setdefault(rank, []).append(f"[[{slug_m}|{mn}]]")
    result = ""
    for rank in RANK_ORDER:
        if rank in moves_by_rank:
            result += f"- **{rank}:** {', '.join(moves_by_rank[rank])}\n"
    return result

def build_form_section(title, data, img_fname=None):
    dex_id = data.get("DexID", "")
    types_raw = [data.get("Type1", "")]
    if data.get("Type2"):
        types_raw.append(data["Type2"])
    types_it = " / ".join(translate_type(t) for t in types_raw if t)
    hp = data.get("BaseHP", 0)
    abs_list = []
    if data.get("Ability1"): abs_list.append(f"[[{data['Ability1']}]]")
    if data.get("Ability2"): abs_list.append(f"[[{data['Ability2']}]]")
    if data.get("HiddenAbility"): abs_list.append(f"[[{data['HiddenAbility']}]] *(Hidden)*")
    abilities_str = ", ".join(abs_list)

    stats = (
        f"| **Strength** | {data.get('Strength',0)}/{data.get('MaxStrength',0)} |\n"
        f"| **Dexterity** | {data.get('Dexterity',0)}/{data.get('MaxDexterity',0)} |\n"
        f"| **Vitality** | {data.get('Vitality',0)}/{data.get('MaxVitality',0)} |\n"
        f"| **Special** | {data.get('Special',0)}/{data.get('MaxSpecial',0)} |\n"
        f"| **Insight** | {data.get('Insight',0)}/{data.get('MaxInsight',0)} |"
    )

    moves_md = build_moves_md(data)
    id_str = f" (#{dex_id})" if dex_id else ""
    img_line = f"\n{IMG_FORM.format(fname=img_fname)}\n" if img_fname else ""

    return f"""
---

## {title}{id_str}
{img_line}
**Type:** {types_it}
**Abilities:** {abilities_str}
**Base HP:** {hp}

| Attribute | Base / Limit |
|---|---|
{stats}

### Mosse

{moves_md}"""


# Costruzione catene evolutive inverse (solo Unova)
def get_chain_root(name, evolves_from, visited=None):
    if visited is None: visited = set()
    if name in visited: return name
    visited.add(name)
    parents = evolves_from.get(name, [])
    if not parents: return name
    return get_chain_root(parents[0], evolves_from, visited)

def get_full_chain(root, all_data, visited=None):
    if visited is None: visited = set()
    if root in visited: return []
    visited.add(root)
    chain = [root]
    for evo in all_data.get(root, {}).get("Evolutions", []):
        target = evo.get("To", "")
        if target and target not in visited:
            chain.extend(get_full_chain(target, all_data, visited))
    return chain


# ── FASE 1: download base ────────────────────────────────────────────────────
print("Fase 1: Download JSON Unova...")
all_data = {}
unova_id_map = {}

for poke_id, name in UNOVA_POKEMON:
    data = fetch_json(url_enc(name))
    if data:
        all_data[name] = data
        unova_id_map[name] = data.get("DexID", f"{poke_id:04d}")
        print(f"  OK #{poke_id} {name}")
    else:
        print(f"  SKIP #{poke_id} {name}")
    time.sleep(0.15)

full_id_map = {**KNOWN_IDS, **unova_id_map}

# ── FASE 2: catene evolutive inverse ────────────────────────────────────────
evolves_from = {}
for name, data in all_data.items():
    for evo in data.get("Evolutions", []):
        target = evo.get("To", "")
        if target:
            evolves_from.setdefault(target, []).append(name)

# ── FASE 3: download forme speciali ─────────────────────────────────────────
print("\nFase 2: Download forme speciali...")
forms_data = {}  # name -> [(title, data, img_fname)]
for name, form_list in UNOVA_FORMS.items():
    forms_data[name] = []
    for url_form, title, img_fname in form_list:
        fdata = fetch_json(url_form)
        if fdata:
            forms_data[name].append((title, fdata, img_fname))
            print(f"  OK forma: {title}")
        else:
            print(f"  SKIP forma: {title}")
        time.sleep(0.12)

# ── FASE 4: genera Markdown ──────────────────────────────────────────────────
print("\nFase 3: Generazione file Markdown...")
generated = 0

for poke_id, name in UNOVA_POKEMON:
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

    str_val = f"{data.get('Strength',0)}/{data.get('MaxStrength',0)}"
    dex_val = f"{data.get('Dexterity',0)}/{data.get('MaxDexterity',0)}"
    vit_val = f"{data.get('Vitality',0)}/{data.get('MaxVitality',0)}"
    spe_val = f"{data.get('Special',0)}/{data.get('MaxSpecial',0)}"
    ins_val = f"{data.get('Insight',0)}/{data.get('MaxInsight',0)}"

    moves_md = build_moves_md(data)

    # Catena evolutiva
    root = get_chain_root(name, evolves_from)
    chain = get_full_chain(root, all_data)
    evo_section = ""
    if len(chain) > 1 or name in evolves_from:
        lines = ["## Correlati\n", "### Catena Evolutiva"]
        for member in chain:
            did = full_id_map.get(member)
            if did:
                lines.append(f"- {dex_link(did, member)}")
            else:
                lines.append(f"- {member}")
        evo_section = "\n".join(lines)

    # Forme speciali come sezioni
    form_sections = ""
    for title, fdata, img_fname in forms_data.get(name, []):
        form_sections += build_form_section(title, fdata, img_fname)

    name_tag = name.lower().replace(" ","").replace("-","").replace(".","").replace("'","")
    tags = [name_tag, "unova"] + types_lower

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
{form_sections}
"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(md)

    generated += 1
    print(f"  Creato {filename}")

print(f"\nFase 3 Completata. File generati: {generated}/{len(UNOVA_POKEMON)}")
