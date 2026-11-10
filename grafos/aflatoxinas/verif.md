# Verificación de afirmaciones sobre aflatoxinas

Fecha: 2026-11-08. Fuente principal: `/home/claude/aflatoxinas/informe-aflatoxinas.md`, verificado ese mismo día con PubMed (DOI indicado) y fuentes oficiales (OMS, IARC vía INCHEM, Reglamento UE 2023/915, Codex vía norma filipina, FDA, MinSalud e INVIMA, USDA FSIS, AESAN, SFA, AGES).

Los veredictos A1–A8 se reutilizan del informe sin cambio. A9–A11 se derivan de la parte de volátiles del mismo informe. No se repitieron búsquedas ya hechas. Las cifras y los DOI se copian del informe. Los datos no confirmados del informe no se usan como hechos. Alertas también en `trabajo/alertas.json`.

## Resumen de veredictos

| A | id | Veredicto | Confianza |
|---|---|---|---|
| A1 | u_coccion_tostado | contradicho | alta |
| A2 | h_sin_olor | contradicho | alta |
| A3 | u_retirar_moho | riesgo documentado | alta |
| A4 | u_nixtamalizacion | respaldado con matices | alta |
| A5 | p_leche | respaldado con matices | media |
| A6 | u_embarazo_peso_nacer | sin evidencia en humanos | media |
| A7 | u_vacuna_vhb | respaldado con matices | alta |
| A8 | h_vigilancia_invima | riesgo omitido | media |
| A9 | u_olfato_humano | contradicho | media |
| A10 | u_nariz_electronica | contradicho | media |
| A11 | c_mvoc_crecimiento | contradicho | media |

Conteo: respaldado 0 · respaldado con matices 3 · sin evidencia en humanos 1 · contradicho 5 · riesgo documentado 1 · riesgo omitido 1.

Nota sobre A6: el informe lo expresa como «sin evidencia concluyente en humanos». Aquí se usa el veredicto «sin evidencia en humanos» porque el metaanálisis de peso al nacer no fue significativo; la transferencia placentaria sí está confirmada.

---

## A1 · u_coccion_tostado
**Afirmación.** Cocinar o tostar elimina las aflatoxinas.
**Veredicto.** Contradicho.
**Evidencia.** Maní tostado a 180 °C por 20 min: degradación de 55 %, 64 % y 81 % según la concentración inicial (35, 332 y 695 µg/kg; p < 0,05). Con 85 µg/kg iniciales, la reducción fue 61,6 % a 160 °C, 83,6 % a 180 °C y 89,7 % a 200 °C; los autores concluyen que el tostado solo no basta (Martins 2017). Dos revisiones sobre estabilidad en cereales coinciden: el procesado reduce de forma significativa, pero no elimina (Milani 2014; Bullerman 2007). La OMS indica que la mayoría de las micotoxinas son estables y sobreviven al procesado.
**Alerta.** Cocinar y tostar no eliminan las aflatoxinas. En maní, el tostado a 180 °C por 20 minutos degradó entre 55 % y 81 %, según la contaminación inicial. Siempre queda toxina residual. Un alimento muy contaminado sigue siendo peligroso después de cocinarlo. La prevención está en el origen: buena cosecha, secado y almacenamiento, y descarte de lotes sospechosos. (Martins 2017; OMS 2023)
**Fuentes.** Martins 2017, Food Res Int, https://doi.org/10.1016/j.foodres.2017.03.052 · Milani 2014, J Sci Food Agric, https://doi.org/10.1002/jsfa.6600 · Bullerman 2007, Int J Food Microbiol, https://doi.org/10.1016/j.ijfoodmicro.2007.07.035 · OMS 2023, https://www.who.int/news-room/fact-sheets/detail/mycotoxins
**Confianza.** Alta.

