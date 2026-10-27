# SPEC — Grafo semántico y científico de crianza
Versión: 1.0.0 | Estado: propuesta | Fecha: 2026-10-27
Repositorio: Melari1593/bookskills

## 1. Objetivo
Evolucionar el grafo comparado de *Más crianza, menos terapia* (Luciano Lutereau, 2018) y *La consciencia y la empatía en la crianza* (Ana Acosta Rodríguez, 2019) desde coocurrencias de conceptos hacia afirmaciones verificables, relaciones tipadas, comparación entre autores y evidencia científica independiente.

## 2. Línea base y alcance
Línea base reportada: 2 libros, 63 secciones, 19 conceptos, 84 nodos y 241 relaciones. **Son cifras previas por auditar**, no verificadas en este documento.
Incluye ingestión EPUB, trazabilidad de fragmentos, ontología, extracción semántica, contraste entre autores, evaluación de evidencia, GraphRAG, exportaciones y visualización. No incluye diagnóstico, recomendaciones clínicas automatizadas ni inferencia causal desde coocurrencias.

## 3. Principios
- Nunca convertir coocurrencia en afirmación causal.
- Separar rigurosamente postura del autor, inferencia del extractor y evidencia externa.
- Cada afirmación debe tener fuente, localizador y fragmento verificable; si no, estado `unverified`.
- Mantener incertidumbre, desacuerdo y evidencia negativa.
- Proteger derechos de autor: guardar fragmentos mínimos para auditoría; no publicar textos íntegros de EPUB protegidos.
- No utilizar el grafo como sustituto de asesoramiento clínico.

## 4. Ontología mínima
Nodos: `Book`, `Author`, `Section`, `Passage`, `Claim`, `Concept`, `ParentalPractice`, `DevelopmentStage`, `PsychologicalProcess`, `Outcome`, `Study`, `EvidenceAssessment`, `Intervention`.
Aristas: `AUTHORED`, `CONTAINS`, `SUPPORTED_BY_PASSAGE`, `ASSERTS`, `MENTIONS`, `RELATES_TO`, `PROPOSES`, `CRITIQUES`, `CONTRADICTS`, `AGREES_WITH`, `APPLIES_TO`, `STUDIES`, `SUPPORTED_BY_STUDY`, `CHALLENGED_BY_STUDY`.
Las aristas semánticas necesitan `source_claim_id`, `confidence`, `review_status` y `extractor_version`. `SUPPORTED_BY_STUDY` no implica causalidad ni calidad alta.

## 5. Contratos de datos
```json
{
  "id": "claim:book1:chapter3:0001",
  "type": "Claim",
  "text": "Afirmación normalizada, pendiente de extracción",
  "asserted_by": "author:book1",
  "book_id": "book:1",
  "section_id": "section:1:3",
  "passage_id": "passage:1:3:15",
  "locator": {"chapter": "3", "epub_cfi": null},
  "claim_kind": "descriptive",
  "polarity": "positive",
  "age_range_months": null,
  "extraction_confidence": null,
  "review_status": "unverified",
  "evidence_status": "not_assessed",
  "extractor_version": "0.1.0"
}
```
Campos adicionales: `created_at`, `source_hash`, `language`, `limitations`, `reviewer_id`, `reviewed_at`. IDs deterministas por fuente+localizador+contenido normalizado. Para estudios: DOI/PMID, población, diseño, comparador, desenlaces, tamaño de efecto, incertidumbre, sesgo y fecha de búsqueda. Calidad de evidencia independiente de confianza de extracción.

