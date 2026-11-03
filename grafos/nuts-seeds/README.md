# Nuts and Seeds in Health and Disease Prevention: grafos de capítulos

Cuatro capítulos de *Nuts and Seeds in Health and Disease Prevention* (Preedy, Watson y Patel, eds.; Elsevier, 1.ª ed. 2011 y 2.ª ed. 2020), cada uno como grafo interactivo con alertas de evidencia actual. Los resúmenes son propios; el texto de los capítulos no se versiona.

| Carpeta | Capítulo | Grafo | Alertas | Hallazgos principales |
|---|---|---|---|---|
| [`cap04-acidos-grasos-1ed`](cap04-acidos-grasos-1ed/) | Cap. 4 (1.ª ed.), Li y Hu: ácidos grasos de frutos secos y semillas | 5 partes, 13 secciones, 24 nodos, 5 tablas | 12 | Riesgos omitidos: ginkgotoxina en semilla de ginkgo, THC en cáñamo, alcaloides pirrolizidínicos en Boraginaceae, alergia al maní. ALA de nuez y palmitoleico de macadamia difieren del USDA. |
| [`cap07-minerales-1ed`](cap07-minerales-1ed/) | Cap. 7 (1.ª ed.), Rodushkin, Baxter y Engström: elementos inorgánicos | 6 partes, 16 secciones, 20 nodos, 2 tablas | 11 | Superado: selenio y cáncer, PTWI de plomo y arsénico, esencialidad del cromo. Riesgo omitido: bario de la nuez de Brasil (≈ 11 g/día alcanzan la RfD de la EPA) y níquel como contaminante. |
| [`cap07-semilla-oregano-2ed`](cap07-semilla-oregano-2ed/) | Cap. 7 (2.ª ed.), Atar y Çölgeçen: semilla de orégano | 3 partes, 10 secciones, 9 nodos | 7 | Sin evidencia en humanos: "las plantas curan" cáncer, sida y Alzheimer; radioprotección. Riesgo omitido: "no superar la dosis del fabricante" no es criterio seguro; alergia cruzada con Lamiaceae. |
| [`cap14-semilla-tamarindo-2ed`](cap14-semilla-tamarindo-2ed/) | Cap. 14 (2.ª ed.), Pal y Mukherjee: semilla de tamarindo | 5 partes, 16 secciones, 12 nodos, 1 tabla | 9 | Riesgo omitido: el extracto no es alternativa al antiveneno (OMS). Errores del capítulo: "araquidónico" por araquídico; arsénico, cadmio y plomo como "esenciales"; interacciones atribuidas a la semilla que vienen de estudios con pulpa. Varias referencias numeradas no tratan el tema citado. |

En cada carpeta: `grafo.html` (mapa interactivo), `grafo.json` (datos), `afirmaciones.md`, `verif.md` (veredicto, fuentes con DOI y log de búsqueda), `alertas.json` y el script que define el grafo (`build_json.py` o `capitulo.py`; los `capitulo.py` se construyen con [`construir.py`](construir.py)).
