"""
ENDOCANNABINOIDES: SEÑALIZACIÓN RETRÓGRADA EN LA SINAPSIS
Animación procedural para Blender 4.x (probado en Blender 4.2)

Fuente del contenido: Di Marzo V. "Endocannabinoids: synthesis and degradation".
Rev Physiol Biochem Pharmacol 2006;160:1-24.

USO
  1. Abre Blender en un archivo NUEVO (el script borra todos los objetos de la escena).
  2. Pestaña "Scripting" > Abrir > este archivo > "Ejecutar script" (Alt+P).
  3. Pulsa Espacio en el viewport (modo "Material Preview") para ver la animación.
  4. Render > Render Animation (Ctrl+F12) exporta un MP4 en la carpeta del .blend.

GUION (24 fps · 960 fotogramas · 40 s). Cada escena tiene un marcador en la línea de tiempo.
  Esc.  Fotogramas  Título en pantalla                  Qué ocurre
  0     1-95        Señalización endocannabinoide       Se presentan las dos neuronas, la hendidura,
                    retrógrada                          receptores, enzimas y la leyenda de colores.
  1     96-215      Liberación de glutamato             Entra Ca2+ por el canal presináptico; una vesícula
                                                        se fusiona y el glutamato llega a sus receptores;
                                                        entra Ca2+ en la neurona postsináptica.
  2     216-335     Síntesis a demanda de 2-AG          PLCβ se activa y genera DAG; la DAGLα (postsináptica)
                                                        lo convierte en 2-AG.
  3     336-435     Síntesis de anandamida              NArPE de membrana es hidrolizada por la NAPE-PLD
                                                        (estimulada por Ca2+) y aparece AEA.
  4     436-575     Mensaje retrógrado                  2-AG y AEA salen por el transportador putativo,
                                                        cruzan la hendidura y se unen a CB1 presináptico.
  5     576-695     CB1 frena la liberación             CB1 brilla, el canal de Ca2+ se vuelve rojo, el Ca2+
                                                        rebota y la siguiente vesícula no se fusiona.
  6     696-845     Inactivación                        2-AG -> MAGL presináptica -> ácido araquidónico + glicerol.
                                                        AEA vuelve -> FAAH postsináptica -> AA + etanolamina.
  7     846-960     Resumen                             Dos vías, dos enzimas de síntesis, dos de degradación
                                                        y las dianas farmacológicas.

PERSONALIZAR
  - Colores: diccionario COL.  - Duración: cambia los números de fotograma en cada escena.
  - Textos: lista ESCENAS (título y subtítulo de cada escena).
"""

import bpy
import math

# ---------------------------------------------------------------------------
# Parámetros generales
# ---------------------------------------------------------------------------
FPS = 24
FRAME_END = 960
Y_MEMB = 1.2    # plano de las membranas (fondo)
Y_ACT = -1.0    # plano de moléculas, receptores y enzimas
Y_LAB = -1.6    # plano de los rótulos (delante de todo)

COL = {
    "fondo":       (0.008, 0.010, 0.018),
    "pre":         (0.10, 0.32, 0.42),
    "post":        (0.30, 0.16, 0.42),
    "vesicula":    (0.75, 0.80, 0.90),
    "glutamato":   (1.00, 0.80, 0.10),
    "calcio":      (0.20, 0.85, 1.00),
    "dag":         (1.00, 0.50, 0.10),
    "2ag":         (0.20, 0.90, 0.35),
    "narpe":       (0.55, 0.35, 0.95),
    "aea":         (1.00, 0.30, 0.65),
    "aa":          (0.90, 0.12, 0.12),
    "glicerol":    (0.92, 0.92, 0.92),
    "cb1":         (0.95, 0.85, 0.30),
    "receptor":    (0.95, 0.65, 0.20),
    "canal":       (0.35, 0.60, 0.85),
    "rojo":        (0.95, 0.10, 0.10),
    "enzima_sint": (0.25, 0.75, 0.55),
    "enzima_deg":  (0.85, 0.35, 0.25),
    "transp":      (0.60, 0.60, 0.70),
    "texto":       (0.95, 0.95, 0.95),
    "titulo":      (1.00, 0.95, 0.80),
}

