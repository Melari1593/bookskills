# Reacciones y fenómenos de la cocina: referencia para gastronomía molecular

Fecha de búsqueda: 2026-11-10.
Alcance: química y física de la cocina, con rangos medibles y riesgos.
Regla de este documento: cada cifra lleva su fuente. Si una cifra no tiene fuente verificada, no aparece en el texto y va a "Datos no confirmados".

## Convenciones

- Temperaturas en °C. Tiempos en s, min, h o días. Masas en g o kg.
- "aw" = actividad de agua (0 a 1).
- "Temperatura del centro" = temperatura medida en el punto más frío de la pieza.
- "Desnaturalización" = pérdida de la forma nativa de una proteína. "Coagulación" = agregación de proteínas desnaturalizadas en una red sólida. "Gelificación" = coagulación que retiene agua en un gel.
- "Según PubMed" marca datos tomados de resúmenes indexados en PubMed. Cada uno lleva su DOI en la sección "Referencias".
- Nivel de la fuente: [R] = revisión revisada por pares. [E] = estudio original revisado por pares. [O] = organismo oficial o norma. [D] = fuente divulgativa, no revisada por pares.
- Química del aroma: no se repite aquí. Para pirazinas, furanonas y aldehídos de Strecker, usa la skill `odorantes-clave` y la base `bookskills/odorantes-db` (ver sección 2.7).

---

## 1. Gastronomía molecular, cocina molecular y cocina "nota a nota"

### 1.1 Definiciones

- La gastronomía molecular es una disciplina científica. Busca los mecanismos de los fenómenos que ocurren al preparar y al consumir un plato. Hervé This y el físico Nicholas Kurti la definieron en 1988 [W-This2013, P-This2009].
- El primer nombre fue "gastronomía molecular y física". El nombre se acortó después de la muerte de Kurti en 1998 [W-This2013].
- "Gastronomía" significa aquí conocimiento sobre la comida. No significa alta cocina [W-This2013].
- La cocina molecular es una técnica, no una ciencia. Produce alimentos con herramientas, ingredientes y métodos "nuevos" (por ejemplo sifón, nitrógeno líquido, alginato de sodio). El término apareció en 1999 en el programa europeo INICON [W-This2013, P-This2009].
- La cocina "nota a nota" construye platos con compuestos puros o con mezclas simples de compuestos. Los compuestos se obtienen al fraccionar tejidos vegetales o animales. This la propuso por primera vez en 1994 en *Scientific American* [W-This2013].

### 1.2 Método de la disciplina

- This divide el trabajo en dos partes: modelar las "definiciones culinarias" (el objetivo de la receta) y explorar las "precisiones culinarias" (trucos, refranes, consejos) [P-This2005, P-This2009].
- Desde 1980 se recogieron más de 25 000 precisiones culinarias solo de la cocina francesa, según PubMed [P-This2009].
- El formalismo CDS/NPOS describe un plato como sistema disperso complejo. CDS describe los materiales coloidales. NPOS describe la organización del plato en el espacio [P-This2009, P-This2005].

### 1.3 Gastronomía molecular frente a cocina modernista

- La fuente de This (2013) separa ciencia (gastronomía molecular) y técnica (cocina molecular). No trata el término "cocina modernista" [W-This2013].
- Regla para esta skill: si la pregunta es "¿por qué pasa?", responde con gastronomía molecular. Si la pregunta es "¿cómo lo hago?", responde con técnica culinaria.

### 1.4 Uso en la cocina

- Toma un truco de cocina. Formula el mecanismo que lo explicaría. Diseña una prueba con una sola variable. Mide el resultado.

### 1.5 Riesgos

- En cocina nota a nota, cada compuesto puro necesita evaluación de toxicología y de dosis. This menciona nutrición, toxicología, costo y aceptación social como temas abiertos [W-This2013].

---

## 2. Reacción de Maillard

### 2.1 Qué pasa a nivel molecular

- Un grupo nucleófilo (amino de aminoácidos, péptidos o proteínas, o tiolato) ataca el carbonilo de un azúcar reductor [P-Maillard2025].
- Esta reacción inicial genera una serie de reacciones paralelas y sucesivas. Los compuestos α-dicarbonílicos son intermediarios muy reactivos. Producen el color y el sabor deseados. También producen productos finales de glicación avanzada (AGE) [P-Maillard2024].
- Las melanoidinas son los polímeros marrones del final de la reacción [P-Maillard2024].
- La degradación de Strecker ocurre cuando un α-dicarbonilo reacciona con un aminoácido libre. En un modelo de bizcocho, la leucina activó la vía de Strecker y formó 3-metilbutanal y pirazinas de forma rápida y específica [P-Cake2024, P-Cake2020].

### 2.2 Variables que la controlan

| Variable | Efecto confirmado | Fuente |
|---|---|---|
| pH | Es un parámetro clave de la velocidad. Controla la concentración de grupos nucleófilos disponibles. | [P-Maillard2025] |
| Temperatura | Controla la velocidad. En un bizcocho modelo, subir la temperatura de horneado aceleró la formación de volátiles de forma no lineal. A 200 °C la mayoría de los marcadores mostró una curva en campana (se forman y después se degradan). | [P-Maillard2025, P-Cake2024] |
| Tiempo | Controla la cantidad de producto. | [P-Maillard2025] |
| Actividad de agua | Influye de forma significativa en la velocidad. | [P-Maillard2025] |
| Convección del horno | En el bizcocho modelo, el nivel de convección no cambió la velocidad de reacción. | [P-Cake2024] |

- Inferencia química (sin cifra): a pH más alto hay más grupos amino sin protonar. Por eso un medio alcalino acelera la reacción. El rango numérico de pH no está confirmado (ver "Datos no confirmados").

### 2.3 Qué produce

- Sabor y aroma: aldehídos de Strecker, pirazinas, furanonas (ver 2.7).
- Color: pardo, por melanoidinas [P-Maillard2024].
- Textura: costra seca en la superficie.
- Otros efectos: los productos de Maillard tienen actividad antioxidante en alimentos modelo y reales [P-MRPantiox2018].

### 2.4 Uso en la cocina

- Si quieres más costra, seca la superficie antes de calentar. La reacción que forma acrilamida se favorece con baja humedad (ver 2.5). La misma condición favorece el dorado.
- Si quieres más aroma tostado, añade una fuente de aminoácidos libres y un azúcar reductor. La leucina más glucosa forma 3-metilbutanal (malta) y pirazinas (tostado) [P-Cake2024].
- Si quieres menos riesgo, para el dorado en color dorado claro (ver 2.5).

### 2.5 Riesgo principal: acrilamida

**Formación**
- La acrilamida se forma al calentar asparagina libre, sobre todo con azúcares reductores. También se forma a partir de productos tempranos de Maillard (N-glicósidos), según PubMed [P-Stadler2002].
- La acrilamida se forma por encima de 120 °C en condiciones de baja humedad [O-EFSA2015, P-AA2013].
- En papa, el sustrato limitante son los azúcares reductores (glucosa y fructosa). En cereales y café, el sustrato limitante es la asparagina libre, según PubMed [P-AA2013].
- El blanqueado reduce los azúcares de la papa [P-AA2013].
- La glicina o la enzima asparaginasa reducen la acrilamida en algunos productos horneados [P-AA2013].

**Evaluación de riesgo (EFSA 2015)**
- Los márgenes de exposición indican preocupación por efectos neoplásicos, con base en estudios en animales [O-EFSA2015].
- Punto de referencia: BMDL10 = 0,17 mg/kg de peso corporal por día (tumores en ratón) [O-EFSA2015].
- Exposición media en Europa: 0,4 a 1,9 µg/kg de peso corporal por día. Percentil 95: 0,6 a 3,4 µg/kg por día [O-EFSA2015].
- Fuente principal en la dieta: productos de papa frita (excepto papas de paquete y snacks) [O-EFSA2015].
- Los estudios epidemiológicos no han demostrado que la acrilamida sea cancerígena en humanos [O-EFSA2015].

**Mitigación en casa (FDA)**
- Guarda la papa fuera de la nevera, en un lugar fresco y oscuro. La papa refrigerada forma más acrilamida al cocinarla [O-FDA-AA].
- Remoja las tajadas crudas de papa en agua durante 15 a 30 min. Escurre y seca antes de freír u hornear [O-FDA-AA].
- Fríe hasta color amarillo dorado, no marrón [O-FDA-AA].
- Tuesta el pan hasta marrón claro. Evita las zonas muy oscuras [O-FDA-AA].
- Orden de formación según FDA: freír > asar trozos > hornear papa entera. Hervir y microondas (papa entera con piel) no forman acrilamida [O-FDA-AA].

