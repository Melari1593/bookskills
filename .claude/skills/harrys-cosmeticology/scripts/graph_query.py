#!/usr/bin/env python3
"""Query the Harry's Cosmeticology knowledge graph (references/graph.json).

Usage:
  graph_query.py search <text>              find concepts by name or alias
  graph_query.py node <concept>             summaries, chapters and all relations
  graph_query.py neighbors <concept> [rel]  relations, optionally one relation type
  graph_query.py path <concept> <concept>   shortest chain of relations between two concepts
  graph_query.py chapter <chapter-file>     concepts a chapter covers, by kind
  graph_query.py community <id|text>        members of a topic community
  graph_query.py top [kind]                 most connected concepts (optionally one kind)

<concept> may be an id (hyaluronic_acid), a label or an alias (case-insensitive).
"""
import json
import re
import sys
from collections import Counter, defaultdict, deque
from pathlib import Path

DATA = json.loads((Path(__file__).resolve().parent.parent / "references" / "graph.json").read_text(encoding="utf-8"))
NODES = {n["id"]: n for n in DATA["nodes"]}
OUT, IN = defaultdict(list), defaultdict(list)
for s, rel, t, conf, chs, ev in DATA["edges"]:
    OUT[s].append((rel, t, conf, chs, ev))
    IN[t].append((rel, s, conf, chs, ev))
DEGREE = Counter({i: len(OUT[i]) + len(IN[i]) for i in NODES})


def norm(text):
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def find(query):
    q = norm(query)
    if q in NODES:
        return NODES[q]
    for n in NODES.values():
        if norm(n["label"]) == q or q in (norm(a) for a in n["aliases"]):
            return n
    hits = search(query, 1)
    if hits:
        return hits[0]
    sys.exit(f"No concept matches '{query}'. Try: graph_query.py search {query}")


def search(query, limit=20):
    q = norm(query)
    scored = []
    for n in NODES.values():
        names = [norm(n["label"])] + [norm(a) for a in n["aliases"]] + [n["id"]]
        if any(q in x for x in names):
            exact = any(x == q for x in names)
            prefix = any(x.startswith(q) for x in names)
            scored.append((not exact, not prefix, -DEGREE[n["id"]], n["id"]))
    return [NODES[i] for *_, i in sorted(scored)[:limit]]


def label(i):
    n = NODES[i]
    return f"{n['label']} [{n['kind']}]"


def show_relations(i, only=None):
    groups = defaultdict(list)
    for rel, t, conf, chs, ev in OUT[i]:
        if only in (None, rel):
            groups[rel].append((t, conf, chs, ev))
    for rel, s, conf, chs, ev in IN[i]:
        if only in (None, rel):
            groups["<- " + rel].append((s, conf, chs, ev))
    for rel in sorted(groups, key=lambda r: -len(groups[r])):
        print(f"\n{rel}:")
        for other, conf, chs, ev in sorted(groups[rel], key=lambda x: -DEGREE[x[0]]):
            mark = "" if conf == "EXTRACTED" else f" ({conf.lower()})"
            print(f"  - {label(other)}{mark} — {ev} [{', '.join(chs)}]" if ev else f"  - {label(other)}{mark} [{', '.join(chs)}]")


def cmd_node(args):
    n = find(" ".join(args))
    print(f"# {n['label']}  ({n['kind']}, id={n['id']})")
    print(f"Community: {DATA['communities'].get(str(n['community']), n['community'])}")
    if n["aliases"]:
        print("Aliases: " + ", ".join(n["aliases"]))
    print("Chapters: " + ", ".join(n["chapters"]))
    for ch, text in n["summaries"]:
        print(f"\n[{ch}] {text}")
    show_relations(n["id"])


def cmd_neighbors(args):
    n = find(args[0])
    show_relations(n["id"], args[1] if len(args) > 1 else None)


def cmd_path(args):
    a, b = find(args[0])["id"], find(args[1])["id"]
    prev = {a: None}
    queue = deque([a])
    while queue:
        cur = queue.popleft()
        if cur == b:
            break
        for rel, nxt, *_ in OUT[cur] + IN[cur]:
            # chapters connect everything; skip them so paths stay conceptual
            if nxt not in prev and NODES[nxt]["kind"] != "chapter":
                prev[nxt] = (cur, rel)
                queue.append(nxt)
    if b not in prev:
        sys.exit("No path between those concepts.")
    chain, cur = [], b
    while prev[cur]:
        p, rel = prev[cur]
        chain.append((p, rel, cur))
        cur = p
    for p, rel, c in reversed(chain):
        fwd = any(r == rel and t == c for r, t, *_ in OUT[p])
        print(f"{label(p)} --{rel}--> {label(c)}" if fwd else f"{label(c)} --{rel}--> {label(p)}")


def cmd_chapter(args):
    q = args[0].removesuffix(".md")
    ids = [i for i, n in NODES.items() if any(q in ch for ch in n["chapters"]) and n["kind"] != "chapter"]
    if not ids:
        sys.exit(f"No chapter matches '{q}'.")
    by_kind = defaultdict(list)
    for i in sorted(ids, key=lambda i: -DEGREE[i]):
        by_kind[NODES[i]["kind"]].append(NODES[i]["label"])
    for kind, labels in sorted(by_kind.items(), key=lambda kv: -len(kv[1])):
        print(f"{kind} ({len(labels)}): " + ", ".join(labels))


def cmd_community(args):
    q = " ".join(args)
    comms = DATA["communities"]
    cid = q if q in comms else next((k for k, v in comms.items() if q.lower() in v.lower()), None)
    if cid is None:
        for k, v in comms.items():
            print(f"{k}: {v}")
        return
    members = sorted((i for i, n in NODES.items() if str(n["community"]) == cid and n["kind"] != "chapter"),
                     key=lambda i: -DEGREE[i])
    print(f"# {comms[cid]} ({len(members)} concepts)")
    print(", ".join(NODES[i]["label"] for i in members))


def cmd_top(args):
    kind = args[0] if args else None
    ids = [i for i in NODES if NODES[i]["kind"] != "chapter" and kind in (None, NODES[i]["kind"])]
    for i in sorted(ids, key=lambda i: -DEGREE[i])[:30]:
        print(f"{DEGREE[i]:4d}  {label(i)}  — {len(NODES[i]['chapters'])} chapters")


def main():
    if len(sys.argv) < 3 and not (len(sys.argv) == 2 and sys.argv[1] in ("top", "community")):
        sys.exit(__doc__)
    cmd, args = sys.argv[1], sys.argv[2:]
    if cmd == "search":
        for n in search(" ".join(args)):
            print(f"{n['id']:40s} {n['label']} [{n['kind']}] — {len(n['chapters'])} chapters")
    else:
        {"node": cmd_node, "neighbors": cmd_neighbors, "path": cmd_path, "chapter": cmd_chapter,
         "community": cmd_community, "top": cmd_top}.get(cmd, lambda a: sys.exit(__doc__))(args)


if __name__ == "__main__":
    main()
