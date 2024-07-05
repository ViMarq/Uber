import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from geopy.geocoders import Nominatim
from haversine import haversine
import datetime
import forex_python
from forex_python.converter import CurrencyRates

# Modelo de regressão linear

# Carregando a base
uber = pd.read_csv('dataset/UBER_TRATADO.csv',sep=',')

# Criação das variáveis de entrada (X) e saída (y)
# Separar os dados em treino e teste
X = uber[['distancia','passenger_count', 'mes']].values
y = uber['fare_amount']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42) #tamanho do teste alocado em 30%

# Controi a arvore de decisao e a profundidade
modelo = DecisionTreeRegressor(max_depth=3)
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)


#Define o agente para consulta de endereço via geo locator.
geolocator = Nominatim(user_agent="my_app")


# Recupera informações passadas pelo usuario de endereço de partida e tenta recuperar latitude e logitude. 
# Maximo de 3 tentativas por usuario.  
for i in range(3):
    local_de_partida = input("Digite o endereço de partida:")
    estado_de_partida = input("Digite o estado do local de partida:")
    local_de_partida="Rua Ramon Schlemmer"
    estado_de_partida="São Paulo"
    try:
        format_location = f'{local_de_partida}, {estado_de_partida}'
        location_partida = geolocator.geocode(f"{format_location}")
        break
    except:
        print("Informações de endereço incorretas. Tente novamente")

# Atribui as variaveis de latitude e longitude do local origem
latitude_partida = location_partida.latitude
longitude_partida = location_partida.longitude


# Recupera informações passadas pelo usuario de endereço de destino e tenta recuperar latitude e logitude. 
# Maximo de 3 tentativas por usuario.  
for i in range(3):
    local_de_destino = input("Digite o endereço de destino:")
    estado_de_destino = input("Digite o estado do local de destino:")
    local_de_destino="Rua minas"
    estado_de_destino="São Paulo"
    try:
        format_location = f'{local_de_destino}, {estado_de_destino}'
        location_destino = geolocator.geocode(f"{format_location}")
        break
    except:
        print("Informações de endereço incorretas. Tente novamente")

# Atribui as variaveis de latitude e longitude do local origem
latitude_destino = location_destino.latitude
longitude_destino = location_destino.longitude


print(f'A latitude e longitude do local de partida são: lat{latitude_partida}, lon{longitude_partida}')
print(f'A latitude e longitude do local de destino são: lat{latitude_destino}, lon{longitude_destino}')


# Calculo de distancia baseada na latitude e longitude do ponto inicial e do ponto final. 
partida = (latitude_partida,longitude_partida)
destino = (latitude_destino,longitude_destino)
try:
    distancia = round(haversine(partida,destino),2)
except:
    raise Exception("Não foi possivel obter a distancia entre os dois pontos. ")

print(f"A distancia do ponto de partida e o destino são de {distancia}KM")

#Pega o mês de referencia do computador ou solicita um mês ao usuario.
result = input("Deseja inserir um mês para viajar ou utilizar o mês atual? (S/N) ").upper()

print (result)
match result: 
    case 'S':
        mes = int(input("Digite o mês desejado para viajar:"))
    case 'N':
        # Obtém a data e hora atual
        data_atual = datetime.datetime.now()
        # Extrai o mês atual
        mes = data_atual.month
    case _:
        raise Exception("Opção escolhida não é valida, tente novamente.")

          
print(f"O mês escolhido para realizar a viagem é o {mes}")

# Pega a quantidade de pessoas que irão participar desta viagem.
# O processo fica em loop até o usuario digitar uma quantidade valida. 
passageiros = 0
while passageiros == 0:
    passageiros = int(input("Digite a quantidade de passageiros da viagem:"))
    if passageiros < 1 or passageiros > 4:
        print("Quantidade de passageiros escolhida é inferior a 1 passageiro ou superior a 4 passageiros.")
        passageiros = 0

print(f"A quantidade de passageios desta viagem é de {passageiros} pessoa(s)")


# Define a biblioteca de dados para IA calcular o preço justo para a corrida. 
parametros_uber = [distancia,mes,passageiros]

# Usar modelo de predição.
prev_modelo_preco = modelo.predict([parametros_uber])

# Varrer o array para devolver somente o valor de dentro
for p in prev_modelo_preco:
    prev_modelo_preco = CurrencyRates().convert('USD', 'BRL', p)
    print(prev_modelo_preco)

# print(f'O preço sugerido para essa corrida é de R${prev_modelo_preco}')