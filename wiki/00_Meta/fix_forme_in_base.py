"""
Sposta le forme alternative (Mega, Primal, Alolan, Galarian, ecc.)
come sezioni dentro la pagina del Pokémon base, poi rimuove i file separati.
"""
import os, json, urllib.request, time, glob

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

# (url_encoded_form, section_title, base_file_path)
# base_file_path = glob pattern che individua il file del Pokémon base
FORMS = [
    # ── KANTO ──────────────────────────────────────────────────────────────────
    ("Venusaur%20(Mega%20Form)",    "Mega Venusaur",          "wiki/03_Pokedex/Kanto/0003_Venusaur.md"),
    ("Charizard%20(Mega%20X%20Form)","Mega Charizard X",      "wiki/03_Pokedex/Kanto/0006_Charizard.md"),
    ("Charizard%20(Mega%20Y%20Form)","Mega Charizard Y",      "wiki/03_Pokedex/Kanto/0006_Charizard.md"),
    ("Blastoise%20(Mega%20Form)",   "Mega Blastoise",         "wiki/03_Pokedex/Kanto/0009_Blastoise.md"),
    ("Beedrill%20(Mega%20Form)",    "Mega Beedrill",          "wiki/03_Pokedex/Kanto/0015_Beedrill.md"),
    ("Pidgeot%20(Mega%20Form)",     "Mega Pidgeot",           "wiki/03_Pokedex/Kanto/0018_Pidgeot.md"),
    ("Alakazam%20(Mega%20Form)",    "Mega Alakazam",          "wiki/03_Pokedex/Kanto/0065_Alakazam.md"),
    ("Kangaskhan%20(Mega%20Form)",  "Mega Kangaskhan",        "wiki/03_Pokedex/Kanto/0115_Kangaskhan.md"),
    ("Pinsir%20(Mega%20Form)",      "Mega Pinsir",            "wiki/03_Pokedex/Kanto/0127_Pinsir.md"),
    ("Gyarados%20(Mega%20Form)",    "Mega Gyarados",          "wiki/03_Pokedex/Kanto/0130_Gyarados.md"),
    ("Aerodactyl%20(Mega%20Form)",  "Mega Aerodactyl",        "wiki/03_Pokedex/Kanto/0142_Aerodactyl.md"),
    ("Mewtwo%20(Mega%20X%20Form)",  "Mega Mewtwo X",          "wiki/03_Pokedex/Kanto/0150_Mewtwo.md"),
    ("Mewtwo%20(Mega%20Y%20Form)",  "Mega Mewtwo Y",          "wiki/03_Pokedex/Kanto/0150_Mewtwo.md"),
    ("Gengar%20(Mega%20Form)",      "Mega Gengar",            "wiki/03_Pokedex/Kanto/0094_Gengar.md"),
    ("Slowbro%20(Mega%20Form)",     "Mega Slowbro",           "wiki/03_Pokedex/Kanto/0080_Slowbro.md"),
    # Alolan
    ("Rattata%20(Alolan%20Form)",   "Rattata (Forma Alola)",  "wiki/03_Pokedex/Kanto/0019_Rattata.md"),
    ("Raticate%20(Alolan%20Form)",  "Raticate (Forma Alola)", "wiki/03_Pokedex/Kanto/0020_Raticate.md"),
    ("Raichu%20(Alolan%20Form)",    "Raichu (Forma Alola)",   "wiki/03_Pokedex/Kanto/0026_Raichu.md"),
    ("Sandshrew%20(Alolan%20Form)", "Sandshrew (Forma Alola)","wiki/03_Pokedex/Kanto/0027_Sandshrew.md"),
    ("Sandslash%20(Alolan%20Form)", "Sandslash (Forma Alola)","wiki/03_Pokedex/Kanto/0028_Sandslash.md"),
    ("Vulpix%20(Alolan%20Form)",    "Vulpix (Forma Alola)",   "wiki/03_Pokedex/Kanto/0037_Vulpix.md"),
    ("Ninetales%20(Alolan%20Form)", "Ninetales (Forma Alola)","wiki/03_Pokedex/Kanto/0038_Ninetales.md"),
    ("Diglett%20(Alolan%20Form)",   "Diglett (Forma Alola)",  "wiki/03_Pokedex/Kanto/0050_Diglett.md"),
    ("Dugtrio%20(Alolan%20Form)",   "Dugtrio (Forma Alola)",  "wiki/03_Pokedex/Kanto/0051_Dugtrio.md"),
    ("Meowth%20(Alolan%20Form)",    "Meowth (Forma Alola)",   "wiki/03_Pokedex/Kanto/0052_Meowth.md"),
    ("Persian%20(Alolan%20Form)",   "Persian (Forma Alola)",  "wiki/03_Pokedex/Kanto/0053_Persian.md"),
    ("Geodude%20(Alolan%20Form)",   "Geodude (Forma Alola)",  "wiki/03_Pokedex/Kanto/0074_Geodude.md"),
    ("Graveler%20(Alolan%20Form)",  "Graveler (Forma Alola)", "wiki/03_Pokedex/Kanto/0075_Graveler.md"),
    ("Golem%20(Alolan%20Form)",     "Golem (Forma Alola)",    "wiki/03_Pokedex/Kanto/0076_Golem.md"),
    ("Grimer%20(Alolan%20Form)",    "Grimer (Forma Alola)",   "wiki/03_Pokedex/Kanto/0088_Grimer.md"),
    ("Muk%20(Alolan%20Form)",       "Muk (Forma Alola)",      "wiki/03_Pokedex/Kanto/0089_Muk.md"),
    ("Exeggutor%20(Alolan%20Form)", "Exeggutor (Forma Alola)","wiki/03_Pokedex/Kanto/0103_Exeggutor.md"),
    ("Marowak%20(Alolan%20Form)",   "Marowak (Forma Alola)",  "wiki/03_Pokedex/Kanto/0105_Marowak.md"),
    # Galarian
    ("Meowth%20(Galarian%20Form)",  "Meowth (Forma Galar)",   "wiki/03_Pokedex/Kanto/0052_Meowth.md"),
    ("Farfetch%27d%20(Galarian%20Form)", "Farfetch'd (Forma Galar)", "wiki/03_Pokedex/Kanto/0083_Farfetchd.md"),
    ("Mr.%20Mime%20(Galarian%20Form)",   "Mr. Mime (Forma Galar)",   "wiki/03_Pokedex/Kanto/0122_Mr_Mime.md"),

    # ── JOHTO ──────────────────────────────────────────────────────────────────
    ("Ampharos%20(Mega%20Form)",    "Mega Ampharos",          "wiki/03_Pokedex/Johto/0181_Ampharos.md"),
    ("Steelix%20(Mega%20Form)",     "Mega Steelix",           "wiki/03_Pokedex/Johto/0208_Steelix.md"),
    ("Scizor%20(Mega%20Form)",      "Mega Scizor",            "wiki/03_Pokedex/Johto/0212_Scizor.md"),
    ("Heracross%20(Mega%20Form)",   "Mega Heracross",         "wiki/03_Pokedex/Johto/0214_Heracross.md"),
    ("Houndoom%20(Mega%20Form)",    "Mega Houndoom",          "wiki/03_Pokedex/Johto/0229_Houndoom.md"),
    ("Tyranitar%20(Mega%20Form)",   "Mega Tyranitar",         "wiki/03_Pokedex/Johto/0248_Tyranitar.md"),
    # Galarian — il file base è in Kanto ma Slowpoke/Slowbro/Slowking hanno note Johto
    ("Slowpoke%20(Galarian%20Form)","Slowpoke (Forma Galar)",  "wiki/03_Pokedex/Kanto/0079_Slowpoke.md"),
    ("Slowbro%20(Galarian%20Form)", "Slowbro (Forma Galar)",   "wiki/03_Pokedex/Kanto/0080_Slowbro.md"),
    ("Slowking%20(Galarian%20Form)","Slowking (Forma Galar)",  "wiki/03_Pokedex/Johto/0199_Slowking.md"),
    ("Corsola%20(Galarian%20Form)", "Corsola (Forma Galar)",   "wiki/03_Pokedex/Johto/0222_Corsola.md"),

    # ── HOENN ──────────────────────────────────────────────────────────────────
    ("Sceptile%20(Mega%20Form)",    "Mega Sceptile",          "wiki/03_Pokedex/Hoenn/0254_Sceptile.md"),
    ("Blaziken%20(Mega%20Form)",    "Mega Blaziken",          "wiki/03_Pokedex/Hoenn/0257_Blaziken.md"),
    ("Swampert%20(Mega%20Form)",    "Mega Swampert",          "wiki/03_Pokedex/Hoenn/0260_Swampert.md"),
    ("Gardevoir%20(Mega%20Form)",   "Mega Gardevoir",         "wiki/03_Pokedex/Hoenn/0282_Gardevoir.md"),
    ("Sableye%20(Mega%20Form)",     "Mega Sableye",           "wiki/03_Pokedex/Hoenn/0302_Sableye.md"),
    ("Mawile%20(Mega%20Form)",      "Mega Mawile",            "wiki/03_Pokedex/Hoenn/0303_Mawile.md"),
    ("Aggron%20(Mega%20Form)",      "Mega Aggron",            "wiki/03_Pokedex/Hoenn/0306_Aggron.md"),
    ("Medicham%20(Mega%20Form)",    "Mega Medicham",          "wiki/03_Pokedex/Hoenn/0308_Medicham.md"),
    ("Manectric%20(Mega%20Form)",   "Mega Manectric",         "wiki/03_Pokedex/Hoenn/0310_Manectric.md"),
    ("Sharpedo%20(Mega%20Form)",    "Mega Sharpedo",          "wiki/03_Pokedex/Hoenn/0319_Sharpedo.md"),
    ("Camerupt%20(Mega%20Form)",    "Mega Camerupt",          "wiki/03_Pokedex/Hoenn/0323_Camerupt.md"),
    ("Altaria%20(Mega%20Form)",     "Mega Altaria",           "wiki/03_Pokedex/Hoenn/0334_Altaria.md"),
    ("Banette%20(Mega%20Form)",     "Mega Banette",           "wiki/03_Pokedex/Hoenn/0354_Banette.md"),
    ("Absol%20(Mega%20Form)",       "Mega Absol",             "wiki/03_Pokedex/Hoenn/0359_Absol.md"),
    ("Glalie%20(Mega%20Form)",      "Mega Glalie",            "wiki/03_Pokedex/Hoenn/0362_Glalie.md"),
    ("Salamence%20(Mega%20Form)",   "Mega Salamence",         "wiki/03_Pokedex/Hoenn/0373_Salamence.md"),
    ("Metagross%20(Mega%20Form)",   "Mega Metagross",         "wiki/03_Pokedex/Hoenn/0376_Metagross.md"),
    ("Latias%20(Mega%20Form)",      "Mega Latias",            "wiki/03_Pokedex/Hoenn/0380_Latias.md"),
    ("Latios%20(Mega%20Form)",      "Mega Latios",            "wiki/03_Pokedex/Hoenn/0381_Latios.md"),
    ("Kyogre%20(Primal%20Form)",    "Kyogre Primordiale",     "wiki/03_Pokedex/Hoenn/0382_Kyogre.md"),
    ("Groudon%20(Primal%20Form)",   "Groudon Primordiale",    "wiki/03_Pokedex/Hoenn/0383_Groudon.md"),
    ("Rayquaza%20(Mega%20Form)",    "Mega Rayquaza",          "wiki/03_Pokedex/Hoenn/0384_Rayquaza.md"),
    ("Deoxys%20(Attack%20Form)",    "Deoxys (Forma Attacco)", "wiki/03_Pokedex/Hoenn/0386_Deoxys.md"),
    ("Deoxys%20(Defense%20Form)",   "Deoxys (Forma Difesa)",  "wiki/03_Pokedex/Hoenn/0386_Deoxys.md"),
    ("Deoxys%20(Speed%20Form)",     "Deoxys (Forma Velocità)","wiki/03_Pokedex/Hoenn/0386_Deoxys.md"),

    # ── SINNOH ─────────────────────────────────────────────────────────────────
    ("Lopunny%20(Mega%20Form)",     "Mega Lopunny",           "wiki/03_Pokedex/Sinnoh/0428_Lopunny.md"),
    ("Lucario%20(Mega%20Form)",     "Mega Lucario",           "wiki/03_Pokedex/Sinnoh/0448_Lucario.md"),
    ("Abomasnow%20(Mega%20Form)",   "Mega Abomasnow",         "wiki/03_Pokedex/Sinnoh/0460_Abomasnow.md"),
    ("Garchomp%20(Mega%20Form)",    "Mega Garchomp",          "wiki/03_Pokedex/Sinnoh/0445_Garchomp.md"),
    ("Gallade%20(Mega%20Form)",     "Mega Gallade",           "wiki/03_Pokedex/Sinnoh/0475_Gallade.md"),
    ("Giratina%20(Origin%20Form)",  "Giratina (Forma Origine)","wiki/03_Pokedex/Sinnoh/0487_Giratina.md"),
    ("Shaymin%20(Sky%20Form)",      "Shaymin (Forma Cielo)",  "wiki/03_Pokedex/Sinnoh/0492_Shaymin.md"),
    ("Rotom%20(Heat%20Form)",       "Rotom Calore",           "wiki/03_Pokedex/Sinnoh/0479_Rotom.md"),
    ("Rotom%20(Wash%20Form)",       "Rotom Lavaggio",         "wiki/03_Pokedex/Sinnoh/0479_Rotom.md"),
    ("Rotom%20(Fan%20Form)",        "Rotom Ventola",          "wiki/03_Pokedex/Sinnoh/0479_Rotom.md"),
    ("Rotom%20(Frost%20Form)",      "Rotom Gelo",             "wiki/03_Pokedex/Sinnoh/0479_Rotom.md"),
    ("Rotom%20(Mow%20Form)",        "Rotom Falcia",           "wiki/03_Pokedex/Sinnoh/0479_Rotom.md"),
    # Wormadam forme extra nella pagina base
    ("Wormadam%20(Ground%20Form)",  "Wormadam (Forma Terra)", "wiki/03_Pokedex/Sinnoh/0413_Wormadam.md"),
    ("Wormadam%20(Steel%20Form)",   "Wormadam (Forma Acciaio)","wiki/03_Pokedex/Sinnoh/0413_Wormadam.md"),
]


