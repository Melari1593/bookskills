#!/usr/bin/env bash
# Regenera el grafo de "Lo que Einstein le contó a su cocinero 2" desde el PDF.
# Uso: ./regenerar.sh ruta/al/libro.pdf   (el texto del libro no se versiona)
# Los pasos con agentes (resúmenes, síntesis, verificación, revisión) ya están hechos y versionados en trabajo/;
# sus instrucciones están en trabajo/instrucciones*.md por si hay que repetirlos.
set -euo pipefail
cd "$(dirname "$0")"
SK=${GRAFO_DE_LIBRO:-$HOME/.claude/skills/grafo-de-libro}
if [ $# -ge 1 ]; then
  python3 "$SK/scripts/extract_structure.py" "$1" trabajo/   # texto.txt (ignorado por git)
  python3 scripts/toc.py && python3 scripts/lotes.py         # toc.json y lotes para agentes
fi
python3 scripts/build_json.py salida/grafo.json
python3 scripts/validate_graph.py salida/grafo.json
[ -f trabajo/texto.txt ] && python3 scripts/pruebas.py salida/grafo.json
python3 scripts/build_graph.py salida/grafo.json salida/grafo-einstein-cocinero-2.html
sed -i 's|<title>Grafo del libro</title>|<title>Einstein y su cocinero 2</title>|' salida/grafo-einstein-cocinero-2.html
