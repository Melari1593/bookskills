# Apharsemon, mirra y olíbano como grafo

[`grafo_mirra_olibano.html`](grafo_mirra_olibano.html) es el mapa interactivo del capítulo "Apharsemon, Myrrh and Olibanum: Ancient Medical Plants" (Ben-Yehoshua y Hanuš), en Z. Yaniv y N. Dudai (eds.), *Medicinal and Aromatic Plants of the Middle-East* (Springer, 2014), pp. 67 y siguientes.

- 9 partes, 39 secciones, 31 nodos (plantas, compuestos, usos y hechos históricos) y 4 tablas.
- Resúmenes con palabras propias: ningún texto del grafo comparte 8 palabras seguidas con el capítulo.
- 14 afirmaciones médicas verificadas en PubMed, Cochrane, EMA/HMPC y OMS, convertidas en 11 alertas.

## Resultado de la verificación

| Veredicto | Afirmaciones |
|---|---|
| Respaldado con matices | Boswellia en artrosis (Cochrane: −17/100 en dolor), asma, actividad antimicrobiana de la mirra |
| Superado | Boswellia en colitis y Crohn (ensayo de 52 semanas sin diferencia con placebo) |
| Contradicho | Mirazid en esquistosomiasis (cura 9–16 % frente a 63–80 % con praziquantel) y en fasciolosis; gugulípido para el colesterol (LDL +4–5 %) |
| Sin evidencia en humanos | Incensol y ánimo, efectos anticancerosos, β-cariofileno, analgesia de la mirra |
| Riesgo omitido | Humo de incienso y carcinoma escamoso respiratorio (RR 1,8); mirra en embarazo, lactancia y niños, interacción con warfarina y dermatitis de contacto |

## Archivos

- [`grafo_mirra_olibano.json`](grafo_mirra_olibano.json): datos del grafo.
- [`capitulo.py`](capitulo.py): definición del grafo (estructura, resúmenes y prerrequisitos).
- [`afirmaciones.md`](afirmaciones.md): las 14 afirmaciones seleccionadas.
- [`verif.md`](verif.md): veredicto, evidencia, fuentes con DOI o PMID, confianza y log de búsqueda.
- [`alertas.json`](alertas.json): textos de las alertas.

## Límites

- LiverTox estaba bloqueado: la hepatotoxicidad de Boswellia queda sin verificar.
- La EMA no tiene monografía de Boswellia.
- Varias cifras del capítulo no se pudieron confirmar (composición de la mirra, algunos valores de laboratorio); están listadas en `verif.md`.
- El texto del capítulo no se versiona.
