---
name: medical-visual-ai
description: Convierte documentos biomédicos en especificaciones de ilustración científica, prompts para Nano Banana y materiales educativos con trazabilidad y revisión clínica.
---
# Medical Visual AI

## Activación
Utilizar cuando se solicite transformar documentos médicos, científicos o de educación sanitaria en ilustraciones, infografías, flashcards o guiones visuales para Nano Banana.

## Entradas
Documento fuente, audiencia, especialidad, objetivo, idioma, formato, estilo y cantidad de piezas. Preguntar únicamente por parámetros imprescindibles; aplicar valores predeterminados para los demás.

## Flujo obligatorio
1. Leer la fuente completa o declarar explícitamente qué secciones fueron revisadas.
2. Extraer conceptos, cifras, unidades, fechas, recomendaciones, grado de evidencia y ubicación de origen (página, sección o líneas).
3. Construir un catálogo de piezas con `id`, `objetivo`, `tipo`, `fuente`, `contenido_verificado`, `incertidumbres` y `estado_revision`.
4. Distinguir datos documentados, inferencias y elementos de diseño. No rellenar vacíos clínicos.
5. Seleccionar el módulo visual apropiado: anatomía, fisiología, patología, biología molecular, procedimientos, desarrollo o educación de pacientes.
6. Crear un prompt independiente por pieza con restricciones anatómicas, texto permitido, composición y aspectos que deben evitarse.
7. Generar imágenes únicamente cuando el usuario solicite generarlas; crear prompts o especificaciones no implica generar imágenes.
8. Validar contra el documento: cifras, cronología, relaciones, nomenclatura, etiquetas, riesgo de error y accesibilidad. Marcar `pendiente_revision_profesional` si corresponde.
9. Entregar prompts, catálogo y observaciones de revisión. No afirmar validación médica automática.

## Prompt universal por pieza
Actúa como ilustrador médico científico y diseñador instruccional. Produce una imagen [TIPO] sobre [CONCEPTO], para [AUDIENCIA], nivel [NIVEL], basada exclusivamente en [FUENTE Y LOCALIZACIÓN]. Incluye [ESTRUCTURAS Y RELACIONES VERIFICADAS]. Composición [COMPOSICIÓN], estilo [ESTILO], relación de aspecto [FORMATO], idioma [IDIOMA]. Etiquetas permitidas: [ETIQUETAS]. No añadir cifras, estructuras, mecanismos, recomendaciones o referencias no verificadas. Distinguir esquemas conceptuales de representaciones anatómicas. Reservar espacio para textos extensos en posproducción.

## Reglas críticas
- El documento es la fuente primaria; no cambiar sus recomendaciones silenciosamente.
- Para verificación externa, identificar fuentes y fechas por separado.
- No inventar referencias, anatomía, evidencia, dosis, proporciones o mecanismos.
- Los diagramas conceptuales deben etiquetarse como tales.
- No presentar imágenes generadas como pruebas diagnósticas o fotografías clínicas reales.
- Para material de pacientes, lenguaje claro y advertencias de seguridad cuando proceda.
- Si Nano Banana no admite dimensiones exactas, pedir relación de aspecto y diseñar márgenes para posterior edición.
- Los textos extensos y tablas deben componerse fuera del generador visual cuando la legibilidad sea crítica.

## Salida
Catálogo trazable, un prompt por imagen, restricciones negativas, revisión de exactitud y elementos pendientes de validación clínica.
