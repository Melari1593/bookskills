"""
PLANTILLA · Animación 2.5D de una vía biológica en Blender (bpy, 3.x/4.x; probado en 4.2)

Copia este archivo, cambia COL, ESCENAS y RESUMEN, y escribe tus actores y escenas
dentro de construir(). Las utilidades de arriba no se tocan.

USO EN BLENDER: archivo nuevo > Scripting > Abrir > Ejecutar script (Alt+P) > Espacio.
El script BORRA todos los objetos de la escena actual.

GUION
  Esc.  Fotogramas  Título            Qué ocurre
  0     1-95        ...               Presentación de compartimentos, actores y leyenda
  ...
"""
import bpy
import math

# ---------------------------------------------------------------------------
# Parámetros (editar)
# ---------------------------------------------------------------------------
FPS, FRAME_END = 24, 240
Y_MEMB, Y_ACT, Y_LAB = 1.2, -1.0, -1.6   # planos: compartimentos / actores / rótulos

COL = {
    "fondo":    (0.008, 0.010, 0.018),
    "sup":      (0.10, 0.32, 0.42),     # compartimento superior
    "inf":      (0.30, 0.16, 0.42),     # compartimento inferior
    "sustrato": (0.55, 0.35, 0.95),
    "producto": (0.20, 0.90, 0.35),
    "enzima":   (0.25, 0.75, 0.55),
    "receptor": (0.95, 0.85, 0.30),
    "texto":    (0.95, 0.95, 0.95),
    "titulo":   (1.00, 0.95, 0.80),
}

ESCENAS = [   # (inicio, fin, título, subtítulo ≤ 100 caracteres)
    (1, 95, "Título de la vía", "Una frase que diga qué se va a ver"),
    (96, 240, "1. La enzima convierte el sustrato", "El producto cruza y activa su receptor"),
]

# Compartimentos: elipses en el plano XZ (centro z, semieje x, semieje z)
SUP_C, SUP_A, SUP_B = 6.0, 9.0, 4.5
INF_C, INF_A, INF_B = -6.0, 10.0, 4.5


def sup_z(x):
    """Borde inferior del compartimento superior en x."""
    return SUP_C - SUP_B * math.sqrt(max(0.0, 1 - (x / SUP_A) ** 2))


def inf_z(x):
    """Borde superior del compartimento inferior en x."""
    return INF_C + INF_B * math.sqrt(max(0.0, 1 - (x / INF_A) ** 2))


# ---------------------------------------------------------------------------
# Utilidades (no editar)
# ---------------------------------------------------------------------------
def limpiar_escena():
    for o in list(bpy.data.objects):
        bpy.data.objects.remove(o, do_unlink=True)
    for datos in (bpy.data.meshes, bpy.data.materials, bpy.data.curves, bpy.data.lights, bpy.data.cameras):
        for b in list(datos):
            if b.users == 0:
                datos.remove(b)
    bpy.context.scene.timeline_markers.clear()


def bsdf(mat):
    return mat.node_tree.nodes.get("Principled BSDF")


def socket_emision(n):
    return n.inputs.get("Emission Color") or n.inputs.get("Emission")   # 4.x / 3.x


def material(nombre, color, alpha=1.0, emision=0.4, rugosidad=0.45):
    m = bpy.data.materials.new(nombre)
    m.use_nodes = True
    n = bsdf(m)
    n.inputs["Base Color"].default_value = (*color, 1)
    n.inputs["Roughness"].default_value = rugosidad
    socket_emision(n).default_value = (*color, 1)
    n.inputs["Emission Strength"].default_value = emision
    if alpha < 1.0:
        n.inputs["Alpha"].default_value = alpha
        if hasattr(m, "surface_render_method"):
            m.surface_render_method = "BLENDED"   # 4.2+
        if hasattr(m, "blend_method"):
            m.blend_method = "BLEND"              # < 4.2
    return m


def _nuevo(nombre, mat):
    o = bpy.context.active_object
    o.name = nombre
    if mat:
        o.data.materials.append(mat)
    return o


def esfera(nombre, x, z, r, mat, y=Y_ACT, escala=None):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=r, location=(x, y, z), segments=32, ring_count=16)
    bpy.ops.object.shade_smooth()
    o = _nuevo(nombre, mat)
    if escala:
        o.scale = escala
    return o


