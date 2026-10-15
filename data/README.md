# Datos del caso

`RetailNuevo3.csv` se utilizó en el trabajo final de Estadística Aplicada y fue distribuido por el curso mediante Moodle. Los materiales del curso no indican la fuente original del conjunto, el periodo ni la moneda.

El archivo tiene 2.000 filas. Las columnas usadas en el análisis son:

| Columna | Uso |
| --- | --- |
| `Sales` | Importe de ventas por registro, en unidad monetaria no documentada. |
| `Profit` | Ganancia o pérdida registrada por fila. |
| `Discount` | Descuento expresado como fracción; `0.2` equivale a 20%. |
| `Category` | Categoría del producto. |
| `Sub-Category` | Subcategoría del producto. |

El CSV incluye además modo de envío, segmento, ubicación, cantidad y una primera columna sin nombre que funciona como identificador de fila. Para calcular los indicadores desde la raíz del repositorio: `python analysis.py`.
