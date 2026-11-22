"""Agrega las alertas de evidencia (campo caution) al grafo de The Five Elements Cookbook,
regenera el HTML con el recuadro «Atención» y copia todo a la skill five-elements-cookbook-grafo."""
import json
import re
import shutil
from pathlib import Path

from alertas import ALERTAS

REPO = Path('/home/claude/bookskills')
SRC = REPO / 'grafos/five-elements-cookbook'
SKILL = REPO / '.claude/skills/five-elements-cookbook-grafo'

g = json.loads((SRC / 'grafo_five_elements_cookbook.json').read_text())
secs = {s['num']: s for c in g['chapters'] for s in c['sections']}
missing = [k for k in ALERTAS if k not in secs]
assert not missing, missing
for s in secs.values():
    s.pop('caution', None)
for k, v in ALERTAS.items():
    assert '"' not in v, k
    secs[k]['caution'] = v
g['meta']['subtitle'] = ('Zoey Xinyi Gong · Fundamentos de la terapia alimentaria china, 50 hierbas y 55 recetas, '
                         'con sus prerrequisitos y alertas de evidencia (2026-11-21)')
text = json.dumps(g, ensure_ascii=False, indent=1)

html = (SRC / 'grafo_five_elements_cookbook.html').read_text()
m = re.search(r'const GRAPH\s*=\s*', html)
end = html.find('};\n', m.end()) + 1
html = html[:m.end()] + json.dumps(g, ensure_ascii=False) + html[end:]
css = ('.caution{font-size:.88rem;line-height:1.45;background:#FBF1DC;border-left:3px solid #B07A12;'
       'color:#4A3A12;padding:8px 10px;margin:0 0 12px;border-radius:0 3px 3px 0}')
if '.caution{' not in html:
    html = html.replace('.formula{', css + '\n.formula{', 1)
old_add = 'desc:s.summary,order:(ci+1)*1000+si+1});'
if 'caution:s.caution' not in html:
    assert old_add in html
    html = html.replace(old_add, 'desc:s.summary,caution:s.caution,order:(ci+1)*1000+si+1});', 1)
old_render = 'if(n.desc) html+=`<p class="p-desc">${esc(n.desc)}</p>`;'
if 'class="caution"' not in html:
    assert old_render in html
    html = html.replace(old_render, old_render +
                        '\n  if(n.caution) html+=`<p class="caution"><strong>Atención:</strong> ${esc(n.caution)}</p>`;', 1)

(SRC / 'grafo_five_elements_cookbook.json').write_text(text + '\n')
(SRC / 'grafo_five_elements_cookbook.html').write_text(html)
(SKILL / 'references').mkdir(parents=True, exist_ok=True)
(SKILL / 'assets').mkdir(parents=True, exist_ok=True)
(SKILL / 'references/grafo.json').write_text(text + '\n')
(SKILL / 'references/alertas.json').write_text(
    json.dumps(dict(sorted(ALERTAS.items(), key=lambda kv: tuple(map(int, kv[0].split('.'))))),
               ensure_ascii=False, indent=1) + '\n')
shutil.copy(SRC / 'grafo_five_elements_cookbook.html', SKILL / 'assets/grafo_five_elements_cookbook.html')

for p in [SRC / 'grafo_five_elements_cookbook.json', SKILL / 'references/grafo.json', SKILL / 'references/alertas.json']:
    json.loads(p.read_text())
m = re.search(r'const GRAPH\s*=\s*', html)
json.loads(html[m.end():html.find('};\n', m.end()) + 1])
print('OK', len(ALERTAS), 'alertas;', sum(1 for s in secs.values() if s.get('caution')), 'secciones con caution')