**Mitigación de referencia para negocios (Reglamento UE 2017/2158, Anexo II, parte A)**
- Almacena la papa por encima de 6 °C [O-UE2017/2158].
- Lava y remoja en agua fría de 30 min a 2 h. Enjuaga antes de freír. Alternativa: remojo corto en agua tibia y enjuague [O-UE2017/2158].
- Blanquea cuando sea posible [O-UE2017/2158].
- Fríe por debajo de 175 °C, tan bajo como lo permita la inocuidad [O-UE2017/2158].
- Retira migas y restos del aceite con frecuencia [O-UE2017/2158].
- Usa y exhibe una guía de color para el personal [O-UE2017/2158].
- Nota: el texto leído es la versión consolidada en legislation.gov.uk. Los niveles de referencia del Anexo IV no se pudieron leer (ver "Fuentes bloqueadas").

### 2.6 Otros compuestos indeseados

| Compuesto | Cómo se forma | Condición de riesgo | Mitigación confirmada | Fuente |
|---|---|---|---|---|
| Furano y metilfuranos | Calentamiento de vitamina C, carbohidratos, aminoácidos, ácidos grasos insaturados y carotenoides | Alimentos listos en frasco o lata (bebés); café; cereales | Recalentar comida infantil en baño de agua sin tapa reduce la exposición de 15 a 30 %. El café hervido o turco pierde más furano que el filtrado o el espresso. | [O-EFSA-furano2017] |
| Furano y furfural | Maillard y caramelización en bizcocho modelo (glucosa + leucina) | Horneado | — | [P-Furan2017] |
| HMF (5-hidroximetilfurfural) y furfural | Se forman por caramelización y por Maillard | Horneado con glucosa | — | [P-Cake2020] |
| Aminas heterocíclicas (HCA/HAA) | Aminoácidos + azúcares + creatina o creatinina a alta temperatura | Carne de músculo frita en sartén o asada a la parrilla. Más formación por encima de 150 °C (300 °F) y con más tiempo. | Evita llama directa y metal muy caliente. Precocina en microondas. Voltea la carne con frecuencia. Retira las partes carbonizadas. No uses los jugos para salsa. | [O-NCI, P-Turesky2018] |
| Hidrocarburos aromáticos policíclicos (PAH) | Grasa y jugos que gotean sobre la llama o el carbón producen humo que cubre la carne. También el ahumado. | Parrilla con goteo; ahumado | Mismas medidas que HCA | [O-NCI, P-Turesky2018] |
| Compuestos N-nitroso (NOC) | Curado de carne con nitrito; el hemo de la carne cataliza su formación | Carne procesada | — | [P-Turesky2018] |
| CML (N6-carboximetil-lisina) y AGE | Vía de los α-dicarbonilos | Calentamiento prolongado | — | [P-Maillard2025, P-Maillard2024] |

- Contexto: la IARC clasificó la carne procesada como cancerígena para humanos (Grupo 1) y la carne roja como probablemente cancerígena (Grupo 2A), según PubMed [P-Turesky2018].
- La temperatura de 150 °C es la conversión de "300 °F" del NCI (148,9 °C).

### 2.7 Enlace con la química del aroma

- No se repite aquí. Consulta `bookskills/skills/odorantes-clave/SKILL.md` y `bookskills/odorantes-db`.
- Odorantes de Maillard y Strecker presentes en la base, con nivel de evidencia A–C:
  - 3-metilbutanal y 2-metilbutanal (malta): cacao, café tostado, avellana tostada.
  - Fenilacetaldehído (miel): cacao.
  - Metional: corteza de pan.
  - Furaneol (HDMF, caramelo): café tostado, cacao, corteza de pan, avellana tostada, ajonjolí tostado.
  - 2-etil-3,5-dimetilpirazina y 2,3-dietil-5-metilpirazina (tostado): café tostado, cacao, corteza de pan, avellana tostada.
- Consulta: `python3 scripts/consulta.py <alimento>` dentro de `odorantes-db`.

---

## 3. Caramelización

### 3.1 Qué pasa a nivel molecular

- La caramelización es la degradación térmica de azúcares sin grupos amino.
- Forma compuestos volátiles como ácido acético, furfural, alcohol furfurílico y HMF. Estos marcadores aparecen tanto en caramelización como en Maillard [P-Cake2020].
- Sin aminoácidos no se forman 3-metilbutanal ni 2,5-dimetilpirazina. Esos compuestos necesitan la vía de Strecker [P-Cake2020].
- Inversión de la sacarosa: la sacarosa se hidroliza en glucosa y fructosa. El calor y el ácido la favorecen. Este mecanismo no tiene fuente verificada en esta búsqueda (ver "Datos no confirmados").

### 3.2 Variables que la controlan

- Temperatura y tiempo. En un estudio con xilooligosacáridos calentados de 140 a 190 °C, la energía de activación de la caramelización fue 94,4 kJ/mol, según PubMed [P-XOS2025]. Esta cifra es de un oligosacárido, no de sacarosa.
- Presencia de aminoácidos: si los hay, compite la reacción de Maillard [P-Cake2020].
- Las temperaturas de inicio por tipo de azúcar (fructosa, glucosa, sacarosa) no están confirmadas.

### 3.3 Etapas del almíbar por temperatura (a nivel del mar)

Fuente: Exploratorium [D-Exploratorium]. Es divulgación de un museo de ciencia, no una revisión. Las cifras originales están en °F. La conversión a °C es propia.

| Etapa | Temperatura | Concentración de azúcar |
|---|---|---|
| Hilo | 110–113 °C | 80 % |
| Bola blanda | 113–116 °C | 85 % |
| Bola firme | 118–121 °C | 87 % |
| Bola dura | 121–129 °C | 92 % |
| Quiebre suave | 132–143 °C | 95 % |
| Quiebre duro | 149–154 °C | 99 % |
| Caramelo claro | 160 °C | 100 % |
| Caramelo marrón | 170 °C | 100 % |
| Azúcar quemado | 177 °C | 100 % |

- Corrección por altitud de la fuente: resta 1 °F por cada 500 pies (≈ 0,56 °C por cada 152 m) [D-Exploratorium].
- En Bogotá (≈ 2600 m), la corrección es ≈ 9 °C. Coincide con la diferencia entre 100 °C y el punto de ebullición local (≈ 91 °C, ver 7.6). Regla práctica: resta a cada etapa la diferencia entre 100 °C y el punto de ebullición del agua medido en tu cocina.

### 3.4 Qué produce

- Color de ámbar a marrón. Sabor de dulce a amargo. Textura de jarabe a sólido vítreo, según la concentración final.

### 3.5 Uso en la cocina

- Si quieres una textura precisa, mide la temperatura del almíbar. No cuentes el tiempo.
- Si cocinas en altura, mide el punto de ebullición del agua el mismo día y corrige.

### 3.6 Riesgos

- Forma HMF y furfural [P-Cake2020]. Ver tabla 2.6.
- Quemaduras: el almíbar supera los 150 °C en quiebre duro [D-Exploratorium].

---

## 4. Proteínas

### 4.1 Qué pasa a nivel molecular

- Las proteínas globulares se expanden al calentarse. Las proteínas fibrosas (colágeno) se contraen [P-Tornberg2005].
- Al desnaturalizarse, las proteínas exponen grupos hidrófobos. Después se agregan y forman una red.

### 4.2 Huevo

**Clara**
- La etapa inicial de gelificación de la clara ocurre entre 56 y 72 °C, según PubMed [P-EW2025].
- En esa etapa se forma una red doble compuesta sobre todo por ovomucina, ovotransferrina y lisozima [P-EW2025].
- La ovotransferrina es la proteína de la clara más lábil al calor [P-OT2006].
- La espuma de clara pierde calidad entre 54 y 60 °C [W-TURJAF2019].
- Las temperaturas exactas de desnaturalización de ovotransferrina y ovoalbúmina no están confirmadas (ver "Datos no confirmados").

**Yema**
- La viscosidad de la yema calentada depende del grado de gelificación de sus proteínas. La textura granulosa depende de la agregación de las lipoproteínas de baja densidad (LDL) [P-Yolk2023].
- Por encima de 75 °C, subir la temperatura ya no acelera ciertos procesos de gelificación de la yema [P-Yolk2023].

