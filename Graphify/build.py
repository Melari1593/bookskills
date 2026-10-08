#!/usr/bin/env python3
"""Construye el grafo de conocimiento de Harry's Cosmeticology a partir de las
extracciones por capítulo (extraction/chunk_*.json).

Sigue el pipeline de graphify (extraer -> fusionar -> agrupar -> analizar ->
exportar) sin dependencias externas: fusiona nodos por id y alias, detecta
comunidades con Louvain, calcula nodos dios y conexiones sorprendentes y
escribe graph.json, GRAPH_REPORT.md y graph.html.

    python3 Graphify/build.py
"""
import json
import random
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EXTRACTION = ROOT / "extraction"
LABELS = ROOT / "labels.json"
SKILL = ROOT.parent / ".claude" / "skills" / "harrys-cosmeticology"

BOOKS = {
    "v1": "Vol. 1 — Marketing, regulación y sustratos",
    "v2": "Vol. 2 — Ingredientes y antienvejecimiento",
    "sus": "Sostenibilidad y eco-responsabilidad",
}
KINDS = ["chapter", "ingredient", "ingredient_class", "anatomy", "mechanism",
         "condition", "product", "technique", "regulation", "concept",
         "organization", "region"]
SCORE = {"EXTRACTED": 1.0, "INFERRED": 0.75, "AMBIGUOUS": 0.2}
# Sinónimos que los extractores crearon como nodos separados (id -> id canónico)
SYNONYMS = {
    "skin_barrier_function": "skin_barrier",
    "skin_lipid_barrier": "skin_barrier",
    "skin_circadian_rhythm": "circadian_rhythm",
    "circadian_clock": "circadian_rhythm",
    "nf_kappa_b": "nf_kb",
    "mitochondrion": "mitochondria",
    "camp": "cyclic_amp",
    "glycerol": "glycerin",
    "freeze_drying": "lyophilization",
    "cutibacterium_acne": "propionibacterium_acne",
    "cox_2": "cyclooxygenase_2",
    "egcg": "epigallocatechin_gallate",
    "retinoic_acid": "tretinoin",
    "qpcr": "quantitative_pcr",
    "t_lymphocyte": "t_cell",
    "ctfa": "personal_care_products_council",
    "pcpc": "personal_care_products_council",
    "nrf2_pathway": "nrf2",
    "hair_color": "hair_dye",
    "hair_colorant": "hair_dye",
    "malignant_melanoma": "melanoma",
    "photodamage": "photoaging",
    "skin_lightening": "skin_whitening",
    "skin_lightening_product": "skin_whitening_product",
    "contact_allergy": "allergic_contact_dermatitis",
    "inci": "inci_name",
    "fema_gra": "gras",
    "emulsion_stability": "emulsion_stabilization",
    "gene_silencing": "rna_interference",
    "rheology_measurement": "rheometry",
    "oral_care_product": "oral_care",
    "nutraceutical": "nutricosmetic",
    "cyclobutane_pyrimidine_dimer": "pyrimidine_dimer",
    "timp": "tissue_inhibitor_of_metalloproteinase",
    "tnf_alpha": "tumor_necrosis_factor_alpha",
    "tgf_beta": "transforming_growth_factor_beta",
    "bse": "bovine_spongiform_encephalopathy",
}
# Siglas que también son palabras con otro significado en el grafo ("lip" = labio)
NOT_ABBREV = {"lip", "nail", "hair", "skin", "age"}


def is_abbrev(short, long):
    """True si `short` son las iniciales de `long` (vegf ~ vascular_endothelial_growth_factor)."""
    words = [w for w in long.split("_") if w and w not in ("of", "and", "the")]
    if short in NOT_ABBREV or "_" in short.strip("_0123456789") or len(words) < 2:
        return False
    initials = "".join(w[0] if not w.isdigit() else w for w in words)
    return short.replace("_", "") in (initials, initials.rstrip("s"))


