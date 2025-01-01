# Explicação do modelo

### 1. Importação de Bibliotecas
```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
```
- **pandas**: biblioteca utilizada para manipulação e análise de dados em formato tabular.
- **matplotlib.pyplot**: biblioteca utilizada para criar gráficos, como o gráfico de dispersão.
- **numpy**: biblioteca para manipulação de arrays e cálculos matemáticos.
- **sklearn.linear_model.LogisticRegression**: classe do `scikit-learn` utilizada para criar e treinar um modelo de regressão logística.

### 2. Carregamento e Exibição dos Dados
```python
df = pd.read_csv('../../datasets/Eleicao.csv', sep=';', encoding='utf-8')
df.head()
```
- **pd.read_csv**: lê um arquivo CSV (aqui, `Eleicao.csv`) e o carrega em um DataFrame do `pandas`. 
- O arquivo usa `;` como delimitador, e o encoding `utf-8` para leitura de caracteres especiais.
- **df.head()**: exibe as primeiras 5 linhas do DataFrame para que você possa ver uma amostra dos dados.

### 3. Análise Inicial dos Dados
```python
df.shape, df.describe()
```
- **df.shape**: retorna as dimensões do DataFrame (número de linhas e colunas).
- **df.describe()**: fornece estatísticas descritivas das variáveis numéricas, como média, desvio padrão, mínimo, máximo, etc.

### 4. Correlação entre as Variáveis
```python
np.corrcoef(df.DESPESAS, df.SITUACAO)
```
- **np.corrcoef**: calcula a correlação entre as variáveis `DESPESAS` (gastos da campanha) e `SITUACAO` (resultado da eleição, 1 para vitória e 0 para derrota).
- Isso ajuda a entender se há uma relação entre as duas variáveis.

### 5. Visualização Gráfica
```python
plt.scatter(df.DESPESAS, df.SITUACAO);
```
- **plt.scatter**: cria um gráfico de dispersão (scatter plot) com as variáveis `DESPESAS` no eixo X e `SITUACAO` no eixo Y. O objetivo aqui é visualizar a relação entre as despesas de campanha e o resultado da eleição.

### 6. Preparação dos Dados para o Modelo
```python
X = df.iloc[:, 2].values
X = X[:, np.newaxis]
y = df.iloc[:, 1].values
```
- **X**: extrai a coluna das despesas (3ª coluna, índice 2) e a transforma em um vetor. `np.newaxis` é utilizado para garantir que `X` seja uma matriz coluna (com uma única coluna).
- **y**: extrai a coluna do resultado da eleição (2ª coluna, índice 1), que é o alvo do modelo.

### 7. Criação e Treinamento do Modelo
```python
modelo = LogisticRegression()
modelo.fit(X, y)
```
- **LogisticRegression()**: cria uma instância do modelo de regressão logística.
- **modelo.fit(X, y)**: treina o modelo com os dados de entrada (`X` - despesas) e o alvo (`y` - situação da eleição).

### 8. Exibindo os Coeficientes do Modelo
```python
modelo.coef_, modelo.intercept_
```
- **modelo.coef_**: exibe o coeficiente da regressão logística. Esse valor indica a relação entre a variável `X` (despesas) e a probabilidade de vitória (`SITUACAO`).
- **modelo.intercept_**: exibe o intercepto (termo constante) do modelo. Isso é o valor de `log(p / (1 - p))` quando as despesas são zero.

### 9. Visualização da Curva de Regressão Logística
```python
plt.scatter(X, y)
X_teste = np.linspace(10, 3000, 100)

def model(x):
    return 1 / (1 + np.exp(-x))

r = model(X_teste * modelo.coef_ + modelo.intercept_).ravel()
plt.plot(X_teste, r, color='red')
```
- **plt.scatter(X, y)**: plota novamente o gráfico de dispersão das despesas e o resultado.
- **X_teste**: cria um conjunto de valores para as despesas, variando entre 10 e 3000.
- **model(x)**: define a função sigmoide que será usada para a regressão logística. A função transforma os valores de `x` em uma probabilidade (valor entre 0 e 1).
- **r**: aplica a função sigmoide para obter a probabilidade de vitória com base nas despesas.
- **plt.plot(X_teste, r, color='red')**: plota a curva de regressão logística (a probabilidade de vitória dada a despesa).

### 10. Carregamento de Novos Dados e Previsões
```python
df_previsoes = pd.read_csv('../../datasets/NovosCandidatos.csv', sep=';', encoding='utf-8')
df_previsoes.head()
```
- Carrega os dados dos novos candidatos (`NovosCandidatos.csv`), que têm apenas as despesas de campanha para os quais queremos fazer previsões.

### 11. Preparação dos Dados para Previsão
```python
despesas = df_previsoes.iloc[:, 1].values
despesas = despesas.reshape(-1, 1)
```
- Extrai a coluna das despesas e a transforma em um vetor coluna para ser compatível com a entrada do modelo.

### 12. Realizando as Previsões
```python
previsoes = modelo.predict(despesas)
previsoes
```
- **modelo.predict(despesas)**: utiliza o modelo treinado para prever a probabilidade de vitória (0 ou 1) com base nas novas despesas.

### 13. Montagem da Base de Previsões
```python
base_previsoes = np.column_stack((df_previsoes, previsoes))
base_previsoes
```
- **np.column_stack**: adiciona as previsões (vitória ou derrota) ao DataFrame original dos novos candidatos, criando uma nova matriz com as despesas e as previsões.

---

### Resumo:
Esse código cria e treina um modelo de regressão logística para prever o resultado de uma eleição com base nas despesas de campanha. Após o treinamento, o modelo pode ser utilizado para prever o resultado de novas eleições com base em despesas de candidatos ainda não eleitos. O fluxo básico do código é:
1. Carregamento dos dados.
2. Análise exploratória (correlação, gráficos).
3. Treinamento do modelo de regressão logística.
4. Visualização da curva logística ajustada.
5. Realização de previsões para novos dados.
