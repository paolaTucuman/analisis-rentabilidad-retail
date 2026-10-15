# Datos del caso

`RetailNuevo3.csv` fue entregado mediante Moodle para el trabajo final de Estadística Aplicada. La autora confirmó que puede redistribuir esta copia. La fuente original del conjunto, su periodo, moneda y licencia de reutilización no constan en los materiales revisados. Se comparte para verificar este caso académico; no se concede una licencia adicional sobre los datos.

El archivo tiene 2.000 filas. Las columnas usadas en el análisis son:

| Columna | Uso |
| --- | --- |
| `Sales` | Importe de ventas por registro, en unidad monetaria no documentada. |
| `Profit` | Ganancia o pérdida registrada por fila. |
| `Discount` | Descuento expresado como fracción; `0.2` equivale a 20%. |
| `Category` | Categoría del producto. |
| `Sub-Category` | Subcategoría del producto. |

El CSV incluye además modo de envío, segmento, ubicación, cantidad y una primera columna sin nombre que funciona como identificador de fila. No contiene nombres de clientes ni direcciones personales en las columnas revisadas. Para regenerar las cifras desde la raíz del repositorio: `python analysis.py`.