**Pasteurización de referencia (inactivación de *Salmonella*)**
- Clara líquida: 56,7 °C durante 3,5 min [W-TURJAF2019].
- Yema líquida: 61,1 °C durante 3,5 min [W-TURJAF2019].
- Huevo con cáscara: 57 °C durante 75 min [W-TURJAF2019].

**Uso en la cocina**
- Si quieres una clara tierna, mantén el agua cerca del inicio del rango de gelificación (56–72 °C) y controla el tiempo.
- Si quieres una yema cremosa, no superes 75 °C en el centro de la yema.

### 4.3 Carne: proteínas miofibrilares y sarcoplásmicas

- La mayoría de las proteínas sarcoplásmicas se agrega entre 40 y 60 °C. Algunas coagulan hasta 90 °C [P-Tornberg2005].
- Proteínas miofibrilares en solución: se despliegan a 30–32 °C. Se asocian entre sí a 36–40 °C. Gelifican a 45–50 °C (concentración > 0,5 % en peso) [P-Tornberg2005].
- El agua sale de la red miofibrilar cuando las proteínas se desnaturalizan. Con más temperatura de cocción, la fibra pierde volumen y la carne pierde agua [P-Meat2014].
- La capacidad de retención de agua depende del agua que está fuera de la red miofibrilar [P-Water2011].
- Jugosidad (relación práctica): a mayor temperatura del centro, más desnaturalización, más contracción y menos agua retenida [P-Meat2014].
- Miosina y actina: las temperaturas exactas de desnaturalización de cada una en carne cocida no están confirmadas.

### 4.4 Colágeno a gelatina

- El colágeno se desnaturaliza entre 53 y 63 °C. Después las fibras se encogen [P-Tornberg2005].
- Si las fibras no tienen enlaces cruzados resistentes al calor, el colágeno se disuelve y forma gelatina al seguir calentando [P-Tornberg2005].
- La conversión de colágeno en gelatina es lenta a temperaturas bajas de cocción (cerca de 60 °C), según PubMed [P-PEF2017].
- Los enlaces cruzados maduros (piridinolina) aumentan con la edad del animal y se correlacionan con mayor dureza [P-Collagen2019].
- El colágeno insoluble al calor tiene un grupo "débil" y uno "fuerte". El grupo débil se degrada más fácil por proteólisis y por calor [P-Purslow2014].

**Uso en la cocina**
- Si el corte tiene mucho tejido conectivo (pecho, rabo, morrillo), cocina largo y húmedo por encima del rango de 53–63 °C.
- Si el corte es magro y tierno, limita la temperatura del centro para no perder agua.
- El tiempo exacto para convertir colágeno a cada temperatura no está confirmado.

### 4.5 Pescado

- La estabilidad térmica de la miosina sigue la temperatura de trabajo del músculo del animal. Temperatura media de fusión de la cola de miosina: pez antártico 33 °C, vieira 39 °C, rana 45 °C, conejo 49 °C, según PubMed [P-Myosin1987].
- Consecuencia práctica: la proteína del pescado de agua fría se desnaturaliza a menor temperatura que la de mamífero. El pescado se cocina antes.

### 4.6 Ácidos: ceviche

- El ácido desnaturaliza la proteína del pescado. El ácido NO pasteuriza.
- Jugo de limón en tilapia (30 o 120 min, a 25 o 4 °C): *Vibrio parahaemolyticus* bajó ≈ 5 log. *Salmonella* en el pescado bajó solo 1 a 2 log, según PubMed [P-Ceviche2013].
- Después de preparar un ceviche tradicional, 98,54 % de *Listeria monocytogenes* seguía viable, según PubMed [P-Ceviche2022].
- El marinado tradicional no destruye las larvas de *Anisakis* [P-Anisakis2005, O-EFSA-parasitos2010].
- In vitro, a 5 °C: ácido acético 10 % mató todas las larvas en 2 semanas. Ácido acético 6 % necesitó 8 semanas. Con NaCl 10 % las larvas seguían vivas a las 4 semanas, según PubMed [P-Anisakis2025]. Estas condiciones no corresponden a un ceviche.

**Uso seguro en la cocina**
- Si el pescado es para ceviche, sushi o marinado crudo, congélalo antes. Congelar o calentar son los procesos más eficaces para matar parásitos [O-EFSA-parasitos2010].
- Combinaciones de congelación de una guía oficial (Ontario): −20 °C durante 7 días, o menos de −35 °C durante 15 h [O-Ontario].
- La congelación doméstica no garantiza −20 °C. Verifica tu congelador con termómetro.
- La congelación no elimina bacterias. Usa pescado muy fresco y mantenlo frío.

### 4.7 Sal y salmuera

- El mecanismo de solubilización de miosina por sal no tiene fuente verificada en esta búsqueda (ver "Datos no confirmados").

### 4.8 Enzimas proteolíticas

- La bromelina, la ficina y la papaína se usan como ablandadores de carne [P-Protease2026].
- La actividad de la bromelina se mide en "unidades de digestión de gelatina" (GDU). La bromelina digiere gelatina [P-Bromelain2024].
- Por eso la piña fresca impide que una gelatina cuaje: la bromelina corta las cadenas de gelatina y la red no se forma.
- El punto isoeléctrico de la bromelina de fruta es pH 4,5. El de la bromelina de tallo es pH 9 [P-Bromelain2024].
- Uso: si quieres usar piña en una gelatina, inactiva la enzima con calor antes. La temperatura y el tiempo exactos de inactivación no están confirmados.
- Actinidina (kiwi): no hay fuente verificada en esta búsqueda.

### 4.9 Riesgos de las proteínas

- Huevo y carne poco cocidos: *Salmonella* y otros patógenos. Usa las condiciones de 4.2 o las temperaturas del centro oficiales (7.6).
- Ceviche y pescado crudo: bacterias y *Anisakis* (4.6).

---

## 5. Almidón

### 5.1 Qué pasa a nivel molecular

- Gelatinización: al calentar en agua, los gránulos de almidón absorben agua, se hinchan y pierden su orden cristalino [P-Starch2010].
- Retrogradación: al enfriar, las cadenas de amilosa y amilopectina se reorganizan y recristalizan [P-Rice2023, P-Starch2010].
- La amilosa también forma complejos con lípidos [P-Starch2010].
- Sinéresis: el gel retrogradado expulsa agua.

### 5.2 Variables y rangos

| Almidón | Dato confirmado | Fuente |
|---|---|---|
| Arroz (5 variedades) | Temperatura pico de gelatinización de 56,12 a 79,05 °C según la variedad | [P-Rice2023] |
| Ñame mapuey (*Dioscorea trifida*) | Inicio de gelatinización de 69,1 a 73,4 °C; claridad del gel de 22,4 a 79,2 % | [P-Mapuey2010] |
| Yuca (5 variedades) | Inicio de gelatinización de 65,35 a 69,35 °C | [W-Moorthy] |
| Arrurruz | Inicio 68,5 °C; final 85,0 °C; temperatura de empaste 75–90 °C | [W-Moorthy] |
| Papa | Propiedades de gelatinización, empaste, gelificación y retrogradación distintas de los almidones de cereal y de leguminosa | [P-Potato2020] |

- Los rangos de maíz y papa en °C no están confirmados.

### 5.3 Retrogradación y almidón resistente

- La retrogradación aumenta con más tiempo de almacenamiento y con menor temperatura. En arroz cocido, el grado más alto se dio a −20 °C durante 12 h. El almidón resistente subió en paralelo, según PubMed [P-Rice2023].
- Arroz blanco cocido, enfriado 24 h a 4 °C y recalentado, en 32 pacientes con diabetes tipo 1: menor glucemia máxima (9,9 frente a 11 mmol/L), menor área bajo la curva (135 frente a 336 mmol/L × 180 min) y pico más temprano (35 frente a 45 min), según PubMed [P-RiceT1D2022].
- Riesgo clínico del mismo estudio: con la dosis estándar de insulina hubo más episodios de hipoglucemia con el arroz enfriado (12 frente a 3) [P-RiceT1D2022].
- Pan duro: es retrogradación de la amilopectina [P-Starch2010].

### 5.4 Diferencias entre almidones (estabilidad)

- Después de refrigerar y de congelar-descongelar, los geles de raíces y tubérculos tuvieron menos sinéresis que los de cereales [P-Waxy2010].
- Los geles de almidones cerosos (sin amilosa), excepto el de papa, no mostraron sinéresis tras 5 semanas a 4 °C [P-Waxy2010].
- La yuca cerosa fue el único almidón sin sinéresis tras 5 semanas a −20 °C [P-Waxy2010].
- La comparación de claridad y estabilidad al ácido entre maíz, papa, yuca y arrurruz no está confirmada con cifras.