ESCENAS = [
    # (inicio, fin, título, subtítulo)
    (1, 95, "Señalización endocannabinoide retrógrada",
     "De la neurona postsináptica al receptor CB1 presináptico"),
    (96, 215, "1. Liberación de glutamato",
     "Entra Ca2+ en el terminal, una vesícula libera glutamato y la neurona postsináptica se despolariza"),
    (216, 335, "2. Síntesis a demanda de 2-AG",
     "El Ca2+ y los receptores Gq activan la PLCβ; la DAGLα convierte el DAG en 2-AG"),
    (336, 435, "3. Síntesis de anandamida",
     "La NAPE-PLD, estimulada por Ca2+, hidroliza NArPE y produce anandamida (AEA)"),
    (436, 575, "4. Mensaje retrógrado",
     "2-AG y AEA salen de la célula (transportador putativo) y cruzan la hendidura hasta CB1"),
    (576, 695, "5. CB1 frena la liberación",
     "La activación de CB1 presináptico reduce la entrada de Ca2+ y la liberación de neurotransmisor"),
    (696, 845, "6. Inactivación",
     "MAGL (presináptica) hidroliza 2-AG; FAAH (postsináptica) hidroliza AEA a ácido araquidónico"),
    (846, 960, "Resumen", ""),
]

RESUMEN = (
    "2-AG:  DAGLα (post)  >  CB1 (pre)  >  MAGL (pre)\n"
    "AEA:  NAPE-PLD (post)  >  CB1 (pre)  >  FAAH (post)\n"
    "Dianas: inhibidores de FAAH, MAGL o de la recaptación elevan el tono endocannabinoide;\n"
    "inhibidores de DAGL lo reducen, como un antagonista de CB1"
)


# ---------------------------------------------------------------------------
# Geometría de las membranas (elipses en el plano XZ)
# ---------------------------------------------------------------------------
PRE_C, PRE_A, PRE_B = 6.0, 9.0, 4.5      # centro z, semiejes x y z
POST_C, POST_A, POST_B = -6.0, 10.0, 4.5


def pre_z(x):
    """Altura del borde inferior de la membrana presináptica en x."""
    return PRE_C - PRE_B * math.sqrt(max(0.0, 1 - (x / PRE_A) ** 2))


def post_z(x):
    """Altura del borde superior de la membrana postsináptica en x."""
    return POST_C + POST_B * math.sqrt(max(0.0, 1 - (x / POST_A) ** 2))


# ---------------------------------------------------------------------------
# Utilidades: escena, materiales, objetos
# ---------------------------------------------------------------------------
def limpiar_escena():
    for o in list(bpy.data.objects):
        bpy.data.objects.remove(o, do_unlink=True)
    for datos in (bpy.data.meshes, bpy.data.materials, bpy.data.curves,
                  bpy.data.lights, bpy.data.cameras):
        for b in list(datos):
            if b.users == 0:
                datos.remove(b)
    bpy.context.scene.timeline_markers.clear()


def bsdf(mat):
    return mat.node_tree.nodes.get("Principled BSDF")


def socket_emision(nodo):
    # Blender 4.x usa "Emission Color"; 3.x usa "Emission"
    return nodo.inputs.get("Emission Color") or nodo.inputs.get("Emission")


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
        if hasattr(m, "surface_render_method"):      # Blender 4.2+
            m.surface_render_method = "BLENDED"
        if hasattr(m, "blend_method"):               # Blender < 4.2
            m.blend_method = "BLEND"
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
    bpy.ops.mesh.primitive_cylinder_add(radius=r, depth=alto, location=(x, y, z), vertices=24)
    bpy.ops.object.shade_smooth()
    return _nuevo(nombre, mat)


