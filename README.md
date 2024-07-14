# Uber

# Objetivo

Esse repositório foi criado com propósito de aprendizado para o portifólio. Esse trabalho foi desenvolvido em dupla com o objetivo de aprender sobre análise de dados e algoritmos de machine learning a partir de uma base de dados, a fim de construí-la e desenvolvê-la de uma forma clara.

Foi utilizado como liguagem de programação o Python sendo executado na IDE do Jupyter Notebook.

Todo o projeto foi desenvolvido a partir dos dados obtidos das corridas de UBER entre 2008 a 2015. Para nos auxiliar com mais informações de corridas, utilizamos um script desenvolvido em python juntamente às bibliotecas pandas, numpy e geopy para gerar dados de distância com distâncias reais dentro do território brasileiro utilizando regras de comissões por distância, mês, dia, hora e quantidade de passageiros de uma corrida.

Nosso objetivo com esse projeto foi saber qual o preço justo a ser cobrado nas corridas de Uber, dessa forma, conseguiríamos perceber a influência de colunas diretamente na variável alvo.



# Processo de desenvolvimento

Ao revisar o dataset inicial notamos uma necessidade de aplicar algumas correções e melhorias ao dataset disponibilizado inicialmente. Para o código de tratamento inicial do dataset (UBER.csv) foi realizada a remoção de campos vazios ou com valores nulos que poderiam nos atrapalhar na obtenção de dados mais precisos. Para campos timestamp foi realizada a trativas dos mesmos deixando colunas especificas de dia, mês, ano e hora na versão tratada, assim, foi possível ter uma visão mais focada e aplicada do nosso dataset. Para colunas de longitude e latitude foi feita a realização de um cálculo utilizando a biblioteca do geopy entre distâncias do ponto inicial e o ponto final, assim, foi entregue o cálculo da distância em KM (Quilômetros) do ponto inicial e do ponto final. A partir dos dados processados, os cálculos para análise e desenvolvimento poderiam ser feitos com mais precisão e velocidade. 

A análise dos dados foi realizado sobre o dataset (UBER_TRATADO.csv) disponibilizado pelo processo anterior com informações corrigidas e melhoradas para uma melhor exatidão em nossos cálculos. Colocamos todos os resultados obtidos em forma escrita e em gráficos dos tipos boxplot, scatterplot, histograma, de barras e de linha para fácil entendimento e melhor comparação.

Com isso, foi possível verificar as variáveis que influenciavam diretamente na cobrança de cada corrida solicitada pelo aplicativo da Uber, em vista disso, aplicamos o modelo de machine learning chamado de regressão linear para analisar o coeficiente de determinação (R²); desvio padrão dos valores residuais (RMSE) para verificar os erros de previsão do modelo; erro médio absoluto (MAE) a fim de avaliar o desempenho do modelo de regressão; erro quadrático médio (MSE) e, por fim, média percentual absoluta do erro (MAPE) ultilizada para fazer comparações entre erro percentuais do modelo entre produtos.

A partir do emprego de 30% da base para teste e o restante para a previsão foi possível obter 92% de acurácia em nosso modelo.


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

- Instalação da máquina virtual
python -m venv .env

- Para iniciar máquina virtual
cd .\.env\Scripts\
.\activate

- Instalar dentro da vm todas as bibliotecas necessárias
cd ../..
pip install -r requirements.txt

- Para atualizar os requerimentos de bibliotecas
pip freeze > requirements.txt