## A2 · h_sin_olor
**Afirmación.** Si no se ve ni se huele moho, el alimento no tiene aflatoxinas.
**Veredicto.** Contradicho.
**Evidencia.** El USDA FSIS señala que solo una parte del moho es visible y que los filamentos pueden ser profundos y difíciles de ver, mientras las toxinas se concentran en y alrededor de esos filamentos y pueden extenderse por todo el alimento. La Singapore Food Agency describe las aflatoxinas como inodoras, insípidas e incoloras. En pistacho la identificación visual es imperfecta: la fluorescencia verde-amarilla brillante se relaciona con el contenido en cosecha, pero su uso en poscosecha tiene limitaciones (Hadavi 2005). Las vigilancias detectan toxina en alimentos de aspecto normal: 27 % de arepas de fábrica en Colombia, media 15,1 µg/kg (Blanco-Lizarazo 2019), y 100 % de 51 leches en polvo del Caribe con M1 (Marimón Sibaja 2019).
**Alerta.** La ausencia de moho visible u olor no garantiza que no haya aflatoxinas. La toxina puede quedar tras desaparecer el hongo, y los filamentos pueden ser invisibles. En Colombia, 27 % de arepas de fábrica tenían aflatoxina B1, con media de 15,1 µg/kg. La leche contaminada con M1 nunca muestra moho. Solo el análisis de laboratorio confirma el nivel. (USDA FSIS; Blanco-Lizarazo 2019)
**Fuentes.** USDA FSIS, Molds on Food, https://www.fsis.usda.gov/sites/default/files/media_file/2021-02/Molds_on_Food.pdf · SFA, https://www.sfa.gov.sg/food-information/risk-at-a-glance/aflatoxins-and-food-safety · Hadavi 2005, Food Addit Contam, https://doi.org/10.1080/02652030500306976 · Blanco-Lizarazo 2019, Food Addit Contam Part A, https://doi.org/10.1080/19440049.2019.1615643 · Marimón Sibaja 2019, Food Addit Contam Part B, https://doi.org/10.1080/19393210.2019.1567611
**Confianza.** Alta.

## A3 · u_retirar_moho
**Afirmación.** Quitar la parte con moho vuelve seguro el alimento.
**Veredicto.** Riesgo documentado.
**Evidencia.** El USDA FSIS distingue dos conductas. En quesos duros y en frutas y verduras firmes se puede cortar al menos 2,5 cm alrededor y por debajo del punto enmohecido, sin tocar el moho con el cuchillo. En cambio indica descartar, entre otros, mantequilla de maní, legumbres, frutos secos, pan y productos de panadería, cereales y pastas cocidas, quesos blandos, embutidos y frutas y verduras blandas. La razón es que los filamentos penetran en profundidad y las toxinas se extienden por todo el alimento. El FSIS añade que las aflatoxinas se consideran contaminantes inevitables incluso con buenas prácticas, y que el maní y el maíz de campo son los alimentos más asociados.
**Alerta.** En maní, frutos secos, legumbres, pan y cereales cocidos, quitar el moho no vuelve seguro el alimento: hay que descartarlo. Los filamentos penetran y la toxina se extiende más allá de la parte visible. Cortar el moho solo se acepta en quesos duros y verduras firmes, retirando al menos 2,5 cm alrededor. (USDA FSIS)
**Fuentes.** USDA FSIS, Molds on Food, https://www.fsis.usda.gov/sites/default/files/media_file/2021-02/Molds_on_Food.pdf · OMS 2023, https://www.who.int/news-room/fact-sheets/detail/mycotoxins · AGES, https://www.ages.at/en/human/nutrition-food/residues-contaminants-from-a-to-z/aflatoxins
**Confianza.** Alta.

