"""
Ingest Pokédex Alola (722-809) da Pokerole-Data JSON.
Genera 88 file Markdown in wiki/03_Pokedex/Alola/.
Le forme speciali vengono aggiunte come sezioni ## nella pagina base.
"""
import os, json, urllib.request, urllib.parse, time

BASE_URL = "https://raw.githubusercontent.com/Pokerole-Software-Development/Pokerole-Data/master/v2.0/Pokedex"

ALOLA_POKEMON = [
    (722, "Rowlet"), (723, "Dartrix"), (724, "Decidueye"),
    (725, "Litten"), (726, "Torracat"), (727, "Incineroar"),
    (728, "Popplio"), (729, "Brionne"), (730, "Primarina"),
    (731, "Pikipek"), (732, "Trumbeak"), (733, "Toucannon"),
    (734, "Yungoos"), (735, "Gumshoos"),
    (736, "Grubbin"), (737, "Charjabug"), (738, "Vikavolt"),
    (739, "Crabrawler"), (740, "Crabominable"),
    (741, "Oricorio"),
    (742, "Cutiefly"), (743, "Ribombee"),
    (744, "Rockruff"), (745, "Lycanroc"),
    (746, "Wishiwashi"),
    (747, "Mareanie"), (748, "Toxapex"),
    (749, "Mudbray"), (750, "Mudsdale"),
    (751, "Dewpider"), (752, "Araquanid"),
    (753, "Fomantis"), (754, "Lurantis"),
    (755, "Morelull"), (756, "Shiinotic"),
    (757, "Salandit"), (758, "Salazzle"),
    (759, "Stufful"), (760, "Bewear"),
    (761, "Bounsweet"), (762, "Steenee"), (763, "Tsareena"),
    (764, "Comfey"),
    (765, "Oranguru"),
    (766, "Passimian"),
    (767, "Wimpod"), (768, "Golisopod"),
    (769, "Sandygast"), (770, "Palossand"),
    (771, "Pyukumuku"),
    (772, "Type: Null"), (773, "Silvally"),
    (774, "Minior"),
    (775, "Komala"),
    (776, "Turtonator"),
    (777, "Togedemaru"),
    (778, "Mimikyu"),
    (779, "Bruxish"),
    (780, "Drampa"),
    (781, "Dhelmise"),
    (782, "Jangmo-o"), (783, "Hakamo-o"), (784, "Kommo-o"),
    (785, "Tapu Koko"), (786, "Tapu Lele"), (787, "Tapu Bulu"), (788, "Tapu Fini"),
    (789, "Cosmog"), (790, "Cosmoem"),
    (791, "Solgaleo"), (792, "Lunala"),
    (793, "Nihilego"),
    (794, "Buzzwole"), (795, "Pheromosa"), (796, "Xurkitree"),
    (797, "Celesteela"), (798, "Kartana"), (799, "Guzzlord"),
    (800, "Necrozma"),
    (801, "Magearna"),
    (802, "Marshadow"),
    (803, "Poipole"), (804, "Naganadel"),
    (805, "Stakataka"),
    (806, "Blacephalon"),
    (807, "Zeraora"),
    (808, "Meltan"), (809, "Melmetal"),
]

# Alcuni Pokémon non hanno un JSON "base" — il file nel repo ha nome diverso
URL_OVERRIDES = {
    "Oricorio":  "Oricorio%20(Baile%20Form)",   # non esiste Oricorio.json
    "Lycanroc":  "Lycanroc%20(Midday%20Form)",   # non esiste Lycanroc.json
    "Type: Null": "Type%20Null",                 # il : causa 404
}

