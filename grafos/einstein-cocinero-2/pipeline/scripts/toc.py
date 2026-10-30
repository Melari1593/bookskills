"""Lee el índice del libro (trabajo/texto.txt) y escribe trabajo/toc.json con capítulos y secciones (título y página impresa)."""
import re, json
T = open('trabajo/texto.txt', encoding='utf-8').read()
s = T.index('ÍNDICE\n', T.index('A SU COCINERO 2')); e = T.index('AGRADECIMIENTOS', s); toc = T[s:e]
chs = {}
for m in re.finditer(r'^\s*(\d{1,2})\s+(.+?)\s*(?:\.\s*)*([\d ]{2,5})\s*$', toc, re.M):
    chs.setdefault(int(m.group(1)), (m.group(2).strip(' .'), m.end()))
P = {1:23,2:63,3:111,4:147,5:197,6:229,7:255,8:303,9:339,10:383,11:407}
secs = []
for n in sorted(chs):
    t, b = chs[n]
    nxt = re.search(r'^\s*(\d{1,2})\s+\S', toc[b:], re.M)
    body = toc[b: b + (nxt.start() if nxt else len(toc) - b)]
    if n == 10: body = body.split('índice analítico')[0]
    body = re.sub(r'-\n\s*', '', body); body = re.sub(r'\s+', ' ', body)
    for m in re.finditer(r'\s*(.+?),\s*(\d{2,3})\s*[;.]', body):
        tt, pg = m.group(1).strip(), int(m.group(2))
        if P[n] <= pg < P[n+1] and not tt.startswith('¿Qué 212') and not any(x['title'] == tt for x in secs):
            secs.append({"ch": n, "title": tt, "page": pg})
for t, p in [("¿Qué ha estado fumando?", 333), ("Cerditos kosher", 334), ("Tomaré vainilla", 335)]:
    if not any(x['title'] == t for x in secs): secs.append({"ch": 8, "title": t, "page": p})
fix = {"E1 segundo plátano": "El segundo plátano", "¿Es lightel aceite lighfí": "¿Es light el aceite light?", "Grasas trans: ¿me lo trans cribe?": "Grasas trans: ¿me lo transcribe?"}
for x in secs: x['title'] = fix.get(x['title'], x['title'])
secs.sort(key=lambda x: (x['ch'], x['page']))
json.dump({"chapters": [{"num": n, "title": chs[n][0], "page": P[n]} for n in sorted(chs)], "sections": secs}, open('trabajo/toc.json', 'w'), ensure_ascii=False, indent=1)
from collections import Counter; print(len(secs), Counter(x['ch'] for x in secs))
