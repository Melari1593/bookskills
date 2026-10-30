#!/usr/bin/env python3
"""Construye el HTML interactivo a partir de un grafo de libro en JSON.

Uso:
  python build_graph.py grafo.json salida.html
  python build_graph.py grafo.json salida.html --d3 ruta/d3.min.js   # incrusta d3 (sin internet)

Valida primero con validate_graph.py; si hay errores, no construye.
La plantilla está en ../assets/plantilla-grafo.html y carga d3 v7 desde cdnjs
salvo que se pase --d3.
"""
import argparse, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from validate_graph import validate, report  # noqa: E402

TEMPLATE = os.path.join(HERE, "..", "assets", "plantilla-grafo.html")
CDN_TAG = '<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js"></script>'
MARK = "/*__GRAPH_DATA__*/"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("graph")
    ap.add_argument("out")
    ap.add_argument("--d3", help="ruta local a d3.min.js para incrustarlo")
    a = ap.parse_args()

    with open(a.graph, encoding="utf-8") as f:
        g = json.load(f)
    if report(*validate(g)):
        sys.exit(1)

    html = open(TEMPLATE, encoding="utf-8").read()
    assert MARK in html and CDN_TAG in html, "La plantilla no tiene los marcadores esperados."
    # JSON seguro dentro de <script>: evita que un texto cierre la etiqueta.
    data = json.dumps(g, ensure_ascii=False).replace("</", "<\\/")
    html = html.replace(MARK, "const GRAPH = " + data + ";")
    if a.d3:
        html = html.replace(CDN_TAG, "<script>" + open(a.d3, encoding="utf-8").read() + "</script>")

    with open(a.out, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"HTML generado: {a.out} ({len(html)//1024} KB)")


if __name__ == "__main__":
    main()