### 5.5 Uso en la cocina

- Si la salsa va a congelarse, prefiere almidón de raíz o tubérculo (yuca) sobre almidón de cereal [P-Waxy2010].
- Si quieres más almidón resistente, enfría el arroz cocido antes de comerlo [P-Rice2023, P-RiceT1D2022].
- Si quieres un pan blando por más tiempo, evita guardarlo en nevera. La retrogradación aumenta a menor temperatura [P-Rice2023]. Este dato es de arroz; se extrapola al pan.

### 5.6 Riesgos

- Personas con diabetes tratadas con insulina: el arroz enfriado cambia la curva de glucosa. Ajusta con el equipo de salud [P-RiceT1D2022].
- Arroz cocido guardado a temperatura ambiente: riesgo microbiológico. La cifra de *Bacillus cereus* no se buscó en este documento.

---

## 6. Emulsiones y espumas

### 6.1 Qué pasa a nivel molecular

- Una emulsión es una dispersión de gotas de un líquido en otro líquido no miscible.
- Un emulsionante se adsorbe en la interfase aceite-agua y baja la tensión interfacial [P-MFGM2025].
- Mecanismos de inestabilidad: separación gravitacional (cremado o sedimentación), floculación, coalescencia, maduración de Ostwald y oxidación de lípidos [P-Nano2019, P-Nano2017].
- Factores que influyen: fuerza iónica, temperatura, distribución del tamaño de gota, carga de la gota, pH y tratamiento térmico [P-Nano2017].

### 6.2 Principios físicos (forma estándar)

- Ley de Stokes: la velocidad de cremado aumenta con el cuadrado del radio de la gota y con la diferencia de densidad. Disminuye con la viscosidad de la fase continua. Por eso gotas más pequeñas y una fase continua más viscosa dan una emulsión más estable.
- Maduración de Ostwald: las gotas pequeñas se disuelven y las grandes crecen. Ocurre cuando la fase dispersa es algo soluble en la fase continua [P-Nano2019].
- Coalescencia: dos gotas se unen en una sola al romperse la película interfacial.
- Nota: estas formulaciones son física estándar. Los resúmenes leídos nombran los mecanismos pero no dan la ecuación.

### 6.3 Espumas de crema

- La crema batida se estabiliza por coalescencia parcial de los glóbulos de grasa [P-Cream2026a, P-Cream2026b].
- Si se reduce la grasa, la coalescencia parcial es insuficiente y la espuma pierde estabilidad. Una crema de 20 % de grasa necesitó estabilizantes tipo Pickering para llegar a ≈ 90 % del rendimiento de batido de un producto comercial, según PubMed [P-Cream2026a].
- Definiciones legales en EE. UU.: "light whipping cream" = 30 % a menos de 36 % de grasa láctea. "Heavy cream" = 36 % o más [O-CFR131.157, O-CFR131.150].
- El porcentaje mínimo de grasa que garantiza el batido no está confirmado como cifra científica. Usa ≥ 30 % como criterio práctico con base en la definición legal.

### 6.4 Espumas de proteína

- La clara forma espuma por sus proteínas. La espuma de clara entera es mejor que la de cada proteína aislada [P-EWfoam2017].
- El calentamiento entre 54 y 60 °C afecta la espuma de clara [W-TURJAF2019].

### 6.5 Uso en la cocina

- Si quieres una emulsión estable, reduce el tamaño de gota (más energía al batir) y aumenta la viscosidad de la fase acuosa.
- Si quieres crema batida firme, usa crema con ≥ 30 % de grasa y mantenla fría. La temperatura óptima no está confirmada.
- Si una salsa emulsionada se corta, añade fase continua y emulsionante (por ejemplo yema) y bate de nuevo.

### 6.6 Riesgos

- Emulsiones con yema cruda (mayonesa casera): riesgo de *Salmonella*. Usa huevo pasteurizado (ver 4.2).
- La causa de que "el aceite frío corta la mayonesa" no está confirmada (ver "Datos no confirmados").

---

## 7. Agua y transferencia de calor

### 7.1 Actividad de agua (aw)

- Definición: aw es la presión de vapor del alimento dividida por la presión de vapor del agua pura en las mismas condiciones [O-FDA-aw].
- La mayoría de los alimentos frescos tiene aw > 0,95. Ese nivel permite crecer a bacterias, levaduras y mohos [O-FDA-aw].
- *Clostridium botulinum* necesita aw ≥ ≈ 0,93 para crecer (hasta 0,96 según el producto) [O-FDA-aw].
- aw 0,85: límite regulatorio en EE. UU. para excluir alimentos de las normas de enlatados de baja acidez y acidificados. No es un límite universal de crecimiento [O-FDA-aw].
- Algunos mohos y levaduras xerófilos crecen a aw 0,61. Es el valor más bajo registrado, según PubMed [P-Grant2004].
- La baja aw limita el crecimiento, pero los patógenos pueden sobrevivir mucho tiempo en ingredientes secos [P-Dry2026].

### 7.2 Ósmosis: salado y curado

- La sal y el azúcar bajan la aw. Los ambientes de alta sal permiten solo microorganismos muy tolerantes (aw de NaCl saturado = 0,75) [P-Grant2004].
- Riesgo del curado con nitrito: formación de compuestos N-nitroso [P-Turesky2018].

### 7.3 Calor específico

- El agua tiene un calor específico alto. Por eso los alimentos húmedos se calientan despacio. La cifra no está confirmada en esta búsqueda.

### 7.4 Conducción y convección

- Conducción: el calor pasa de molécula a molécula dentro del sólido. Es el modo dominante dentro de un trozo de carne.
- Convección: el calor viaja con el movimiento del fluido (aire, agua, aceite).
- En un bizcocho modelo, el nivel de convección del horno no cambió la velocidad de las reacciones químicas [P-Cake2024].
- Nota: las definiciones de conducción y convección son física estándar.

### 7.5 Evaporación y estancamiento térmico ("the stall")

- Mecanismo propuesto: el agua que se evapora en la superficie absorbe calor. La temperatura del centro deja de subir durante horas, aunque el horno siga caliente.
- Fuente: experimento de G. Blonder con esponjas y lomo de cerdo [D-Blonder2011]. No es una fuente revisada por pares.
- Uso: si quieres acortar el estancamiento, reduce la evaporación (envolver en papel aluminio). La fuente indica que envolver retiene humedad pero cambia el sabor de la corteza [D-Blonder2011].

### 7.6 Punto de ebullición y altitud

**Dato**
- A nivel del mar el agua hierve a 100 °C. Cada 500 pies (152 m) de altitud, el punto de ebullición baja algo menos de 1 °F (0,56 °C) [O-USDA-altitud].
- USDA: 2000 pies (610 m) → 208 °F (97,8 °C). 7500 pies (2286 m) → ≈ 198 °F (≈ 92,2 °C) [O-USDA-altitud].
- **Bogotá (≈ 2600 m): ≈ 91 °C.** Cálculo propio con presión de atmósfera estándar (737 hPa) y la ecuación de Antoine para agua. El mismo método reproduce los dos puntos de USDA (97,97 °C y 92,39 °C). La presión real cambia con el clima. Rango esperado: 91 a 92 °C.
- Verificación práctica: mide con termómetro el agua en ebullición en tu cocina.

**Efecto en la cocción**
- Si el agua hierve a menor temperatura, los alimentos hervidos o en fuego lento se cocinan más despacio y necesitan más tiempo [O-USDA-altitud].
- Subir el fuego no acelera la cocción. Solo evapora el agua más rápido [O-USDA-altitud].
- La carne en calor húmedo puede necesitar hasta 25 % más de tiempo a 5000 pies (1524 m) [O-USDA-altitud].
- El horno no cambia con la altitud. El asado en horno sigue las guías de nivel del mar [O-USDA-altitud].
- Huevos, pasta y legumbres: necesitan más tiempo en Bogotá. Los minutos exactos no están confirmados.

