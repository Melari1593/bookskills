---
name: acupuntura-puntos
description: Referencia clínica en español de los 361 puntos clásicos de acupuntura de la Medicina Tradicional China (MTC), organizada por meridiano, con índice por síntoma y tabla de categorías (Cinco Shu, Yuan, Luo, Xi, Shu dorsales, Mu, Hui, puntos de confluencia). Usa esta skill SIEMPRE que el usuario pregunte qué puntos de acupuntura o acupresión usar para un síntoma, patrón o enfermedad (ej. "¿qué puntos para lumbalgia?", "puntos para insomnio por deficiencia de Yin de Riñón"), pida la ubicación, funciones, indicaciones, profundidad de inserción o contraindicaciones de un punto (por código como ST36, LI4, SP6, o por nombre pinyin como Zusanli, Hegu, Sanyinjiao), quiera listar los puntos de un meridiano o una categoría, o arme una receta/protocolo de puntos -- aunque no diga "medicina tradicional china" (ej. "¿dónde queda el 36 de estómago?", "puntos prohibidos en embarazo"). NO usar para fitoterapia china (fórmulas herbales), diagnóstico por lengua/pulso sin relación con puntos, ni medicina convencional.
---

# Puntos de acupuntura (MTC)

Referencia para estudio y práctica profesional. El usuario es estudiante o practicante: usa lenguaje técnico (pinyin, cun, patrones de MTC), sin simplificar de más, pero siempre con los datos de seguridad que un profesional necesita tener a la vista.

## Archivos de referencia

| Archivo | Cuándo leerlo |
|---|---|
| `references/indice-sintomas.md` | **Primero**, ante cualquier consulta por síntoma, enfermedad o patrón. Mapea síntomas → puntos principales y complementarios según patrón. |
| `references/categorias.md` | Para categorías de puntos (Cinco Shu, Yuan, Luo, Xi, Shu dorsales, Mu, Hui, 8 de confluencia, He inferiores, Ventanas del Cielo, Mar, Estrellas de Ma Danyang…) y para la **lista de puntos contraindicados en embarazo**. |
| `references/meridianos/<COD>.md` | Ficha completa de cada punto del meridiano. Lee solo los archivos de los meridianos que necesites. |

Códigos de meridiano (nomenclatura estándar OMS) y archivos:

| Código | Meridiano | Puntos | Archivo |
|---|---|---|---|
| LU | Pulmón (Shou Taiyin) | 11 | `LU.md` |
| LI | Intestino Grueso (Shou Yangming) | 20 | `LI.md` |
| ST | Estómago (Zu Yangming) | 45 | `ST.md` |
| SP | Bazo (Zu Taiyin) | 21 | `SP.md` |
| HT | Corazón (Shou Shaoyin) | 9 | `HT.md` |
| SI | Intestino Delgado (Shou Taiyang) | 19 | `SI.md` |
| BL | Vejiga (Zu Taiyang) | 67 | `BL.md` |
| KI | Riñón (Zu Shaoyin) | 27 | `KI.md` |
| PC | Pericardio (Shou Jueyin) | 9 | `PC.md` |
| TE | Triple Calentador / San Jiao (Shou Shaoyang) | 23 | `TE.md` |
| GB | Vesícula Biliar (Zu Shaoyang) | 44 | `GB.md` |
| LR | Hígado (Zu Jueyin) | 14 | `LR.md` |
| CV | Ren Mai / Vaso Concepción | 24 | `CV.md` |
| GV | Du Mai / Vaso Gobernador | 28 (+ GV29 Yintang) | `GV.md` |

Los puntos extra (EX-HN3 Yintang, EX-B2 Huatuojiaji, EX-HN5 Taiyang, etc.) están en `categorias.md`.

Equivalencias frecuentes de códigos que puede usar el usuario: P = LU; IG = LI; E = ST; B/BP = SP; C = HT; ID = SI; V = BL; R = KI; PC/MC = PC; SJ/TR/TC = TE; VB = GB; H/Hg = LR; RM/VC = CV; DM/VG = GV. Ejemplos: "E36" = ST36, "IG4" = LI4, "BP6" = SP6, "VB34" = GB34, "H3" = LR3. Si el usuario da solo el nombre pinyin (con o sin tildes: "Zusanli", "Zúsānlǐ"), búscalo con grep en `references/meridianos/`.

Para localizar rápido: `grep -n "^### ST36" references/meridianos/ST.md` y lee desde esa línea ~12 líneas. Para buscar por nombre o término: `grep -rin "zusanli" references/`.

## Flujos de consulta