# Forme speciali Alola: (url_encoded, sezione_titolo, img_fname_o_None)
ALOLA_FORMS = {
    "Oricorio": [
        ("Oricorio%20(Pom-pom%20Form)", "Oricorio (Forma Pom-Pom)",  None),
        ("Oricorio%20(Pa%27u%20Form)",  "Oricorio (Forma Pa'u)",     None),
        ("Oricorio%20(Sensu%20Form)",   "Oricorio (Forma Sensu)",    None),
    ],
    "Lycanroc": [
        ("Lycanroc%20(Midnight%20Form)", "Lycanroc (Forma Mezzanotte)", None),
        ("Lycanroc%20(Dusk%20Form)",     "Lycanroc (Forma Crepuscolo)", None),
    ],
    "Wishiwashi": [
        ("Wishiwashi%20(Swarm%20Form)", "Wishiwashi (Forma Sciame)", None),
    ],
    "Minior": [
        ("Minior%20Core", "Minior (Forma Nucleo)", None),
    ],
    "Necrozma": [
        ("Necrozma%20(Dusk%20Mane%20Form)",   "Necrozma (Criniera del Tramonto)", None),
        ("Necrozma%20(Dawn%20Wings%20Form)",   "Necrozma (Ali dell'Alba)",         None),
        ("Necrozma%20(Ultra%20Burst%20Form)",  "Necrozma Ultra",                   None),
    ],
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
    "Caterpie":"0010","Metapod":"0011","Butterfree":"0012",
    "Weedle":"0013","Kakuna":"0014","Beedrill":"0015",
    "Pidgey":"0016","Pidgeotto":"0017","Pidgeot":"0018",
    "Pikachu":"0025","Raichu":"0026",
    "Clefairy":"0035","Clefable":"0036",
    "Jigglypuff":"0039","Wigglytuff":"0040",
    "Zubat":"0041","Golbat":"0042","Crobat":"0169",
    "Oddish":"0043","Gloom":"0044","Vileplume":"0045","Bellossom":"0182",
    "Slowpoke":"0079","Slowbro":"0080","Slowking":"0199",
    "Magnemite":"0081","Magneton":"0082","Magnezone":"0462",
    "Onix":"0095","Steelix":"0208",
    "Lickitung":"0108","Lickilicky":"0463",
    "Rhydon":"0112","Rhyhorn":"0111","Rhyperior":"0464",
    "Chansey":"0113","Blissey":"0242","Happiny":"0440",
    "Tangela":"0114","Tangrowth":"0465",
    "Horsea":"0116","Seadra":"0117","Kingdra":"0230",
    "Mr. Mime":"0122","Mime Jr.":"0439",
    "Scyther":"0123","Scizor":"0212",
    "Jynx":"0124","Smoochum":"0238",
    "Electabuzz":"0125","Elekid":"0239","Electivire":"0466",
    "Magmar":"0126","Magby":"0240","Magmortar":"0467",
    "Eevee":"0133","Vaporeon":"0134","Jolteon":"0135","Flareon":"0136",
    "Espeon":"0196","Umbreon":"0197","Leafeon":"0470","Glaceon":"0471","Sylveon":"0700",
    "Porygon":"0137","Porygon2":"0233","Porygon-Z":"0474",
    "Snorlax":"0143","Munchlax":"0446",
    "Hitmonlee":"0106","Hitmonchan":"0107","Hitmontop":"0237","Tyrogue":"0236",
    "Poliwag":"0060","Poliwhirl":"0061","Poliwrath":"0062","Politoed":"0186",
    "Abra":"0063","Kadabra":"0064","Alakazam":"0065",
    "Machop":"0066","Machoke":"0067","Machamp":"0068",
    "Geodude":"0074","Graveler":"0075","Golem":"0076",
    "Gastly":"0092","Haunter":"0093","Gengar":"0094",
    "Dratini":"0147","Dragonair":"0148","Dragonite":"0149",
    # Johto
    "Chikorita":"0152","Bayleef":"0153","Meganium":"0154",
    "Cyndaquil":"0155","Quilava":"0156","Typhlosion":"0157",
    "Totodile":"0158","Croconaw":"0159","Feraligatr":"0160",
    "Pichu":"0172","Cleffa":"0173","Igglybuff":"0174",
    "Togepi":"0175","Togetic":"0176","Togekiss":"0468",
    "Marill":"0183","Azumarill":"0184","Azurill":"0298",
    "Aipom":"0190","Ambipom":"0424",
    "Yanma":"0193","Yanmega":"0469",
    "Murkrow":"0198","Honchkrow":"0430",
    "Misdreavus":"0200","Mismagius":"0429",
    "Wobbuffet":"0202",
    "Gligar":"0207","Gliscor":"0472",
    "Sneasel":"0215","Weavile":"0461",
    "Slugma":"0218","Magcargo":"0219",
    "Swinub":"0220","Piloswine":"0221","Mamoswine":"0473",
    "Corsola":"0222","Remoraid":"0223","Octillery":"0224",
    "Mantine":"0226","Mantyke":"0458",
    "Skarmory":"0227",
    "Houndour":"0228","Houndoom":"0229",
    "Phanpy":"0231","Donphan":"0232",
    "Stantler":"0234","Smeargle":"0235",
    "Miltank":"0241",
    "Raikou":"0243","Entei":"0244","Suicune":"0245",
    "Larvitar":"0246","Pupitar":"0247","Tyranitar":"0248",
    "Lugia":"0249","Ho-Oh":"0250","Celebi":"0251",
    # Hoenn
    "Treecko":"0252","Grovyle":"0253","Sceptile":"0254",
    "Torchic":"0255","Combusken":"0256","Blaziken":"0257",
    "Mudkip":"0258","Marshtomp":"0259","Swampert":"0260",
    "Ralts":"0280","Kirlia":"0281","Gardevoir":"0282","Gallade":"0475",
    "Roselia":"0315","Budew":"0406","Roserade":"0407",
    "Carvanha":"0318","Sharpedo":"0319",
    "Numel":"0322","Camerupt":"0323",
    "Trapinch":"0328","Vibrava":"0329","Flygon":"0330",
    "Swablu":"0333","Altaria":"0334",
    "Lileep":"0345","Cradily":"0346",
    "Anorith":"0347","Armaldo":"0348",
    "Shuppet":"0353","Banette":"0354",
    "Duskull":"0355","Dusclops":"0356","Dusknoir":"0477",
    "Absol":"0359",
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
    "Cranidos":"0408","Rampardos":"0409",
    "Shieldon":"0410","Bastiodon":"0411",
    "Burmy":"0412","Wormadam":"0413","Mothim":"0414",
    "Drifloon":"0425","Drifblim":"0426",
    "Buneary":"0427","Lopunny":"0428",
    "Chingling":"0433",
    "Bonsly":"0438","Riolu":"0447","Lucario":"0448",
    "Skorupi":"0451","Drapion":"0452",
    "Croagunk":"0453","Toxicroak":"0454",
    "Snover":"0459","Abomasnow":"0460",
    "Rotom":"0479",
    "Uxie":"0480","Mesprit":"0481","Azelf":"0482",
    "Dialga":"0483","Palkia":"0484","Heatran":"0485",
    "Regigigas":"0486","Giratina":"0487","Cresselia":"0488",
    "Phione":"0489","Manaphy":"0490",
    "Darkrai":"0491","Shaymin":"0492","Arceus":"0493",
    # Unova
    "Victini":"0494",
    "Snivy":"0495","Servine":"0496","Serperior":"0497",
    "Tepig":"0498","Pignite":"0499","Emboar":"0500",
    "Oshawott":"0501","Dewott":"0502","Samurott":"0503",
    "Audino":"0531",
    "Zorua":"0570","Zoroark":"0571",
    "Gothita":"0574","Gothorita":"0575","Gothitelle":"0576",
    "Solosis":"0577","Duosion":"0578","Reuniclus":"0579",
    "Joltik":"0595","Galvantula":"0596",
    "Axew":"0610","Fraxure":"0611","Haxorus":"0612",
    "Golett":"0622","Golurk":"0623",
    "Pawniard":"0624","Bisharp":"0625",
    "Deino":"0633","Zweilous":"0634","Hydreigon":"0635",
    "Cobalion":"0638","Terrakion":"0639","Virizion":"0640",
    "Reshiram":"0643","Zekrom":"0644","Kyurem":"0646",
    "Keldeo":"0647","Meloetta":"0648","Genesect":"0649",
    # Kalos
    "Chespin":"0650","Quilladin":"0651","Chesnaught":"0652",
    "Fennekin":"0653","Braixen":"0654","Delphox":"0655",
    "Froakie":"0656","Frogadier":"0657","Greninja":"0658",
    "Flabébé":"0669","Floette":"0670","Florges":"0671",
    "Goomy":"0704","Sliggoo":"0705","Goodra":"0706",
    "Phantump":"0708","Trevenant":"0709",
    "Noibat":"0714","Noivern":"0715",
    "Xerneas":"0716","Yveltal":"0717","Zygarde":"0718",
    "Diancie":"0719","Hoopa":"0720","Volcanion":"0721",
}

