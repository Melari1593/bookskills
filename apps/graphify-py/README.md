# Graphify como aplicación Python en bookskills

Este paquete instala y ejecuta [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) mediante su distribución oficial `graphifyy`, fijada en la versión **0.9.91**. Incluye los extras `pdf` y `office` para documentos. El código de Graphify se obtiene del paquete oficial durante la instalación; este directorio contiene un lanzador, no una copia modificada del proyecto.

## Instalar

Requiere Python 3.10 o superior. Desde este directorio:

```bash
python -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install .
```

En Windows, usar `.venv\Scripts\python` en lugar de `.venv/bin/python`.

## Ejecutar

```bash
.venv/bin/bookskills-graphify --help
.venv/bin/bookskills-graphify extract /ruta/al/proyecto --code-only
.venv/bin/bookskills-graphify cluster-only /ruta/al/proyecto
.venv/bin/bookskills-graphify query "¿Qué conecta estos conceptos?" --graph /ruta/al/proyecto/graphify-out/graph.json
```

También funciona como módulo: `.venv/bin/python -m bookskills_graphify --help`. El comando original `graphify` queda instalado en el mismo entorno. `extract --code-only` analiza código de forma local y produce `graphify-out/graph.json`; `cluster-only` genera también `graph.html` y `GRAPH_REPORT.md`. Para documentos y PDF, ejecutar `extract` con un backend semántico configurado siguiendo la documentación oficial. Consulta las opciones actuales con `--help`.

La salida `graphify-out/` es generada a partir de los archivos que se analicen; no se incluye en este repositorio. Las funciones de análisis semántico de documentos pueden requerir configuración de un modelo o credenciales según el modo elegido.

## Procedencia y licencia

Dependencia: [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify), paquete `graphifyy==0.9.91`, licencia [Apache 2.0](https://github.com/Graphify-Labs/graphify/blob/v8/LICENSE). Conservar sus avisos y términos cuando se redistribuya el paquete original. Este lanzador no incorpora código fuente de Graphify.
