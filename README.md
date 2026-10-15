# Rentabilidad y descuentos en ventas minoristas

Análisis exploratorio de ventas realizado en el trabajo final de Estadística Aplicada de un diplomado. A partir del conjunto de datos del curso, estudié los márgenes por subcategoría y la relación observada entre descuentos y ganancias. El repositorio incluye los datos, el notebook y un script para reproducir los indicadores principales.

![Relación entre descuentos y ganancias, gráfico del notebook original](images/discount_vs_profit_original.png)

*Gráfico de la sección “ANÁLISIS EXTRA” del notebook académico: cada punto representa una venta; la línea horizontal marca ganancia cero.*

**Resultado principal:** cuatro subcategorías registraron pérdida neta. Los registros con descuentos mayores al 20% también sumaron pérdidas, una asociación descriptiva que no demuestra causalidad.

## Inicio rápido

Requiere Python 3.10 o posterior. Desde la raíz del repositorio:

```powershell
python -m pip install -r requirements.txt
python analysis.py
```

El script lee `data/RetailNuevo3.csv`, imprime los agregados y regenera `images/profit_by_subcategory.png`. También acepta otro archivo con `python analysis.py --data ruta/al/archivo.csv` si conserva las columnas necesarias.

## Estructura

```text
.
├── README.md                         # descripción del proyecto
├── analysis.py                       # cálculo y gráfico reproducibles
├── requirements.txt
├── data/
│   ├── README.md                     # origen, columnas y límites del CSV
│   └── RetailNuevo3.csv
├── images/
│   ├── discount_vs_profit_original.png # descuentos y ganancias
│   └── profit_by_subcategory.png      # rentabilidad por subcategoría
└── notebooks/
    └── trabajo_final_academico.ipynb # trabajo final de Estadística Aplicada
```

## Datos

El CSV fue facilitado por los docentes del diplomado de la UPB para el trabajo final de Estadística Aplicada. Contiene 2.000 registros, 3 categorías, 17 subcategorías y 47 estados. El análisis usa `Sales`, `Profit`, `Discount`, `Category` y `Sub-Category`. El periodo, la moneda y la procedencia original del conjunto no están documentados. [Diccionario de datos](data/README.md).

## Método

Sumé `Sales` y `Profit` por subcategoría y calculé el margen agregado como `sum(Profit) / sum(Sales)`. Comparé la ganancia acumulada de registros con descuentos `≤20%` y `>20%`. Los grupos tienen tamaños distintos y la comparación no controla por categoría, producto u otros factores; sirve para priorizar una revisión, no para estimar el efecto de cambiar descuentos.

## Resultados

1. Las ventas suman **452.790,42** y la ganancia neta **54.704,30**, con un margen agregado de **12,08%**.
2. Cuatro subcategorías tienen pérdida neta: **Tables** (−5.949,17), **Machines** (−5.416,28), **Bookcases** (−1.573,74) y **Supplies** (−1.086,95). [Ver rentabilidad por subcategoría](images/profit_by_subcategory.png).
3. Los **1.733** registros con descuento de hasta 20% suman **84.922,09** de ganancia; los **267** con descuento superior a 20% suman **−30.217,79**.

**Recomendación:** revisar descuentos y costos de las cuatro subcategorías deficitarias antes de cambiar promociones. El archivo no permite atribuir las pérdidas al descuento ni afirmar un impacto comercial real.

## Mi contribución

Resolví las preguntas de segmentación, visualización e inferencia de la consigna académica. Amplié el trabajo con análisis de márgenes por subcategoría y exploración de descuentos y ganancias, identificados como “ANÁLISIS EXTRA” en el [notebook](notebooks/trabajo_final_academico.ipynb).


