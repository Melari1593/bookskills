---
name: grafo-cientifico
description: Construye grafos de conocimiento trazables a partir de libros, artículos y documentos; compara afirmaciones, vincula evidencia externa y exporta formatos interoperables. Usar cuando se solicite $grafo-cientifico o convertir fuentes documentales en grafos semánticos verificables.
version: 0.1.0
---

# Grafo científico — Skill universal

## Objetivo
Transformar documentos de cualquier disciplina (crianza, nutrición, farmacología, medicina tradicional china, biomedicina, ingeniería) en un grafo de afirmaciones verificables con procedencia documental y evaluación independiente de evidencia. La skill no sustituye la revisión científica humana.

## Entrada
- Uno o varios documentos accesibles (EPUB, PDF, TXT, HTML o Markdown).
- Opcional: dominio, idioma, preguntas de investigación, ontología específica, fuentes externas autorizadas y ruta de exportación.
- Si los archivos no son accesibles, informar y solicitar acceso; no inventar extracción.

## Flujo obligatorio
1. Inventariar documentos, títulos, autores, ediciones, idioma, licencia y SHA-256; registrar limitaciones de extracción.
2. Extraer secciones y fragmentos con localizadores reproducibles (página, capítulo, EPUB CFI cuando exista); conservar estructura original.
3. Detectar conceptos y entidades; normalizar sinónimos sin fusionar entidades distintas.
4. Extraer afirmaciones **atómicas**; clasificar como descriptiva, normativa, causal, hipótesis, recomendación u opinión. Separar contenido explícito de inferencias.
5. Enlazar cada afirmación a su fuente y fragmento; registrar confianza de extracción y estado de revisión por separado.
6. Proponer aristas semánticas tipadas. Una mera coocurrencia se representa como MENTIONS/CO_OCCURS, nunca como CAUSES o SUPPORTS.
7. Comparar autores solo con contexto equivalente (población, intervención, resultado, época); distinguir acuerdo, desacuerdo explícito, énfasis distinto y no comparable.
8. Cuando el usuario autorice investigación externa, buscar literatura científica y documentar estrategia, fecha, DOI/PMID verificados, población, diseño, resultados y limitaciones. Mantener evidencia externa separada de afirmaciones de los libros.
9. Validar IDs, referencias, duplicados, aristas huérfanas, fuentes y estados. Enviar relaciones ambiguas a revisión humana.
10. Exportar JSON de nodos/aristas, GraphML y opcionalmente JSON-LD/CSV; producir reporte de calidad y README. Solo afirmar que se generó un archivo o se subió a GitHub tras confirmar su existencia o commit.

## Ontología base
Nodos: Source, Author, Section, Passage, Claim, Concept, Intervention, Population, Outcome, Study, EvidenceAssessment.
Aristas: AUTHORED, CONTAINS, ANCHORED_IN, ASSERTS, MENTIONS, RELATES_TO, CONTRADICTS, AGREES_WITH, APPLIES_TO, EVALUATES, SUPPORTED_BY_STUDY, CHALLENGED_BY_STUDY.
Todas las aristas semánticas requieren source_claim_id, confidence, review_status y extractor_version.

## Registro mínimo de afirmación
```json
{
  "id": "claim:<source_hash>:<locator>:<hash>",
  "text": "Afirmación fiel a la fuente",
  "source_id": "source:...",
  "passage_id": "passage:...",
  "locator": {"chapter": null, "page": null, "epub_cfi": null},
  "kind": "descriptive",
  "extraction_confidence": null,
  "review_status": "unverified",
  "evidence_status": "not_assessed"
}
```

## Reglas de calidad
- Ninguna afirmación publicada sin source_id, passage_id y localizador; si falta, cuarentena.
- Ninguna arista causal basada solo en coocurrencia.
- Nunca inventar DOI, páginas, citas textuales, autores o resultados.
- Registrar incertidumbre, contradicciones y evidencia negativa.
- No versionar obras completas protegidas por derechos de autor; almacenar solo metadatos y citas breves permitidas.
- Para información biomédica, distinguir estudios preclínicos de clínicos, asociaciones de causalidad, y no convertir el grafo en prescripción.
- Para medicina tradicional china, preservar terminología de la fuente y diferenciar teoría tradicional de mecanismos biomédicos validados.

## Salida esperada
- graph.json (nodes, edges, metadata)
- provenance.json (source hashes, locators, extraction settings)
- quality_report.json (conteos, huérfanos, revisiones, cobertura)
- graph.graphml (si hay conversor disponible)
- README.md (metodología, limitaciones y reproducción)
- optional evidence.json (solo si se hizo búsqueda externa)

## Verificación final
Comprobar consistencia de extremos de aristas, unicidad de IDs, anclaje documental, cobertura y validez de exportaciones. Informar qué se ejecutó realmente y qué permanece planificado.

## Referencias
- Véase ../../grafo-crianza/SPEC.md para un caso de aplicación.
- Véase references/schema.md para reglas de modelado y revisión.