RANK_ORDER = ["Starter", "Beginner", "Amateur", "Ace", "Pro", "Master", "Champion"]
IMG_FORM = '<img src="../../assets/images/pokemon/forms/{fname}" align="right" width="200" style="margin-left:16px;margin-bottom:8px;">'

md_dir = "wiki/03_Pokedex/Alola"
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
    return urllib.parse.quote(name, safe='')

def translate_type(t):
    return TYPE_IT.get(t, t)

def make_slug(name):
    slug = name
    for ch in [":", " ", ".", "'", "(", ")"]:
        slug = slug.replace(ch, "_" if ch == " " else "")
    slug = slug.replace("-", "_")
    slug = slug.replace("é", "e").replace("è", "e")
    # Rimuovi underscore multipli
    while "__" in slug:
        slug = slug.replace("__", "_")
    return slug.strip("_")

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
print("Fase 1: Download JSON Alola...")
all_data = {}
alola_id_map = {}

for poke_id, name in ALOLA_POKEMON:
    enc = URL_OVERRIDES.get(name, url_enc(name))
    data = fetch_json(enc)
    if data:
        all_data[name] = data
        alola_id_map[name] = data.get("DexID", f"{poke_id:04d}")
        print(f"  OK #{poke_id} {name}")
    else:
        print(f"  SKIP #{poke_id} {name}")
    time.sleep(0.15)

