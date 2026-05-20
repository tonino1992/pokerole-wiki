"""
Fix per i Pokémon Kalos non generati dallo script principale:
- Flabébé (#669): file nel repo è 'Flabebe.json' (senza accenti)
- Zygarde (#718): file nel repo è 'Zygarde 50%.json', forme '10%' e '100%'
"""
import os, json, urllib.request, time

BASE_URL = "https://raw.githubusercontent.com/Pokerole-Software-Development/Pokerole-Data/master/v2.0/Pokedex"
md_dir = "wiki/03_Pokedex/Kalos"

RANK_ORDER = ["Starter", "Beginner", "Amateur", "Ace", "Pro", "Master", "Champion"]
IMG_FORM = '<img src="../../assets/images/pokemon/forms/{fname}" align="right" width="200" style="margin-left:16px;margin-bottom:8px;">'

TYPE_IT = {
    "Normal": "Normale", "Fire": "Fuoco", "Water": "Acqua",
    "Grass": "Erba", "Electric": "Elettro", "Ice": "Ghiaccio",
    "Fighting": "Lotta", "Poison": "Veleno", "Ground": "Terra",
    "Flying": "Volante", "Psychic": "Psico", "Bug": "Insetto",
    "Rock": "Roccia", "Ghost": "Spettro", "Dragon": "Drago",
    "Dark": "Buio", "Steel": "Acciaio", "Fairy": "Folletto",
}

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


def make_page(display_name, poke_id, data, form_sections=""):
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
    name_tag = display_name.lower().replace(" ","").replace("-","").replace(".","").replace("'","").replace("é","e")
    tags = [name_tag, "kalos"] + types_lower
    img_path = f"assets/images/pokemon/{poke_id:03d}.png"
    img_tag = f'<img src="../../assets/images/pokemon/{poke_id:03d}.png" align="right" width="220" style="margin-left:20px;margin-bottom:8px;">'

    slug_name = display_name.replace(" ", "_").replace("é", "e").replace("'","").replace(".","").replace("-","_")
    filename = f"{dex_id}_{slug_name}.md"
    filepath = os.path.join(md_dir, filename)

    md = f"""---
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

{form_sections}
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"  Creato {filename}")
    return filename


# ── Flabébé (#669) ──────────────────────────────────────────────────────────
print("Fixing Flabebe (#669)...")
data = fetch_json("Flabebe")
if data:
    make_page("Flabébé", 669, data)
else:
    print("  ERRORE: impossibile fetchare Flabebe")

time.sleep(0.2)

# ── Zygarde (#718) ──────────────────────────────────────────────────────────
print("\nFixing Zygarde (#718)...")
data_50 = fetch_json("Zygarde%2050%25")
time.sleep(0.15)
data_10 = fetch_json("Zygarde%2010%25")
time.sleep(0.15)
data_100 = fetch_json("Zygarde%20100%25")
time.sleep(0.15)

if data_50:
    form_sections = ""
    if data_10:
        form_sections += build_form_section("Zygarde (Forma 10%)", data_10)
    if data_100:
        form_sections += build_form_section("Zygarde (Forma 100%)", data_100)
    make_page("Zygarde", 718, data_50, form_sections)
else:
    print("  ERRORE: impossibile fetchare Zygarde 50%")

print("\nFix completato.")
