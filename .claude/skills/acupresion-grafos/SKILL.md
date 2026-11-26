---
name: acupresion-grafos
description: Grafo combinado de tres libros de acupresión y MTC (Dalet, Acupressure Self-Care Handbook; Rosenfarb, Healing Your Eyes; Patzek, Medicina tradicional china para mujeres) con puntos compartidos, 34 artículos de PubMed y alertas de seguridad. Úsala para saber qué dice cada libro de un punto (SP6, PC6, LI4) o de un síntoma (náuseas del embarazo, dolor menstrual, migraña, ojo seco, insomnio), comparar los libros, ver la evidencia y los riesgos, o entregar el HTML, aunque no nombren los libros.
---

# Grafos de acupresión: Dalet, Rosenfarb y Patzek

Esta skill une tres grafos de libro en uno. Agrega puentes entre ellos: puntos compartidos, evidencia de PubMed por tema y alertas comunes.

| Prefijo | Libro | Contenido |
|---|---|---|
| D | Dalet, *Acupressure Self-Care Handbook* (2023) | 13 partes, 83 cuadros por aparato. Puntos con código asignado y verificado con `acupuntura-puntos`. |
| R | Rosenfarb, *Healing Your Eyes with Chinese Medicine* (2007) | 8 capítulos: teoría, patrones oculares, acupuntura, hierbas, qigong, casos y terapias en casa. |
| P | Patzek y Hertzer, *Medicina tradicional china para mujeres* (2003) | Fundamentos, diagnóstico, ginecología y embarazo. Incluye 28 fórmulas, 13 recetas resumidas y 16 puntos de la oreja. |
| X | Puentes (creados por Claude) | X1: 32 puntos usados en dos o tres libros. X2: evidencia de PubMed por tema. X3: seguridad común. |

Archivos:
- `references/grafo.json`: el grafo combinado (esquema de la skill `grafo-de-libro`). Las secciones llevan el prefijo del libro (`P3.5` = Patzek 3.5) y los ítems también (`p_sp6`, `d_ev_pc6_nvp`, `x_sp6`).
- `references/evidencia.md`: tabla de los 34 artículos de PubMed con PMID, DOI y sección, log de búsqueda y huecos.
- `scripts/buscar.py`: busca un punto, un síntoma o una sección.
- `assets/grafo-acupresion-tres-libros.html`: el HTML combinado. También están los tres HTML de cada libro.

Si estos archivos no están en la sesión, lee el repositorio GitHub `Melari1593/bookskills`, carpeta `.claude/skills/acupresion-grafos/`. Los grafos de cada libro están en `grafos/`.

## Consultar

1. Ejecuta `python scripts/buscar.py "<término>"`. Acepta:
   - un código OMS (`SP6`, `PC6`, `BL67`);
   - un síntoma o concepto, con o sin acentos (`náuseas`, `migraña`, `Yang de riñón`);
   - un número de sección (`P3.5`, `X2.5`).
2. Lee la salida. Trae las secciones y los ítems de cada libro, los prerrequisitos, la evidencia de PubMed relacionada y las alertas ⚠.
3. Para una comparación entre libros, empieza por la sección `X1.<código>` del punto. Sus prerrequisitos son las secciones de cada libro que usan el punto.
4. Para la evidencia de un tema, abre la sección `X2.x`. Sus prerrequisitos son las secciones de los libros que tratan el tema.

Los arcos de prerrequisito son una interpretación de Claude, no una cita de los autores.

## Responder

- Separa lo que dice el libro de la evidencia. El `summary` de una sección resume al autor. La evidencia está en los ítems con PMID.
- Si citas un hallazgo de PubMed, di "según PubMed" y da el DOI como enlace.
- Si el libro de un punto lo ubica distinto a la ficha estándar, dilo. Ejemplo: Patzek ubica SP6 a 4 cun; la ficha OMS lo ubica a 3 cun.
- Patzek usa la numeración antigua de vejiga: V 54 = BL40 hoy.
- Para la ubicación exacta, las funciones y la técnica de un punto, usa también la skill `acupuntura-puntos`. Para el diagnóstico por patrones, usa su `references/diagnostico.md`.
- Si el tema no tiene evidencia en `evidencia.md`, no la supongas. Busca en PubMed (skill `biotech-research`), da la fecha de búsqueda y el DOI.

