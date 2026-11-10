# Aflatoxinas

Grafo de evidencia y revisión sobre las aflatoxinas. Se construyó desde PubMed y fuentes oficiales (IARC, OMS, EFSA, USDA FSIS, INVIMA, MinSalud), no desde un libro. Verificado el 2026-11-08.

- **Grafo:** [`grafo-aflatoxinas.html`](grafo-aflatoxinas.html). Tiene 9 partes, 37 secciones, 32 ítems y 11 alertas de evidencia. Abre sin servidor.
- **Informe completo:** [`informe-aflatoxinas.md`](informe-aflatoxinas.md). Cubre toxicología, límites regulatorios, Colombia, mitigación, volátiles de *Aspergillus* y métodos de detección. Incluye el log de búsqueda y los datos no confirmados.

## Partes del grafo

1. Qué son: AFB1, B2, G1, G2, M1 y los hongos productores.
2. Alimentos de riesgo y biomarcadores de exposición.
3. Mecanismo y toxicidad.
4. Cáncer hepático y hepatitis B.
5. Embarazo, lactancia e infancia.
6. Límites regulatorios: UE, Codex, FDA y Colombia.
7. Situación en Colombia y América Latina.
8. Mitigación y detección.
9. Conclusiones.

## Veredictos (11 afirmaciones)

| Veredicto | N.º | Afirmaciones |
|---|---|---|
| Contradicho | 5 | Cocinar o tostar las elimina; sin moho ni olor no hay aflatoxina; el olfato humano detecta la contaminación; una nariz electrónica reemplaza el análisis; los volátiles indican que la cepa es toxigénica |
| Respaldado con matices | 3 | Nixtamalización (reduce 83–94 %, pero reaparece al acidificar); AFM1 en la leche y riesgo infantil; vacuna de la hepatitis B |
| Riesgo documentado | 1 | Quitar la parte con moho no vuelve seguro el maní ni los frutos secos |
| Riesgo omitido | 1 | El plan del INVIMA 2024 no muestrea frutos secos importados |
| Sin evidencia en humanos | 1 | Menor peso al nacer: el metaanálisis de 7 estudios no fue significativo; el efecto en el crecimiento del primer año es más consistente |

## Hallazgos clave

- **Sinergia con hepatitis B:** OR de carcinoma hepatocelular de 73,0 con las dos exposiciones, 11,3 con solo el virus y 6,4 con solo aflatoxina (Liu 2012, doi:10.1016/j.ejca.2012.02.009).
- **Límites en Colombia frente a la UE:** leche 0,5 frente a 0,050 µg/kg de AFM1; maní de consumo directo 10 frente a 4 µg/kg. La Resolución 4506 de 2013 no fija un límite de AFB1 sola ni para alimentos de lactantes.
- **Exposición en Colombia:** AFM1 en 90 % de 50 muestras de leche materna; 27 % de las arepas de fábrica con AFB1 (media 15,1 µg/kg).
- **Olor:** las aflatoxinas no tienen olor. Los volátiles de *Aspergillus* son de nivel D (presentes, no probados como olorosos). Un lote sin olor a moho no está libre de aflatoxina.

## Archivos

- `grafo.json`, `capitulo.py`: datos y estructura del grafo.
- `afirmaciones.md`, `verif.md`, `alertas.json`: afirmaciones, verificación y alertas.
- `fuentes.md`: fuentes por sección con DOI o URL.

Grafos relacionados: [`../monografias-ingredientes/almendras-gestantes/`](../monografias-ingredientes/almendras-gestantes/) (aflatoxinas en la almendra) y la base [`../../odorantes-db/`](../../odorantes-db/) (volátiles de maní y avellana tostados).