def fetch_json(url_encoded):
    url = f"{BASE_URL}/{url_encoded}.json"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        resp = urllib.request.urlopen(req, timeout=15)
        return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"  ERRORE {url_encoded}: {e}")
        return None

def translate_type(t):
    return TYPE_IT.get(t, t)

def build_form_section(section_title, data):
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

    str_val = f"{data.get('Strength', 0)}/{data.get('MaxStrength', 0)}"
    dex_val = f"{data.get('Dexterity', 0)}/{data.get('MaxDexterity', 0)}"
    vit_val = f"{data.get('Vitality', 0)}/{data.get('MaxVitality', 0)}"
    spe_val = f"{data.get('Special', 0)}/{data.get('MaxSpecial', 0)}"
    ins_val = f"{data.get('Insight', 0)}/{data.get('MaxInsight', 0)}"

    moves_by_rank = {}
    for move in data.get("Moves", []):
        rank = move.get("Learned", "Unknown")
        mn = move.get("Name", "")
        if mn:
            slug_m = mn.replace(" ", "_").replace("-", "_").replace("'", "")
            moves_by_rank.setdefault(rank, []).append(f"[[{slug_m}|{mn}]]")
    moves_md = ""
    for rank in RANK_ORDER:
        if rank in moves_by_rank:
            moves_md += f"- **{rank}:** {', '.join(moves_by_rank[rank])}\n"

    id_str = f" (#{dex_id})" if dex_id else ""
    return f"""
---

## {section_title}{id_str}

**Type:** {types_it}
**Abilities:** {abilities_str}
**Base HP:** {hp}

| Attribute | Base / Limit |
|---|---|
| **Strength** | {str_val} |
| **Dexterity** | {dex_val} |
| **Vitality** | {vit_val} |
| **Special** | {spe_val} |
| **Insight** | {ins_val} |

### Mosse

{moves_md}"""