**Efecto en la inocuidad**
- Las temperaturas mínimas del centro no cambian con la altitud. Ejemplos USDA: 145 °F (63 °C) para cortes enteros de res, cerdo, cordero y ternera; 160 °F (71 °C) para carne molida; 165 °F (74 °C) para aves [O-USDA-altitud].
- En olla lenta, USDA recomienda mantener la comida a 200 °F (93 °C) o más. En Bogotá el agua hierve por debajo de esa cifra. Verifica la temperatura del centro con termómetro [O-USDA-altitud].
- Agua a 91 °C supera las condiciones de pasteurización del huevo (56,7–61,1 °C, ver 4.2). Hervir sigue pasteurizando.
- Hervir NO esteriliza conservas de baja acidez. Las conservas de baja acidez (carnes, aves) necesitan olla a presión a cualquier altitud. Para llegar a 240 °F (116 °C) con manómetro de dial: 11 lb hasta 2000 pies, 12 lb de 2001 a 4000 pies, 13 lb de 4001 a 6000 pies. Con pesa, usa 15 lb por encima de 1000 pies [O-USDA-altitud].
- La presión para Bogotá (≈ 8530 pies) no aparece en la fuente. Consulta una tabla oficial de conservas por altitud.

---

## 8. pH y color

### 8.1 Antocianinas (repollo morado)

- Las antocianinas cambian de color con el pH. Su estabilidad depende de la luz, la temperatura, la humedad y el oxígeno [P-Indicator2024].
- Una película con antocianina de repollo morado pasó de morado a azul cuando el calamar se descompuso (aumento de bases volátiles) [P-Squid2026].
- Uso: el jugo de repollo morado sirve como indicador casero de pH. Ácido → hacia rojo. Básico → hacia azul y verde. Los colores por cada valor de pH no están confirmados.
- Riesgo: ninguno relevante a dosis culinarias.

### 8.2 Clorofila

- El ácido y el calor desplazan el magnesio de la clorofila (desmagnesiación). Se forman feofitinas y pirofeofitina a. El color pasa de verde a amarillo-marrón (oliva) [P-Chloro2025].
- Los ácidos orgánicos propios de la verdura (oxálico, cítrico, málico, fumárico) favorecen esta pérdida de color [P-Chloro2025].
- La precocción y el almacenamiento congelado aceleraron la formación de feofitinas en pak choi. El verde (valor −a) bajó de 34,5 a 49,8 % frente a los controles [P-Chloro2025].
- Uso: cocina las verduras verdes poco tiempo. No las tapes durante la cocción para dejar salir los ácidos volátiles. Añade el ácido (limón, vinagre) al servir.
- El efecto del bicarbonato sobre la clorofila no está confirmado (ver "Datos no confirmados").

### 8.3 Oscurecimiento enzimático

- La polifenoloxidasa (PPO) es la enzima clave del oscurecimiento de frutas y verduras cortadas [P-PPO2023].
- Métodos que reducen la actividad de PPO: tratamiento térmico (blanqueado), baja temperatura, inhibidores químicos e inhibidores naturales [P-PPO2024, P-PPO2023].
- Algunos productos de Maillard inhiben el oscurecimiento enzimático porque quelan metales [P-MRPantiox2018].
- Uso: aguacate, papa y manzana cortados. Enfría, limita el oxígeno (película en contacto), o blanquea si el plato admite cocción.
- El mecanismo y la dosis de ácido ascórbico o de jugo de limón no están confirmados.

---

## 9. Fermentación y enzimas (principios)

### 9.1 Qué pasa

- Bacterias ácido lácticas, levaduras y hongos filamentosos tienen papeles complementarios: acidifican, hidrolizan proteínas, producen aroma, cambian la textura y degradan fitatos [P-Ferm2026].
- El resultado depende del sustrato, de la cepa y del proceso [P-Ferm2026].
- Las bacterias ácido lácticas y sus bacteriocinas inhiben *Listeria monocytogenes* en algunos alimentos [P-LAB2026].

### 9.2 Koji y glutamato

- *Aspergillus oryzae* es el hongo del koji. Secreta enzimas en abundancia y es central en la fermentación de la salsa de soya [P-Koji2026].
- Un koji con más actividad de enzimas de carbohidratos produjo más ácido glutámico, dipéptidos y γ-glutamil-péptidos. Estos se asocian a umami y kokumi [P-Koji2026].
- Las fosfatasas ácidas del koji degradan los nucleótidos (IMP). Por eso el miso se trata con calor antes de añadir nucleótidos [P-Miso2013].

### 9.3 Umami y sinergia

- Las sustancias umami son glutamato, 5'-inosinato y 5'-guanilato [P-Kurihara2015].
- Hay sinergia entre glutamato y 5'-nucleótidos. Solo el receptor T1R1 + T1R3 muestra esa sinergia [P-Kurihara2015].
- En humanos, la respuesta a la mezcla glutamato + 5'-inosinato es ≈ 8 veces mayor que la respuesta a glutamato solo. En ratas es ≈ 1,7 veces, según PubMed [P-Kurihara2015].
- Uso: combina una fuente de glutamato (tomate maduro, queso curado, salsa de soya, alga kombu) con una fuente de inosinato (carne, pescado seco) o de guanilato (hongos secos). El contenido de glutamato y nucleótidos de cada alimento no se buscó en este documento.

### 9.4 Riesgos

- Las aminas biógenas (sobre todo histamina) pueden llegar a concentraciones dañinas en fermentados vegetales, en especial con fermentación espontánea (chucrut, kimchi, salsa de soya, miso, tempeh, encurtidos) [P-BA2026].
- El pH objetivo para una fermentación láctica segura no está confirmado en esta búsqueda.

---

## 10. Tabla resumen

| Fenómeno | Variable clave | Rango | Resultado | Riesgo |
|---|---|---|---|---|
| Maillard | Temperatura, pH, aw, tiempo | Acrilamida > 120 °C con baja humedad; fritura < 175 °C (UE) | Color pardo, aromas tostados (pirazinas, aldehídos de Strecker) | Acrilamida, furano, HMF, CML |
| Acrilamida (control) | Remojo y color final | Remojo 15–30 min (FDA) o 30 min–2 h (UE); papa almacenada > 6 °C | Menos asparagina y azúcar reductor en superficie | BMDL10 0,17 mg/kg pc/día (animal) |
| Carne a alta temperatura | Temperatura y tiempo | Más HCA > 150 °C | Costra | HCA, PAH (goteo y humo) |
| Caramelización / almíbar | Temperatura (≈ concentración) | Hilo 110 °C a caramelo 160–177 °C (nivel del mar) | Textura de jarabe a vidrio; color ámbar | HMF, furfural; quemaduras |
| Clara de huevo | Temperatura | Gelificación inicial 56–72 °C | Gel blanco | *Salmonella* si se cocina poco |
| Yema de huevo | Temperatura | Cambio de dinámica > 75 °C | De cremosa a granulosa | *Salmonella* si se cocina poco |
| Proteínas miofibrilares | Temperatura del centro | Despliegue 30–32 °C; gel 45–50 °C | Firmeza; pérdida de agua | Patógenos si poco cocida |
| Colágeno | Temperatura y tiempo | Desnaturaliza 53–63 °C; lento cerca de 60 °C | Gelatina; carne tierna | — |
| Miosina de pescado | Especie (temperatura de hábitat) | Tm 33 °C (pez antártico) frente a 49 °C (conejo) | Cocción más rápida | — |
| Ceviche | pH ácido, tiempo | 30–120 min con limón | Proteína opaca y firme | *Salmonella* (−1 a 2 log), *Listeria* (≈ 98 % viable), *Anisakis* |
| Parásitos del pescado | Congelación | −20 °C 7 días o < −35 °C 15 h | Larvas muertas | Congelador doméstico insuficiente |
| Bromelina | Enzima activa | Fruta fresca sin calentar | Gelatina no cuaja; carne más blanda | Textura pastosa |
| Gelatinización del almidón | Temperatura, agua | Inicio 65–73 °C (yuca, mapuey); pico 56–79 °C (arroz) | Espesa | — |
| Retrogradación | Frío y tiempo | Máxima a −20 °C 12 h (arroz) | Almidón resistente; pan duro | Hipoglucemia con insulina estándar |
| Sinéresis | Tipo de almidón | Raíz/tubérculo < cereal | Gel estable al congelar | — |
| Emulsión | Tamaño de gota, viscosidad | Stokes: v ∝ r² | Salsa estable | *Salmonella* con yema cruda |
| Crema batida | % de grasa | ≥ 30 % (definición legal EE. UU.) | Espuma por coalescencia parcial | — |
| Actividad de agua | aw | *C. botulinum* ≥ ≈ 0,93; xerófilos hasta 0,61 | Conservación | Supervivencia de patógenos en secos |
| Altitud | Presión | Bogotá ≈ 91 °C de ebullición | Cocción en agua más lenta | Conservas de baja acidez sin presión |
| Clorofila | Ácido + calor | — | Verde a oliva (feofitinas) | — |
| Antocianinas | pH | — | Rojo (ácido) a azul (básico) | — |
| Oscurecimiento enzimático | PPO + oxígeno | — | Pardo en corte | — |
| Umami | Glutamato + nucleótido | ≈ 8× en humanos | Sabor umami intenso | — |
| Fermentación | Microorganismo, sustrato | — | Ácido, aroma, umami | Aminas biógenas (histamina) |

