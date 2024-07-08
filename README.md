# Uber

# Objetivo

Esse repositório foi criado com propósito de aprendizado para o portifólio. Esse trabalho foi desenvolvido em dupla com o objetivo de aprender sobre analise de dados e algoritmos de machine learning a partir de uma base de dados, a fim de construí-la e desenvolvê-la de uma forma clara.

Foi utilizado como liguagem de programação o Python sendo executado na IDE do Jupyter Notebook.

A partir dos dados obtidos das corridas de UBER entre 2008 a 2015 também criamos através de da biblioteca geodesic do python

# Processo de desenvolvimento



# Variável alvo e colunas consideradas para essa análise

Nosso projeto tem como objetivo determinar qual o preço ideal para corridas de Uber, com isso em mente, escolhemos dentre as colunas disponíveis no dataset "Uber Fares Dataset" as que definimos como relevantes, dentre elas temos:

- fare_amount

O custo de cada viagem

- distancia

Distância em Kilometros das viagens

- mes

Mês da solicitação de corrida

- hora

Horário da solicitação de corrida

- passenger_count

Quantidade de passegeiros presentes na corrida

# Fonte

O dataset escolhido pertence ao Kaggle e pode ser encontrado no link abaixo:
https://www.kaggle.com/datasets/yasserh/uber-fares-dataset/data

# Observação

# Instalação da máquina virtual
python -m venv .env

# Para iniciar máquina virtual
cd .\.env\Scripts\
.\activate

# Instalar dentro da vm todas as bibliotecas necessárias
cd ../..
pip install -r requirements.txt

# Para atualizar os requerimentos de bibliotecas
pip freeze > requirements.txt