# PDF → animación en Blender

Skill que convierte una vía o mecanismo descrito en un PDF científico en un guion por escenas y un script de Python (bpy) que lo anima en Blender 4.x. Cada script se prueba renderizando un fotograma por escena antes de entregarlo.

- `SKILL.md`: flujo e instrucciones.
- `scripts/plantilla_blender.py`: plantilla con las utilidades de animación y un ejemplo mínimo.
- `scripts/test_render.py`: prueba sin interfaz (bpy) y genera la hoja de contacto.
- `examples/`: vía endocannabinoide (Di Marzo 2006), con script completo y hoja de contacto.

Uso del script generado: Blender → archivo nuevo → Scripting → Abrir → Ejecutar script → Espacio. Ctrl+F12 exporta el MP4.