---

## 11. Referencias

### PubMed (según PubMed; DOI enlazado)

- [P-This2009] This H. Molecular gastronomy, a scientific look at cooking. *Acc Chem Res*. 2009;42(5):575-83. [R] https://doi.org/10.1021/ar8002078
- [P-This2005] This H. Modelling dishes and exploring culinary 'precisions': the two issues of molecular gastronomy. *Br J Nutr*. 2005;93 Suppl 1:S139-46. [R] https://doi.org/10.1079/bjn20041352
- [P-This2002] This H. Molecular gastronomy. *Angew Chem Int Ed*. 2002;41(1):83-8. [R] (resumen no disponible; solo metadatos) https://doi.org/10.1002/1521-3773(20020104)41:1<83::aid-anie83>3.0.co;2-f
- [P-Stadler2002] Stadler RH et al. Acrylamide from Maillard reaction products. *Nature*. 2002;419:449-50. [E] https://doi.org/10.1038/419449a
- [P-AAreview2007] Zhang Y, Zhang Y. Formation and reduction of acrylamide in Maillard reaction: a review. *Crit Rev Food Sci Nutr*. 2007;47(5):521-42. [R] https://doi.org/10.1080/10408390600920070
- [P-AA2013] Current issues in dietary acrylamide: formation, mitigation and risk assessment. *J Sci Food Agric*. 2013. [R] https://doi.org/10.1002/jsfa.6349
- [P-Maillard2025] Maillard Reaction: Mechanism, Influencing Parameters, Advantages, Disadvantages, and Food Industrial Applications: A Review. *Foods*. 2025;14(11):1881. [R] https://doi.org/10.3390/foods14111881
- [P-Maillard2024] The Maillard reactions: Pathways, consequences, and control. *Vitam Horm*. 2024. [R] https://doi.org/10.1016/bs.vh.2024.04.002
- [P-MRPantiox2018] The Maillard reaction products as food-born antioxidant and antibrowning agents in model and real food systems. *Food Chem*. 2018. [R] https://doi.org/10.1016/j.foodchem.2018.09.083
- [P-Cake2020] Potential of model cakes to study reaction kinetics through the dynamic on-line extraction of volatile markers and TD-GC-MS analysis. *Food Res Int*. 2020. [E] https://doi.org/10.1016/j.foodres.2020.109087
- [P-Cake2024] Unravelling caramelization and Maillard reactions in glucose and glucose + leucine model cakes. *Food Res Int*. 2024. [E] https://doi.org/10.1016/j.foodres.2024.114183
- [P-Furan2017] Kinetic study of furan and furfural generation during baking of cake models. *Food Chem*. 2017. [E] https://doi.org/10.1016/j.foodchem.2017.06.126
- [P-XOS2025] Hygroscopic stability of xylooligosaccharides and application on the corn flakes. *Food Chem X*. 2025. [E] https://doi.org/10.1016/j.fochx.2025.102504
- [P-Turesky2018] Turesky RJ. Mechanistic evidence for red meat and processed meat intake and cancer risk. *Chimia*. 2018;72(10):718-724. [R] https://doi.org/10.2533/chimia.2018.718
- [P-Tornberg2005] Tornberg E. Effects of heat on meat proteins. *Meat Sci*. 2005. [R] https://doi.org/10.1016/j.meatsci.2004.11.021
- [P-PEF2017] Understanding the effect of pulsed electric fields on thermostability of connective tissue isolated from beef pectoralis muscle. *Food Res Int*. 2017. [E] https://doi.org/10.1016/j.foodres.2017.08.025
- [P-Collagen2019] Production factors affecting the contribution of collagen to beef toughness. *J Anim Sci*. 2019. [R] https://doi.org/10.1093/jas/skz097
- [P-Purslow2014] New developments on the role of intramuscular connective tissue in meat toughness. *Annu Rev Food Sci Technol*. 2014. [R] https://doi.org/10.1146/annurev-food-030212-182628
- [P-Meat2014] A structural approach to understanding the interactions between colour, water-holding capacity and tenderness. *Meat Sci*. 2014. [R] https://doi.org/10.1016/j.meatsci.2014.05.022
- [P-Water2011] Water distribution and mobility in meat during the conversion of muscle to meat and ageing. *Meat Sci*. 2011. [R] https://doi.org/10.1016/j.meatsci.2011.04.007
- [P-Myosin1987] Thermal stability of myosin rod from various species. *Biochemistry*. 1987. [E] https://doi.org/10.1021/bi00400a032
- [P-EW2025] Enhanced thermal stability of liquid egg white via disrupting the double-network structure at the initial stage of gelation. *Food Res Int*. 2025. [E] https://doi.org/10.1016/j.foodres.2025.117033
- [P-OT2006] Preventive effect of egg yolk phosvitin on heat-insolubilization of egg white protein. *Biosci Biotechnol Biochem*. 2006. [E] https://doi.org/10.1271/bbb.70.836
- [P-Yolk2023] Exploring non-equilibrium processes and spatio-temporal scaling laws in heated egg yolk using coherent X-rays. *Nat Commun*. 2023. [E] https://doi.org/10.1038/s41467-023-41202-z
- [P-EWfoam2017] Effect of a multiple freeze-thaw process on structural and foaming properties of individual egg white proteins. *Food Chem*. 2017. [E] https://doi.org/10.1016/j.foodchem.2017.02.005
- [P-Ceviche2013] Effect of lime juice on *Vibrio parahaemolyticus* and *Salmonella enterica* inactivation during the preparation of ceviche. *J Food Prot*. 2013. [E] https://doi.org/10.4315/0362-028X.JFP-12-526
- [P-Ceviche2022] Ceviche—natural preservative: possibility of microbiota survival. *Foods*. 2022. [E] https://doi.org/10.3390/foods11060860
- [P-Anisakis2005] A new procedure for marinating fresh anchovies and ensuring the rapid destruction of *Anisakis* larvae. *J Food Prot*. 2005. [E] https://doi.org/10.4315/0362-028x-68.5.1066
- [P-Anisakis2025] Survival of *Anisakis simplex* L3 exposed to different combinations of acetic acid and sodium chloride. *Food Waterborne Parasitol*. 2025. [E] https://doi.org/10.1016/j.fawpar.2025.e00293
- [P-Bromelain2024] Enhancing bromelain recovery from pineapple by-products. *Foods*. 2024. [E] https://doi.org/10.3390/foods13040589
- [P-Protease2026] Comparative mass spectrometric analysis of proteolytic activity in wine and wine vinegars. *J Mass Spectrom*. 2026. [E] https://doi.org/10.1002/jms.70003
- [P-Starch2010] Fate of starch in food processing: from raw materials to final food products. *Annu Rev Food Sci Technol*. 2010. [R] https://doi.org/10.1146/annurev.food.102308.124211
- [P-Potato2020] What makes starch from potato tubers unique: a review. *Compr Rev Food Sci Food Saf*. 2020. [R] https://doi.org/10.1111/1541-4337.12596
- [P-Cassava2025] Physicochemical characterization and properties of cassava starch: a review. *Polymers*. 2025. [R] (solo resumen; sin cifras) https://doi.org/10.3390/polym17121663
- [P-Mapuey2010] Physicochemical, functional, and macromolecular properties of waxy yam starches from "Mapuey" (*Dioscorea trifida*). *J Agric Food Chem*. 2010. [E] https://doi.org/10.1021/jf100418r
- [P-Waxy2010] Sánchez T et al. (CIAT, Cali). Comparison of pasting and gel stabilities of waxy and normal starches from potato, maize, and rice with those of a novel waxy cassava starch. *J Agric Food Chem*. 2010. [E] https://doi.org/10.1021/jf1001606
- [P-Rice2023] Effect of storage time and temperature on digestibility, thermal, and rheological properties of retrograded rice. *Gels*. 2023. [E] https://doi.org/10.3390/gels9020142
- [P-RiceT1D2022] Influence of resistant starch resulting from the cooling of rice on postprandial glycemia in type 1 diabetes. *Nutr Diabetes*. 2022. [E] https://doi.org/10.1038/s41387-022-00196-1
- [P-Nano2019] Food-grade nanoemulsions: preparation, stability and application. *Molecules*. 2019. [R] https://doi.org/10.3390/molecules24234242
- [P-Nano2017] Challenges associated in stability of food grade nanoemulsions. *Crit Rev Food Sci Nutr*. 2017. [R] https://doi.org/10.1080/10408398.2015.1006767
- [P-MFGM2025] Effect of phospholipid-protein interfacial interactions on aeration emulsion quality. *Food Chem X*. 2025. [E] https://doi.org/10.1016/j.fochx.2025.102547
- [P-Cream2026a] Enzymatically hydrolyzed egg yolk peptide-quercetin complexes as Pickering stabilizers for reduced-fat whipping cream. *Food Res Int*. 2026. [E] https://doi.org/10.1016/j.foodres.2026.120521
- [P-Cream2026b] Whipped cream regulation by hydrophilic sucrose esters. *Foods*. 2026. [E] https://doi.org/10.3390/foods15172995
- [P-Grant2004] Grant WD. Life at low water activity. *Philos Trans R Soc Lond B*. 2004. [R] https://doi.org/10.1098/rstb.2004.1502
- [P-Dry2026] A risk-based framework for ranking microbiological hazards for dried fruits, vegetables, herbs, and spices. *Compr Rev Food Sci Food Saf*. 2026. [R] https://doi.org/10.1111/1541-4337.70567
- [P-Indicator2024] A review on improving the sensitivity and color stability of naturally sourced pH-sensitive indicator films. *Compr Rev Food Sci Food Saf*. 2024. [R] https://doi.org/10.1111/1541-4337.13390
- [P-Squid2026] Deep learning-assisted digital interpretation of an anthocyanin-based colorimetric pH indicator for packaged raw squid. *Food Sci Biotechnol*. 2026. [E] https://doi.org/10.1007/s10068-026-02287-6
- [P-Chloro2025] Insight into the impact of pre-cooking and freezing on the colour stability of pakchoi during thermal processing. *Food Chem*. 2025. [E] https://doi.org/10.1016/j.foodchem.2025.144065
- [P-PPO2023] Enzymatic browning and polyphenol oxidase control strategies. *Curr Opin Biotechnol*. 2023. [R] https://doi.org/10.1016/j.copbio.2023.102921
- [P-PPO2024] Inhibition of polyphenol oxidase for preventing browning in edible mushrooms: a review. *J Food Sci*. 2024. [R] https://doi.org/10.1111/1750-3841.17322
- [P-Ferm2026] Fermented plant-based foods: insights and emerging trends. *Food Res Int*. 2026. [R] https://doi.org/10.1016/j.foodres.2026.120536
- [P-BA2026] Occurrence and control of biogenic amines in plant-based fermented foods. *Crit Rev Food Sci Nutr*. 2026. [R] https://doi.org/10.1080/10408398.2026.2714471
- [P-LAB2026] Lactic acid bacteria and their bacteriocins: promising food safety tools for controlling *Listeria monocytogenes*. *World J Microbiol Biotechnol*. 2026. [R] https://doi.org/10.1007/s11274-026-05074-x
- [P-Koji2026] Synergistic effects of co-culturing two *Aspergillus oryzae* strains on soy sauce flavor enhancement. *Food Chem*. 2026. [E] https://doi.org/10.1016/j.foodchem.2026.148017
- [P-Miso2013] Reduction of the degradation activity of umami-enhancing purinic ribonucleotide supplement in miso. *Int J Food Microbiol*. 2013. [E] https://doi.org/10.1016/j.ijfoodmicro.2013.07.006
- [P-Kurihara2015] Kurihara K. Umami the fifth basic taste: history of studies on receptor mechanisms and role as a food flavor. *Biomed Res Int*. 2015. [R] https://doi.org/10.1155/2015/189402
- [P-Kurihara2000] Kurihara K, Kashiwayanagi M. Physiological studies on umami taste. *J Nutr*. 2000. [R] https://doi.org/10.1093/jn/130.4.931S

