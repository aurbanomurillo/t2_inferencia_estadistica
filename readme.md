# Trabajo 2 - Inferencia Estadistica Meteorologica

![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0)
![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?logo=scipy&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Analisis de inferencia estadistica aplicado a series meteorologicas diarias en la celda 01, organizado por apartados del enunciado y desarrollado en notebooks de Jupyter.

## Resumen Del Proyecto

- Variables analizadas: temperatura a 2 m, irradiacion solar descendente en superficie y precipitacion total.
- Cobertura temporal: 2014-01-01 a 2025-12-31.
- Resolucion temporal: diaria.
- Enfoque: contrastes de hipotesis, ajuste de distribuciones, Bootstrap y simulacion.
- Flujo de trabajo: carga de datos, analisis por apartados y documentacion del informe.

## Estructura Del Repositorio

```text
.
|-- src/
|   |-- carga_de_datos.py
|   |-- carga_de_datos.ipynb
|   |-- Apartado_1.ipynb
|   |-- Apartado_2.ipynb
|   |-- Apartado_3.ipynb
|   `-- Apartado_4.ipynb
|-- documentation/
|   |-- Informe del trabajo.docx
|   `-- OBJETIVOS2026_TrabajoInferencia.pdf
|-- requirements.txt
|-- LICENSE
|-- .gitignore
`-- README.md
```

## Contenido Analitico (Por Apartados)

### Apartado 1

- Contrastes de hipotesis para la media estival de temperatura en celda 01.
- Contraste unilateral superior e inferior respecto a 30 C.
- Nivel de confianza del 90% bajo supuesto de normalidad.

### Apartado 2

- Contraste KS por trimestres para normalidad en irradiacion, temperatura y precipitacion.
- Apoyo visual mediante qqplots.
- Ajuste global de distribuciones uniforme, exponencial, normal, beta, triangular y kernel.

### Apartado 3

- Intervalos de confianza Bootstrap para medias trimestrales de irradiacion.
- Repeticion del analisis para temperatura y precipitacion.
- Comparacion de solape de intervalos para niveles de confianza del 50% y 99%.

### Apartado 4

- Simulacion pseudoaleatoria a partir de distribuciones elegidas en el apartado 2.2.
- Tamano muestral n1 = 10, n2 = 100, n3 = 1000, n4 = 10000.
- Comparacion entre distribuciones de muestras simuladas y datos reales.

## Entorno Y Dependencias

Dependencias principales:

- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `scipy`
- `jupyter` / `notebook` / `ipykernel`

Instalacion:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Ejecucion Reproducible

Orden sugerido para reproducir el trabajo:

1. `src/carga_de_datos.ipynb` o `src/carga_de_datos.py`
2. `src/Apartado_1.ipynb`
3. `src/Apartado_2.ipynb`
4. `src/Apartado_3.ipynb`
5. `src/Apartado_4.ipynb`

Para lanzar Jupyter:

```bash
python -m notebook
```

## Documentacion Entregable

En `documentation` se incluye:

- Enunciado oficial del trabajo 2.
- Informe del trabajo en formato editable.

## Licencia

Proyecto bajo licencia MIT. Consulta el fichero `LICENSE` para el texto completo.
