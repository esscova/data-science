

### Guia de Estudos: Séries Temporais com Python e ARIMA

Este guia objetiva ajudar na revisão e compreensão de conceitos de séries temporais com Python, utilizando o modelo ARIMA (AutoRegressive Integrated Moving Average) para previsão. Vamos abordar este tema, segmentando os conceitos principais de forma clara e objetiva.

---

#### Sumário:
1. **Introdução a Séries Temporais**
   - Leitura e exploração dos dados.
2. **Decomposição de Séries Temporais**
   - Análise da decomposição de séries temporais.
3. **Modelagem e Previsão com ARIMA**
   - Construção de modelos ARIMA.
   - Previsões de séries temporais.

---

### 1. **Introdução a Séries Temporais**
   - **Leitura de Dados e Exploração:**
     - Utilizando `pandas`, os dados de passageiros de avião são carregados de um arquivo CSV, com o índice sendo a coluna de datas. Exemplo:
       ```python
       df = pd.read_csv(url, parse_dates=['Month'], index_col='Month')
       df.index = pd.to_datetime(df.index, format='%Y-%m')
       ```
     - A série temporal é extraída com:
       ```python
       ts = df['#Passengers']
       ```

   - **Visualização:**
     - Para visualizar a série temporal:
       ```python
       plt.plot(ts)
       ```
     - Resampling da série para agregações anuais e mensais:
       ```python
       ts_ano = ts.resample('YE').sum()  # Resample por ano
       ts_mes = ts.groupby([lambda x: x.month]).sum()  # Resample por mês
       ```

   - **Exemplo de Indexação por Data:**
     - Indexação de datas específicas, como:
       ```python
       ts['1949-02']  # Acesso por data específica
       ts[datetime(1949, 2, 1)]  # Acesso por objeto datetime
       ts['1950-01-01':'1950-07-31']  # Intervalo de datas
       ```

---

### 2. **Decomposição de Séries Temporais**
   - **Objetivo da Decomposição:**
     - Decompor a série em componentes: tendência, sazonalidade e resíduos.
     - Utilizando a função `seasonal_decompose` do `statsmodels`:
       ```python
       decomposicao = seasonal_decompose(ts)
       ```

   - **Analisando Componentes:**
     - **Tendência**:
       ```python
       decomposicao.trend.plot()  # Gráfico da tendência
       ```
     - **Sazonalidade**:
       ```python
       decomposicao.seasonal.plot()  # Gráfico da sazonalidade
       ```
     - **Resíduos**:
       ```python
       decomposicao.resid.plot()  # Gráfico dos resíduos
       ```
     - A decomposição pode ser visualizada totalmente com:
       ```python
       decomposicao.plot()
       ```

---

### 3. **Modelagem e Previsão com ARIMA**
   - **Configuração do Modelo ARIMA:**
     - Utilizando o `auto_arima` da biblioteca `pmdarima` para selecionar os melhores parâmetros do modelo ARIMA:
       ```python
       modelo = auto_arima(df, start_p=1, start_q=1, start_d=0, max_p=6, max_q=6, m=12, seasonal=True, trace=True)
       ```
     - **Parâmetros do Modelo ARIMA:**
       - `p`: Número de termos autoregressivos.
       - `q`: Número de termos de média móvel.
       - `d`: Número de diferenciações necessárias para tornar a série estacionária.
       - `m`: Número de períodos sazonais.

   - **Ajuste e Avaliação do Modelo:**
     - O modelo é treinado com um conjunto de dados de treino (1949 a 1959) e avaliado com um conjunto de dados de teste (1960 em diante):
       ```python
       train = df.loc['1949-01-01':'1959-12-01']
       test = df.loc['1960-01-01':]
       modelo.fit(train)
       ```

   - **Previsão com ARIMA:**
     - O modelo ARIMA é utilizado para prever os próximos 12 períodos (12 meses):
       ```python
       previsao = modelo.predict(n_periods=12)
       ```
     - A previsão é então comparada com os dados reais, através da visualização combinada:
       ```python
       pd.concat([test, pd.DataFrame(previsao, index=test.index, columns=["#Passengers"])], axis=1).plot()
       ```

---

### **Resumo dos Conceitos Principais:**

1. **Séries Temporais**:
   - São sequências de dados indexados por tempo.
   - Análises como decomposição e modelagem são essenciais para identificar tendências e padrões.

2. **Decomposição**:
   - Separação da série em componentes: tendência, sazonalidade e resíduos.
   - A decomposição ajuda a entender o comportamento da série e a identificar padrões sazonais.

3. **ARIMA (AutoRegressive Integrated Moving Average)**:
   - É um modelo estatístico para prever séries temporais.
   - A escolha dos parâmetros `p`, `d` e `q` é crucial para o sucesso do modelo.

---

### **Glossário:**
- **Série Temporal:** Dados organizados em função do tempo.
- **Decomposição:** Técnica para separar uma série temporal em componentes.
- **ARIMA:** Modelo que combina autoregressão, diferenciação e média móvel.
- **Auto_ARIMA:** Método automatizado para seleção dos parâmetros do modelo ARIMA.