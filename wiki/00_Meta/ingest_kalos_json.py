"""
Ingest Pokédex Kalos (650-721) da Pokerole-Data JSON.
Genera 72 file Markdown in wiki/03_Pokedex/Kalos/.
Le forme speciali vengono aggiunte come sezioni ## nella pagina base.
"""
import os, json, urllib.request, urllib.parse, time

BASE_URL = "https://raw.githubusercontent.com/Pokerole-Software-Development/Pokerole-Data/master/v2.0/Pokedex"

KALOS_POKEMON = [
    (650, "Chespin"), (651, "Quilladin"), (652, "Chesnaught"),
    (653, "Fennekin"), (654, "Braixen"), (655, "Delphox"),
    (656, "Froakie"), (657, "Frogadier"), (658, "Greninja"),
    (659, "Bunnelby"), (660, "Diggersby"),
    (661, "Fletchling"), (662, "Fletchinder"), (663, "Talonflame"),
    (664, "Scatterbug"), (665, "Spewpa"), (666, "Vivillon"),
    (667, "Litleo"), (668, "Pyroar"),
    (669, "Flabébé"), (670, "Floette"), (671, "Florges"),
    (672, "Skiddo"), (673, "Gogoat"),
    (674, "Pancham"), (675, "Pangoro"),
    (676, "Furfrou"),
    (677, "Espurr"), (678, "Meowstic"),
    (679, "Honedge"), (680, "Doublade"), (681, "Aegislash"),
    (682, "Spritzee"), (683, "Aromatisse"),
    (684, "Swirlix"), (685, "Slurpuff"),
    (686, "Inkay"), (687, "Malamar"),
    (688, "Binacle"), (689, "Barbaracle"),
    (690, "Skrelp"), (691, "Dragalge"),
    (692, "Clauncher"), (693, "Clawitzer"),
    (694, "Helioptile"), (695, "Heliolisk"),
    (696, "Tyrunt"), (697, "Tyrantrum"),
    (698, "Amaura"), (699, "Aurorus"),
    (700, "Sylveon"),
    (701, "Hawlucha"),
    (702, "Dedenne"),
    (703, "Carbink"),
    (704, "Goomy"), (705, "Sliggoo"), (706, "Goodra"),
    (707, "Klefki"),
    (708, "Phantump"), (709, "Trevenant"),
    (710, "Pumpkaboo"), (711, "Gourgeist"),
    (712, "Bergmite"), (713, "Avalugg"),
    (714, "Noibat"), (715, "Noivern"),
    (716, "Xerneas"),
    (717, "Yveltal"),
    (718, "Zygarde"),
    (719, "Diancie"),
    (720, "Hoopa"),
    (721, "Volcanion"),
]

