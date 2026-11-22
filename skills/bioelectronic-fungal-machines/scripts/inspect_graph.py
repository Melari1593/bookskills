#!/usr/bin/env python3
"""Resumen reproducible del grafo compartido; sin dependencias externas."""
import json
from pathlib import Path
p = Path(__file__).resolve().parents[3] / "grafos" / "fungal-machines" / "graph.json"
g = json.loads(p.read_text(encoding="utf-8"))
print("Libro:", g.get("metadata", {}).get("title"))
print("Nodos:", len(g.get("nodes", [])))
print("Relaciones:", len(g.get("edges", [])))
print("Capítulos:", sum(n.get("type") == "chapter" for n in g.get("nodes", [])))