## A4 · u_nixtamalizacion
**Afirmación.** La nixtamalización elimina las aflatoxinas del maíz.
**Veredicto.** Respaldado con matices. Reduce mucho, pero no elimina, y parte reaparece en medio ácido.
**Evidencia.** La nixtamalización tradicional redujo la B1 en 94 %, la M1 en 90 % y el dihidrodiol de B1 en 93 % (Elias-Orozco 2002). En condiciones reales de Honduras la reducción de grano a tortilla fue 83 % (Cabrera-Meraz 2021). El matiz es la reversibilidad: en maíz con 678,3 µg/kg de aflatoxinas totales la reducción aparente en tortilla fue 93,2 %, pero al acidificar los extractos reapareció 57,2 % en la masa y 33,9 % en la tortilla; los autores concluyen que el proceso no logra detoxificación total porque el medio ácido de la digestión puede reconstituir la molécula (Méndez-Albores 2004). En mezcla de maíz y frijol, hasta 2,5 % de hidróxido de calcio redujo la toxina en 75 % (Mannara 2024). En México se halló B1 sobre el límite de detección en maíz nixtamalizado, con márgenes de exposición entre 257 y 15, por debajo de 10 000 (Gilbert Sandoval 2019).
**Alerta.** La nixtamalización reduce mucho las aflatoxinas, entre 83 % y 94 % según el estudio, pero no las elimina. Al acidificar las muestras reapareció entre 33,9 % y 57,2 % de la toxina, lo que sugiere que el medio ácido del estómago puede reconstituirla. No se debe nixtamalizar maíz visiblemente contaminado para «recuperarlo». (Elias-Orozco 2002; Méndez-Albores 2004)
**Fuentes.** Elias-Orozco 2002, Food Addit Contam, https://doi.org/10.1080/02652030210145054 · Méndez-Albores 2004, J Sci Food Agric, https://doi.org/10.1002/jsfa.1853 · Mannara 2024, Mycotoxin Res, https://doi.org/10.1007/s12550-024-00570-1 · Cabrera-Meraz 2021, Heliyon, https://doi.org/10.1016/j.heliyon.2021.e08506 · Gilbert Sandoval 2019, Toxicol Rep, https://doi.org/10.1016/j.toxrep.2019.10.008
**Confianza.** Alta.

## A5 · p_leche
**Afirmación.** Las aflatoxinas en la leche son un riesgo para los niños.
**Veredicto.** Respaldado con matices. El riesgo depende del nivel y del volumen consumido; algunas evaluaciones lo clasifican como aceptable y otras no.
**Evidencia.** La M1 es un metabolito cancerígeno de la B1 que pasa a la leche. En Colombia, 100 % de 51 muestras de leche en polvo del Caribe tenían M1 (0,20–1,19 µg/kg) y 55 % superó 0,5 µg/kg; la ingesta máxima estimada (0,007–0,013 µg/persona/día) quedó por encima de la media estimada para América Latina por el JECFA (0,0035 µg/persona/día) (Marimón Sibaja 2019). En Bogotá, 69,2 % y 79,4 % de 241 leches tenían M1 por encima de 10 ng/L, con máximos de 213 y 288,9 ng/L; todas cumplían la norma local de entonces (400 ng/L) (Diaz 2006). Una revisión en África subsahariana halló muestras por encima del límite europeo en todos los estudios, con lactantes y niños pequeños como los más expuestos (Mayezana 2026). En el metaanálisis global de leche materna el margen de exposición fue aceptable salvo en un país (Fakhri 2025).
**Alerta.** La leche puede contener aflatoxina M1 y los niños son el grupo más expuesto, por su mayor consumo relativo. En leche en polvo del Caribe colombiano, 55 % de las muestras superó 0,5 µg/kg. El límite europeo es 0,050 µg/kg, diez veces más estricto. No hay que suspender la leche; hay que exigir vigilancia y producto de origen controlado. (Marimón Sibaja 2019; Reg. UE 2023/915)
**Fuentes.** Marimón Sibaja 2019, Food Addit Contam Part B, https://doi.org/10.1080/19393210.2019.1567611 · Diaz 2006, Food Addit Contam, https://doi.org/10.1080/02652030600681617 · Mayezana 2026, J Food Prot, https://doi.org/10.1016/j.jfp.2026.100956 · Fakhri 2025, J Food Prot, https://doi.org/10.1016/j.jfp.2025.100462 · Reglamento (UE) 2023/915, resumen: https://www.food-safety.com/articles/8573-new-eu-maximum-levels-for-contaminants-in-foods-aflatoxins-metals-and-more
**Confianza.** Media.

