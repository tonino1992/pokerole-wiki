import os
import re
import urllib.request
import urllib.parse
import json
import time

moves_dir = 'wiki/05_Mosse_e_Abilita/Mosse'

TYPE_MAP = {
    "Normal": "Normale", "Fire": "Fuoco", "Water": "Acqua",
    "Electric": "Elettro", "Grass": "Erba", "Ice": "Ghiaccio",
    "Fighting": "Lotta", "Poison": "Veleno", "Ground": "Terra",
    "Flying": "Volante", "Psychic": "Psico", "Bug": "Insetto",
    "Rock": "Roccia", "Ghost": "Spettro", "Dragon": "Drago",
    "Dark": "Buio", "Steel": "Acciaio", "Fairy": "Folletto",
    "Typeless": "Senza Tipo",
}

# Parole chiave di gioco da proteggere nella traduzione dell'Effect
KEYWORDS = [
    "Will Points", "Will Point", "Dice Pool", "Dice", "Base HP",
    "Strength", "Dexterity", "Vitality", "Special", "Insight",
    "HP", "Will", "Accuracy", "Damage", "Target", "Effect",
    "Fight", "Evasion", "Channel", "Alert", "Athletic",
    "Round", "Rounds", "Turn", "Clash", "STAB", "Critical Hit",
    "Burn", "Paralysis", "Sleep", "Poison", "Frozen", "Confused",
    "Confusion", "Flinched", "Flinch", "Disabled",
    "Starter", "Beginner", "Amateur", "Ace", "Pro", "Master", "Champion",
    "Physical", "Support", "Foe", "Ally", "Battlefield", "Self",
]

def google_translate(text):
    if not text or text.strip() in ['-', 'N/A', '']:
        return text
    url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=it&dt=t&q={urllib.parse.quote(text)}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req, timeout=15)
        result = json.loads(response.read().decode('utf-8'))
        return ''.join([part[0] for part in result[0] if part[0]])
    except Exception as e:
        print(f"  [ERR] {e}")
        return text

def protect_and_translate(text):
    """Protegge wikilink e keyword di gioco, traduce, poi ripristina."""
    if not text or text.strip() in ['-', 'N/A', '']:
        return text
    placeholders = {}
    protected = text
    idx = 0
    # Proteggi wikilink [[...]]
    for link in re.findall(r'\[\[.*?\]\]', text):
        ph = f'ZZZPH{idx}ZZZ'
        placeholders[ph] = link
        protected = protected.replace(link, ph, 1)
        idx += 1
    # Proteggi keywords (ordina per lunghezza decrescente per evitare sostituzioni parziali)
    for kw in sorted(KEYWORDS, key=len, reverse=True):
        pattern = re.compile(r'\b' + re.escape(kw) + r'\b')
        if pattern.search(protected):
            ph = f'ZZZPH{idx}ZZZ'
            placeholders[ph] = kw
            protected = pattern.sub(ph, protected)
            idx += 1
    # Traduci
    translated = google_translate(protected)
    # Ripristina
    for ph, original in placeholders.items():
        translated = translated.replace(ph, original)
    # Correggi nomi tipo residui
    for en, it in TYPE_MAP.items():
        translated = re.sub(r'\b' + re.escape(en) + r'\b', it, translated)
    return translated

def fix_types_in_text(text):
    for en, it in TYPE_MAP.items():
        text = re.sub(r'\b' + re.escape(en) + r'\b', it, text)
    return text

files = sorted([f for f in os.listdir(moves_dir) if f.endswith('.md')])
total = len(files)
print(f"File da elaborare: {total}")

for i, filename in enumerate(files, 1):
    filepath = os.path.join(moves_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Salta se già tradotto
    if 'locale: it' in content:
        print(f'[{i}/{total}] Skip (già tradotto): {filename}')
        continue

    original = content

    # 1. Traduci tipo nell'header *Type | Category*
    def translate_header(m):
        it_type = TYPE_MAP.get(m.group(1), m.group(1))
        return f'*{it_type} | {m.group(2)}*'
    content = re.sub(r'\*([A-Za-z]+) \| ([A-Za-z ]+)\*', translate_header, content)

    # 2. Aggiorna tipo nel frontmatter tags
    def translate_tag(m):
        tag_type = m.group(1).capitalize()
        it_type = TYPE_MAP.get(tag_type, m.group(1)).lower()
        return f'[move, {it_type}, {m.group(2)}]'
    content = re.sub(r'\[move, ([a-z]+), ([a-z ]+)\]', translate_tag, content)

    # 3. Traduci Effect
    effect_match = re.search(r'- \*\*Effect:\*\* (.+)', content)
    if effect_match:
        orig_effect = effect_match.group(1)
        new_effect = protect_and_translate(orig_effect)
        content = content.replace(f'- **Effect:** {orig_effect}', f'- **Effect:** {new_effect}', 1)

    # 4. Traduci Description (blockquote)
    desc_match = re.search(r'^> (.+)$', content, re.MULTILINE)
    if desc_match:
        orig_desc = desc_match.group(1)
        new_desc = protect_and_translate(orig_desc)
        content = content.replace(f'> {orig_desc}', f'> {new_desc}', 1)

    # 5. Aggiungi marker traduzione nel frontmatter
    content = content.replace('category: Move', 'category: Move\nlocale: it', 1)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    print(f'[{i}/{total}] OK {filename}')
    time.sleep(0.25)

print(f'\nCompletato! {total} file elaborati.')
