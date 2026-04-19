<div align="center">

# Trabajo 2 - Inferencia Estadistica Meteorologica

Inferencia estadistica aplicada a series meteorologicas diarias, con flujo reproducible en Jupyter y organizacion por apartados del enunciado oficial.

![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?logo=scipy&logoColor=white)
![Statsmodels](https://img.shields.io/badge/Statsmodels-1f77b4)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

</div>

---

## Vision General

- Variables: temperatura a 2m, irradiacion solar descendente y precipitacion total.
- Cobertura temporal: 2014-01-01 a 2025-12-31.
- Frecuencia: diaria.
- Alcance metodologico: contrastes de hipotesis, ajuste de distribuciones, bootstrap y simulacion.
- Entorno: notebooks Jupyter + script de carga reutilizable.

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
|-- DATOS_IMAT_2026/
|-- images/
|-- documentation/
|-- CONTRIBUTING.md
|-- CODE_OF_CONDUCT.md
|-- SECURITY.md
|-- requirements.txt
|-- LICENSE
|-- .gitignore
`-- README.md
```

## Ruta Analitica

| Apartado | Objetivo |
|---|---|
| 1 | Contrastes sobre la media estival de temperatura en celda 01 |
| 2 | Normalidad por trimestres y ajuste de distribuciones |
| 3 | Intervalos de confianza bootstrap y solape trimestral |
| 4 | Simulacion por tamano muestral y comparacion con datos reales |

## Puesta En Marcha

1. Crear entorno virtual:

```bash
python -m venv .venv
```

2. Activar entorno:

Windows (PowerShell):

```bash
.\.venv\Scripts\Activate.ps1
```

Linux / macOS:

```bash
source .venv/bin/activate
```

3. Instalar dependencias:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

4. Lanzar notebooks:

```bash
python -m notebook
```

## Ejecucion Reproducible

Orden recomendado:

1. `src/carga_de_datos.ipynb` (o `src/carga_de_datos.py`)
2. `src/Apartado_1.ipynb`
3. `src/Apartado_2.ipynb`
4. `src/Apartado_3.ipynb`
5. `src/Apartado_4.ipynb`

## Colaboracion

Este repositorio incluye soporte de contribucion estandar:

- Guia de contribucion en `CONTRIBUTING.md`
- Codigo de conducta en `CODE_OF_CONDUCT.md`
- Politica de seguridad en `SECURITY.md`
- Plantillas de issues y pull request en `.github/`

## Licencia

Proyecto bajo licencia MIT. Consulta `LICENSE` para el texto completo.
