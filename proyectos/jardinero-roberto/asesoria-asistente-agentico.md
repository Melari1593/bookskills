# Asesoría: asistente agéntico de cultivo para Roberto

Fecha: 2026-11-19
Marco: *La empresa agéntica* (Hodjat y Blondeau, O'Reilly, 2026), skill `empresa-agentica-grafo`, modo Asesorar.

Supuestos: Roberto usa WhatsApp y envía texto y fotos. Karla construye y supervisa el sistema. Corregir si no aplica.

## 1. Veredicto

Encaja, con límites. Al principio basta un asistente pequeño: un coordinador y dos agentes. Roberto pregunta, el sistema responde con la evidencia del skill `cultivo` y pasa a un humano lo que es riesgoso. Un sistema de muchos agentes sería excesivo para un solo usuario.

## 2. Preparación

| Dimensión | Estado | Razón |
|---|---|---|
| Liderazgo | Verde | Karla lo impulsa y lo supervisa |
| Datos | Ámbar | La base de evidencia apenas empieza: guía de esquejes y compost, y el skill `cultivo` |
| Gobernanza | Ámbar | Falta definir qué temas se pasan a un humano |
| Arquitectura | Ámbar | Falta elegir el canal y el modelo |
| Recursos técnicos | Verde | Karla sabe construirlo |
| Gestión del cambio | Ámbar | Hay que confirmar que Roberto lo usará en su día a día |

## 3. Diseño propuesto

- **Coordinador:** recibe cada mensaje, lo clasifica y guarda el registro de todo.
- **Agente de cultivo:** responde a partir del skill `cultivo` y de la base de evidencia. Da pasos concretos con su nivel de confianza.
- **Agente de protección:** revisa cada respuesta antes de enviarla. Detecta plaguicidas, plantas tóxicas o medicinales y diagnósticos hechos con fotos.
- **Lo que hace el código, no el LLM:** las reglas fijas (lista de temas que se derivan), el registro y los datos de Roberto (teléfono, ubicación).
- **Lo que no necesita agente:** los recordatorios de riego y la bitácora de esquejes pueden ser software simple (1.3, 9.1).

## 4. Autonomía

- **Responde solo:** técnicas de esqueje, sustratos, compost, riego y luz.
- **Un humano aprueba cada caso:** dosis de plaguicidas, consumo de plantas medicinales y plagas identificadas por foto.
- **Umbral:** el sistema genera la respuesta 3 veces. Si las versiones no coinciden, responde «lo consulto» y avisa a Karla.
- **Botón de apagado:** Karla puede desactivarlo en cualquier momento.

## 5. Riesgos

- **Operacional:** un mal consejo mata una planta. El costo es bajo y se acepta.
- **Responsabilidad:** un consejo sobre químicos o plantas tóxicas puede ser grave. Por eso esos temas se derivan siempre a un humano.
- **Privacidad:** las fotos, la ubicación y el teléfono son datos personales. La SIC indica que las herramientas de IA están sujetas a la Ley 1581 de 2012. La Circular Externa 002 de 2024 de la SIC da lineamientos para el tratamiento de datos personales en sistemas de IA. Hay una reforma de la Ley 1581 radicada en la Cámara en agosto de 2026; verificar su estado.
- **RACI mínimo:** el agente decide sobre técnicas de cultivo. Karla responde por los temas derivados y por los límites de datos. Todo queda registrado en el coordinador.

## 6. Piloto y ROI

- **Duración:** 6 semanas.
- **Línea base:** porcentaje de esquejes que enraízan y tiempo que Roberto gasta buscando respuestas.
- **Grupo de control:** la mitad de los lotes sigue el protocolo del asistente y la otra mitad su método habitual.
- **Criterio de éxito:** enraizamiento igual o mayor, más del 80 % de preguntas resueltas sin derivar y ningún consejo riesgoso enviado.

## 7. Construir o comprar

- **Comprar:** el modelo y el canal (WhatsApp Business).
- **Construir:** la base de evidencia, el agente de protección y las reglas.
- **Contra el lock-in:** pasarela neutral entre los agentes y el proveedor del modelo, y protocolos abiertos. MCP conecta las aplicaciones de IA con herramientas y datos; A2A comunica agentes independientes. Desde agosto de 2026, A2A está con MCP en la Agentic AI Foundation de la Linux Foundation.

## 8. Para leer

Secciones 2.1–2.4 (encaje y preparación), 1.2–1.3 (varios agentes, LLM frente a código), 6.1–6.3 (autonomía), 7.3, 7.5 y 7.7 (riesgos, RACI y orquestador), 4.2 y 4.7 (ROI y piloto), 8.1–8.2 y 8.5 (lock-in y protocolos).

Páginas pendientes: el archivo `grafo.json` del libro no está en este repositorio. Los prerrequisitos entre secciones son una interpretación pedagógica, no una cita de los autores.

## Fuentes

- [RCN Radio: la SIC responde sobre IA y datos personales](https://newsroom.rcnradio.com/actualidad/como-proteger-tus-datos-personales-con-el-auge-de-la-ia-la-sic-responde)
- [SIC, Circular Externa 002 de 2024](https://sedeelectronica.sic.gov.co/sites/default/files/normativa/Circular%20Externa%20No.%20002%20del%2021%20de%20agosto%20de%202024.pdf)
- [Facephi: reforma de la Ley 1581 radicada en agosto de 2026](https://facephi.com/observatory/reforma-ley-1581-biometria-dato-sensible/)
- [Axios: A2A se une a la Agentic AI Foundation](https://axios.com/2026/08/17/a2a-agentic-ai-foundation-open-ai-standards)
- [Algeria Tech News: A2A y MCP bajo la AAIF](https://algeriatech.news/?p=35142)