## Seguridad (lee X3 siempre que haya embarazo, hierbas o un cuadro grave)

- **Embarazo**: no estimular LI4, SP6, BL60, BL67, GB21, BL31–BL34, Zigong, Duyin ni el abdomen bajo. Excepción: BL67 con moxa para la presentación de nalgas, con indicación profesional. Varios cuadros de Dalet y de Patzek usan estos puntos; `x_prohibidos` lista dónde.
- **Hierbas**:
  - Acónito (fu zi): está en You Gui Wan de Rosenfarb y en 4 fórmulas de Patzek. Es cardiotóxico. En el embarazo está contraindicado.
  - Toosendan: es hepatotóxico.
  - Mu tong: puede venir sustituido por *Aristolochia*.
  - Danggui: potencia la warfarina.
  - Los nombres clásicos de las fórmulas de Patzek son una identificación de Claude.
- **Derivar sin demora**: pérdida de visión, dolor ocular, glaucoma o DMAE húmeda; hipertensión o edema en el embarazo; fiebre con mastitis; sangrado uterino anormal; dolor torácico. No retrases anti-VEGF ni hipotensores oculares, aunque Rosenfarb los presente como último recurso.

## Evidencia: resumen por tema

| Tema | Hallazgo | Certeza |
|---|---|---|
| Náuseas del embarazo (PC6) | Reduce síntomas | Baja a moderada |
| Presentación de nalgas (BL67 + moxa) | Menos presentaciones no cefálicas | Moderada |
| Dolor del parto | La acupresión puede reducir un poco el dolor | Baja a muy baja |
| Dolor lumbopélvico del embarazo | A favor de la acupuntura | Fuerte, según la revisión 2015 |
| Prevención de migraña (agujas) | Menos crisis; efecto pequeño frente a simulada | Moderada |
| Lumbalgia crónica | Menos dolor y discapacidad | Baja (6 ECA pequeños) |
| Ansiedad | Reduce la ansiedad | Baja, heterogeneidad alta |
| Insomnio | Mejor que solo higiene del sueño | Baja |
| Estreñimiento (auricular, masaje) | Más deposiciones | Baja a muy baja |
| Ojo seco | Mejora pruebas lagrimales, no los síntomas | Baja |
| Miopía infantil (auricular) | Podría frenar la progresión | Baja |
| DMAE, retinosis, glaucoma | Sin mejoría clara | Baja a muy baja |
| Dismenorrea, SPM, sofocos | Insuficiente o sin efecto claro | Baja |
| FIV (transferencia) | Sin efecto en nacidos vivos | Moderada a alta |
| Placenta retenida | Solo series de casos | Muy baja |

La fila completa de cada tema, con PMID y DOI, está en `references/evidencia.md`.

## Entregar el mapa

- Para ver los tres libros juntos, entrega `assets/grafo-acupresion-tres-libros.html`. Tiene un buscador, una leyenda con un color por libro y tres vistas. El botón «Trazar prerrequisitos» lleva de un punto o tema a las secciones de cada libro.
- Para un solo libro, entrega su HTML.
- Para modificar el grafo, edita el `grafo.json` del libro en `grafos/`. Después ejecuta `combinar.py` y reconstruye el HTML con la skill `grafo-de-libro`. Si no tienes `combinar.py`, edita `references/grafo.json` directamente.

## Límites

- El grafo resume los libros con palabras de Claude. No reproduce el texto, las cantidades de las fórmulas ni los pasos de las recetas.
- Dalet no da códigos de puntos: los asignó Claude y los verificó con `acupuntura-puntos`.
- Los puntos de la oreja de Patzek siguen la escuela alemana. Confirma su ubicación en un atlas auricular.
- La evidencia es de la búsqueda del 2026-11-26. No sustituye la valoración clínica.
