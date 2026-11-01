# odorantes-db: base de odorantes clave de alimentos

Base consultable de **odorantes clave** (compuestos de aroma por encima de su umbral) de 18 alimentos, extraída de estudios con olfatometría, dilución de extracto aromático (AEDA), dilución isotópica (SIDA), valores de actividad de olor (OAV) y recombinación. Da soporte a la skill [`odorantes-clave`](../skills/odorantes-clave/SKILL.md).

## Qué contiene

- `datos/alimentos.json`: los 18 alimentos con su forma culinaria definida.
- `datos/extracciones/lote_*.json`: estudios (DOI, muestra, métodos, nota propia) y odorantes (nombre, descriptor, FD, OAV, nivel A–D, ubicación en la fuente).
- `datos/sinonimos.json`: unificación de nombres (por ejemplo, furaneol = HDMF).
- `datos/odorantes.sqlite` y `datos/odorantes.csv`: la base construida.

## Niveles de evidencia de cada odorante

| Nivel | Método |
|---|---|
| A | Recombinación validada u omisión significativa |
| B | Cuantificación (idealmente SIDA) con OAV ≥ 1 |
| C | Olfatometría / AEDA u OAV semicuantitativo |
| D | Solo GC-MS, sin olfatometría |

Confianza de un odorante compartido: **alta** si está en nivel A–C en los dos alimentos; **media** si está en A–C en uno y D en el otro; **baja** si es D en los dos.

## Uso

```bash
python3 scripts/build_db.py                       # construye la base
python3 scripts/consulta.py matcha frambuesa      # odorantes compartidos
python3 scripts/consulta.py matcha                # perfil y mejores puentes
python3 scripts/buscar.py "alga matcha"           # búsqueda de texto con fuente (capa RAG)
python3 scripts/pruebas.py                        # integridad, regresión, sinónimos
```

## Límites

- Solo 10 de los 60 estudios tenían texto completo de acceso abierto. Los demás se extrajeron del resumen, así que faltan cifras de FD/OAV y algunos compuestos.
- Los FD y OAV no se comparan entre estudios: dependen del método y la matriz.
- La asignación de tipo de aroma (14 tipos de Foodpairing) es una heurística por palabras del descriptor.
- No se guarda texto de los artículos: solo datos (nombres, cifras, métodos) y notas parafraseadas.

## Ampliar la base

Añade el alimento a `datos/alimentos.json` con un nuevo número de lote y sigue `docs/instrucciones_extraccion.md`. Después ejecuta `build_db.py` y `pruebas.py`.
