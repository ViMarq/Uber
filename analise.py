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
print(uber.head(5))

# Calculo de medidas de tendencia central

# m_fare_amount = uber['fare_amount'].mean()
# print(f'M = {m_fare_amount:.2f}')

# m_distancia = uber['distancia'].mean()
# print(f'M = {m_distancia:.3f}')

# med_fare_amount = uber['fare_amount'].median()
# print(f'Med = {med_fare_amount:.2f}')

# med_distancia = uber['distancia'].median()
# print(f'Med = {med_distancia:.3f}')

# mo_fare_amount = uber['fare_amount'].mode().values
# print(f'Mo = {mo_fare_amount}')

# mo_distancia = uber['distancia'].mode().values
# print(f'Mo = {mo_distancia}')

# Calculo de medidas de dispersão

# ampl_fare_amount = uber['fare_amount'].max() - uber['fare_amount'].min()
# print(f'Ampl = {ampl_fare_amount}') #Amplitude
# ampl_distancia = uber['distancia'].max() - uber['distancia'].min()
# print(f'Ampl = {ampl_distancia}')

# var_fare_amount = uber['fare_amount'].var()
# print(f'Var = {var_fare_amount}')

# var_distancia = uber['distancia'].var()
# print(f'Var = {var_distancia}')

# corr_fare_amount = uber['fare_amount'].corr()
# print(f'Corr = {corr_fare_amount}')

# cov_fare_amount = uber['fare_amount'].cov()
# print(f'Cov = {corr_fare_amount}')

# dp_fare_amount = uber['fare_amount'].std()
# print(f'DP = {dp_fare_amount:.2f}')

# dp_distancia = uber['distancia'].std()
# print(f'DP = {dp_distancia:.3f}')

# Gerando arquivo .csv da base tratada
# uber.to_csv('dataset/UBER_TESTE.csv', index=False)



# Comparação entre variavel alvo e quantidade de passageiros

# Scatterplot
plt.scatter(uber['passenger_count'], uber['fare_amount'], color='blue', s=2)
plt.title('Preço x Passageiros')
plt.xlabel('Passageiros')
plt.ylabel('Preço')
plt.show()

# Histograma


plt.hist(uber['passenger_count'], bins=20)
plt.title('Número de passageiros que mais solicitam corridas')
plt.xlabel('Passageiros')
plt.ylabel('Frequência')
plt.show()

# Comparação entre variavel alvo e distancia

# Scatterplot

plt.scatter(uber['fare_amount'], uber['distancia'], color='blue', s=2)
plt.title('Preço x Distância')
plt.xlabel('Preço')
plt.ylabel('Distancia')
plt.show()

# Histograma

plt.hist(uber['fare_amount'], bins=20)
plt.title('Qtd. de preços mais cobrados')
plt.xlabel('Preço')
plt.ylabel('Frequência')
plt.show()

# Comparação entre variavel alvo e mês

# Scatterplot

plt.scatter(uber['mes'], uber['fare_amount'], color='blue', s=2)
plt.title('Preço x Mês')
plt.xlabel('Mês')
plt.ylabel('Preço')
plt.show()

# Histograma

plt.hist(uber['mes'], bins=20)
plt.title('Qtd. de meses mais solicitados')
plt.xlabel('Meses')
plt.ylabel('Frequência')
plt.show()