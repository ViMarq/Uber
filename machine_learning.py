import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, root_mean_squared_error
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.tree import export_graphviz
from sklearn.metrics import mean_squared_error
from sklearn import tree
import graphviz
import seaborn as sns

# Modelo de regressão linear

# Carregando a base
uber = pd.read_csv('dataset/UBER_TRATADO.csv',sep=',')

# Listar todas as colunas do dataset
print(uber.columns.tolist())

uber.drop(index=uber[uber['fare_amount'] == 0].index, inplace=True)
minimo = uber['fare_amount'].min()
maximo = uber['fare_amount'].max()
print(f'Preço mínimo: {minimo}')
print(f'Preço maximo: {maximo}')

# Criação das variáveis de entrada (X) e saída (y)
# Separar os dados em treino e teste
X = uber[['distancia','passenger_count', 'mes']].values
y = uber['fare_amount']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42) #tamanho do teste alocado em 30%

# Controi a arvore de decisao e a profundidade
modelo = DecisionTreeRegressor(max_depth=3)
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)

# Determinacao do R² 
r2 = r2_score(y_test, y_pred)
print('Coeficiente de determinação (R²):', r2)

print(uber[['fare_amount','distancia']].head(10).sort_values(by='fare_amount'))

# Calculando o quadrado da diferença entre os valores das variáveis observada e a predita do modelo
# OBS: acc = accuracy_score(y_test, y_pred) -->> Espera um valor booleano entre 0 e 1 e como os preço são número continuos não tem como usar acurácia.
mse = mean_squared_error(y_test, y_pred)
print(f'MSE = {mse}')

# Calculo da média percentual absoluta do Erro. Ultilizada para fazer comparações entre erro percentuais do modelo entre produtos. 
mape = mean_absolute_percentage_error(y_test, y_pred)
print(f'MAPE = {mape}')

# Caculo da média dos erros absolutos(MAE). Ultilizada para medida em séries temporarias. 
mae = mean_absolute_error(y_test, y_pred)
print(f'MAE = {mae}')

# Calcula da raiz do erro quadrático cédio
rmse  = root_mean_squared_error(y_test, y_pred)
print(f'RMSE = {rmse}')


# Ultilizar além do R² o calculos de métricas MAPE e MAE para base do comitê.  
