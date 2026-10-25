#!/usr/bin/env python3
"""CLI sin dependencias para explorar el grafo PMBOK 6."""
import json, sys
from pathlib import Path

G = json.loads((Path(__file__).resolve().parent.parent / 'data' / 'grafo.json').read_text(encoding='utf-8'))
N = G['nodes']; E = G['edges']

def emit(x): print(json.dumps(x, ensure_ascii=False, indent=2))
def main(args):
    cmd = args[0] if args else 'stats'
    if cmd == 'stats':
        emit({'source':G['source'], 'nodes':len(N), 'edges':len(E), 'types':{t:sum(n['type']==t for n in N) for t in sorted({n['type'] for n in N})}})
    elif cmd == 'areas': emit([n for n in N if n['type']=='AreaConocimiento'])
    elif cmd == 'area' and len(args)>1:
        a='area:'+args[1]; ids={e['target'] for e in E if e['source']==a}
        emit([n for n in N if n['id'] in ids])
    elif cmd == 'search' and len(args)>1:
        term=' '.join(args[1:]).casefold(); emit([n for n in N if term in n['label'].casefold()])
    elif cmd == 'validate':
        ids=[n['id'] for n in N]; bad=[e for e in E if e['source'] not in ids or e['target'] not in ids]
        emit({'valid':len(ids)==len(set(ids)) and not bad,'duplicate_ids':len(ids)-len(set(ids)),'dangling_edges':bad})
    else:
        raise SystemExit('Uso: query_graph.py [stats|areas|area NUM|search TEXTO|validate]')
if __name__=='__main__': main(sys.argv[1:])