def cilindro(nombre, x, z, r, alto, mat, y=Y_ACT):
    """Receptores, canales y transportadores (dos cilindros finos = un poro)."""
    bpy.ops.mesh.primitive_cylinder_add(radius=r, depth=alto, location=(x, y, z), vertices=24)
    bpy.ops.object.shade_smooth()
    return _nuevo(nombre, mat)


def enzima(nombre, x, z, mat, r=0.55):
    bpy.ops.mesh.primitive_ico_sphere_add(radius=r, subdivisions=2, location=(x, Y_ACT, z))
    o = _nuevo(nombre, mat)
    o.scale = (1.25, 1.0, 0.9)
    return o


def texto(nombre, cuerpo, x, z, tam=0.42, mat=None, alinear="CENTER", y=Y_LAB):
    """Tildes, ñ, α y β se ven bien; evita →, ⁺ y subíndices Unicode (usa Ca2+, >)."""
    cu = bpy.data.curves.new(nombre, "FONT")
    cu.body, cu.size, cu.align_x, cu.align_y = cuerpo, tam, alinear, "CENTER"
    o = bpy.data.objects.new(nombre, cu)
    bpy.context.scene.collection.objects.link(o)
    o.location = (x, y, z)
    o.rotation_euler = (math.pi / 2, 0, 0)
    if mat:
        cu.materials.append(mat)
    return o


def aparecer(o, f, d=8):
    if "escala_base" not in o:
        o["escala_base"] = tuple(o.scale)
        o.scale = (0, 0, 0)
        o.keyframe_insert("scale", frame=1)
    o.scale = (0, 0, 0)
    o.keyframe_insert("scale", frame=f)
    o.scale = tuple(o["escala_base"])
    o.keyframe_insert("scale", frame=f + d)


def desaparecer(o, f, d=8):
    o.scale = tuple(o["escala_base"]) if "escala_base" in o else tuple(o.scale)
    o.keyframe_insert("scale", frame=f)
    o.scale = (0, 0, 0)
    o.keyframe_insert("scale", frame=f + d)


def trayecto(o, puntos):
    """puntos: [(fotograma, x, z), ...]; la y se conserva."""
    for f, x, z in puntos:
        o.location = (x, o.location.y, z)
        o.keyframe_insert("location", frame=f)


def brillo(mat, f, pico=2.5, mantener=40, base=None):
    """Activación de una enzima o receptor. Pico > 3 satura a blanco."""
    s = bsdf(mat).inputs["Emission Strength"]
    base = s.default_value if base is None else base
    for fr, v in ((1, base), (f, base), (f + 6, pico), (f + mantener, pico), (f + mantener + 12, base)):
        s.default_value = v
        s.keyframe_insert("default_value", frame=fr)
    s.default_value = base


def cambiar_color(mat, f, color, d=10):
    n = bsdf(mat)
    for sk in (n.inputs["Base Color"], socket_emision(n)):
        sk.keyframe_insert("default_value", frame=1)
        sk.keyframe_insert("default_value", frame=f)
        sk.default_value = (*color, 1)
        sk.keyframe_insert("default_value", frame=f + d)


def configurar_render(salida="//animacion_"):
    sc = bpy.context.scene
    for motor in ("BLENDER_EEVEE_NEXT", "BLENDER_EEVEE"):
        try:
            sc.render.engine = motor
            break
        except TypeError:
            continue
    sc.render.fps = FPS
    sc.frame_start, sc.frame_end = 1, FRAME_END
    sc.render.resolution_x, sc.render.resolution_y = 1920, 1080
    sc.render.filepath = salida
    try:
        sc.render.image_settings.file_format = "FFMPEG"
        sc.render.ffmpeg.format, sc.render.ffmpeg.codec = "MPEG4", "H264"
        sc.render.ffmpeg.constant_rate_factor = "HIGH"
    except (TypeError, AttributeError):
        pass
    sc.view_settings.view_transform = "Standard"
    w = sc.world or bpy.data.worlds.new("Mundo")
    sc.world = w
    w.use_nodes = True
    bg = w.node_tree.nodes.get("Background")
    bg.inputs["Color"].default_value = (*COL["fondo"], 1)
    bg.inputs["Strength"].default_value = 1.0


