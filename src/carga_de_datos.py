# Importar librerías
import pandas as pd
import numpy as np
from scipy import stats
from scipy import optimize as opt  # para estimación por máxima verosimilitud
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['figure.dpi'] = 75
import os

from statsmodels.distributions.empirical_distribution import ECDF

import statsmodels.api as sm
from statsmodels.nonparametric.kde import KDEUnivariate

from statsmodels.nonparametric.kernel_density import KDEMultivariate
import matplotlib.tri as tri


nom_fi_datos_temp = 'G09B_2m_temperature.csv'
nom_fi_datos_irrad = 'G09B_surface_solar_radiation_downwards.csv'
nom_fi_datos_precip = 'G09B_total_precipitation.csv'
ruta = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'DATOS_IMAT_2026')




ruta_csv = os.path.join(ruta, f'{nom_fi_datos_temp}')
df_orig_temp = pd.read_csv(ruta_csv)

# parseamos la fecha (cadena) para que sea un datetime con formato yyyy/mm/dd 
df_orig_temp['FECHA'] = pd.to_datetime(df_orig_temp['FECHA'], format='%Y-%m-%d')

s = df_orig_temp.loc[:,'FECHA']
df_orig_temp['FECHA'] =  s.dt.date

print('Tamaño de df_orig_temp con los datos cargados:', df_orig_temp.shape)
print('Dataframe con todos los datos leidos (filas: días, columnas: variables):')
print(df_orig_temp)




ruta_csv = os.path.join(ruta, f'{nom_fi_datos_irrad}')
df_orig_irrad = pd.read_csv(ruta_csv)

# parseamos la fecha (cadena) para que sea un datetime con formato yyyy/mm/dd 
df_orig_irrad['FECHA'] = pd.to_datetime(df_orig_irrad['FECHA'], format='%Y-%m-%d')

s = df_orig_irrad.loc[:,'FECHA']
df_orig_irrad['FECHA'] =  s.dt.date

print('Tamaño de df_orig_irrad con los datos cargados:', df_orig_irrad.shape)
print('Dataframe con todos los datos leidos (filas: días, columnas: variables):')
print(df_orig_irrad)




ruta_csv = os.path.join(ruta, f'{nom_fi_datos_precip}')
df_orig_precip = pd.read_csv(ruta_csv)

# parseamos la fecha (cadena) para que sea un datetime con formato yyyy/mm/dd 
df_orig_precip['FECHA'] = pd.to_datetime(df_orig_precip['FECHA'], format='%Y-%m-%d')

s = df_orig_precip.loc[:,'FECHA']
df_orig_precip['FECHA'] =  s.dt.date

print('Tamaño de df_orig_precip con los datos cargados:', df_orig_precip.shape)
print('Dataframe con todos los datos leidos (filas: días, columnas: variables):')
print(df_orig_precip)