## 6. Pipeline
1. Ingestar EPUB con metadatos, capítulos y localizadores reproducibles; registrar SHA-256.
2. Normalizar conceptos, resolver sinónimos y deduplicar con revisión de ambigüedades.
3. Extraer afirmaciones atómicas y clasificarlas (descriptiva, normativa, causal, recomendación, opinión).
4. Anclar cada afirmación a un pasaje y registrar la cita mínima y su ubicación.
5. Detectar relaciones y contradicciones; exigir evidencia textual para cada relación.
6. Ejecutar revisión humana en relaciones de riesgo, baja confianza o contradicción.
7. Enriquecer mediante búsqueda bibliográfica reproducible (fecha, consulta, filtros); registrar evidencia externa sin atribuirla a los libros.
8. Exportar JSON, JSON-LD, GraphML y CSV; cargar opcionalmente a Neo4j.
9. Indexar pasajes autorizados y afirmaciones validadas para GraphRAG; responder con citas y abstención ante falta de evidencia.

## 7. Comparación entre autores
Comparar afirmaciones con misma población, etapa, intervención y resultado. Etiquetas: `agreement`, `explicit_disagreement`, `different_emphasis`, `not_comparable`, `insufficient_context`. Nunca etiquetar como contradicción solo porque un autor omita un tema.

## 8. Evidencia científica
Fuentes candidatas: PubMed, Cochrane, OMS y UNICEF. Registrar protocolo de búsqueda, criterios de inclusión, fecha de consulta y limitaciones. Evaluar diseño, riesgo de sesgo, consistencia, precisión, aplicabilidad y certeza; distinguir consenso, hipótesis y opinión. Prohibido fabricar DOI, resultados o niveles de evidencia.

## 9. Consultas de aceptación
- ¿Qué afirma cada autor sobre límites en primera infancia? Mostrar fragmentos y capítulos.
- ¿Qué afirmaciones sobre berrinches son compatibles o contradictorias? Mostrar motivo y revisión.
- ¿Qué estudios respaldan una intervención específica en edades de 24–48 meses? Mostrar población y calidad.
- ¿Qué relaciones carecen de fuente verificable? Deben poder filtrarse.
- ¿Qué afirmaciones no cuentan con evidencia externa? Deben distinguirse de evidencia contraria.

## 10. Criterios de aceptación (MVP)
- 100 % de `Claim` publicados con `book_id`, `section_id`, `passage_id` y localizador; de lo contrario quedan en cuarentena.
- 100 % de aristas semánticas con procedencia y estado de revisión.
- Cero afirmaciones etiquetadas como científicamente respaldadas sin referencia externa identificable.
- Exportaciones JSON y GraphML válidas y reimportables; prueba de integridad de IDs y extremos de aristas.
- Pruebas de no atribución: ninguna evidencia externa se presenta como texto de autor.
- Muestra estratificada revisada manualmente; registrar precisión por tipo de relación y errores, sin prometer umbrales no medidos.
- Respuestas GraphRAG incluyen procedencia o indican explícitamente que no hay respaldo.

## 11. Organización sugerida
```text
grafo-crianza/
  SPEC.md
  schema/ontology.jsonld
  schema/claim.schema.json
  data/README.md
  src/ingest.py
  src/extract_claims.py
  src/validate.py
  src/export.py
  tests/test_provenance.py
  tests/test_graph_integrity.py
  docs/evidence_protocol.md
```
Los archivos distintos de SPEC.md son **entregables futuros**, no implementaciones ya existentes.

## 12. Fases
**Fase 0:** auditar artefactos existentes y verificar cifras.  
**Fase 1:** ontología, IDs y trazabilidad.  
**Fase 2:** extracción semántica y revisión humana.  
**Fase 3:** comparación entre autores y evidencias.  
**Fase 4:** GraphRAG, visualización y pruebas de regresión.

## 13. Riesgos y mitigaciones
Alucinación de relaciones → verificación de pasajes y revisión. Sesgo entre autores → categorías neutrales. Derechos de autor → no versionar EPUB ni pasajes extensos. Información de menores → no incluir datos personales. Obsolescencia científica → fecha de búsqueda y revalidación. Sobreinterpretación clínica → etiquetas de evidencia y advertencias contextuales.

## 14. Definition of Done
Especificación aprobada; línea base auditada; ontología validada; afirmaciones trazables; exportaciones reproducibles; pruebas de integridad superadas; documentación de limitaciones y protocolo de evidencia disponibles.