# --- ESECUZIONE ---
print("Fase 1: Fetch dati e append sezioni nei file base...")
appended = 0
skipped = 0

for url_enc, section_title, base_path in FORMS:
    if not os.path.exists(base_path):
        print(f"  FILE BASE NON TROVATO: {base_path}")
        skipped += 1
        continue

    # Evita duplicati: controlla se la sezione è già presente
    with open(base_path, "r", encoding="utf-8") as f:
        content = f.read()
    if f"## {section_title}" in content:
        print(f"  GIA' PRESENTE: {section_title} in {os.path.basename(base_path)}")
        continue

    data = fetch_json(url_enc)
    if not data:
        skipped += 1
        time.sleep(0.1)
        continue

    section = build_form_section(section_title, data)
    with open(base_path, "a", encoding="utf-8") as f:
        f.write(section)

    appended += 1
    print(f"  OK: {section_title} -> {os.path.basename(base_path)}")
    time.sleep(0.12)

print(f"\nFase 1 completata. Sezioni aggiunte: {appended}, Saltate: {skipped}")

# --- FASE 2: rimuovi i file separati ---
print("\nFase 2: Rimozione file separati...")
to_remove = []
patterns = [
    "wiki/03_Pokedex/Kanto/*M1_*.md",
    "wiki/03_Pokedex/Kanto/*M2_*.md",
    "wiki/03_Pokedex/Kanto/*A_*Form.md",
    "wiki/03_Pokedex/Kanto/*G_*Form.md",
    "wiki/03_Pokedex/Kanto/0080M_*.md",
    "wiki/03_Pokedex/Johto/*M1_*.md",
    "wiki/03_Pokedex/Johto/*G_*.md",
    "wiki/03_Pokedex/Hoenn/*M1_*.md",
    "wiki/03_Pokedex/Hoenn/*F[0-9]_*.md",
    "wiki/03_Pokedex/Sinnoh/*M1_*.md",
    "wiki/03_Pokedex/Sinnoh/0413F*.md",
    "wiki/03_Pokedex/Sinnoh/0479F*.md",
    "wiki/03_Pokedex/Sinnoh/0487F*.md",
    "wiki/03_Pokedex/Sinnoh/0492F*.md",
]
import glob as _glob
for p in patterns:
    to_remove.extend(_glob.glob(p))
to_remove = sorted(set(to_remove))

for f in to_remove:
    os.remove(f)
    print(f"  Rimosso: {f}")

print(f"\nFase 2 completata. File rimossi: {len(to_remove)}")
