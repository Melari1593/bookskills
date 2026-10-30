# Lo que Einstein le contó a su cocinero 2 (Robert L. Wolke) como grafo

[`grafo_einstein_cocinero_2.html`](grafo_einstein_cocinero_2.html) es la versión **profunda** del grafo: no añade nodos, sino causas.

- **141 preguntas** del libro (10 capítulos, con página), cada una resumida con palabras propias.
- **26 conceptos científicos** (de 59 iniciales, fusionados con una visión global del libro), cada uno con tres capas: el **mecanismo**, el **error común** que corrige y qué cambia **en la cocina**.
- **Enlaces con su porqué**: 30 entre conceptos ("se apoya en", "es consecuencia de") y 22 entre secciones; los 7 contrastes se muestran como texto, no como dependencias.
- **24 alertas de vigencia**: la ciencia del libro (2005) contrastada con la de 2026; 15 superadas, 8 vigentes con matices y 1 en disputa. Detalle en [`verif_A.md`](pipeline/trabajo/verif_A.md), [`verif_B.md`](pipeline/trabajo/verif_B.md) y [`log_busqueda.md`](pipeline/trabajo/log_busqueda.md).

## Cómo se comprobó
- [`pruebas.md`](pipeline/trabajo/pruebas.md): control de copia (0 coincidencias de 8 palabras con el libro en 474 textos), 10/10 preguntas de control cuya traza pasa por los conceptos esperados y métricas sin huérfanos.
- [`revision.md`](pipeline/trabajo/revision.md): revisión independiente de los 26 conceptos, una muestra de 20 secciones y los enlaces; sus correcciones ([`correcciones.json`](pipeline/trabajo/correcciones.json)) se aplican al construir.
- [`validacion_extraccion.md`](pipeline/trabajo/validacion_extraccion.md): secciones atípicas de la extracción del PDF y cómo se resolvieron.

## Reproducir
`pipeline/regenerar.sh [libro.pdf]` reconstruye el grafo. El texto del libro no se versiona (derechos de autor); las instrucciones de cada paso con agentes están en `pipeline/trabajo/instrucciones*.md`.