full_id_map = {**KNOWN_IDS, **alola_id_map}

# ── FASE 2: catene evolutive inverse ────────────────────────────────────────
evolves_from = {}
for name, data in all_data.items():
    for evo in data.get("Evolutions", []):
        target = evo.get("To", "")
        if target:
            evolves_from.setdefault(target, []).append(name)

# ── FASE 3: download forme speciali ─────────────────────────────────────────
print("\nFase 2: Download forme speciali...")
forms_data = {}
for name, form_list in ALOLA_FORMS.items():
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
errors = []

for poke_id, name in ALOLA_POKEMON:
    data = all_data.get(name)
    if not data:
        print(f"  SKIP {name} (dati mancanti)")
        errors.append(name)
        continue

    # Per Oricorio/Lycanroc il DexID nel JSON potrebbe avere suffisso forma — forziamo l'ID standard
    dex_id_raw = data.get("DexID", f"{poke_id:04d}")
    # Se il DexID contiene lettere (es. 0741F1) usiamo l'ID numerico puro
    dex_id = dex_id_raw if dex_id_raw.isdigit() or (len(dex_id_raw) == 4 and dex_id_raw.isdigit()) else f"{poke_id:04d}"

    types_raw = [data.get("Type1", "")]
    if data.get("Type2"):
        types_raw.append(data["Type2"])
    types_it = " / ".join(translate_type(t) for t in types_raw if t)
    types_lower = [t.lower() for t in types_raw if t]

    category = data.get("DexCategory", "Pokemon")
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

    # Forme speciali come sezioni inline
    form_sections = ""
    for title, fdata, img_fname in forms_data.get(name, []):
        form_sections += build_form_section(title, fdata, img_fname)

    name_tag = name.lower().replace(" ","").replace("-","").replace(".","").replace("'","").replace(":","").replace("é","e")
    tags = [name_tag, "alola"] + types_lower

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

print(f"\nFase 3 Completata. File generati: {generated}/{len(ALOLA_POKEMON)}")
if errors:
    print(f"ERRORI ({len(errors)}): {', '.join(errors)}")