### 1. Por síntoma / enfermedad / patrón (el caso más frecuente)

1. Lee `references/indice-sintomas.md` y ubica la entrada (usa grep con sinónimos: "lumbalgia" / "dolor lumbar" / "espalda baja").
2. Si el síntoma tiene varios patrones de MTC y el usuario no dio suficiente información para diferenciarlo, presenta los puntos generales y luego los complementarios **por patrón** (ej. insomnio por deficiencia de Sangre de Corazón y Bazo vs. hiperactividad de Fuego de Hígado), explicando brevemente qué signos orientan a cada uno. No inventes un patrón que el usuario no mencionó.
3. Para cada punto recomendado, consulta su ficha en el meridiano correspondiente y extrae ubicación resumida, por qué se usa aquí (su acción relevante) y la inserción.
4. Cruza con las precauciones: si algún punto tiene contraindicación relevante (embarazo, órganos subyacentes, vasos), señálalo junto al punto.

Formato de respuesta sugerido para síntoma:

```
## <Síntoma> — puntos sugeridos

**Principales** (base de la receta)
| Punto | Nombre | Ubicación breve | Por qué | Inserción |
|---|---|---|---|---|
| ... |

**Complementarios según patrón**
- *<Patrón A>* (signos: ...): puntos + razón
- *<Patrón B>* (...): ...

**Puntos locales / distales** (si aplica)

⚠️ Precauciones: ...
```

### 2. Por punto (código o nombre)

Lee la ficha y respóndela completa: código, pinyin, caracteres, traducción, ubicación, categorías, acciones, indicaciones, inserción, moxibustión, precauciones. Si el usuario pregunta algo concreto (solo la ubicación, solo la profundidad), responde eso primero y ofrece el resto en una línea.

### 3. Por meridiano o categoría

- Meridiano: lista los puntos del archivo en una tabla (código, pinyin, ubicación breve, categoría principal). Añade el trayecto general si lo pide.
- Categoría (ej. "puntos Xi", "Shu dorsales", "puntos Mar"): usa `categorias.md`.

### Consultas mixtas

Si la pregunta combina flujos (ej. "ficha del E36 y ¿puedo usarlo con IG4 en embarazada?"), responde primero la pregunta directa en 1–2 líneas (sí/no y por qué), luego la ficha pedida y al final la alternativa o receta. Quien pregunta "¿puedo…?" necesita el veredicto antes que el detalle.

### 4. Armar una receta / protocolo

Combina 6–12 puntos típicamente: puntos locales + distales + según patrón, respetando principios clásicos (combinación arriba-abajo, izquierda-derecha, Yuan-Luo, Shu-Mu). Explica la lógica de cada elección. Indica técnica de estimulación orientativa (tonificación / dispersión / neutra) según el patrón.

## Criterios de calidad

- **Fidelidad a las fuentes.** Los datos provienen de la tradición estándar (textos como *A Manual of Acupuncture* de Deadman, *Fundamentos de Acupuntura y Moxibustión de China*, estándar OMS de localización 2008). Si el usuario pregunta algo que no está en los archivos, puedes responder con tu conocimiento, pero dilo ("no está en la referencia; según la tradición…") y evita inventar datos específicos como profundidades.
- **Divergencias entre fuentes.** Cuando las referencias den criterios distintos (profundidad, restricción en embarazo, ubicación), menciona ambos y aplica el más conservador en la recomendación práctica. Si el índice divide un síntoma en varias entradas (ej. lumbalgia aguda / crónica), presenta cada una en su propia sección.
- **Seguridad siempre visible.** Puntos sobre tórax/espalda alta (riesgo de neumotórax), cerca de arterias (ST9, LU9, HT1…), sobre órganos, en fontanelas, o contraindicados en embarazo (LI4, SP6, BL60, BL67, GB21, CV3–CV7 bajo abdomen, puntos lumbosacros…) deben llevar su advertencia cuando se recomiendan.
- **Ubicación en cun.** Da la ubicación en cun (proporcional) y con referencias anatómicas palpables. Si el usuario parece no conocer el cun, explícalo una vez (1 cun ≈ ancho de la articulación interfalángica del pulgar del paciente; 3 cun ≈ ancho de cuatro dedos juntos a nivel de la articulación IFP del índice).
- **No sustituye diagnóstico.** Ante síntomas de alarma (dolor torácico, déficit neurológico agudo, fiebre alta, sangrado, trauma), menciona que requieren evaluación médica y no solo acupuntura. Una línea basta; no sermonees.
- **Idioma.** Responde en español. Mantén pinyin con tonos cuando esté en la ficha y los caracteres chinos.
