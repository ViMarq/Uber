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
uber = pd.read_csv("UBER.csv", sep=',')

# Removendo valores nulos e valores iguais a 0
uber = uber.dropna()
uber = uber[uber['pickup_longitude'] != 0]
uber = uber[uber['pickup_latitude'] != 0]
uber = uber[uber['dropoff_longitude'] != 0]
uber = uber[uber['dropoff_latitude'] != 0]

# Dropando colunas não desejadas, no caso, unnamed e key
uber.drop(['Unnamed: 0','key'], axis=1, inplace=True)
display(uber.head())

