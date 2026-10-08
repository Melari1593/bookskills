# bookskills

Skills de Claude basadas en libros y obras de referencia.

| Skill | Descripción |
|---|---|
| [`acupuntura-puntos`](.claude/skills/acupuntura-puntos/SKILL.md) | Los 361 puntos clásicos de acupuntura (MTC) por meridiano, con índice por síntoma y categorías (Shu, Yuan, Luo, Xi, Mu, Hui…). |

## Atlas de Meridianos

`atlas/atlas-meridianos.html` es un mapa interactivo de los puntos de `acupuntura-puntos`: vistas anterior, posterior y de cabeza lateral, fichas completas y recetas por síntoma. Se abre directamente en el navegador.

Se genera a partir de las fichas de la skill, así que después de corregir una ficha hay que regenerarlo:

```bash
python3 atlas/build.py
```

`atlas/template.html` contiene la página (estilos y lógica) y `atlas/build.py` extrae los datos de `references/` y asigna a cada punto una posición esquemática en la figura.

## Graphify — Harry's Cosmeticology

`Graphify/graph.html` es un grafo de conocimiento interactivo de *Harry's Cosmeticology* (Vol. 1, Vol. 2 y Sostenibilidad): 2129 conceptos y 6434 relaciones entre ingredientes, anatomía, mecanismos, afecciones y regulación. El reporte está en `Graphify/GRAPH_REPORT.md`; detalles en [`Graphify/README.md`](Graphify/README.md).

## Instalación

Las skills viven en `.claude/skills/` y Claude Code las carga automáticamente al abrir este repo. Cada carpeta es una skill independiente (`SKILL.md` + `references/`). Para instalarla en claude.ai, comprime la carpeta como `.skill` (zip) y súbela en *Settings → Capabilities → Skills*, o cópiala a `~/.claude/skills/` para Claude Code.

> ⚠️ El contenido se redactó a partir de fuentes estándar (Deadman, localización OMS 2008) sin cotejo página a página. Verifica ubicaciones y profundidades de puntos de riesgo antes del uso clínico.
