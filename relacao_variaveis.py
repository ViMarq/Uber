# Bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy
from sklearn.ensemble import IsolationForest
import datetime
import time
from IPython.display import display

# Carregando a base
uber = sns.load_dataset("UBER_TRATADO.csv")

# Matriz de correlação

# ax = sns.pairplot(uber.loc[:,['fare_amount', 'pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude', 'passenger_count', 'dia', 'mes', 'ano']],
# y_vars='fare_amount',
# x_vars=['pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude', 'passenger_count', 'dia', 'mes', 'ano'],
# kind='reg',
# plot_kws={'line_kws':{'color':'red'}})
# ax.fig.suptitle("Dispersão entre as variáveis", fontsize=20, y=1.1) # o argumento y indica a posição do titulo em relação ao eixo y
# sns.heatmap()

ax = sns.load_dataset(uber).pivot(index="fare_amount", columns=['fare_amount', 'pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude', 'passenger_count', 'dia', 'mes', 'ano'], values="Score")