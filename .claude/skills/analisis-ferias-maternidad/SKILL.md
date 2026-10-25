---
name: analisis-ferias-maternidad
description: Audita páginas de maternidad y ferias, compara competidores con evidencias, detecta oportunidades de mercado y genera especificaciones funcionales de una plataforma web.
---
# Skill: Inteligencia competitiva y diseño de plataformas de maternidad

## Activadores
Usar ante peticiones de análisis de páginas de maternidad, comparación de ferias, benchmarking, oportunidades de mercado, UX, canales comerciales o generación de un PRD/spec de plataforma.

## Flujo obligatorio
1. **Alcance**: determinar geografía, segmento (gestantes, posparto, primera infancia, B2B), objetivo y fecha.
2. **Fuentes**: visitar URL principal y páginas de compra, FAQ, servicios, contacto, expositores, privacidad y redes cuando sean accesibles. Registrar URL, fecha de consulta y estado (confirmado/inferido/no verificado).
3. **Auditoría individual**: propuesta de valor, segmentos, funcionalidades, arquitectura, CTAs, accesibilidad, móvil, confianza, precios, embudos B2C/B2B, monetización y datos.
4. **Competidores**: identificar 3-7 comparables relevantes mediante búsqueda; diferenciar competencia directa, indirecta y sustitutos. Nunca inventar empresas, tarifas, tráfico o funcionalidades.
5. **Matriz comparativa**: filas = competidores, columnas = audiencia, propuesta, oferta, compra, agenda, contenido, personalización, B2B, retención, canales, monetización, evidencia y fecha. Usar 'NV' cuando no se verifique. Una celda sin evidencia no equivale a ausencia de función.
6. **Puntuación opcional**: usar escala 0-4 por criterio (0 no observado con inspección suficiente, 1 rudimentario, 2 básico, 3 sólido, 4 destacado, NV no verificable). Calcular promedio ponderado solo de criterios evaluables y reportar cobertura; no comparar puntuaciones de coberturas muy distintas.
7. **Oportunidades**: derivar brechas, jobs-to-be-done y problemas. Priorizar por impacto, confianza de evidencia, esfuerzo y riesgo (ICE/RICE con supuestos explícitos). Separar ideas de hechos.
8. **Especificación de producto**: redactar PRD implementable: objetivo, personas, JTBD, casos de uso, alcance MVP/no alcance, journeys, sitemap, historias de usuario, criterios de aceptación, entidades y datos, roles/permisos, integraciones, métricas, accesibilidad, seguridad, privacidad, arquitectura sugerida, backlog y fases.
9. **Validación**: diseñar entrevistas, test de tareas, prototipo, eventos analíticos y experimentos A/B; no prometer resultados.
10. **Entrega**: resumen ejecutivo, tabla de fuentes, matriz, mapa de oportunidades, PRD y plan de medición; explicitar limitaciones.

## Plantilla de matriz
| Competidor | Tipo | Público | Funciones verificadas | Compra | B2B | Contenido | Diferenciador | Evidencia | Fecha |
|---|---|---|---|---|---|---|---|---|---|
| Nombre | Directo/indirecto | Segmentos | Lista o NV | Sí/No/NV | Sí/No/NV | Sí/No/NV | Hallazgo | URL | AAAA-MM-DD |

## Plantilla de oportunidades
| Problema/JTBD | Evidencia | Solución candidata | Segmento | Impacto 1-5 | Confianza 1-5 | Esfuerzo 1-5 | Riesgo | Prioridad |
|---|---|---|---|---:|---:|---:|---|---|

## Especificación funcional de referencia: plataforma de maternidad
**Visión**: acompañamiento continuo desde embarazo hasta primera infancia, combinando educación, eventos, comercio y servicios profesionales.

### Roles
- Visitante: consulta información pública.
- Familia: administra perfil, preferencias, inscripciones y compras.
- Expositor: gestiona perfil de marca, productos y contactos autorizados.
- Profesional: administra contenidos/servicios dentro de su habilitación.
- Organizador: administra ferias, programación, entradas y reportes.
- Administrador: gestiona usuarios, permisos, moderación y auditoría.

### MVP recomendado
- Landing segmentada y CMS con contenidos revisados.
- Catálogo de eventos, agenda, filtros e inscripción.
- Venta/reserva de entradas con pasarela externa, comprobante y QR.
- Portal B2B de solicitud de participación con seguimiento de estado.
- Registro opcional, consentimiento granular, panel personal básico.
- Notificaciones transaccionales y panel analítico de embudo.
- Diseño responsivo, accesibilidad WCAG 2.2 AA como objetivo.

### Fase posterior
Marketplace, cursos, itinerarios por etapa gestacional, comunidad moderada, panel avanzado de expositores y servicios clínicos solo tras evaluación normativa.

### Historias y criterios de aceptación (muestras)
- Como asistente quiero ver precio total, fecha, ubicación y condiciones antes de pagar. **Aceptación**: resumen y desglose visibles; si evento venció, compra deshabilitada.
- Como asistente quiero recibir entrada QR. **Aceptación**: QR único, verificación de estado y protección contra doble uso.
- Como expositor quiero solicitar un stand. **Aceptación**: formulario con consentimiento, número de solicitud y seguimiento.
- Como organizador quiero medir conversión. **Aceptación**: eventos `view_event`, `start_checkout`, `purchase`, `exhibitor_lead` documentados sin datos clínicos sensibles.

### Entidades sugeridas
User, Profile, Consent, Event, Session, Venue, TicketType, Order, PaymentReference, Ticket, CheckIn, Exhibitor, ExhibitorLead, Content, Notification, AuditLog. Minimizar datos y separar perfil clínico de comercio.

### Requisitos no funcionales
Autenticación segura, RBAC, cifrado en tránsito/reposo, backups, observabilidad, retención definida, eliminación/exportación de datos, rendimiento móvil y protección contra abuso de QR. No recopilar semanas gestacionales ni datos médicos sin propósito y base legal claros.

### Riesgos Colombia
Evaluar Ley 1581 de 2012 y normas aplicables de datos personales, protección del consumidor, comercio electrónico, publicidad sanitaria y habilitación de servicios de salud cuando corresponda. Evitar presentar información educativa como diagnóstico individual.

## Caso de referencia: Gestar con Amor Bogotá
- URL: https://gestarconamor.com/feria-gestar-con-amor-bogota/
- Análisis inicial: 2026-10-25; edición mencionada 7-8 marzo 2026 (evento pasado).
- Público: gestantes, madres recientes, familias; B2B marcas y profesionales.
- Oferta descrita: educación, entretenimiento, exposición comercial; entradas, sorteos, charlas, blog, contacto y preinscripción de expositores.
- Fricciones hipotéticas: dispersión de información, diferencias de tarifas históricas, gestión de acceso, escasa personalización; validar con observación.
- La puntuación heurística 3/5 del análisis anterior NO es un dato medido ni benchmark.

## Referencias iniciales
- https://gestarconamor.com/feria-gestar-con-amor-bogota/
- https://gestarconamor.com/compra-tu-boleta-bogota/
- https://gestarconamor.com/preinscripcion-feria/
- https://gestarconamor.com/
- https://gestarconamor.com/contactanos/

## Reglas de rigor
Distinguir confirmado, inferido, propuesto y no verificado. No afirmar inspección visual, test UX, velocidad, métricas, ingresos o funcionalidad no comprobados. Actualizar precios y fechas antes de recomendar decisiones. Para una comparación real buscar y citar fuentes actuales de cada competidor.
