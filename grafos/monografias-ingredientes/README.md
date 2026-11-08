# Monografías de ingredientes

11 grafos: 10 monografías con la estructura de 9 partes de [`mirra-olibano-apharsemon`](../mirra-olibano-apharsemon/README.md). y un grafo de pregunta clínica (almendras en gestantes). Cada uno se construyó desde literatura científica (PubMed) y fuentes oficiales, no desde un libro. Cada afirmación de salud tiene un veredicto y una alerta dentro del grafo.

Índice visual: [`index.html`](index.html).

| Ingrediente | Especie | Secciones | Ítems | Afirmaciones | Alertas | Grafo |
|---|---|---|---|---|---|---|
| Guanábana | *Annona muricata* | 36 | 27 | 15 | 12 | [`grafo-guanabana.html`](guanabana/grafo-guanabana.html) |
| Guayaba | *Psidium guajava* | 31 | 31 | 13 | 12 | [`grafo-guayaba.html`](guayaba/grafo-guayaba.html) |
| Corozo | *Bactris guineensis* | 32 | 30 | 13 | 12 | [`grafo-corozo.html`](corozo/grafo-corozo.html) |
| Aguacate | *Persea americana* | 33 | 32 | 14 | 14 | [`grafo-aguacate.html`](aguacate/grafo-aguacate.html) |
| Café | *Coffea arabica · C. canephora* | 30 | 32 | 14 | 13 | [`grafo-cafe.html`](cafe/grafo-cafe.html) |
| Gulupa | *Passiflora edulis f. edulis* | 29 | 31 | 13 | 12 | [`grafo-gulupa.html`](gulupa/grafo-gulupa.html) |
| Açaí y asaí | *Euterpe oleracea · E. precatoria* | 31 | 32 | 14 | 14 | [`grafo-acai.html`](acai/grafo-acai.html) |
| Murumuru | *Astrocaryum murumuru s.l.* | 29 | 31 | 13 | 13 | [`grafo-murumuru.html`](murumuru/grafo-murumuru.html) |
| Camu camu | *Myrciaria dubia* | 30 | 32 | 13 | 11 | [`grafo-camu-camu.html`](camu-camu/grafo-camu-camu.html) |
| Aguaje (canangucha) | *Mauritia flexuosa* | 35 | 32 | 12 | 11 | [`grafo-aguaje.html`](aguaje/grafo-aguaje.html) |
| Almendras en gestantes | *Prunus dulcis · gestación y lactancia* | 34 | 31 | 13 | 13 | [`grafo-almendras-gestantes.html`](almendras-gestantes/grafo-almendras-gestantes.html) |

**Total:** 147 afirmaciones y 137 alertas.

| Veredicto | N.º |
|---|---|
| respaldado | 9 |
| respaldado con matices | 36 |
| sin evidencia en humanos | 53 |
| contradicho | 18 |
| riesgo documentado | 16 |
| riesgo omitido | 15 |

## Hallazgo principal por ingrediente

- **Guanábana.** La annonacina es neurotóxica. La cifra «10 000 veces más potente que la quimioterapia» viene de un estudio in vitro de 1996.
- **Guayaba.** La infusión de hoja no reemplaza el suero oral y el zinc en la diarrea infantil.
- **Corozo.** 7 de 13 afirmaciones no tienen evidencia en humanos. El vino artesanal tiene riesgo de metanol.
- **Aguacate.** El ensayo HAT contradice el efecto sobre el peso. Interactúa con la warfarina. La semilla no tiene evidencia en humanos.
- **Café.** Interacción con fluvoxamina. La cafeína pura en polvo y los enemas de café tienen riesgo documentado.
- **Gulupa.** Los ensayos con P. incarnata no aplican a la gulupa. La cáscara tiene glucósidos cianogénicos.
- **Açaí y asaí.** La pulpa sin pasteurizar transmite Chagas oral. Interfiere con la resonancia magnética.
- **Murumuru.** El material colombiano puede ser A. macrocalyx. La manteca es rica en ácidos láurico y mirístico.
- **Camu camu.** No previene resfriados. El polvo pierde vitamina C. Las dosis altas tienen riesgo de cálculos renales.
- **Aguaje (canangucha).** La cosecha con tala de palmas hembra no es sostenible. Falta evidencia de seguridad en el embarazo.
- **Almendras en gestantes.** No hay ensayos con almendra en diabetes gestacional. No se deben evitar los frutos secos por alergia. La almendra no reemplaza los suplementos ni la leche.

## Archivos por carpeta

- `grafo-<ingrediente>.html`: grafo interactivo. Abre sin servidor.
- `grafo.json`: datos del grafo.
- `capitulo.py`: partes, secciones, ítems y prerrequisitos.
- `fuentes.md`: fuentes con DOI o URL.
- `afirmaciones.md`, `verif.md`, `alertas.json`: afirmaciones, verificación y alertas. `verif.md` lista los datos no confirmados.

## Reconstruir un grafo

1. Copia `capitulo.py` a `scripts/` y `alertas.json` a `trabajo/` en una carpeta de trabajo.
2. Ejecuta `construir.py` de [`../nuts-seeds/`](../nuts-seeds/) para obtener `grafo.json`.
3. Renderiza con `build_graph.py` de la plantilla que muestra el campo `caution`.
