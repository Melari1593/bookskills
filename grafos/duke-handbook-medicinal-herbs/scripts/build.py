"""Build the knowledge graph of Duke's Handbook of Medicinal Herbs (2nd ed., 2002) from data.json.
Outputs (in out/): nodes.csv, edges.csv, graph.json, graph.graphml, compact.json (for the HTML), validation.json.
Usage: python3 scripts/build.py data.json out/"""
import csv, json, os, re, sys, unicodedata
from collections import Counter
from xml.sax.saxutils import escape

d = json.load(open(sys.argv[1], encoding='utf-8'))
out = sys.argv[2]; os.makedirs(out, exist_ok=True)
DOC = 'Duke JA et al. Handbook of Medicinal Herbs, 2nd ed. CRC Press, 2002'
OFFSET = 23  # printed page = pdf page - 23 (constant for all monographs)

def slug(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')

def clean_src(s):
    m = re.match(r'^[.\s]*([A-Z0-9]{2,4})', s)
    return m.group(1) if m else None

SAFETY = {'X': 'X: no tomar sin guía experta', '+': '+: menos segura que el café',
          '++': '++: tan segura como el café', '+++': '+++: más segura que el café'}
SCORE = {'f': 'folclor sin respaldo', '1': 'fitoquímico o extracto en estudios experimentales (no clínicos)',
         '2': 'extracto o té con estudios, o aprobación de Comisión E o TRAMIL', '3': 'ensayos clínicos con la planta'}
seg_id = {'X': 'seg:x', '+': 'seg:1', '++': 'seg:2', '+++': 'seg:3'}

nodes, edges = {}, []
def add_node(nid, **kw):
    if nid not in nodes: nodes[nid] = dict(id=nid, **kw)
    return nid

for s, lab in SAFETY.items():
    add_node(seg_id[s], label=lab, type='Seguridad', description=lab, source=DOC, chapter='Introduction', section='Safety score', page='')

seen_herb = Counter()
compact = []
for h in d['herbs']:
    base = 'hierba:' + slug(h['scientific'].split(' (')[0] + ' ' + h['common'].split(',')[0])
    seen_herb[base] += 1
    hid = base if seen_herb[base] == 1 else f'{base}-{seen_herb[base]}'
    page = h['pdf_page'] - OFFSET
    sec = h['sections']
    add_node(hid, label=h['common'].title(), type='Hierba', scientific=h['scientific'], safety=h['safety'],
             safety_raw=h.get('safety_raw', ''), qualifier=h.get('qualifier', ''),
             description=('Sinónimos: ' + sec['Synonyms']) if sec.get('Synonyms') else '',
             dosages=sec.get('Dosages', ''), downsides=sec.get('Contraindications, Interactions, and Side Effects', ''),
             extracts=sec.get('Extracts', ''), notes=h.get('notes', ''),
             source=DOC, chapter='Catalog of Herbs (A to Z)', section=h['common'], page=page)
    edges.append(dict(source=hid, target=seg_id[h['safety']], relation='calificacion_seguridad',
                      evidence=f"{h['common']} ({h['scientific']}) {h.get('safety_raw', h['safety'])}",
                      source_document=DOC, page=page, inferred=False, score='', refs=''))
    items_c = []
    for kind, rel, ntype, prefix in (('activities', 'tiene_actividad', 'Actividad', 'act'), ('indications', 'indicada_para', 'Indicación', 'ind')):
        for it in h[kind]:
            nm = it['name']
            if not nm or len(nm) > 60: continue
            tid = add_node(f'{prefix}:{slug(nm)}', label=nm, type=ntype, description='', source=DOC,
                           chapter='Catalog of Herbs (A to Z)', section=('Activities' if prefix == 'act' else 'Indications'), page='')
            refs = sorted(set(filter(None, (clean_src(s) for s in it['sources']))))
            edges.append(dict(source=hid, target=tid, relation=rel,
                              evidence=f"{nm} ({it['score']}; {'; '.join(it['sources'])})",
                              source_document=DOC, page=page, inferred=False, score=it['score'], refs=';'.join(refs)))
            items_c.append([0 if prefix == 'act' else 1, tid, it['score'], refs])
    compact.append({'id': hid, 'c': h['common'], 's': h['scientific'], 'q': h.get('qualifier', ''), 'z': h['safety'],
                    'zr': h.get('safety_raw', ''), 'p': page, 'n': h.get('notes', '')[:1500],
                    'd': sec.get('Dosages', ''), 'k': sec.get('Contraindications, Interactions, and Side Effects', ''),
                    'e': sec.get('Extracts', ''), 'y': sec.get('Synonyms', ''), 'i': items_c})

use = Counter(e['target'] for e in edges if e['relation'] in ('tiene_actividad', 'indicada_para'))
for nid, n in nodes.items():
    if n['type'] in ('Actividad', 'Indicación'):
        n['description'] = f"Citada en {use[nid]} monografías"

ids = [n['id'] for n in nodes.values()]
deg = Counter()
for e in edges: deg.update([e['source'], e['target']])
val = {
    'nodes': len(nodes), 'edges': len(edges),
    'node_types': Counter(n['type'] for n in nodes.values()),
    'relations': Counter(e['relation'] for e in edges),
    'score_distribution': Counter(e['score'] for e in edges if e['score']),
    'safety_distribution': Counter(n['safety'] for n in nodes.values() if n['type'] == 'Hierba'),
    'duplicate_ids': len(ids) - len(set(ids)),
    'orphans': [i for i in ids if deg[i] == 0],
    'edges_missing_endpoint': sum(1 for e in edges if e['source'] not in nodes or e['target'] not in nodes),
    'edges_missing_page': sum(1 for e in edges if e['page'] in ('', None)),
    'herbs_without_items': [n['label'] for n in nodes.values() if n['type'] == 'Hierba' and deg[n['id']] <= 1],
    'duplicate_herb_ids_renamed': [k for k, v in seen_herb.items() if v > 1],
}
json.dump(val, open(os.path.join(out, 'validation.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1, default=dict)

NF = ['id', 'label', 'type', 'description', 'source', 'chapter', 'section', 'page', 'scientific', 'safety', 'safety_raw', 'qualifier', 'dosages', 'downsides', 'extracts']
with open(os.path.join(out, 'nodes.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=NF, extrasaction='ignore'); w.writeheader()
    for n in nodes.values(): w.writerow(n)
EF = ['source', 'target', 'relation', 'evidence', 'source_document', 'page', 'inferred', 'score', 'refs']
with open(os.path.join(out, 'edges.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=EF); w.writeheader()
    for e in edges: w.writerow(e)
meta = {'title': 'Handbook of Medicinal Herbs, 2nd ed.', 'authors': 'James A. Duke, Mary Jo Bogenschutz-Godwin, Judi duCellier, Peggy-Ann K. Duke',
        'publisher': 'CRC Press', 'year': 2002, 'isbn': '0-8493-1284-1', 'language': 'en',
        'scope': 'Catalog of Herbs (A to Z), pp. 1-814; Reference Abbreviations pp. 815-820',
        'scales': {'safety': SAFETY, 'efficacy': SCORE}, 'page_note': 'page = número impreso del libro (página del PDF - 23)'}
json.dump({'metadata': meta, 'nodes': list(nodes.values()), 'edges': edges}, open(os.path.join(out, 'graph.json'), 'w', encoding='utf-8'), ensure_ascii=False)
with open(os.path.join(out, 'graph.graphml'), 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<graphml xmlns="http://graphml.graphdrawing.org/xmlns">\n')
    for k in NF[1:]: f.write(f'<key id="n_{k}" for="node" attr.name="{k}" attr.type="string"/>\n')
    for k in EF[2:]: f.write(f'<key id="e_{k}" for="edge" attr.name="{k}" attr.type="string"/>\n')
    f.write('<graph id="duke" edgedefault="directed">\n')
    for n in nodes.values():
        f.write(f'<node id="{escape(n["id"])}">' + ''.join(f'<data key="n_{k}">{escape(str(n.get(k, "")))}</data>' for k in NF[1:] if n.get(k, '') != '') + '</node>\n')
    for i, e in enumerate(edges):
        f.write(f'<edge id="e{i}" source="{escape(e["source"])}" target="{escape(e["target"])}">' + ''.join(f'<data key="e_{k}">{escape(str(e[k]))}</data>' for k in EF[2:]) + '</edge>\n')
    f.write('</graph>\n</graphml>\n')
terms = {nid: [n['label'], 0 if n['type'] == 'Actividad' else 1] for nid, n in nodes.items() if n['type'] in ('Actividad', 'Indicación')}
abbr = {k: v for k, v in d.get('abbreviations', {}).items() if re.fullmatch(r'[A-Z0-9]{2,4}', k)}
json.dump({'meta': meta, 'herbs': compact, 'terms': terms, 'abbr': abbr}, open(os.path.join(out, 'compact.json'), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print(json.dumps({k: v for k, v in val.items() if k != 'orphans'}, ensure_ascii=False, default=dict)[:1500])
print('orphans', len(val['orphans']))
