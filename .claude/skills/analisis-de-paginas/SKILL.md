---
name: analisis-de-paginas
description: Analiza sitios web y aplicaciones, identifica público objetivo, funcionalidades, UX, canales de venta, modelo de negocio, competidores y oportunidades de integración técnica. Produce benchmarking y especificaciones implementables.
---
# Skill: Análisis integral de páginas web

## Activación
Usar cuando se solicite analizar una URL, auditar UX, identificar público y utilidades, evaluar canales comerciales, comparar competidores, diseñar una plataforma similar o planificar su integración con un repositorio existente.

## Entradas
- URL o conjunto de URLs.
- Mercado, idioma y sector (si se conocen).
- Objetivo: investigación, benchmark, rediseño, validación de negocio o integración.
- Repositorio GitHub de destino (opcional).

## Flujo de análisis
1. **Verificación**: abrir sitio y rutas clave (inicio, producto, precios, FAQ, compra, contacto, privacidad); registrar fecha y enlaces. Si no es accesible, señalarlo.
2. **Descripción**: propósito, propuesta de valor, arquitectura de información y recorrido principal.
3. **Público**: segmentos B2C/B2B, JTBD, problemas y motivaciones; separar segmentos confirmados de hipótesis.
4. **Funcionalidades**: inventariar lo verificable (catálogo, cuenta, pagos, reservas, contenido, comunidad, formularios, analítica visible).
5. **UX**: evaluar claridad, navegación, contenido, CTA, formularios, confianza, móvil y accesibilidad. Etiquetar observaciones heurísticas; no fingir pruebas o mediciones.
6. **Ventas**: canales orgánicos, pagados, redes, presencial, alianzas, embudos, ingresos confirmados frente a hipotéticos.
7. **Benchmarking**: seleccionar 3-7 competidores reales cuando se solicite; documentar URL, evidencia y fecha; usar NV para no verificado.
8. **Oportunidades**: detectar brechas y formular hipótesis priorizadas por impacto, confianza, esfuerzo y riesgo.
9. **Integración técnica**: si hay repositorio, revisar README, dependencias, rutas, servicios, datos, autenticación, checkout, despliegue y pruebas. Proponer reutilización, módulos nuevos, riesgos, migraciones y fases. Nunca afirmar cambios no realizados.
10. **PRD/spec**: definir objetivo, personas, alcance MVP, sitemap, flujos, historias con criterios de aceptación, entidades, permisos, integraciones, métricas, requisitos no funcionales y backlog.
11. **Salida**: informe con hallazgos, tabla de evidencia, recomendaciones priorizadas, limitaciones y fuentes.

## Plantilla de informe
1. Ficha de la página (URL, fecha, mercado).
2. Descripción y propuesta de valor.
3. Segmentos y necesidades.
4. Funcionalidades comprobadas.
5. Auditoría UX (fortalezas, fricciones, hipótesis).
6. Canales de captación y venta.
7. Modelo de negocio.
8. Benchmarking (si aplica).
9. Oportunidades y priorización.
10. Arquitectura de integración y PRD (si aplica).
11. Evidencias, riesgos y siguientes pasos.

## Matriz de comparación
| Plataforma | Mercado | Audiencia | Funcionalidades | UX observada | Compra | B2B | Canales | Evidencia | Fecha |
|---|---|---|---|---|---|---|---|---|---|
| Nombre | Región | Segmentos | Confirmadas/NV | Heurística/NV | Sí/No/NV | Sí/No/NV | Identificados | URL | AAAA-MM-DD |

## Matriz de oportunidades
| Problema | Evidencia | Propuesta | Usuario | Impacto (1-5) | Confianza (1-5) | Esfuerzo (1-5) | Riesgo | Validación |
|---|---|---|---|---:|---:|---:|---|---|

## Plan de integración con GitHub
- Inventario de stack, archivos y servicios.
- Mapa de componentes reutilizables y dependencias.
- Arquitectura objetivo con rutas, datos, roles y APIs.
- Backlog ordenado en MVP, fase 2 y fase 3.
- Criterios de aceptación, pruebas de regresión y despliegue.
- Trabajar en rama separada cuando se implementen cambios y verificar compilación antes de fusionar.

## Casos de referencia
- Feria de maternidad: https://gestarconamor.com/feria-gestar-con-amor-bogota/
- Skill especializada: ../analisis-ferias-maternidad/SKILL.md
- Ejemplo de integración: repositorio Melari1593/rehabilitacion-muscular (Next.js, Shopify, cursos, análisis de postura y control prenatal); validar el estado actual antes de reutilizarlo.

## Rigor y seguridad
No inventar métricas de tráfico, ventas, conversiones, resultados UX, accesibilidad, precios o integraciones. Diferenciar confirmado, inferido, propuesto y no verificado. No convertir hipótesis de mercado en hechos. Para datos de salud, exigir minimización, consentimiento y evaluación normativa aplicable. Incluir URLs y fechas en hallazgos basados en web.
