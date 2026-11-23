---
name: empresa-agentica-grafo
description: Explora el grafo de La empresa agéntica (Hodjat y Blondeau, O'Reilly, 2026) y aplica sus marcos a un proyecto real. Úsala para localizar conceptos (AAOSA, sly_data, RACI de segunda capa, pasarela de modelos, MCP/A2A), trazar una ruta de lectura con páginas, entregar el HTML interactivo, o evaluar y diseñar un sistema multiagente — encaje del caso, preparación, autonomía, riesgos, ROI, construir o comprar, lock-in — aunque la persona no nombre el libro.
---

# La empresa agéntica — grafo y asesor

Fuente: *La empresa agéntica*, Babak Hodjat y Antoine Blondeau (O'Reilly, ed. en español, 2026).
El grafo tiene introducción y 9 capítulos, 68 secciones, 63 conceptos, 12 figuras y 184 prerrequisitos.
Las páginas son las impresas del libro.

Archivos:
- `references/grafo.json` — capítulos, secciones, conceptos (`items`) y prerrequisitos (`requires`).
- `assets/grafo_empresa_agentica.html` — mapa interactivo autocontenido.
- `scripts/ruta.py` — busca un tema y lista la ruta de lectura.

Si la carpeta no tiene estos archivos, búsquelos en el repositorio GitHub `Melari1593/bookskills`,
en `.claude/skills/empresa-agentica-grafo/`. La copia publicada del grafo está en `grafos/la-empresa-agentica/`.

## Elegir el modo

- Modo **Explorar**: la persona pregunta qué dice el libro, dónde está un tema, cómo se conectan dos ideas o qué leer primero.
- Modo **Asesorar**: la persona describe un proyecto, una empresa o una decisión, y quiere aplicar el libro.
- Si la petición tiene las dos partes, haga primero Asesorar y añada al final la ruta de lectura de los conceptos que usó.

## Modo Explorar

1. Ejecute `python scripts/ruta.py "término"`. Acepta un término («AAOSA»), un número de sección («7.5»), un id de concepto («raci_segunda_capa») o «capítulo 8».
2. Lea en `grafo.json` el resumen y el esquema (`formula`) de los nodos encontrados.
3. Explique la idea con palabras propias. No copie pasajes del libro.
4. Dé la ruta de lectura en orden, con número de sección y página impresa.
5. Diga que los prerrequisitos son una interpretación pedagógica, no una cita de los autores.
6. Si la persona quiere ver el mapa, entregue `assets/grafo_empresa_agentica.html`. Tiene tres vistas, buscador, leyenda filtrable y el botón «Trazar prerrequisitos».
7. Si la persona quiere cambiar el grafo, edite `grafo.json` y reconstruya el HTML con la skill `grafo-de-libro`.

Números de sección: «I.x» es la introducción. El libro no numera las secciones ni las viñetas del capítulo 4 ni del capítulo 7. Esos números son del grafo.

## Modo Asesorar

Objetivo: decidir si conviene un sistema agéntico y cómo construirlo con riesgo controlado.
Primero entienda el caso. Si faltan datos clave (flujo de trabajo, datos que toca, quién es responsable, presupuesto), pregunte una vez. Si la persona no está, suponga lo razonable y dígalo.

Recorra los pasos en este orden. Cada paso cita su sección del libro.

### 1. ¿Encaja un sistema agéntico? (2.1–2.3)
- Pregunte qué se automatiza: ¿pasos fijos o resultados? Pasos fijos: basta RPA o código. Resultados con juicio y datos no estructurados: candidato agéntico.
- Clasifique el valor en una de tres capas: productividad operativa, calidad y resiliencia, sistemas adaptativos.
- Descarte o limite el caso cuando dependa de juicio subjetivo, de conocimiento tácito no registrado o de un error de alto costo sin revisión humana.

### 2. Preparación de la organización (2.4)
Califique seis dimensiones con semáforo rojo, ámbar o verde: liderazgo, infraestructura de datos, gobernanza y riesgo, arquitectura, recursos técnicos, gestión del cambio.
Una dimensión en rojo es una tarea previa, no un detalle.

### 3. Diseño del sistema (I.3, 1.2–1.3, 5.1–5.9, 6.5, 9.1)
- Parta de los flujos de trabajo reales, no del organigrama (5.1).
- Divida en varios agentes con roles claros, no en un agente que lo hace todo (1.2). Ventajas: menos contexto por agente, modelos más pequeños, ajuste fino por rol, menor costo.
- Asigne al LLM el razonamiento y el texto no estructurado. Asigne al código las reglas y lo que debe ser consistente. Pase los datos sensibles por código, sin el LLM (sly_data, 1.3).
- Si una parte no necesita autonomía, hágala módulo de software, no agente (1.3, 9.1).
- Coordinación: jerarquía donde cada agente coordina a sus subordinados (AAOSA, 5.4).
- Ancle cada agente a datos y sistemas reales. Use solo herramientas o habilidades registradas y revisadas (5.3, 5.6).
- Revise la granularidad y los errores comunes: bucles sin salida, agentes sobrecargados, un coordinador único como cuello de botella (6.5, 9.1).

### 4. Nivel de autonomía (1.3, 6.1–6.2)
Aplique el proceso de decisión en este orden:
1. Escriba las responsabilidades y los límites en el prompt del sistema.
2. Añada agentes de protección que vigilen a los demás.
3. Ponga reglas deterministas para lo que no admite excepciones.
4. Mida la incertidumbre (por ejemplo, varias muestras de la misma respuesta) y derive a un humano sobre un umbral.
5. Dé a un humano un botón de desconexión.
Defina qué decisiones tienen humano «en el ciclo» (aprueba cada una) y cuáles «sobre el ciclo» (supervisa y puede intervenir) (6.3).
Mida la confianza con componentes concretos y vigílelos de forma continua (6.2).

### 5. Riesgos y responsabilidad (4.1, 7.1–7.9)
- Recorra cinco riesgos: estratégico, organizacional, gobernanza y cumplimiento, operacional, responsabilidad legal (4.1).
- Recorra el panorama técnico: acciones inseguras, vulnerabilidades, privacidad, fuga de propiedad intelectual (7.3).
- Las restricciones críticas no deben vivir solo en el contexto del agente, porque el agente puede truncarlo (7.3).
- Arme un RACI de segunda capa: alcance del juicio del agente, umbrales de riesgo, límites de datos, resolución de conflictos y registro (7.5).
- Haga del orquestador el plano de control: toda solicitud pasa por él y él guarda la auditoría (7.7).
- Organice las mitigaciones en tres pilares: barreras técnicas, supervisión humana, gobernanza y transparencia (7.8).
- Señale el marco regulatorio que aplica (7.9). Verifique en la web la versión vigente, porque estas normas cambian.

### 6. Valor y ROI (4.1–4.7)
- Mida con grupo de control: resultado con IA menos resultado sin IA (4.2).
- Defina las unidades de valor propias del caso. No use una plantilla genérica (4.5).
- Piense en plataforma más cartera de casos, no en un proyecto aislado (4.5).
- Para el piloto: fije línea base y criterios de éxito antes de empezar, y diseñe para reutilizar la plataforma. Así se evita el «purgatorio de pilotos» (4.7).

### 7. Construir o comprar, y evitar el lock-in (4.6, 8.1–8.5)
- Decida con cuatro criterios: diferenciación, sensibilidad de los datos, talento interno, interoperabilidad y salida (4.6).
- Regla práctica del libro: comprar modelos e infraestructura; construir orquestación, barreras y agentes del dominio.
- Ponga una pasarela neutral entre los agentes y los proveedores de modelos (8.2).
- Exponga las acciones de negocio en un catálogo con API estables (8.1).
- Instrumente el costo en cada capa y ponga topes (8.2).
- Para actualizar sin riesgo: separe capas, versione, despliegue de forma progresiva, tenga reversión (8.3).
- Use MCP para herramientas y datos, y A2A entre agentes (8.5). Verifique en la web el estado actual de estos protocolos.

### Formato de la respuesta del modo Asesorar

Use estos títulos, en este orden:
1. **Veredicto** — encaja, encaja con límites o no encaja. Una o dos frases.
2. **Preparación** — tabla de seis dimensiones con semáforo y la razón.
3. **Diseño propuesto** — agentes, rol de cada uno, qué hace el LLM y qué hace el código, coordinación.
4. **Autonomía** — qué decide el sistema solo, qué aprueba un humano, umbrales.
5. **Riesgos** — los principales, su mitigación y el RACI resumido.
6. **Piloto y ROI** — línea base, métrica, grupo de control, criterio de éxito.
7. **Construir o comprar** — decisión por componente y medidas contra el lock-in.
8. **Para leer** — secciones y páginas del libro que respaldan lo anterior.

Ajuste la extensión al caso. Una pregunta puntual («¿cuánta autonomía doy a este agente?») usa solo el paso que aplica, más «Para leer».

## Límites

- El grafo resume el libro con palabras propias. No reproduzca pasajes, tablas ni figuras.
- Las cifras de los casos (por ejemplo, la caída de tickets de 1C o la revisión de código) son de los autores. Atribúyalas al libro.
- El libro describe productos, protocolos y normas de 2025–2026. Verifique en la web cualquier dato actual antes de recomendarlo.
- Salud, finanzas y otros sectores regulados exigen además su propia normativa. El libro no la sustituye.