### Revistas revisadas por pares leídas en la web (no PubMed)

- [W-This2013] This H. Molecular gastronomy is a scientific discipline, and note by note cuisine is the next culinary trend. *Flavour*. 2013;2:1. [R] https://doi.org/10.1186/2044-7248-2-1
- [W-TURJAF2019] Kavuşan HS, Serdaroğlu M. The role of novel pasteurization approaches on altering functional properties of egg proteins. *Turk J Agric Food Sci Technol*. 2019;7(sp1):138-144. [R] https://doi.org/10.24925/turjaf.v7isp1.138-144.2787
- [W-Moorthy] Moorthy SN. Physicochemical and functional properties of tropical tuber starches: a review. Copia en el sitio del autor (moorthy.co.in). [R] La revista y el año no se verificaron en la página leída. https://moorthy.co.in/physicochemical-and-functional-properties-of-tropical-tuber-starches-a-review.html/11.html

### Organismos oficiales y normas

- [O-EFSA2015] EFSA CONTAM Panel. Scientific Opinion on acrylamide in food. *EFSA Journal*. 2015;13(6):4104. https://doi.org/10.2903/j.efsa.2015.4104 (leído vía DOAJ)
- [O-EFSA-furano2017] EFSA. Furan in food – EFSA confirms health concerns (nota de prensa, 2017-10-25). Opinión: https://doi.org/10.2903/j.efsa.2017.5005 . Página: https://www.efsa.europa.eu/en/press/news/171025
- [O-EFSA-parasitos2010] EFSA BIOHAZ Panel. Scientific Opinion on risk assessment of parasites in fishery products. *EFSA Journal*. 2010. https://doi.org/10.2903/j.efsa.2010.1543 (resumen leído vía DOAJ)
- [O-FDA-AA] FDA. Acrylamide and diet, food storage, and food preparation. https://www.fda.gov/food/process-contaminants-food/acrylamide-and-diet-food-storage-and-food-preparation
- [O-UE2017/2158] Reglamento (UE) 2017/2158, Anexo II, parte A (versión consolidada en legislation.gov.uk). https://legislation.gov.uk/eur/2017/2158/annex/II/part/A
- [O-NCI] National Cancer Institute. Chemicals in meat cooked at high temperatures and cancer risk. https://www.cancer.gov/about-cancer/causes-prevention/risk/diet/cooked-meats-fact-sheet
- [O-FDA-aw] FDA. Water activity (aw) in foods — Inspection Technical Guide. https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/inspection-technical-guides/water-activity-aw-foods
- [O-USDA-altitud] USDA FSIS. High altitude cooking. https://www.fsis.usda.gov/food-safety/safe-food-handling-and-preparation/food-safety-basics/high-altitude-cooking
- [O-Ontario] Gobierno de Ontario. Fish plant guidelines F.B.14.17 Parasite control. https://ontario.ca/document/fish-plant-guidelines/fb1417-parasite-control
- [O-CFR131.157] 21 CFR 131.157 Light whipping cream. https://www.law.cornell.edu/cfr/text/21/131.157
- [O-CFR131.150] 21 CFR 131.150 Heavy cream. https://www.law.cornell.edu/cfr/text/21/131.150

### Divulgación (no revisada por pares)

- [D-Exploratorium] Exploratorium. Sugar stages (The Accidental Scientist: Science of Cooking). https://annex.exploratorium.edu/cooking/candy/sugar-stages.html
- [D-Blonder2011] Blonder G. Experimento sobre el estancamiento térmico (2011). Sitio personal. https://www.genuineideas.com/ArticlesIndex/spray.html

### Archivos locales enlazados

- `/home/claude/bookskills/skills/odorantes-clave/SKILL.md`
- `/home/claude/bookskills/odorantes-db/datos/odorantes.csv` (consultado con grep para Maillard y Strecker)

---

## 12. Log de búsqueda (2026-11-10)