def camara_y_luces():
    """Cámara frontal ESTÁTICA (un zoom recorta títulos y leyenda); luces SIN sombras."""
    cd = bpy.data.cameras.new("Camara")
    cd.lens = 35
    cam = bpy.data.objects.new("Camara", cd)
    bpy.context.scene.collection.objects.link(cam)
    cam.location = (0, -34, 0.4)
    cam.rotation_euler = (math.pi / 2, 0, 0)
    bpy.context.scene.camera = cam
    sol = bpy.data.lights.new("Sol", "SUN")
    sol.energy, sol.use_shadow = 3.0, False
    o = bpy.data.objects.new("Sol", sol)
    o.rotation_euler = (math.radians(60), 0, math.radians(-20))
    bpy.context.scene.collection.objects.link(o)
    a = bpy.data.lights.new("Relleno", "AREA")
    a.energy, a.size, a.use_shadow = 1500, 20, False
    o = bpy.data.objects.new("Relleno", a)
    o.location = (0, -20, 8)
    o.rotation_euler = (math.radians(65), 0, 0)
    bpy.context.scene.collection.objects.link(o)


def titulos(m_titulo, m_texto):
    """Títulos (z 8.7), subtítulos (z 7.85) y un marcador de línea de tiempo por escena."""
    for i, (ini, fin, tit, sub) in enumerate(ESCENAS):
        bpy.context.scene.timeline_markers.new(f"Esc{i} {tit}", frame=ini)
        t = texto(f"Titulo_{i}", tit, 0, 8.7, 0.75, m_titulo)
        aparecer(t, ini)
        if fin < FRAME_END:
            desaparecer(t, fin - 8)
        if sub:
            s = texto(f"Subtitulo_{i}", sub, 0, 7.85, 0.4, m_texto)
            aparecer(s, ini + 4)
            if fin < FRAME_END:
                desaparecer(s, fin - 8)


def leyenda(items, m, m_texto):
    """items: [(nombre visible, clave de COL)]; columna en x = -15.9."""
    for i, (nombre, clave) in enumerate(items):
        z = 3.2 - i * 0.8
        p = esfera(f"Leyenda_{clave}", -15.9, z, 0.2, m[clave], y=Y_LAB)
        t = texto(f"Leyenda_t_{clave}", nombre, -15.5, z, 0.32, m_texto, alinear="LEFT")
        aparecer(p, 40 + i * 3)
        aparecer(t, 40 + i * 3)


# ---------------------------------------------------------------------------
# Escena (editar): ejemplo mínimo sustrato -> enzima -> producto -> receptor
# ---------------------------------------------------------------------------
def construir():
    limpiar_escena()
    configurar_render()
    camara_y_luces()

    m = {k: material(k, c) for k, c in COL.items() if k not in ("fondo", "sup", "inf")}
    m["texto"] = material("texto", COL["texto"], emision=1.5)
    m["titulo"] = material("titulo", COL["titulo"], emision=2.5)
    m_enz = material("enzima_A", COL["enzima"], emision=0.3)      # propio: va a brillar
    m_rec = material("receptor_A", COL["receptor"], emision=0.3)

    # Compartimentos
    esfera("Compartimento_sup", 0, SUP_C, 1.0, material("sup", COL["sup"], 0.55, 0.25), y=Y_MEMB,
           escala=(SUP_A, 0.4, SUP_B))
    esfera("Compartimento_inf", 0, INF_C, 1.0, material("inf", COL["inf"], 0.55, 0.25), y=Y_MEMB,
           escala=(INF_A, 0.4, INF_B))

    # Actores fijos
    enzima("Enzima_A", -3.0, -3.0, m_enz)
    cilindro("Receptor_A", 2.0, sup_z(2.0), 0.32, 1.0, m_rec)
    for i, (r, x, z) in enumerate((("Enzima A", -3.0, -3.85), ("Receptor", 2.0, 2.75))):
        aparecer(texto(f"R_{i}", r, x, z, 0.36, m["texto"]), 12 + i * 5)
    leyenda([("Sustrato", "sustrato"), ("Producto", "producto")], m, m["texto"])
    titulos(m["titulo"], m["texto"])

    # Escena 1: sustrato -> enzima -> producto -> receptor
    s = esfera("Sustrato", -1.0, -2.3, 0.2, m["sustrato"])
    aparecer(s, 100)
    trayecto(s, [(110, -1.0, -2.3), (140, -2.4, -2.8)])
    brillo(m_enz, 138)
    desaparecer(s, 146, 6)
    p = esfera("Producto", -3.0, -2.4, 0.2, m["producto"])
    aparecer(p, 150)
    trayecto(p, [(160, -3.0, -2.4), (185, -1.0, inf_z(-1.0) + 0.5), (215, 2.0, sup_z(2.0) - 0.75)])
    brillo(m_rec, 212, mantener=20)

    bpy.context.scene.frame_set(1)


if __name__ == "__main__":
    construir()