def enzima(nombre, x, z, mat, r=0.55):
    bpy.ops.mesh.primitive_ico_sphere_add(radius=r, subdivisions=2, location=(x, Y_ACT, z))
    o = _nuevo(nombre, mat)
    o.scale = (1.25, 1.0, 0.9)
    return o


def texto(nombre, cuerpo, x, z, tam=0.42, mat=None, alinear="CENTER", y=Y_LAB):
    cu = bpy.data.curves.new(nombre, "FONT")
    cu.body = cuerpo
    cu.size = tam
    cu.align_x = alinear
    cu.align_y = "CENTER"
    o = bpy.data.objects.new(nombre, cu)
    bpy.context.scene.collection.objects.link(o)
    o.location = (x, y, z)
    o.rotation_euler = (math.pi / 2, 0, 0)    # mirando a la cámara (eje -Y)
    if mat:
        cu.materials.append(mat)
    return o


# ---------------------------------------------------------------------------
# Utilidades de animación
# ---------------------------------------------------------------------------
def oculto_al_inicio(o):
    o["escala_base"] = tuple(o.scale)
    o.scale = (0, 0, 0)
    o.keyframe_insert("scale", frame=1)


def aparecer(o, f, d=8):
    if "escala_base" not in o:
        oculto_al_inicio(o)
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
    """puntos: lista de (fotograma, x, z). La y se mantiene en el plano de actores."""
    for f, x, z in puntos:
        o.location = (x, o.location.y, z)
        o.keyframe_insert("location", frame=f)


def brillo(mat, f, pico=2.5, mantener=40, base=None):
    s = bsdf(mat).inputs["Emission Strength"]
    base = s.default_value if base is None else base
    for fr, v in ((1, base), (f, base), (f + 6, pico), (f + mantener, pico), (f + mantener + 12, base)):
        s.default_value = v
        s.keyframe_insert("default_value", frame=fr)
    s.default_value = base


def cambiar_color(mat, f, color, d=10):
    n = bsdf(mat)
    for socket in (n.inputs["Base Color"], socket_emision(n)):
        socket.keyframe_insert("default_value", frame=1)
        socket.keyframe_insert("default_value", frame=f)
        socket.default_value = (*color, 1)
        socket.keyframe_insert("default_value", frame=f + d)


# ---------------------------------------------------------------------------
# Construcción de la escena
# ---------------------------------------------------------------------------
def configurar_render():
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
    sc.render.filepath = "//endocannabinoides_"
    try:
        sc.render.image_settings.file_format = "FFMPEG"
        sc.render.ffmpeg.format = "MPEG4"
        sc.render.ffmpeg.codec = "H264"
        sc.render.ffmpeg.constant_rate_factor = "HIGH"
    except (TypeError, AttributeError):
        pass
    sc.view_settings.view_transform = "Standard"

    mundo = sc.world or bpy.data.worlds.new("Mundo")
    sc.world = mundo
    mundo.use_nodes = True
    fondo = mundo.node_tree.nodes.get("Background")
    fondo.inputs["Color"].default_value = (*COL["fondo"], 1)
    fondo.inputs["Strength"].default_value = 1.0


def camara_y_luces():
    cam_data = bpy.data.cameras.new("Camara")
    cam_data.lens = 35
    cam = bpy.data.objects.new("Camara", cam_data)
    bpy.context.scene.collection.objects.link(cam)
    cam.location = (0, -34, 0.4)
    cam.rotation_euler = (math.pi / 2, 0, 0)
    bpy.context.scene.camera = cam

    sol = bpy.data.lights.new("Sol", "SUN")
    sol.energy = 3.0
    sol.use_shadow = False      # evita sombras de textos sobre las membranas
    o = bpy.data.objects.new("Sol", sol)
    o.rotation_euler = (math.radians(60), 0, math.radians(-20))
    bpy.context.scene.collection.objects.link(o)

    area = bpy.data.lights.new("Relleno", "AREA")
    area.energy = 1500
    area.size = 20
    area.use_shadow = False
    o = bpy.data.objects.new("Relleno", area)
    o.location = (0, -20, 8)
    o.rotation_euler = (math.radians(65), 0, 0)
    bpy.context.scene.collection.objects.link(o)