| # | Herramienta | Consulta o URL | Resultado |
|---|---|---|---|
| 1 | Bash | Listar `bookskills`, `odorantes-db`, `skills/odorantes-clave` | Existen. Se leyó SKILL.md y README. |
| 2 | Bash | grep de pirazinas, furaneol, metional, metilbutanal, fenilacetaldehído en `odorantes.csv` | Odorantes de Maillard en 5 alimentos (sección 2.7). |
| 3 | PubMed | `This H[Author] AND molecular gastronomy` | 32 resultados; 15 leídos. Varios "challenges" sin resumen. |
| 4 | PubMed | `This H[Author] AND (note by note OR "molecular gastronomy" AND review[pt])` | 3: Br J Nutr 2005, Angew Chem 2002. |
| 5 | PubMed | `This H[Author] AND (Kurti OR "food for tomorrow" OR ...)` | 0. |
| 6 | PubMed | `acrylamide formation asparagine Maillard reaction[Title]` | 21; Stadler 2002, Zhang 2007. |
| 7 | PubMed | `umami synergism glutamate inosinate guanylate review` | 2: Kurihara 2015 y 2000. |
| 8 | PubMed | `heterocyclic amines polycyclic aromatic hydrocarbons meat cooking temperature review` | 17; Turesky 2018. |
| 9 | PubMed | `Anisakis marinated fish survival vinegar salt` | 2. |
| 10 | PubMed | `egg white proteins denaturation temperature ovotransferrin ovalbumin DSC` | 4; sin temperaturas útiles. |
| 11 | PubMed | colágeno, almidón (yuca/papa/maíz), arroz enfriado, antocianinas, clorofila, PPO | Varias con 0–4 resultados; se acortaron las consultas. |
| 12 | PubMed | `intramuscular collagen heat solubility meat cooking review[pt]`; `myofibrillar ... review[pt]`; `starch gelatinization retrogradation review[pt]` | Purslow 2014, Meat Sci 2011/2014, Annu Rev 2010, papa 2020. |
| 13 | WebSearch | EFSA acrylamide 2015; Reglamento 2017/2158; FDA acrylamide; This/Kurti note by note | Enlaces oficiales y *Flavour* 2013. |
| 14 | WebFetch | pmc.ncbi.nlm.nih.gov/articles/PMC1679779 | **Bloqueado** (CAPTCHA). |
| 15 | WebFetch | *Flavour* 2013 (BMC PDF) | Leído. |
| 16 | WebFetch | FDA acrylamide and diet | Leído. |
| 17 | WebFetch | legislation.gov.uk Reg. 2017/2158 Anexo II A | Leído. |
| 18 | WebFetch | DOAJ EFSA 2015 acrilamida | Leído. |
| 19 | WebFetch | legislation.gov.uk Anexo IV | **Bloqueado** (fuera de la lista permitida). |
| 20 | WebSearch | Punto de ebullición Bogotá 2600 m | Solo calculadoras y blogs; no se usaron. |
| 21 | WebSearch + WebFetch | Etapas del almíbar → Exploratorium | Leído. |
| 22 | WebSearch + WebFetch | USDA FSIS high altitude cooking | Leído. |
| 23 | WebSearch | Caramelización por azúcar (fructosa 110, glucosa 160, sacarosa 160) | Solo blogs y Wikipedia; no se usaron. |
| 24 | WebSearch | Crema batida % de grasa | Sin fuente revisada con cifra mínima. |
| 25 | PubMed | `caramelization sugars temperature kinetics`; `whipping cream fat content ...`; `Maillard reaction pH effect browning flavor review[pt]` | 17 artículos leídos (archivo guardado, procesado con Python). |
| 26 | WebFetch | mdpi.com Foods 14(11):1881 (texto completo) | **Bloqueado** (fuera de la lista permitida). Se usó solo el resumen de PubMed. |
| 27 | PubMed | Tornberg; ceviche; bromelina; huevo; emulsiones; koji; miosina de pescado; sal y miofibrilares | Tornberg 2005, 2 de ceviche, Myosin 1987, 2 de nanoemulsiones; sal = 0. |
| 28 | PubMed | huevo (gel, ovotransferrina), yema LDL, yuca revisión, repollo morado, aw | 19 + 8 artículos leídos. |
| 29 | WebFetch | NCI cooked meats | Leído. |
| 30 | WebFetch | FDA water activity guide | Leído. |
| 31 | WebFetch | food.gov.uk → gov.uk (congelación de pescado) | Redirección; gov.uk **bloqueado** (fuera de la lista permitida). |
| 32 | WebFetch | EFSA furano 2017 (nota de prensa) | Leído. |
| 33 | PubMed | `This "scientific look at cooking"` → PMID 19449900 | Acc Chem Res 2009 leído. |
| 34 | PubMed | koji/miso; fermentación láctica; almidones congelación-descongelación | 8 leídos (incluye CIAT 2010). |
| 35 | WebFetch | Europe PMC texto completo de la revisión de yuca | **Bloqueado** (fuera de la lista permitida). |
| 36 | WebFetch | eCFR 131.157 y 131.150 (Cornell LII) | Leídos. |
| 37 | WebFetch | Blonder 2011 (stall) | Leído; no revisado por pares. |
| 38 | Bash | Cálculo de ebullición con atmósfera estándar + Antoine | Bogotá 2600 m: 737,5 hPa → 91,34 °C. Validado con USDA (2000 pies: 97,97 °C; 7500 pies: 92,39 °C). |
| 39 | WebFetch | webbook.nist.gov (constantes de Antoine) | **Bloqueado** (fuera de la lista permitida). Constantes usadas: A 5,08354; B 1663,125; C −45,622 (agua, 344–373 K, bar). |
| 40 | WebFetch | Revisión de Moorthy (tubérculos tropicales) | Leído; cita de revista incompleta. |
| 41 | WebFetch | TURJAF 2019 (huevo) | Leído; sin temperaturas de desnaturalización por proteína. |
| 42 | PubMed | `ovalbumin thermal denaturation temperature 84`; almidones DSC comparación | 0 y 0. |
| 43 | WebFetch | Guía de Ontario (parásitos) | Leído. |
| 44 | WebFetch | DOAJ EFSA parásitos 2010 | Leído (resumen). |

Nota: no se usó curl para rodear ningún bloqueo.

---

## 13. Datos no confirmados

Estos datos se pidieron o se mencionan en la práctica culinaria. No tienen fuente verificada en esta búsqueda. No se dan cifras.

1. Umbral de temperatura de superficie para una reacción de Maillard rápida (se cita con frecuencia "≈ 140 °C").
2. Rango numérico de pH en que la reacción de Maillard se acelera, y el efecto cuantitativo del bicarbonato en la cebolla.
3. Rango óptimo de actividad de agua para la reacción de Maillard.
4. Temperaturas de inicio de la caramelización de fructosa, glucosa y sacarosa.
5. Condiciones (pH, temperatura, tiempo) de la inversión de la sacarosa.
6. Temperaturas de desnaturalización específicas de ovotransferrina, ovoalbúmina y lisozima, y temperatura de gelificación de la yema.
7. Temperaturas de desnaturalización de miosina y actina en carne cocida, y su relación numérica con la jugosidad.
8. Tiempo de conversión de colágeno a gelatina a cada temperatura.
9. Mecanismo y concentración de sal para solubilizar miosina en salmuera.
10. Temperatura y tiempo de inactivación de bromelina, papaína y actinidina; efecto de la actinidina (kiwi) sobre la gelatina.
11. Congelación de pescado según el Reglamento (CE) 853/2004 (cifras de la UE). La página oficial del Reino Unido estaba bloqueada.
12. Rangos de gelatinización de almidón de maíz y de papa.
13. Comparación de claridad y de estabilidad al ácido entre maíz, papa, yuca y arrurruz.
14. Porcentaje mínimo de grasa que garantiza el batido de la crema (hay solo definición legal) y temperatura óptima de batido.
15. Causa física de que el aceite frío corte la mayonesa.
16. Valor del calor específico del agua.
17. Temperatura del estancamiento térmico en carne (solo hay un experimento no revisado por pares).
18. Minutos extra de cocción en Bogotá para huevos, pasta y legumbres.
19. Presión de olla para conservas en Bogotá (≈ 8530 pies).
20. Colores de la antocianina de repollo morado para cada valor de pH.
21. Efecto del bicarbonato sobre la clorofila.
22. Mecanismo y dosis del ácido ascórbico o del limón contra la polifenoloxidasa.
23. pH objetivo para una fermentación láctica segura.
24. Niveles de referencia de acrilamida del Anexo IV del Reglamento (UE) 2017/2158.
25. Contenido de glutamato y nucleótidos por alimento.

## 14. Fuentes bloqueadas

- PubMed Central (pmc.ncbi.nlm.nih.gov): página de CAPTCHA.
- mdpi.com, europepmc (ebi.ac.uk), gov.uk, webbook.nist.gov, legislation.gov.uk/…/annex/IV: fuera de la lista de URL permitidas de la sesión.
