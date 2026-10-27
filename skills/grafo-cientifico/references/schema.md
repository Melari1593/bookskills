# Modelo de datos y criterios de revisión

## Nodos
Cada nodo incluye `id`, `type`, `label`, `properties`. Source registra título, autor, fecha, tipo, hash y restricciones de publicación. Passage registra source_id, section_id, locator y hash del fragmento. Claim registra passage_id, texto normalizado, clasificación y estados independientes de extracción y evidencia.

## Aristas
`source`, `target`, `type`, `source_claim_id`, `confidence`, `review_status`, `extractor_version`. Los extremos deben existir. Las relaciones de procedencia pueden usar `source_claim_id: null`; las relaciones semánticas no.

## Estados
review_status: unverified | needs_review | verified | rejected.
evidence_status: not_assessed | insufficient | mixed | supported | challenged.
Una etiqueta `supported` requiere al menos una referencia identificable y evaluación documentada; no implica evidencia de alta certeza.

## Comparaciones
agreement | explicit_disagreement | different_emphasis | not_comparable | insufficient_context.
Registrar criterio de comparación y fragmentos de ambas fuentes.

## Pruebas mínimas
IDs únicos; sin aristas huérfanas; claims anclados; no atribuir estudios externos a autores; no inferir causalidad de coocurrencias; exportaciones legibles; auditoría manual estratificada y métricas reportadas sin cifras inventadas.
