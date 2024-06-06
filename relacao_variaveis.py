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
from haversine import haversine

# Carregando a base
uber = pd.read_csv('dataset/UBER_TRATADO.csv',sep=',')
print(uber.head(10))
#uber_test = sns.load_dataset(uber)

# Matriz de correlação

#ax = sns.pairplot(data_set.loc[:,['fare_amount', 'pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude', 'passenger_count', 'dia', 'mes', 'ano']],
#y_vars='fare_amount',
#x_vars=['pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude', 'passenger_count', 'dia', 'mes', 'ano'],
#plot_kws={'line_kws':{'color':'red'}})
#ax.fig.suptitle("Dispersão entre as variáveis", fontsize=20, y=1.1) # o argumento y indica a posição do titulo em relação ao eixo y
#plt.show()

#ax = sns.load_dataset(uber).pivot(index="fare_amount", columns=['fare_amount', 'pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude', 'passenger_count', 'dia', 'mes', 'ano'], values="Score")
i = 0
for column,row in uber.iterrows():
    longitude_ini = row['pickup_longitude']
    latitude_ini = row['pickup_latitude']
    longitude_fim = row['dropoff_longitude']
    latitude_fim = row['dropoff_latitude']
    partida = (latitude_ini,longitude_ini)
    destino = (latitude_fim,longitude_fim)
    try:
        result = haversine(partida,destino)
        uber.at[column, 'distancia'] = f'{result:.3f}'
        print(f'{result:.3f} KM')
    except:
        i = i + 1  

print(f'Foram encontrato {i} linha com problema')
# Gerando arquivo .csv da base tratada
uber.to_csv('UBER_teste.csv', index=False)