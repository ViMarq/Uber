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

m_fare_amount = uber['fare_amount'].mean()
print(f'M preço  = {m_fare_amount:.2f}')

m_distancia = uber['distancia'].mean()
print(f'M distancia = {m_distancia:.3f}')

m_distancia = uber['passenger_count'].mean()
print(f'M passageiros = {m_distancia:.3f}')

m_distancia = uber['mes'].mean()
print(f'M mes = {m_distancia:.3f}')


med_fare_amount = uber['fare_amount'].median()
print(f'Med preço = {med_fare_amount:.2f}')

med_distancia = uber['distancia'].median()
print(f'Med distancia = {med_distancia:.3f}')

med_fare_amount = uber['passenger_count'].median()
print(f'Med passageiros = {med_fare_amount:.2f}')

med_fare_amount = uber['mes'].median()
print(f'Med mes = {med_fare_amount:.2f}')


mo_fare_amount = uber['fare_amount'].mode().values
print(f'Mo preço = {mo_fare_amount}')

mo_distancia = uber['distancia'].mode().values
print(f'Mo distancia = {mo_distancia}')

mo_distancia = uber['passenger_count'].mode().values
print(f'Mo passageiros = {mo_distancia}')

mo_distancia = uber['mes'].mode().values
print(f'Mo mes = {mo_distancia}')


# Calculo de medidas de dispersão

ampl_fare_amount = uber['fare_amount'].max() - uber['fare_amount'].min()
print(f'Ampl preço = {ampl_fare_amount}') #Amplitude

ampl_distancia = uber['distancia'].max() - uber['distancia'].min()
print(f'Ampl distancia = {ampl_distancia}') #Amplitude

ampl_distancia = uber['passenger_count'].max() - uber['passenger_count'].min()
print(f'Ampl passageiros = {ampl_distancia}') #Amplitude

ampl_distancia = uber['mes'].max() - uber['mes'].min()
print(f'Ampl mes = {ampl_distancia}') #Amplitude


var_fare_amount = uber['fare_amount'].var()
print(f'Var preço = {var_fare_amount}')

var_distancia = uber['distancia'].var()
print(f'Var distancia = {var_distancia}')

var_distancia = uber['passenger_count'].var()
print(f'Var passageiros = {var_distancia}')

var_distancia = uber['mes'].var()
print(f'Var mes = {var_distancia}')




# Criando uma função de correlação para calcular a relação de forma padronizada, dentro do intervalo 0 a 1, para verificar a relação entre duas variáveis
# Quanto mais próximo de 1 maior a relação entre as variáveis e quanto mais próximo de 0 menor a relação entre as variaveis em questão.

def corr(x, y):
    n = len(x)
    x_m = x - np.mean(x)
    x_m = x_m / np.std(x, ddof=1)
    y_m = y - np.mean(y)
    y_m = y_m / np.std(y, ddof=1)
    return (x_m * y_m).sum() / (n - 1)


print(f'Corr preço e distancia {corr(uber['fare_amount'], uber['distancia'])}')
print(f'Corr preço e passageiros {corr(uber['fare_amount'], uber['passenger_count'])}')
print(f'Corr preço e mes {corr(uber['fare_amount'], uber['mes'])}')


# Criando uma função de covariância para calcular a relação de forma não padronizada, dentro do intervalo - infinito a + infinito, para verificar não só a força como também a relação linear entre duas variáveis  

def covariance(x, y):
    n = len(x)
    x_m = x - np.mean(x)
    y_m = y - np.mean(y)
    return (x_m * y_m).sum() / (n - 1)

print(f'Cov preço e distancia = {covariance(uber['fare_amount'], uber['distancia'])}')
print(f'Cov preço e passageiros = {covariance(uber['fare_amount'], uber['passenger_count'])}')
print(f'Cov preço e mes = {covariance(uber['fare_amount'], uber['mes'])}')


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

# Correlação em um único plot

# sns.pairplot(uber, diag_kws={'edgecolor':'k'}, plot_kws={'alpha':0.5, 'edgecolor':'k'})


# Boxplot mostrando a distribuição de dados entre fare_amount, distancia, passenger_count, mes de uma forma resumida e visual
# É uma ferramenta útil para identificar valores extremos e assimetrias nos dados, além de permitir a comparação de diferentes conjuntos de dados.

preco = uber
preco = preco.sort_values('fare_amount', ascending=False)[['fare_amount', 'distancia', 'passenger_count', 'mes']].head(10)
print(preco.head(10))

plt.boxplot(preco, vert = 0, patch_artist = False)
# plt.boxplot(boxplot_preco['distancia'], vert=True)
# plt.xlabel('Preço')
# plt.ylabel('Preço')
plt.title('Gráfico de comparação entre preço, distancia, número de passageiros e mês')
plt.show()

# Analise de correlação
# Matriz de correlação

plt.figure(figsize = (7,7))
sns.heatmap(uber.corr("spearman"), annot = True, cmap = "YlGnBu")
plt.title("Mapa de Correlação", fontsize = 15)
plt.show()