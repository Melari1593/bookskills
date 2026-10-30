"""Corta el cuerpo del libro por secciones (búsqueda secuencial del título) y escribe lotes para los agentes que
resumen con palabras propias: trabajo/lotes/lote_N.md. Añade ids n.k a trabajo/toc.json."""
import json, re, os, unicodedata
T = open('trabajo/texto.txt', encoding='utf-8').read(); pages = T.split('\f'); LP = [p.split('\n') for p in pages]
d = json.load(open('trabajo/toc.json')); secs = d['sections']
def norm(s): return re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFKD', s).encode('ascii','ignore').decode().lower())
def match(l, t):
    a, b = norm(l), norm(t); return a and (a == b or (len(a) > 8 and b.startswith(a)))
phys = next(i for i, p in enumerate(LP) if i > 10 and any(norm(l) == norm('Hielo albino') for l in p))
cur = (phys, 0)
for s in secs:
    found = None; pi = cur[0]
    while pi < len(LP) and not found:
        for j in range(cur[1] if pi == cur[0] else 0, len(LP[pi])):
            if match(LP[pi][j], s['title']): found = (pi, j); break
        pi += 1
    s['_start'] = found or cur; s['found'] = bool(found)
    if found: cur = (found[0], found[1] + 1)
print("no encontradas:", [s['title'] for s in secs if not s['found']])
for i, s in enumerate(secs):
    a = s['_start']; b = secs[i+1]['_start'] if i+1 < len(secs) else (len(LP) - 1, 0)
    txt = []
    for pi in range(a[0], b[0] + 1):
        L = LP[pi]; txt += L[(a[1] if pi == a[0] else 0):(b[1] if pi == b[0] else len(L))]
    s['text'] = re.sub(r'-\n\s*', '', '\n'.join(txt))
for k, s in enumerate(secs): s['id'] = f"{s['ch']}.{sum(1 for x in secs[:k] if x['ch'] == s['ch']) + 1}"
os.makedirs('trabajo/lotes', exist_ok=True)
for k, chs in {1: [1, 2], 2: [3, 4], 3: [5, 6], 4: [7, 8], 5: [9, 10]}.items():
    out = []
    for c in d['chapters']:
        if c['num'] in chs:
            out.append(f"\n\n======== CAPÍTULO {c['num']}: {c['title']}")
            out += [f"\n==== SECCIÓN id={s['id']} (p. {s['page']}): {s['title']}\n{s['text']}" for s in secs if s['ch'] == c['num']]
    open(f'trabajo/lotes/lote_{k}.md', 'w').write('\n'.join(out)); print(k, len(' '.join(out).split()))
for s in secs: s.pop('_start'); s.pop('text')
json.dump(d, open('trabajo/toc.json', 'w'), ensure_ascii=False, indent=1)
