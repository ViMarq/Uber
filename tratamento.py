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
uber = pd.read_csv("dataset/Uber.csv", sep=',')

# Removendo valores nulos e valores iguais a 0
uber = uber.dropna()
uber = uber[uber['pickup_longitude'] != 0]
uber = uber[uber['pickup_latitude'] != 0]
uber = uber[uber['dropoff_longitude'] != 0]
uber = uber[uber['dropoff_latitude'] != 0]
uber = uber[uber['passenger_count'] != 0]

# Dropando colunas não desejadas, no caso, unnamed e key
uber.drop(['Unnamed: 0','key'], axis=1, inplace=True)

# Inicializar as novas colunas com valores nulos
uber['dia'] = None
uber['mes'] = None
uber['ano'] = None

for index, row in uber.iterrows():
    data = pd.to_datetime(row['pickup_datetime'])
    uber.at[index, 'dia'] = data.day
    uber.at[index, 'mes'] = data.month
    uber.at[index, 'ano'] = data.year
uber.drop(['pickup_datetime'], axis=1, inplace=True)

# Acesando os valores da biblioteca uber pela colunas e linhas. 
# Para index sao retornado todos os valores que estao em sua respectiva coluna baseada no nome pre definido no .csv
# Para row sao retornado todos os valores de um linha baseado na sua numeracao pre definida pelo panda. 
# Ao acessar com ['column_name'] retornamos o valor especifico da linha e coluna.   
for index, row in uber.iterrows():
    if (row['pickup_longitude'] < -180 or row['pickup_longitude'] > 180):
        row['pickup_longitude'] = row['pickup_longitude']/10
    
    if (row['dropoff_longitude'] < -180 or row['dropoff_longitude'] > 180):
        row['dropoff_longitude'] = row['dropoff_longitude']/10

    if (row['pickup_latitude'] < -90 or row['pickup_latitude'] > 90):
        row['pickup_latitude'] = row['pickup_latitude']/10
    
    if (row['dropoff_latitude'] < -90 or row['dropoff_latitude'] > 90):
        row['dropoff_latitude'] = row['dropoff_latitude']/10

    uber.at[index, 'pickup_longitude'] = row['pickup_longitude']
    uber.at[index, 'dropoff_longitude'] = row['dropoff_longitude']
    uber.at[index, 'pickup_latitude'] = row['pickup_latitude']
    uber.at[index, 'dropoff_latitude'] = row['dropoff_latitude']



# Gerando arquivo .csv da base tratada
uber.to_csv('dataset/UBER_TRATADO.csv', index=False)