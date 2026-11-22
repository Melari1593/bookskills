---
name: bioelectronic-fungal-machines
description: Analiza bioelectricidad de hongos, diseña conceptualmente biosensores miceliales, compara dispositivos bioelectrónicos y construye grafos de conocimiento basados en Fungal Machines (Adamatzky, ed., 2023). Úsala para protocolos de medición, análisis de señales, modelado de compuertas lógicas y evaluación de evidencia.
---

# Bioelectronic & Fungal Machines

## Objetivo
Convertir literatura sobre electrofisiología fúngica en modelos verificables, grafos y propuestas experimentales reproducibles, sin confundir resultados observados con hipótesis o aplicaciones prospectivas.

## Fuentes
- Fuente principal: *Fungal Machines: Sensing and Computing with Fungi*, Andrew Adamatzky (ed.), Springer, 2023, DOI: 10.1007/978-3-031-38336-6.
- Grafo del repositorio: `../../grafos/fungal-machines/graph.json`, `nodes.csv`, `edges.csv`.
- El grafo es una extracción temática inicial, no una revisión sistemática. Los extractos del libro pueden contener errores de conversión de texto; comprobar números y unidades con la fuente primaria.
- No reproducir capítulos completos ni ilustraciones protegidas.

## Activación
Invocar con `$bioelectronic-fungal-machines <tarea>`.

## Procedimiento obligatorio
1. Identificar tarea: grafo, revisión, biosensor, bioelectrónica, análisis de señales, computación o docencia.
2. Recuperar conceptos y capítulos relevantes del grafo; verificar afirmaciones numéricas contra el libro original si está disponible.
3. Construir tabla de evidencia con: especie, sustrato, preparación, estímulo, respuesta, equipo, parámetros, controles, tamaño de muestra, limitaciones y cita/capítulo.
4. Etiquetar cada afirmación `observado`, `interpretación del autor`, `hipótesis`, `propuesta de diseño` o `no verificado`.
5. Para diseño experimental, definir variable independiente, variable dependiente, controles negativos, replicación biológica, muestreo, calibración, confusores, seguridad y criterios de éxito.
6. Para señales: preservar unidades y tasa de muestreo; inspeccionar deriva, ruido, artefactos y eventos; reportar umbrales, amplitud, ancho, intervalo entre picos, distribución e incertidumbre. No llamar potenciales de acción neuronales a señales extracelulares solo por su forma.
7. Para computación: especificar codificación de entradas/salidas, ventanas temporales, tabla de verdad, repetibilidad y tasa de error. Distinguir simulación de hardware vivo validado.
8. Entregar hallazgos, limitaciones, trazabilidad y archivos reproducibles cuando corresponda.

## Módulos
- M1 Electrofisiología: potenciales extracelulares, oscilaciones, trenes de picos, artefactos.
- M2 Biosensores y wearables: peso, presión, humedad, luz, compuestos químicos y respuestas de micelio.
- M3 Electrónica fúngica: capacitancia, comportamiento memristivo, filtros y transferencia de señal.
- M4 Computación fúngica: compuertas, discriminación de frecuencias, autómatas celulares y circuitos.
- M5 Cognición y lenguaje: hipótesis de comunicación; evitar antropomorfismo y afirmaciones de conciencia.

## Salidas estándar
- `evidence.csv`: claim_id,capitulo,especie,variable,resultado,unidad,tipo_evidencia,limitaciones.
- `nodes.csv` y `edges.csv` o `graph.json` con identificadores estables y procedencia.
- `protocol.md`: materiales, controles, mediciones, análisis, criterios de éxito, riesgos.
- `analysis.md`: resultados, incertidumbres, replicabilidad, posibles explicaciones alternativas.

## Seguridad y calidad
- Trabajar con especies no patógenas identificadas y fuentes autorizadas; no recomendar cultivo de especies psicoactivas o peligrosas.
- En montaje eléctrico con material húmedo: usar alimentación aislada de bajo voltaje y evitar conexión directa a la red.
- No extrapolar prototipos de laboratorio a dispositivos médicos ni atribuir capacidad diagnóstica sin validación clínica y regulatoria.
- Tratar diferencias de especies, electrodos, geometría, humedad, temperatura y sustrato como fuentes de confusión.

## Ejemplos
- `$bioelectronic-fungal-machines compara Pleurotus djamor y Ganoderma resinaceum en señales extracelulares`
- `$bioelectronic-fungal-machines diseña un biosensor conceptual de humedad con Pleurotus ostreatus`
- `$bioelectronic-fungal-machines analiza CSV de potencial eléctrico y devuelve eventos y controles de calidad`
- `$bioelectronic-fungal-machines construye subgrafo de compuertas lógicas con trazabilidad`
