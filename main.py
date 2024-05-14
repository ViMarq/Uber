import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy
from sklearn.ensemble import IsolationForest

uber = pd.read_csv("UBER.csv", sep=',')


uber = uber.rename(columns={
    'Date': 'Data', 'Open': 'Preco_inicial', 'High': 'Preco_maximo',
    'Low': 'Preco_menor', 'Close': 'Preco_fechamento',
    'Adj Close': 'Preco_fechamanto_acao', 'Volume': 'Total'
})

print(uber.head())

ax = sns.pairplot(uber.loc[:,['Preco_inicial', 'Preco_maximo', 'Preco_menor', 'Preco_fechamento', 'Preco_fechamanto_acao', 'Total']],
                      y_vars='Total', 
                      x_vars=['Preco_inicial', 'Preco_maximo', 'Preco_menor', 'Preco_fechamento', 'Preco_fechamanto_acao'],
                      kind='reg', 
                      plot_kws={'line_kws':{'color':'red'}})
ax.fig.suptitle("Dispersão entre as variáveis", fontsize=10, y=1) # o argumento y indica a posição do titulo em relação ao eixo y
plt.show()