def norm_id(text):
    s = re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")
    return s


def singular(s):
    # Colapsa plurales simples para fusionar "peptides" con "peptide".
    if s.endswith("ies") and len(s) > 5:
        return s[:-3] + "y"
    if s.endswith("ses") or s.endswith("xes"):
        return s[:-2]
    if s.endswith("s") and not s.endswith(("ss", "us", "is", "sis")) and len(s) > 4:
        return s[:-1]
    return s


def book_of(source_file):
    return (source_file or "").split("-")[0]


# --------------------------------------------------------------------- merge
def load_chunks():
    nodes, edges, hyper = [], [], []
    for path in sorted(EXTRACTION.glob("chunk_*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        nodes += data.get("nodes", [])
        edges += data.get("edges", [])
        hyper += data.get("hyperedges", [])
    return nodes, edges, hyper


def merge(nodes, edges, hyper):
    # 1) canonical id por nodo: singular del id normalizado
    canon = {}
    for n in nodes:
        raw = n["id"]
        cid = raw if n.get("kind") == "chapter" else singular(norm_id(raw))
        canon[raw] = cid

    # 2) alias -> id canónico. Si el alias ya es otro nodo, sólo se fusionan
    #    sigla y nombre completo (p. ej. "VEGF"); los alias de los extractores
    #    a veces son términos más amplios (dimethicone ~ "silicone").
    ids = set(canon.values())
    alias_map = dict(SYNONYMS)
    for n in nodes:
        if n.get("kind") == "chapter":
            continue
        cid = canon[n["id"]]
        for a in n.get("aliases") or []:
            aid = singular(norm_id(a))
            if aid == cid or aid not in ids or aid in alias_map or cid in alias_map:
                continue
            if is_abbrev(aid, cid):
                alias_map[aid] = cid
            elif is_abbrev(cid, aid):
                alias_map[cid] = aid
    for n in nodes:
        if n.get("kind") == "chapter":
            continue
        cid = canon[n["id"]]
        for a in [n.get("label", "")] + list(n.get("aliases") or []):
            aid = singular(norm_id(a))
            if len(aid) < 3 or aid == cid:
                continue
            if aid in ids or aid in alias_map:
                continue
            alias_map.setdefault(aid, cid)
    # un label que normaliza a un alias conocido apunta al canónico
    def resolve(i):
        c = canon.get(i, singular(norm_id(i)) if not i.startswith("ch_") else i)
        seen = set()
        while c in alias_map and c not in seen:
            seen.add(c)
            c = alias_map[c]
        return c

    merged = {}
    for n in nodes:
        cid = resolve(n["id"])
        m = merged.get(cid)
        if m is None:
            m = merged[cid] = {
                "id": cid, "label": n.get("label") or cid, "kind": n.get("kind", "concept"),
                "summaries": [], "sources": [], "aliases": set(), "authors": [],
                "_kinds": Counter(),
            }
        m["_kinds"][n.get("kind", "concept")] += 1
        src = n.get("source_file")
        if src and src not in m["sources"]:
            m["sources"].append(src)
        summ = (n.get("summary") or "").strip()
        if summ and src and all(s["text"] != summ for s in m["summaries"]):
            m["summaries"].append({"source": src, "text": summ})
        for a in n.get("aliases") or []:
            m["aliases"].add(a)
        if n.get("label") and n["label"] != m["label"]:
            m["aliases"].add(n["label"])
        for a in n.get("authors") or []:
            if a not in m["authors"]:
                m["authors"].append(a)

    for m in merged.values():
        m["kind"] = m.pop("_kinds").most_common(1)[0][0]
        m["aliases"] = sorted(a for a in m["aliases"] if a != m["label"])

    # 3) aristas: resolver extremos, descartar lazos y fusionar duplicados
    out = {}
    for e in edges:
        s, t = resolve(e["source"]), resolve(e["target"])
        if s == t or s not in merged or t not in merged:
            continue
        key = (s, t, e.get("relation", "conceptually_related_to"))
        conf = e.get("confidence", "INFERRED")
        score = e.get("confidence_score", SCORE.get(conf, 0.75))
        cur = out.get(key)
        if cur is None:
            out[key] = {
                "source": s, "target": t, "relation": key[2], "confidence": conf,
                "confidence_score": score, "weight": 1, "sources": [e.get("source_file")],
                "evidence": [e["evidence"]] if e.get("evidence") else [],
            }
        else:
            cur["weight"] += 1
            if score > cur["confidence_score"]:
                cur["confidence_score"], cur["confidence"] = score, conf
            if e.get("source_file") not in cur["sources"]:
                cur["sources"].append(e.get("source_file"))
            if e.get("evidence") and len(cur["evidence"]) < 3:
                cur["evidence"].append(e["evidence"])

    # un concepto aparece en todo capítulo cuyas aristas lo mencionan
    for e in out.values():
        for end in (e["source"], e["target"]):
            m = merged[end]
            if m["kind"] == "chapter":
                continue
            for src in e["sources"]:
                if src and src not in m["sources"]:
                    m["sources"].append(src)
    for m in merged.values():
        m["sources"].sort()

    hyperedges = []
    for h in hyper:
        members = sorted({resolve(x) for x in h.get("nodes", [])} & merged.keys())
        if len(members) >= 3:
            hyperedges.append({"id": h["id"], "label": h.get("label", h["id"]),
                               "nodes": members, "source_file": h.get("source_file")})
    return merged, list(out.values()), hyperedges


# ------------------------------------------------------------------- louvain
def louvain(node_ids, edges, seed=7, resolution=1.0):
    rng = random.Random(seed)
    adj = defaultdict(lambda: defaultdict(float))
    for e in edges:
        if e["relation"] == "covers":
            continue  # las aristas capítulo->tema dominarían el agrupamiento
        w = e["confidence_score"] * e["weight"]
        adj[e["source"]][e["target"]] += w
        adj[e["target"]][e["source"]] += w
    for n in node_ids:
        adj[n]
    partition = {n: n for n in adj}  # nodo original -> comunidad
    graph = {n: dict(nb) for n, nb in adj.items()}
    members = {n: [n] for n in graph}

    while True:
        m2 = sum(sum(nb.values()) for nb in graph.values())
        if m2 == 0:
            break
        deg = {n: sum(nb.values()) for n, nb in graph.items()}
        comm = {n: n for n in graph}
        tot = dict(deg)
        moved_any = False
        improved = True
        while improved:
            improved = False
            order = list(graph)
            rng.shuffle(order)
            for n in order:
                c0 = comm[n]
                links = defaultdict(float)
                for nb, w in graph[n].items():
                    if nb != n:
                        links[comm[nb]] += w
                tot[c0] -= deg[n]
                best, gain = c0, links.get(c0, 0) - resolution * tot[c0] * deg[n] / m2
                for c, w in links.items():
                    g = w - resolution * tot[c] * deg[n] / m2
                    if g > gain + 1e-12:
                        best, gain = c, g
                tot[best] += deg[n]
                if best != c0:
                    comm[n] = best
                    improved = moved_any = True
        if not moved_any:
            break
        new_graph = defaultdict(lambda: defaultdict(float))
        for n, nb in graph.items():
            new_graph[comm[n]]
            for m, w in nb.items():
                new_graph[comm[n]][comm[m]] += w
        new_members = defaultdict(list)
        for n in graph:
            new_members[comm[n]] += members[n]
        graph = {n: dict(nb) for n, nb in new_graph.items()}
        members = dict(new_members)

    result = {}
    for cid, (_, mem) in enumerate(sorted(members.items(), key=lambda kv: -len(kv[1]))):
        for n in mem:
            result[n] = cid
    return result


# ------------------------------------------------------------------ analysis
def analyze(merged, edges, comm):
    degree = Counter()
    for e in edges:
        degree[e["source"]] += 1
        degree[e["target"]] += 1
    concept_deg = [(n, d) for n, d in degree.items() if merged[n]["kind"] != "chapter"]
    gods = sorted(concept_deg, key=lambda x: -x[1])[:20]

    # cohesión: fracción de aristas internas de cada comunidad
    inside, total = Counter(), Counter()
    for e in edges:
        if e["relation"] == "covers":
            continue
        cs, ct = comm[e["source"]], comm[e["target"]]
        total[cs] += 1
        total[ct] += 1
        if cs == ct:
            inside[cs] += 2
    cohesion = {c: round(inside[c] / total[c], 2) if total[c] else 0 for c in set(comm.values())}

    # sorprendentes: aristas que unen comunidades distintas cuyos extremos,
    # fuera de esa arista, viven en capítulos (y libros) diferentes
    surprises = []
    for e in edges:
        if e["relation"] in ("covers", "is_a", "part_of"):
            continue
        a, b = merged[e["source"]], merged[e["target"]]
        if a["kind"] == "chapter" or b["kind"] == "chapter" or comm[a["id"]] == comm[b["id"]]:
            continue
        if degree[a["id"]] < 4 or degree[b["id"]] < 4:
            continue
        sa, sb = set(a["sources"]), set(b["sources"])
        jaccard = len(sa & sb) / len(sa | sb)
        books_a, books_b = {book_of(x) for x in sa}, {book_of(x) for x in sb}
        score = 2 * (1 - jaccard) + (1 if books_a != books_b else 0) + e["confidence_score"]
        surprises.append((score, e))
    surprises.sort(key=lambda x: -x[0])
    # puentes: conceptos citados en más capítulos
    bridges = sorted((m for m in merged.values() if m["kind"] != "chapter"),
                     key=lambda m: -len(m["sources"]))[:20]
    return degree, gods, cohesion, [e for _, e in surprises[:15]], bridges


def auto_labels(merged, comm, degree):
    groups = defaultdict(list)
    for n, c in comm.items():
        if merged[n]["kind"] != "chapter":
            groups[c].append(n)
    labels = {}
    for c, mem in groups.items():
        top = sorted(mem, key=lambda n: -degree[n])[:3]
        labels[c] = " / ".join(merged[n]["label"] for n in top)
    return labels


# -------------------------------------------------------------------- export
def main():
    nodes, edges, hyper = load_chunks()
    merged, edges, hyper = merge(nodes, edges, hyper)
    comm = louvain(list(merged), edges)
    degree, gods, cohesion, surprises, bridges = analyze(merged, edges, comm)

    labels = auto_labels(merged, comm, degree)
    if LABELS.exists():
        # labels.json mapea la firma de la comunidad (su nodo de mayor grado) a un nombre
        curated = json.loads(LABELS.read_text(encoding="utf-8"))
        groups = defaultdict(list)
        for n, c in comm.items():
            groups[c].append(n)
        for c, mem in groups.items():
            for n in sorted(mem, key=lambda n: -degree[n]):
                if n in curated:
                    labels[c] = curated[n]
                    break

    # los capítulos toman la comunidad mayoritaria de los temas que cubren
    covers = defaultdict(Counter)
    for e in edges:
        if e["relation"] == "covers" and merged[e["source"]]["kind"] == "chapter":
            covers[e["source"]][comm[e["target"]]] += 1
    for ch, cnt in covers.items():
        comm[ch] = cnt.most_common(1)[0][0]

    sizes = Counter(comm.values())
    out_nodes = []
    for n in merged.values():
        out_nodes.append({
            "id": n["id"], "label": n["label"], "kind": n["kind"],
            "community": comm[n["id"]], "degree": degree[n["id"]],
            "sources": n["sources"], "aliases": n["aliases"],
            "summaries": n["summaries"], **({"authors": n["authors"]} if n["authors"] else {}),
        })
    out_nodes.sort(key=lambda n: (-n["degree"], n["id"]))
    graph = {
        "meta": {
            "title": "Harry's Cosmeticology — grafo de conocimiento",
            "books": BOOKS,
            "nodes": len(out_nodes), "edges": len(edges),
            "communities": len(sizes), "hyperedges": len(hyper),
        },
        "communities": [{"id": c, "label": labels.get(c, f"Comunidad {c}"), "size": s,
                         "cohesion": cohesion.get(c, 0)} for c, s in sorted(sizes.items())],
        "nodes": out_nodes, "edges": edges, "hyperedges": hyper,
    }
    (ROOT / "graph.json").write_text(json.dumps(graph, ensure_ascii=False, indent=1), encoding="utf-8")
    if SKILL.exists():
        export_skill_graph(graph)
    (ROOT / "GRAPH_REPORT.md").write_text(report(graph, merged, gods, surprises, bridges, labels, comm),
                                          encoding="utf-8")
    template = (ROOT / "template.html").read_text(encoding="utf-8")
    compact = json.dumps(graph, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    page = template.replace("/*__GRAPH__*/null", compact)
    (ROOT / "graph.html").write_text(
        '<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        "</head>\n<body>\n" + page + "\n</body>\n</html>\n", encoding="utf-8")
    print(f"{len(out_nodes)} nodos, {len(edges)} aristas, {len(sizes)} comunidades, "
          f"{len(hyper)} hiperaristas")


def skill_chapter_map():
    """Archivo del corpus (v2-06-Part_4.1.3.md) -> ficha de la skill (v2-p4-1-3-...)."""
    chapters = {p.stem: p.stem for p in (SKILL / "chapters").glob("*.md")}
    def lookup(source):
        book = book_of(source)
        m = re.search(r"Part[_-]*([0-9.]+?)\.?md$", source.replace(" ", ""))
        if not m:
            return None
        part = m.group(1).rstrip(".").replace(".", "-")
        for stem in chapters:
            if stem.startswith(f"{book}-p{part}-"):
                return stem
        # intros de sección ("4.1.0", "3.3.0") no tienen ficha propia
        return None
    return lookup


def export_skill_graph(graph):
    """Copia compacta del grafo para la skill (la consulta scripts/graph_query.py)."""
    lookup = skill_chapter_map()
    def chap(src):
        return lookup(src) or src.removesuffix(".md")
    nodes = []
    for n in graph["nodes"]:
        nodes.append({
            "id": n["id"], "label": n["label"], "kind": n["kind"], "community": n["community"],
            "aliases": n["aliases"], "chapters": sorted({chap(s) for s in n["sources"]}),
            "summaries": [[chap(x["source"]), x["text"]] for x in n["summaries"]],
        })
    edges = [[e["source"], e["relation"], e["target"], e["confidence"],
              sorted({chap(s) for s in e["sources"] if s}), (e["evidence"] or [""])[0]]
             for e in graph["edges"]]
    data = {"communities": {c["id"]: c["label"] for c in graph["communities"]},
            "nodes": nodes, "edges": edges,
            "hyperedges": [[h["label"], h["nodes"]] for h in graph["hyperedges"]]}
    (SKILL / "references").mkdir(exist_ok=True)
    (SKILL / "references" / "graph.json").write_text(
        json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")


def report(graph, merged, gods, surprises, bridges, labels, comm):
    meta = graph["meta"]
    chapters = sorted((n for n in graph["nodes"] if n["kind"] == "chapter"), key=lambda n: n["sources"][0])
    kinds = Counter(n["kind"] for n in graph["nodes"])
    conf = Counter(e["confidence"] for e in graph["edges"])
    L = []
    w = L.append
    w("# Graph Report — Harry's Cosmeticology (9.ª ed.)\n")
    w("Grafo de conocimiento construido con el método de [graphify](https://github.com/Graphify-Labs/graphify) "
      "a partir de tres libros: *Harry's Cosmeticology* Vol. 1 y Vol. 2, y el *focus book* "
      "*Sustainability and Eco-responsibility*.\n")
    w("## Resumen\n")
    w(f"- **{meta['nodes']} nodos**, **{meta['edges']} aristas**, **{meta['communities']} comunidades**, "
      f"{meta['hyperedges']} hiperaristas")
    w(f"- {len(chapters)} capítulos procesados")
    w("- Tipos de nodo: " + ", ".join(f"{k} {v}" for k, v in kinds.most_common()))
    w("- Confianza de las aristas: " + ", ".join(f"{k} {v}" for k, v in conf.most_common()))
    w("")
    w("## Nodos dios (los conceptos más conectados)\n")
    w("| # | Concepto | Tipo | Grado | Capítulos |")
    w("|---|---|---|---|---|")
    for i, (n, d) in enumerate(gods, 1):
        m = merged[n]
        w(f"| {i} | {m['label']} | {m['kind']} | {d} | {len(m['sources'])} |")
    w("")
    w("## Conceptos puente (aparecen en más capítulos)\n")
    for m in bridges[:15]:
        books = sorted({book_of(s) for s in m["sources"]})
        w(f"- **{m['label']}** — {len(m['sources'])} capítulos ({', '.join(books)})")
    w("")
    w("## Comunidades\n")
    groups = defaultdict(list)
    for n in graph["nodes"]:
        if n["kind"] != "chapter":
            groups[n["community"]].append(n)
    for c in graph["communities"]:
        mem = sorted(groups.get(c["id"], []), key=lambda n: -n["degree"])
        if len(mem) < 3:
            continue
        w(f"### {c['id']}. {c['label']}\n")
        w(f"{len(mem)} conceptos · cohesión {c['cohesion']}  ")
        w("Principales: " + ", ".join(n["label"] for n in mem[:12]))
        chs = [n["label"] for n in chapters if n["community"] == c["id"]]
        if chs:
            w("  \nCapítulos: " + "; ".join(chs))
        w("")
    small = sum(1 for c in graph["communities"] if len(groups.get(c["id"], [])) < 3)
    if small:
        w(f"_Además, {small} comunidades de menos de 3 conceptos (nodos aislados o pares)._\n")
    w("## Conexiones sorprendentes\n")
    w("Aristas que cruzan comunidades entre conceptos que, por lo demás, aparecen en capítulos distintos.\n")
    for e in surprises:
        a, b = merged[e["source"]], merged[e["target"]]
        ev = f" — _{e['evidence'][0]}_" if e["evidence"] else ""
        w(f"- **{a['label']}** → `{e['relation']}` → **{b['label']}** "
          f"({e['confidence']}, {e['confidence_score']}){ev}")
    w("")
    if graph["hyperedges"]:
        w("## Hiperaristas (grupos de 3+ conceptos)\n")
        for h in graph["hyperedges"]:
            names = ", ".join(merged[x]["label"] for x in h["nodes"])
            w(f"- **{h['label']}**: {names}")
        w("")
    w("## Preguntas sugeridas para explorar el grafo\n")
    for g, _ in gods[:6]:
        m = merged[g]
        w(f"- ¿Qué relación tiene **{m['label']}** con las demás comunidades?")
    for e in surprises[:4]:
        w(f"- ¿Por qué **{merged[e['source']]['label']}** se conecta con **{merged[e['target']]['label']}**?")
    w("")
    w("## Capítulos\n")
    w("| Archivo | Capítulo | Comunidad |")
    w("|---|---|---|")
    for n in chapters:
        w(f"| {n['sources'][0]} | {n['label']} | {labels.get(n['community'], n['community'])} |")
    w("")
    return "\n".join(L)


if __name__ == "__main__":
    main()
