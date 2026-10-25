---
name: pmbok6-project-knowledge
description: Consulta un grafo estructural de la Guía del PMBOK sexta edición (2017) para identificar áreas de conocimiento, procesos y relaciones, y orientar la planificación de proyectos sin inventar datos ausentes.
---

# PMBOK 6 — Skill de conocimiento para dirección de proyectos

## Cuándo utilizar
Activa esta skill cuando el usuario solicite explorar el PMBOK 6, ubicar procesos por área, crear un mapa conceptual, identificar procesos para planificar un proyecto o consultar el grafo derivado del documento aportado.

## Fuente y límites
- Fuente: *Guía de los fundamentos para la dirección de proyectos (Guía del PMBOK)*, sexta edición, PMI, 2017.
- El grafo es una **extracción estructural inicial** de áreas y procesos. No es una transcripción del libro ni contiene entradas, herramientas, técnicas y salidas (ITTO) verificadas.
- La versión local del grafo contiene 60 nodos y 59 aristas; no asumir cobertura completa sin validar.
- No presentar la sexta edición como versión vigente del estándar PMI.
- No copiar pasajes extensos ni redistribuir el PDF original, protegido por derechos de autor.

## Procedimiento
1. Consultar `data/grafo.json` con `scripts/query_graph.py` cuando los datos estén instalados.
2. Ejecutar `stats`, `areas`, `area <número>`, `search <texto>` o `validate`.
3. Las aristas `CONTIENE` y `CONTIENE_PROCESO` expresan jerarquía, no dependencia, secuencia o causalidad.
4. Para detalles ausentes, revisar el PDF original y registrar evidencia, sección/página y confianza.
5. Separar procesos documentados de recomendaciones propias para un proyecto concreto.

## Ejemplos
```bash
python scripts/query_graph.py stats
python scripts/query_graph.py areas
python scripts/query_graph.py area 11
python scripts/query_graph.py search riesgos
python scripts/query_graph.py validate
```

## Esquema
- Nodo: `id`, `label`, `type`, `page` (opcional), `section` (opcional).
- Arista: `source`, `target`, `relation`.
- Relaciones: `CONTIENE`, `CONTIENE_PROCESO`.
- Futuras ampliaciones: `evidence`, `source_section`, `source_page`, `confidence`, `edition`.

## Archivos
- `data/grafo.json`: grafo principal (se requiere importar el paquete local).
- `data/nodos.csv`, `data/relaciones.csv`: tablas interoperables (se requiere importar el paquete local).
- `scripts/query_graph.py`: CLI para consulta y validación.