# Forme speciali Kalos: (url_encoded, sezione_titolo, img_fname_o_None)
KALOS_FORMS = {
    "Meowstic": [("Meowstic%20(Female%20Form)",          "Meowstic (Forma Femminile)",     None)],
    "Aegislash": [("Aegislash%20(Blade%20Form)",          "Aegislash (Forma Lama)",         None)],
    "Zygarde": [
        ("Zygarde%20(10%20Percent%20Form)",   "Zygarde (Forma 10%)",            None),
        ("Zygarde%20(Complete%20Form)",       "Zygarde (Forma Completa)",       None),
    ],
    "Diancie": [("Diancie%20(Mega%20Form)",               "Mega Diancie",                   "diancie-mega.png")],
    "Hoopa":   [("Hoopa%20(Unbound%20Form)",              "Hoopa (Forma Senza Catene)",     None)],
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
    "Eevee":"0133","Vaporeon":"0134","Jolteon":"0135","Flareon":"0136",
    "Porygon":"0137","Snorlax":"0143",
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
    # Unova
    "Victini":"0494",
    "Snivy":"0495","Servine":"0496","Serperior":"0497",
    "Tepig":"0498","Pignite":"0499","Emboar":"0500",
    "Oshawott":"0501","Dewott":"0502","Samurott":"0503",
    "Patrat":"0504","Watchog":"0505",
    "Lillipup":"0506","Herdier":"0507","Stoutland":"0508",
    "Purrloin":"0509","Liepard":"0510",
    "Pansage":"0511","Simisage":"0512",
    "Pansear":"0513","Simisear":"0514",
    "Panpour":"0515","Simipour":"0516",
    "Munna":"0517","Musharna":"0518",
    "Pidove":"0519","Tranquill":"0520","Unfezant":"0521",
    "Blitzle":"0522","Zebstrika":"0523",
    "Roggenrola":"0524","Boldore":"0525","Gigalith":"0526",
    "Woobat":"0527","Swoobat":"0528",
    "Drilbur":"0529","Excadrill":"0530",
    "Audino":"0531",
    "Timburr":"0532","Gurdurr":"0533","Conkeldurr":"0534",
    "Tympole":"0535","Palpitoad":"0536","Seismitoad":"0537",
    "Throh":"0538","Sawk":"0539",
    "Sewaddle":"0540","Swadloon":"0541","Leavanny":"0542",
    "Venipede":"0543","Whirlipede":"0544","Scolipede":"0545",
    "Cottonee":"0546","Whimsicott":"0547",
    "Petilil":"0548","Lilligant":"0549",
    "Basculin":"0550",
    "Sandile":"0551","Krokorok":"0552","Krookodile":"0553",
    "Darumaka":"0554","Darmanitan":"0555",
    "Maractus":"0556",
    "Dwebble":"0557","Crustle":"0558",
    "Scraggy":"0559","Scrafty":"0560",
    "Sigilyph":"0561",
    "Yamask":"0562","Cofagrigus":"0563",
    "Tirtouga":"0564","Carracosta":"0565",
    "Archen":"0566","Archeops":"0567",
    "Trubbish":"0568","Garbodor":"0569",
    "Zorua":"0570","Zoroark":"0571",
    "Minccino":"0572","Cinccino":"0573",
    "Gothita":"0574","Gothorita":"0575","Gothitelle":"0576",
    "Solosis":"0577","Duosion":"0578","Reuniclus":"0579",
    "Ducklett":"0580","Swanna":"0581",
    "Vanillite":"0582","Vanillish":"0583","Vanilluxe":"0584",
    "Deerling":"0585","Sawsbuck":"0586",
    "Emolga":"0587",
    "Karrablast":"0588","Escavalier":"0589",
    "Foongus":"0590","Amoonguss":"0591",
    "Frillish":"0592","Jellicent":"0593",
    "Alomomola":"0594",
    "Joltik":"0595","Galvantula":"0596",
    "Ferroseed":"0597","Ferrothorn":"0598",
    "Klink":"0599","Klang":"0600","Klinklang":"0601",
    "Tynamo":"0602","Eelektrik":"0603","Eelektross":"0604",
    "Elgyem":"0605","Beheeyem":"0606",
    "Litwick":"0607","Lampent":"0608","Chandelure":"0609",
    "Axew":"0610","Fraxure":"0611","Haxorus":"0612",
    "Cubchoo":"0613","Beartic":"0614",
    "Cryogonal":"0615",
    "Shelmet":"0616","Accelgor":"0617",
    "Stunfisk":"0618",
    "Mienfoo":"0619","Mienshao":"0620",
    "Druddigon":"0621",
    "Golett":"0622","Golurk":"0623",
    "Pawniard":"0624","Bisharp":"0625",
    "Bouffalant":"0626",
    "Rufflet":"0627","Braviary":"0628",
    "Vullaby":"0629","Mandibuzz":"0630",
    "Heatmor":"0631","Durant":"0632",
    "Deino":"0633","Zweilous":"0634","Hydreigon":"0635",
    "Larvesta":"0636","Volcarona":"0637",
    "Cobalion":"0638","Terrakion":"0639","Virizion":"0640",
    "Tornadus":"0641","Thundurus":"0642",
    "Reshiram":"0643","Zekrom":"0644",
    "Landorus":"0645",
    "Kyurem":"0646",
    "Keldeo":"0647",
    "Meloetta":"0648",
    "Genesect":"0649",
}

RANK_ORDER = ["Starter", "Beginner", "Amateur", "Ace", "Pro", "Master", "Champion"]
IMG_FORM = '<img src="../../assets/images/pokemon/forms/{fname}" align="right" width="200" style="margin-left:16px;margin-bottom:8px;">'

md_dir = "wiki/03_Pokedex/Kalos"
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
    for ch in [" ", ".", "'", "(", ")"]:
        slug = slug.replace(ch, "_" if ch == " " else "")
    slug = slug.replace("-", "_")
    # Normalizza caratteri accentati per i filename
    slug = slug.replace("é", "e").replace("è", "e").replace("ê", "e")
    return slug

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
print("Fase 1: Download JSON Kalos...")
all_data = {}
kalos_id_map = {}

for poke_id, name in KALOS_POKEMON:
    data = fetch_json(url_enc(name))
    if data:
        all_data[name] = data
        kalos_id_map[name] = data.get("DexID", f"{poke_id:04d}")
        print(f"  OK #{poke_id} {name}")
    else:
        print(f"  SKIP #{poke_id} {name}")
    time.sleep(0.15)

full_id_map = {**KNOWN_IDS, **kalos_id_map}

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
for name, form_list in KALOS_FORMS.items():
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

for poke_id, name in KALOS_POKEMON:
    data = all_data.get(name)
    if not data:
        print(f"  SKIP {name} (dati mancanti)")
        errors.append(name)
        continue

    dex_id = data.get("DexID", f"{poke_id:04d}")
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

    # Forme speciali come sezioni
    form_sections = ""
    for title, fdata, img_fname in forms_data.get(name, []):
        form_sections += build_form_section(title, fdata, img_fname)

    name_tag = name.lower().replace(" ","").replace("-","").replace(".","").replace("'","").replace("é","e").replace("è","e")
    tags = [name_tag, "kalos"] + types_lower

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

print(f"\nFase 3 Completata. File generati: {generated}/{len(KALOS_POKEMON)}")
if errors:
    print(f"ERRORI ({len(errors)}): {', '.join(errors)}")
