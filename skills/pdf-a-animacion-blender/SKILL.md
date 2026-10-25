---
name: pdf-a-animacion-blender
description: Convierte una vía o mecanismo descrito en un PDF científico en un guion por escenas y un script de Python que lo anima en Blender, probado con renders. Úsala cuando pidan animar, ilustrar en 3D o hacer un video de una vía, ciclo o mecanismo de un artículo, revisión o capítulo.
---

# PDF → guion → script de Blender

Toma un PDF (artículo, revisión, capítulo) y entrega:
1. un **guion por escenas** fiel a la fuente;
2. un **script de Python (bpy)** autocontenido que construye una escena 2.5D y la anima;
3. una **hoja de contacto** con un fotograma renderizado por escena, como prueba de que funciona.

El valor está en la fidelidad al texto y en que el script se ejecute a la primera. La estética ya está resuelta en la plantilla.

## Archivos
- `scripts/plantilla_blender.py`: utilidades probadas (materiales, formas, textos, aparecer/desaparecer, trayectos, brillo, cambio de color, cámara, luces, títulos, leyenda) y un `construir()` mínimo de ejemplo. Parte siempre de aquí.
- `scripts/test_render.py`: ejecuta el script con `bpy`, renderiza un fotograma por escena y arma `hoja_contacto.png`.
- `examples/endocannabinoides_blender.py`: ejemplo completo (Di Marzo 2006, señalización endocannabinoide retrógrada, 8 escenas, 960 fotogramas) y `examples/endocannabinoides_hoja_contacto.png`.

`SKILL_DIR` en los comandos es la carpeta de esta skill.

## Flujo

### 1. Leer la fuente y elegir la vía
- Lee el PDF con la skill `pdf-reading` (o `pypdf`: texto por página a un archivo y lee solo las páginas relevantes).
- Si trae varias vías y la persona no dijo cuál, elige la más central, dilo en una línea y sigue. Pregunta solo si hay dos igual de centrales.
- Anota, con página:
  - **Compartimentos** (neurona pre/post, célula, núcleo, luz, plasma…).
  - **Actores**: moléculas, enzimas, receptores, canales y transportadores, y dónde están.
  - **Eventos en orden**: estímulo → síntesis → transporte → unión → efecto → inactivación.
  - **Lo que la fuente marca como hipotético** ("putativo", "no clonado"): se rotula así en pantalla.
- Todo lo que añadas y no esté en el PDF (mecanismos estándar, acoplamiento a proteínas G…) se anota para decirlo al entregar.

### 2. Escribir el guion
Tabla con: escena, fotogramas, título, subtítulo y qué se mueve.
- 6–8 escenas de ~100–150 fotogramas a 24 fps (30–45 s), salvo que pidan otra duración.
- Escena 0 = presentación (compartimentos, rótulos, leyenda). Última = resumen (cada vía en una línea, más la implicación terapéutica o clínica si la fuente la da).
- Un evento principal por escena. Subtítulo ≤ 100 caracteres, en el idioma de la persona.
- Un color por especie molecular, constante en todo el video. Cuando una molécula se transforma, desaparece en la enzima y aparece el producto con otro color.
- El guion va en el docstring del script y también en la respuesta.

### 3. Diseñar el plano (2.5D)
- Cámara frontal en (0, −34, 0.4), lente 35 mm, **estática**: un zoom recorta títulos y leyenda. Encuadre útil: x ∈ [−16, 16], z ∈ [−9, 10].
- Tres planos en y: compartimentos (elipsoides aplanados, y = 1.2, alpha 0.55), actores (y = −1) y rótulos (y = −1.6).
- Títulos en z ≈ 8.7, subtítulos en z ≈ 7.85 y leyenda en columna en x ≈ −15.9.
- Coloca los actores de membrana con las funciones de borde de la elipse (`sup_z(x)` / `inf_z(x)`) para que queden justo sobre la membrana.
- Deja ≥ 1 unidad entre rótulos; los nombres de las enzimas van debajo de su forma.

### 4. Escribir el script
Copia `scripts/plantilla_blender.py`, edita COL, ESCENAS, los compartimentos y `construir()`. No toques las utilidades. Lo que ya resuelven y no debes deshacer:
- Compatibilidad 3.x/4.x: motor `BLENDER_EEVEE_NEXT` con *fallback* a `BLENDER_EEVEE`, socket `Emission Color`/`Emission` y transparencia con `surface_render_method`/`blend_method`.
- **Luces sin sombras**: si no, los textos proyectan "fantasmas" sobre las membranas.
- Pico de brillo ≤ 3; más alto satura a blanco y se pierde el color de la enzima.
- La visibilidad se anima con la escala (0 → base), no con `hide_render`, para que se vea igual en el viewport.
- Textos: la fuente por defecto muestra tildes, ñ, α y β. **Evita** → , ⁺, ²⁺ y los subíndices Unicode: escribe "Ca2+", "->" o ">".
- Un marcador de línea de tiempo por escena (lo usa `test_render.py`).
- El script borra la escena: avísalo en el docstring.
- Patrón de cada escena: `aparecer` sustrato → `trayecto` hasta la enzima → `brillo` de la enzima → `desaparecer` sustrato → `aparecer` producto en la enzima → `trayecto` a su destino.

### 5. Probarlo de verdad
```bash
SP=<scratchpad>
uv venv -q -p 3.11 $SP/bvenv
uv pip install -q -p $SP/bvenv/bin/python bpy==4.2.0 pillow
$SP/bvenv/bin/python SKILL_DIR/scripts/test_render.py <mi_script.py> $SP/frames
```
Mira `$SP/frames/hoja_contacto.png` con Read. El aviso `EGL_BAD_MATCH` es inofensivo; si EEVEE falla, el script cae a Cycles CPU.

Revisa en la hoja:
- títulos y leyenda dentro del encuadre en todas las escenas;
- sin sombras fantasma ni textos superpuestos;
- cada molécula llega a su destino (receptor, enzima, membrana) y desaparece cuando debe;
- las enzimas activas brillan sin quedarse blancas;
- caracteres especiales visibles.

Corrige y vuelve a renderizar hasta que todo pase.

### 6. Entregar
- Envía el `.py` y la hoja de contacto con SendUserFile.
- Respuesta breve:
  - la tabla del guion;
  - cómo usarlo: archivo nuevo → Scripting → Ejecutar → Espacio; Ctrl+F12 exporta el MP4;
  - dónde se personaliza: COL, ESCENAS y los fotogramas;
  - límites honestos: es un esquema didáctico, no a escala, y qué añadiste que no está en la fuente.
- Ofrece una sola mejora concreta (otra rama de la vía, espacio para narración).