## A6 · u_embarazo_peso_nacer
**Afirmación.** La exposición en el embarazo reduce el peso al nacer.
**Veredicto.** Sin evidencia en humanos (para el peso al nacer). La asociación es plausible y hay datos de crecimiento posnatal, pero el metaanálisis no fue significativo.
**Evidencia.** La revisión sistemática de desenlaces neonatales (7 estudios, 4047 participantes) no halló asociación significativa agrupada con pequeño para la edad gestacional, parto pretérmino, bajo peso al nacer, peso ni talla al nacer. La heterogeneidad fue alta (I² 68,6 % para bajo peso; 96,8 % para peso; 93,1 % para talla). El análisis de sensibilidad sí sugirió mayor probabilidad de bajo peso y relación inversa con peso y talla (Ghorbani Nejad 2025). La evidencia de crecimiento posnatal es más consistente: en Gambia la albúmina aducida materna predijo la ganancia de peso (p = 0,012) y de talla (p = 0,044) en el primer año, con una estimación de +0,8 kg y +2 cm al bajar de 110 a 10 pg/mg (Turner 2007). La transferencia placentaria está confirmada por la IARC y por los aductos en sangre de cordón (media geométrica 10,1 pg/mg).
**Alerta.** La aflatoxina cruza la placenta, pero el metaanálisis de siete estudios no confirmó menor peso al nacer. La heterogeneidad fue muy alta y el análisis de sensibilidad sí apuntó a más bajo peso. Donde la evidencia es más consistente es en el crecimiento del primer año. Reducir la exposición en el embarazo sigue siendo razonable. (Ghorbani Nejad 2025; Turner 2007)
**Fuentes.** Ghorbani Nejad 2025, Arch Environ Occup Health, https://doi.org/10.1080/19338244.2025.2603898 · Turner 2007, Int J Epidemiol, https://doi.org/10.1093/ije/dym122 · Castelino 2013, Trop Med Int Health, https://doi.org/10.1111/tmi.12250 · IARC vol. 82, https://inchem.org/documents/iarc/vol82/82-04.html
**Confianza.** Media.

## A7 · u_vacuna_vhb
**Afirmación.** La vacuna de hepatitis B reduce el riesgo de cáncer por aflatoxinas.
**Veredicto.** Respaldado con matices. Elimina el cofactor viral, no la exposición a aflatoxina.
**Evidencia.** La interacción es multiplicativa: OR 73,0 (IC 95 % 36,0–148,3) con ambas exposiciones, frente a 11,3 solo con virus y 6,37 solo con aflatoxina; la fracción atribuible a aflatoxina fue 21 % en positivos para el virus y 8,8 % en negativos (Liu 2012). La vacunación reduce el cáncer hepático: en Taiwán la incidencia en niños de 6 a 14 años bajó de 0,70 a 0,36 por 100 000 (p < 0,01) (Chang 1997). En el ensayo por conglomerados de Qidong la eficacia a 30 años sobre cáncer hepático primario fue 84 % (IC 95 % 23–97 %) (Qu 2014) y a 37 años el HR fue 0,28 (0,11–0,70; p = 0,007), con 72 % de protección (Cao 2022). El matiz es el riesgo residual en personas sin el virus.
**Alerta.** La vacuna de hepatitis B reduce el cáncer de hígado de forma comprobada: 72 % de protección a 37 años en el ensayo de Qidong. Al quitar el virus, desaparece la sinergia con la aflatoxina, que multiplicaba el riesgo (OR 73,0 frente a 6,37). Pero la aflatoxina sigue siendo cancerígena sin el virus. Hay que vacunar y además controlar los alimentos. (Liu 2012; Cao 2022)
**Fuentes.** Liu 2012, Eur J Cancer, https://doi.org/10.1016/j.ejca.2012.02.009 · Chang 1997, N Engl J Med, https://doi.org/10.1056/NEJM199706263362602 · Qu 2014, PLoS Med, https://doi.org/10.1371/journal.pmed.1001774 · Cao 2022, Cancer Lett, https://doi.org/10.1016/j.canlet.2022.215652
**Confianza.** Alta.

