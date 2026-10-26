import json,sys
from pathlib import Path
g=json.loads((Path(__file__).resolve().parents[1]/"data/grafo.json").read_text(encoding="utf-8"))
n=g["nodes"];e=g["edges"]
cmd=sys.argv[1] if len(sys.argv)>1 else "stats"
if cmd=="stats": result={"nodes":len(n),"edges":len(e),"chapters":sum(x["type"]=="Chapter" for x in n)}
elif cmd=="chapters":result=[x for x in n if x["type"]=="Chapter"]
elif cmd=="chapter":
 key="chapter:%02d"%int(sys.argv[2]);ids={x["target"] for x in e if x["source"]==key};result=[x for x in n if x["id"] in ids]
elif cmd=="search":result=[x for x in n if " ".join(sys.argv[2:]).casefold() in x["label"].casefold()]
elif cmd=="validate":
 ids=[x["id"] for x in n];result={"unique_ids":len(ids)==len(set(ids)),"valid_edges":all(x["source"] in ids and x["target"] in ids for x in e)}
else:raise SystemExit("Commands: stats, chapters, chapter N, search TERM, validate")
print(json.dumps(result,ensure_ascii=False,indent=2))
