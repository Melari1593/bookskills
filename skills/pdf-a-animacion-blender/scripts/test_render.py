"""
Prueba un script de animación de Blender sin abrir Blender.

Ejecuta el script con el módulo bpy, renderiza un fotograma por escena (40 fotogramas
después de cada marcador de la línea de tiempo) a baja resolución, guarda un .blend
y arma una hoja de contacto 2 columnas x N filas (si Pillow está disponible).

Uso:
  uv venv -q -p 3.11 bvenv && uv pip install -q -p bvenv/bin/python bpy==4.2.0 pillow
  bvenv/bin/python test_render.py <script_animacion.py> <carpeta_salida> [fotograma ...]

El aviso "EGL_BAD_MATCH" que puede salir en consola es inofensivo.
"""
import os
import runpy
import sys

import bpy


def main():
    args = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else sys.argv[1:]
    if len(args) < 2:
        sys.exit(__doc__)
    script, salida = os.path.abspath(args[0]), os.path.abspath(args[1])
    os.makedirs(salida, exist_ok=True)

    runpy.run_path(script, run_name="__main__")
    sc = bpy.context.scene
    print("Motor:", sc.render.engine, "| objetos:", len(bpy.data.objects), "| fotogramas:", sc.frame_end)

    if len(args) > 2:
        fotogramas = [int(a) for a in args[2:]]
    else:
        marcas = sorted(m.frame for m in sc.timeline_markers)
        fotogramas = [min(f + 40, sc.frame_end) for f in marcas] or [sc.frame_end // 2]

    sc.render.resolution_percentage = 40
    sc.render.image_settings.file_format = "PNG"
    try:
        sc.eevee.taa_render_samples = 8
    except AttributeError:
        pass

    rutas = []
    for f in fotogramas:
        sc.frame_set(f)
        sc.render.filepath = os.path.join(salida, f"f{f:04d}.png")
        try:
            bpy.ops.render.render(write_still=True)
        except RuntimeError as e:   # sin GPU/EGL: cae a Cycles CPU
            print("EEVEE no disponible, uso Cycles:", e)
            sc.render.engine = "CYCLES"
            sc.cycles.device = "CPU"
            sc.cycles.samples = 8
            bpy.ops.render.render(write_still=True)
        rutas.append(sc.render.filepath)

    bpy.ops.wm.save_as_mainfile(filepath=os.path.join(salida, "prueba.blend"))

    try:
        from PIL import Image
        ims = [Image.open(r) for r in rutas]
        w, h = ims[0].size
        filas = (len(ims) + 1) // 2
        hoja = Image.new("RGB", (w * 2, h * filas))
        for i, im in enumerate(ims):
            hoja.paste(im, ((i % 2) * w, (i // 2) * h))
        destino = os.path.join(salida, "hoja_contacto.png")
        hoja.save(destino)
        print("Hoja de contacto:", destino)
    except ImportError:
        print("Pillow no instalado: revisa los PNG uno a uno.")


if __name__ == "__main__":
    main()