## A8 · h_vigilancia_invima
**Afirmación.** Los frutos secos importados en Colombia están controlados.
**Veredicto.** Riesgo omitido. Existe norma, pero el plan de vigilancia 2024 no incluye frutos secos importados.
**Evidencia.** La Resolución 4506 de 2013 fija límites para maní y otras semillas oleaginosas, almendra, pistacho, semilla de albaricoque, avellana, nuez de Brasil y otros frutos de cáscara arbóreos, entre 4,0 y 15,0 µg/kg de suma según producto y destino. El documento técnico del plan de micotoxinas 2024 del INVIMA lista como alimentos muestreados arepa, avena, maní, harina de maíz, maíz, arroz, café, galletas, harina de trigo y bienestarina; los únicos productos importados muestreados son maíz, café y galletas. No aparecen leche, cacao, especias ni frutos secos importados. En la vigilancia de 2020 se analizaron 10 muestras de maní (0 no conformes, 1 detectable con 3,87 µg/kg) y no se reportó una categoría de frutos secos importados. El INVIMA sí describe muestreo en puertos, aeropuertos y pasos de frontera para los productos incluidos en el plan.
**Alerta.** Colombia tiene límites para frutos secos en la Resolución 4506 de 2013, entre 4 y 15 µg/kg. Pero el plan de vigilancia de micotoxinas 2024 del INVIMA no incluye frutos secos importados: solo muestrea maíz, café y galletas de importación. En la práctica, los frutos secos importados no tienen monitoreo sistemático publicado. Convendría preferir producto empacado con trazabilidad. (Res. 4506 de 2013; INVIMA 2024)
**Fuentes.** Resolución 4506 de 2013, https://normograma.invima.gov.co/compilacion/docs/resolucion_minsaludps_4506_2013.htm · INVIMA, plan micotoxinas 2024, https://www.invima.gov.co/invima_website/static/attachments/alimentos_otros_alimentos_y_bebidas/documento_tecnico_plan_micotoxinas_2024.pdf · INVIMA, informe micotoxinas 2020, https://www.invima.gov.co/invima_website/static/attachments/alimentos_otros_alimentos_y_bebidas/Informe_20Micotoxina_202020.pdf
**Confianza.** Media.

## A9 · u_olfato_humano
**Afirmación.** Si el alimento no huele a moho, no hay aflatoxina; el olfato basta para decidir.
**Veredicto.** Contradicho.
**Evidencia.** La búsqueda del informe en PubMed y en la web no halló ningún estudio que compare la intensidad de olor evaluada por personas con la concentración medida de aflatoxina (0 resultados en seis consultas específicas). La toxina es inodora, insípida e incolora según la Singapore Food Agency, de modo que lo que se percibe es el hongo o la oxidación de la matriz. Los volátiles de olor a moho citados en granos provienen de muchos hongos y de bacterias (Tuma 1989; Josselin 2021). Una nariz electrónica clasificó el olor de granos en dos clases con cerca de 90 % de acierto y superó el acuerdo entre dos inspectores humanos, pero ese estudio no midió micotoxinas (Börjesson 1996). La agencia austriaca advierte que el moho puede no haberse extendido de forma visible.
**Alerta.** Ningún estudio relaciona el olor percibido por personas con la concentración de aflatoxina. La toxina no tiene olor. Si un lote huele a moho, hay crecimiento fúngico: descártelo. Si no huele, eso no descarta la toxina. El olfato no sirve como prueba de seguridad. (SFA; AGES; informe 2026-11-08)
**Fuentes.** SFA, https://www.sfa.gov.sg/food-information/risk-at-a-glance/aflatoxins-and-food-safety · AGES, https://www.ages.at/en/human/nutrition-food/residues-contaminants-from-a-to-z/aflatoxins · Tuma 1989, Int J Food Microbiol, https://doi.org/10.1016/0168-1605(89)90065-2 · Börjesson 1996, Cereal Chem 73(4):457-461 (DOI no confirmado), https://cerealsgrains.org/publications/cc/backissues/1996/Documents/CC1996a78.html
**Confianza.** Media (ausencia de estudios, no prueba de ausencia de relación).

## A10 · u_nariz_electronica
**Afirmación.** Una nariz electrónica o un sensor de gases puede reemplazar el análisis de laboratorio.
**Veredicto.** Contradicho.
**Evidencia.** El único estudio con muestras naturales de maíz y una referencia analítica clasificó bien el 81 % de 161 muestras en dos clases y el 65 % en tres clases, con validación cruzada dejando uno fuera, y sus autores piden un conjunto de datos mayor; no informa sensibilidad ni especificidad (Ottoboni 2018). Los rendimientos altos vienen de muestras inoculadas en laboratorio: 100 % de identificación de granos infectados y error cuadrático medio de 1,0292 µg/kg con sensores y red neuronal, sin validación externa en el resumen (Foods 2026). Un biosensor con modelos de regresión bajó de R² 0,98 interno a 0,91 externo en maíz y de 0,97 a 0,86 en maní (J Hazard Mater 2025). Dos estudios, GC-IMS en maíz y SPME en almendra, detectan crecimiento fúngico y no miden aflatoxina.
**Alerta.** La nariz electrónica y los sensores de gases son, por ahora, herramientas de tamizaje. Con muestras naturales de maíz la exactitud informada fue 81 %. Las cifras cercanas al 100 % vienen de muestras inoculadas en laboratorio. Ningún estudio informa sensibilidad y especificidad separadas. Para aceptar o rechazar un lote, use un método validado. (Ottoboni 2018)
**Fuentes.** Ottoboni 2018, Toxins, https://doi.org/10.3390/toxins10100416 · Foods 2026, https://doi.org/10.3390/foods15050882 · J Hazard Mater 2025, https://doi.org/10.1016/j.jhazmat.2025.139883 · Front Microbiol 2024 (GC-IMS), https://doi.org/10.3389/fmicb.2024.1470115 · Beck 2016, J Agric Food Chem, https://doi.org/10.1021/acs.jafc.6b04220
**Confianza.** Media.