def construir():
    limpiar_escena()
    configurar_render()
    camara_y_luces()

    m = {k: material(k, c) for k, c in COL.items() if k not in ("pre", "post", "fondo")}
    m["texto"] = material("texto", COL["texto"], emision=1.5)
    m["titulo"] = material("titulo", COL["titulo"], emision=2.5)
    m_pre = material("membrana_pre", COL["pre"], alpha=0.55, emision=0.25)
    m_post = material("membrana_post", COL["post"], alpha=0.55, emision=0.25)

    # Materiales propios para lo que cambia de brillo o color
    m_cb1 = material("CB1", COL["cb1"], emision=0.3)
    m_canal = material("canal_Ca", COL["canal"], emision=0.3)
    m_rec = material("rec_glu", COL["receptor"], emision=0.3)
    m_plc = material("PLC", COL["enzima_sint"], emision=0.3)
    m_dagl = material("DAGL", COL["enzima_sint"], emision=0.3)
    m_nape = material("NAPE-PLD", COL["enzima_sint"], emision=0.3)
    m_magl = material("MAGL", COL["enzima_deg"], emision=0.3)
    m_faah = material("FAAH", COL["enzima_deg"], emision=0.3)

    # --- Membranas ----------------------------------------------------------
    esfera("Neurona_presinaptica", 0, PRE_C, 1.0, m_pre, y=Y_MEMB, escala=(PRE_A, 0.4, PRE_B))
    esfera("Neurona_postsinaptica", 0, POST_C, 1.0, m_post, y=Y_MEMB, escala=(POST_A, 0.4, POST_B))

    # --- Estructuras fijas --------------------------------------------------
    cb1 = [cilindro(f"CB1_{i}", x, pre_z(x), 0.32, 1.0, m_cb1) for i, x in enumerate((-3.0, 3.0))]
    canal = cilindro("Canal_Ca_pre", -0.9, pre_z(-0.9), 0.28, 1.0, m_canal)
    rec = [cilindro(f"Receptor_glu_{i}", x, post_z(x), 0.3, 1.0, m_rec) for i, x in enumerate((-1.2, 1.2))]
    transp = []
    for i, x in enumerate((-3.4, 3.4)):
        for dx in (-0.32, 0.32):
            transp.append(cilindro(f"Transportador_{i}_{dx:+.1f}", x + dx, post_z(x), 0.14, 0.9, m["transp"]))

    plc = enzima("PLCbeta", -1.6, -3.3, m_plc)
    dagl = enzima("DAGLalfa", -5.2, -2.75, m_dagl)
    nape = enzima("NAPE-PLD", 4.2, -3.4, m_nape)
    faah = enzima("FAAH", 6.0, -3.9, m_faah)
    magl = enzima("MAGL", -5.5, 3.4, m_magl)

    vesiculas = [esfera(f"Vesicula_{i}", x, z, 0.55, m["vesicula"])
                 for i, (x, z) in enumerate(((0.9, 3.0), (2.4, 3.5), (-1.9, 3.7), (0.3, 4.6), (3.6, 4.4)))]

    # --- Rótulos fijos (aparecen en la escena 0) -----------------------------
    rotulos = [
        texto("R_pre", "Neurona presináptica", 0, 5.9, 0.6, m["texto"]),
        texto("R_post", "Neurona postsináptica", 0, -7.6, 0.6, m["texto"]),
        texto("R_hend", "Hendidura\nsináptica", 9.6, 0.2, 0.45, m["texto"]),
        texto("R_cb1a", "CB1", -3.0, 2.75, 0.4, m["texto"]),
        texto("R_cb1b", "CB1", 3.0, 2.75, 0.4, m["texto"]),
        texto("R_canal", "Canal de Ca2+", -1.6, 2.55, 0.32, m["texto"]),
        texto("R_rec", "Receptores de glutamato", 0, -2.55, 0.32, m["texto"]),
        texto("R_transp", "Transportador\n(putativo)", -5.2, -0.6, 0.32, m["texto"]),
        texto("R_plc", "PLCβ", -1.6, -4.15, 0.36, m["texto"]),
        texto("R_dagl", "DAGLα", -5.2, -3.6, 0.36, m["texto"]),
        texto("R_nape", "NAPE-PLD", 4.2, -4.25, 0.36, m["texto"]),
        texto("R_faah", "FAAH", 6.0, -4.75, 0.36, m["texto"]),
        texto("R_magl", "MAGL", -5.5, 4.25, 0.36, m["texto"]),
    ]
    for i, r in enumerate(rotulos):
        aparecer(r, 12 + i * 5)

    # Leyenda de colores
    leyenda = [("Glutamato", "glutamato"), ("Ca2+", "calcio"), ("DAG", "dag"), ("2-AG", "2ag"),
               ("NArPE", "narpe"), ("Anandamida (AEA)", "aea"), ("Ácido araquidónico", "aa"),
               ("Glicerol / etanolamina", "glicerol")]
    for i, (nombre, clave) in enumerate(leyenda):
        z = 3.2 - i * 0.8
        p = esfera(f"Leyenda_{clave}", -15.9, z, 0.2, m[clave], y=Y_LAB)
        t = texto(f"Leyenda_t_{clave}", nombre, -15.5, z, 0.32, m["texto"], alinear="LEFT")
        aparecer(p, 40 + i * 3)
        aparecer(t, 40 + i * 3)

    # Títulos y subtítulos por escena + marcadores en la línea de tiempo
    for i, (ini, fin, tit, sub) in enumerate(ESCENAS):
        bpy.context.scene.timeline_markers.new(f"Esc{i} {tit}", frame=ini)
        t = texto(f"Titulo_{i}", tit, 0, 8.7, 0.75, m["titulo"])
        aparecer(t, ini, 8)
        if fin < FRAME_END:
            desaparecer(t, fin - 8, 8)
        if sub:
            s = texto(f"Subtitulo_{i}", sub, 0, 7.85, 0.4, m["texto"])
            aparecer(s, ini + 4, 8)
            if fin < FRAME_END:
                desaparecer(s, fin - 8, 8)
    resumen = texto("Resumen_texto", RESUMEN, 0, 7.4, 0.36, m["texto"])
    aparecer(resumen, 856, 10)

    # =======================================================================
    # ESCENA 1 · Liberación de glutamato (96-215)
    # =======================================================================
    ca_pre = []
    for i in range(3):
        c = esfera(f"Ca_pre_{i}", -0.9 + (i - 1) * 0.25, -0.3, 0.13, m["calcio"])
        aparecer(c, 98 + i * 3, 6)
        trayecto(c, [(100 + i * 3, -0.9 + (i - 1) * 0.25, -0.3),
                     (122 + i * 3, -0.9 + (i - 1) * 0.3, 2.6)])
        desaparecer(c, 135 + i * 3, 8)
        ca_pre.append(c)
    brillo(m_canal, 100, pico=2.5, mantener=25)

    v0 = vesiculas[0]
    trayecto(v0, [(118, 0.9, 3.0), (132, 0.9, 2.05)])
    desaparecer(v0, 136, 8)   # fusión con la membrana

    destinos = [(-1.35, -0.85), (-1.05, -0.8), (-1.2, -0.65), (1.05, -0.8), (1.35, -0.85), (1.2, -0.65)]
    for i, (x, z) in enumerate(destinos):
        g = esfera(f"Glutamato_{i}", 0.9, 1.4, 0.14, m["glutamato"])
        aparecer(g, 136 + i, 5)
        trayecto(g, [(138 + i, 0.9, 1.4), (150 + i, (0.9 + x) / 2, 0.4), (166 + i, x, z)])
        desaparecer(g, 300, 10)
    brillo(m_rec, 166, pico=2.5, mantener=40)
    brillo(m_post, 170, pico=0.8, mantener=30, base=0.25)    # despolarización

    ca_post = []
    for i, (x, xf, zf) in enumerate(((-1.2, -1.9, -2.6), (1.2, 2.2, -2.7), (-1.2, -3.6, -2.4), (1.2, 3.4, -2.9))):
        c = esfera(f"Ca_post_{i}", x, 0.2, 0.13, m["calcio"])
        aparecer(c, 170 + i * 3, 6)
        trayecto(c, [(172 + i * 3, x, 0.2), (190 + i * 3, x, -1.9), (210 + i * 3, xf, zf)])
        desaparecer(c, 330, 10)
        ca_post.append(c)

    # =======================================================================
    # ESCENA 2 · Síntesis a demanda de 2-AG (216-335)
    # =======================================================================
    brillo(m_plc, 225, pico=2.5, mantener=30)
    dag = esfera("DAG", -1.8, -2.35, 0.2, m["dag"])
    aparecer(dag, 245, 8)
    trayecto(dag, [(255, -1.8, -2.35), (290, -4.55, -2.5)])
    brillo(m_dagl, 285, pico=2.5, mantener=35)
    desaparecer(dag, 296, 6)

    dosag = []
    for i, (dx, dz) in enumerate(((0.0, 0.55), (-0.55, 0.15), (0.55, 0.2))):
        a = esfera(f"2AG_{i}", -5.2 + dx, -2.75 + dz, 0.2, m["2ag"])
        aparecer(a, 300 + i * 4, 8)
        dosag.append(a)

    # =======================================================================
    # ESCENA 3 · Síntesis de anandamida (336-435)
    # =======================================================================
    aeas = []
    for i, (x0, z0) in enumerate(((4.8, -2.35), (5.6, -2.55))):
        n = esfera(f"NArPE_{i}", x0, z0, 0.2, m["narpe"])
        aparecer(n, 345 + i * 5, 8)
        trayecto(n, [(360 + i * 5, x0, z0), (392 + i * 5, 4.2 + (i - 0.5) * 0.6, -2.95)])
        desaparecer(n, 398 + i * 5, 6)
    brillo(m_nape, 385, pico=2.5, mantener=35)
    for i, (dx, dz) in enumerate(((-0.55, 0.45), (0.55, 0.45))):
        a = esfera(f"AEA_{i}", 4.2 + dx, -3.4 + dz, 0.2, m["aea"])
        aparecer(a, 402 + i * 5, 8)
        aeas.append(a)

    # =======================================================================
    # ESCENA 4 · Mensaje retrógrado (436-575)
    # =======================================================================
    for i, a in enumerate(dosag):
        x0, z0 = a.location.x, a.location.z
        d = i * 6
        trayecto(a, [(445 + d, x0, z0), (475 + d, -3.4, -2.45), (492 + d, -3.4, -1.1),
                     (528 + d, -3.0 + (i - 1) * 0.42, 0.9)])
    for i, a in enumerate(aeas):
        x0, z0 = a.location.x, a.location.z
        d = 10 + i * 6
        trayecto(a, [(445 + d, x0, z0), (475 + d, 3.4, -2.45), (492 + d, 3.4, -1.1),
                     (528 + d, 3.0 + (i - 0.5) * 0.5, 0.9)])
    brillo(m["transp"], 470, pico=1.5, mantener=40, base=0.4)

    # =======================================================================
    # ESCENA 5 · CB1 frena la liberación (576-695)
    # =======================================================================
    brillo(m_cb1, 545, pico=3, mantener=150)
    cambiar_color(m_canal, 590, COL["rojo"], 12)
    for i in range(3):
        c = esfera(f"Ca_bloqueado_{i}", -0.9 + (i - 1) * 0.3, -0.6, 0.13, m["calcio"])
        aparecer(c, 598 + i * 3, 6)
        trayecto(c, [(600 + i * 3, -0.9 + (i - 1) * 0.3, -0.6),
                     (625 + i * 3, -0.9 + (i - 1) * 0.3, 0.75),
                     (650 + i * 3, -0.9 + (i - 1) * 0.6, -0.4)])
        desaparecer(c, 680, 10)
    v1 = vesiculas[1]
    trayecto(v1, [(600, 2.4, 3.5), (630, 2.0, 2.75), (660, 2.0, 2.75), (690, 2.4, 3.5)])
    cruz = texto("Sin_liberacion", "X", 2.0, 1.9, 0.9, material("cruz", COL["rojo"], emision=3))
    aparecer(cruz, 632, 6)
    desaparecer(cruz, 688, 8)

    # =======================================================================
    # ESCENA 6 · Inactivación (696-845)
    # =======================================================================
    for i, a in enumerate(dosag):
        x0 = -3.0 + (i - 1) * 0.42
        d = i * 6
        trayecto(a, [(700 + d, x0, 0.9), (722 + d, -3.6, 2.6), (745 + d, -5.5 + (i - 1) * 0.5, 2.85)])
        desaparecer(a, 758 + d, 6)
    brillo(m_magl, 745, pico=2.5, mantener=35)
    for i in range(3):
        aa = esfera(f"AA_magl_{i}", -5.5, 3.4, 0.18, m["aa"])
        gl = esfera(f"Glicerol_{i}", -5.5, 3.4, 0.14, m["glicerol"])
        aparecer(aa, 766 + i * 6, 6)
        aparecer(gl, 766 + i * 6, 6)
        ang = math.radians(60 + i * 50)
        trayecto(aa, [(768 + i * 6, -5.5, 3.4), (810 + i * 6, -5.5 + 1.4 * math.cos(ang), 3.4 + 1.1 * math.sin(ang))])
        trayecto(gl, [(768 + i * 6, -5.5, 3.4), (810 + i * 6, -5.5 - 1.3 * math.cos(ang), 3.4 + 0.9 * math.sin(ang))])

    for i, a in enumerate(aeas):
        x0 = 3.0 + (i - 0.5) * 0.5
        d = i * 6
        trayecto(a, [(700 + d, x0, 0.9), (720 + d, 3.4, -1.1), (735 + d, 3.4, -2.45), (765 + d, 6.0 + (i - 0.5) * 0.6, -3.2)])
        desaparecer(a, 772 + d, 6)
    brillo(m_faah, 765, pico=2.5, mantener=35)
    for i in range(2):
        aa = esfera(f"AA_faah_{i}", 6.0, -3.9, 0.18, m["aa"])
        et = esfera(f"Etanolamina_{i}", 6.0, -3.9, 0.14, m["glicerol"])
        aparecer(aa, 780 + i * 6, 6)
        aparecer(et, 780 + i * 6, 6)
        trayecto(aa, [(782 + i * 6, 6.0, -3.9), (820 + i * 6, 7.2, -4.6 - i * 0.6)])
        trayecto(et, [(782 + i * 6, 6.0, -3.9), (820 + i * 6, 4.9, -4.9 - i * 0.5)])

    bpy.context.scene.frame_set(1)


if __name__ == "__main__":
    construir()
    print("Escena de endocannabinoides creada: 960 fotogramas a 24 fps.")
