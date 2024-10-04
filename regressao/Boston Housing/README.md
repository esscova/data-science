## Regressão para Predição de Preços de Imóveis**

### **Descrição do Projeto**
Este projeto tem como objetivo prever o valor médio dos imóveis com base em características socioeconômicas e estruturais, como o número de cômodos, a proporção de população de baixa renda, e a proporção de alunos por professor. Foram utilizados diversos modelos de regressão, desde métodos lineares até algoritmos mais avançados de **Machine Learning** como **XGBoost** e **CatBoost**.

O projeto inclui etapas de exploração de dados, análise de correlações, treinamento de modelos, validação cruzada e comparação de desempenho entre os diferentes algoritmos de regressão.

---

### **Estrutura do Repositório**

```bash
.
├── data/
│   ├── dependente.csv
│   ├── housing.csv
│   └── independente.csv
├── models/
│   └── regressor.pkl
├── notebooks/
│   ├── Boston housing - avaliaçao com statsmodel.ipynb
│   ├── Boston housing - EDA.ipynb
│   ├── Boston housing - regressao linear.ipynb
├── reports/
│   ├── Relatório - avaliaçao de regressao com statsmodel.md
│   ├── Relatório - EDA.md
│   ├── Relatório final.md
└── README.md

```

---

### **Tecnologias Utilizadas**

- **Python 3.x**
- **Bibliotecas**:
  - `pandas` - Manipulação de dados
  - `numpy` - Operações numéricas
  - `matplotlib` e `seaborn` - Visualização de dados
  - `scikit-learn` - Modelos de regressão e validação
  - `XGBoost`, `LightGBM`, `CatBoost` - Modelos avançados de Gradient Boosting
  - `statsmodels` - Análise de modelos estatísticos
  - `pickle` - Salvamento do modelo treinado
  
---

### **Instalação**

1. Clone este repositório para a sua máquina local:
    ```bash
    git clone https://github.com/esscova/data-science.git
    ```

2. Crie um ambiente virtual e ative-o:
    ```bash
    python -m venv env
    source env/bin/activate  # Linux/MacOS
    .\env\Scripts\activate  # Windows
    ```

3. Instale as dependências necessárias.

---

### **Uso do Projeto**

1. **Exploração e Análise de Dados**:
   Acesse o notebook `notebooks/Boston housing - EDA.ipynb` para explorar e visualizar os dados brutos. Ele contém gráficos de dispersão, histogramas e análises estatísticas iniciais dos dados.

2. **Treinamento dos Modelos**:
   Utilize o notebook `notebooks/Boston housing - regressao linear.ipynb` para treinar diferentes modelos de regressão, como Regressão Linear, Regressão Polinomial, SVR, Random Forest, XGBoost, e outros. Ele também inclui as métricas de avaliação como **MAE**, **MSE**, e **R²**.

3. **Previsão com o Modelo Treinado**:
   O modelo final, um **Random Forest Regressor**, está salvo no arquivo `models/regressor.pkl`. Você pode carregar o modelo para fazer previsões com novos dados da seguinte forma:
   
   ```python
   import pickle
   import numpy as np

   # Carregar o modelo treinado
   with open('models/regressor.pkl', 'rb') as f:
       model = pickle.load(f)

   # Prever o valor de uma nova amostra
   nova_amostra = np.array([[8, 12, 18]])  # Exemplo: [RM, LSTAT, PTRATIO]
   previsao = model.predict(nova_amostra)
   print(f'Valor previsto: {previsao}')
   ```

---

### **Relatórios**
Todos os notebooks forum documentados através de seus relatórios, você pode conferir aqui:
- [Relatório da análise exploratória de dados](/reports/Relatório - EDA.md)
- [Relatório da avaliação dos modelos de regressão simples e múltipas com StatsModel](/reports/Relatório - avaliação de regressao com statsmodel.md)
- [Relatório do com as métricas dos algoritmos treinados e conclusão do projeto](/reports/Relatório final.md)


### **Conclusão**

Este projeto comparou e avaliou diferentes modelos de regressão para prever o valor dos imóveis, com destaque para os modelos **XGBoost** e **Random Forest**, que apresentaram os melhores resultados. O modelo treinado pode ser utilizado para fazer previsões em novos conjuntos de dados relacionados ao mercado imobiliário.

---


### **Contato**

Caso tenha alguma dúvida ou sugestão, entre em contato:

- **Email**: wsantos08@hotmail.com
- **LinkedIn**: [LinkedIn](https://www.linkedin.com/in/wellington-moreira-santos)

---