## A11 · c_mvoc_crecimiento
**Afirmación.** Los volátiles de Aspergillus indican que la cepa produce toxina.
**Veredicto.** Contradicho (para los volátiles de olor a moho más citados).
**Evidencia.** El 3-metil-1-butanol y el 2-metil-1-butanol los emitieron por igual una cepa no toxigénica, una toxigénica y su mutante no productor; el 1-octen-3-ol y la 3-octanona son volátiles de deterioro fúngico general en trigo y los producen varios hongos y bacterias (Josselin 2021; Tuma 1989). En el mismo estudio de 2021 aparecieron volátiles ligados a la ausencia de producción, no a la producción. Los candidatos a marcar toxigenicidad son sesquiterpenos: el alfa-gurjuneno y el trans-cariofileno aparecieron solo en cepas toxigénicas, con pico en el día 3 y ausencia en los días 1, 2, 8 y 10 (Zeringue 1993). Toda esta evidencia es de nivel D, solo con cromatografía de gases y sin olfatometría, con pocas cepas y en cultivo. No hay estudios equivalentes en Aspergillus parasiticus.
**Alerta.** Los volátiles de olor a moho (3-metil-1-butanol, 1-octen-3-ol, 3-octanona) no separan cepas que producen toxina de las que no: los emiten varios hongos y bacterias. Algunos sesquiterpenos solo aparecieron en cepas toxigénicas, pero la señal fue transitoria: presente el día 3 y ausente los días 1, 2, 8 y 10. (Zeringue 1993; Josselin 2021)
**Fuentes.** Josselin 2021, Toxins, https://doi.org/10.3390/toxins13100705 · Josselin 2022 (revisión), Int J Mol Sci, https://doi.org/10.3390/ijms232415557 · Zeringue 1993, Appl Environ Microbiol, https://doi.org/10.1128/aem.59.7.2264-2270.1993 · Tuma 1989, Int J Food Microbiol, https://doi.org/10.1016/0168-1605(89)90065-2 · Chen 2023, Food Chem, https://doi.org/10.1016/j.foodchem.2023.137048
**Confianza.** Media.

---

## Log de búsqueda

No se hicieron búsquedas nuevas: el informe de origen ya las hizo y se verificó el 2026-11-08. Esta tabla indica de dónde sale cada veredicto.

| # | Fuente | Consulta o sección usada | Resultado | Uso |
|---|---|---|---|---|
| 1 | Archivo local | informe-aflatoxinas.md, secciones 1 a 6 | 103 KB | Contenido de las 9 partes y de los 32 ítems |
| 2 | Archivo local | informe-aflatoxinas.md, sección 7 (ocho verificaciones) | 8 veredictos | A1–A8 reutilizados sin cambio |
| 3 | Archivo local | informe-aflatoxinas.md, parte 2, secciones 2 a 4 | tablas de MVOC y métodos | A9–A11 |
| 4 | Archivo local | informe-aflatoxinas.md, secciones 9.1, 9.2 y parte 2 sección 10 | 12 + 11 + 11 puntos | Datos no confirmados, excluidos del grafo |
| 5 | Archivo local | informe-aflatoxinas.md, secciones 9.3 y parte 2 sección 8 | 50 + 24 referencias | fuentes.md, con DOI copiados |
| 6 | Archivo local | informe-aflatoxinas.md, logs de búsqueda (40 + 31 entradas) | — | Se comprobó que las consultas de A9–A11 ya estaban hechas, por eso no se repitieron |
| 7 | PubMed | — | 0 consultas nuevas | Ninguna afirmación nueva lo requirió |
