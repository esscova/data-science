## **Relatório Final: Avaliação de Modelos de Regressão para Predição de Preços de Imóveis**

**Autor**: Wellington Moreira - Cientista de Dados  
**Contatos**: wsantos08@hotmail.com | [Linkedin](https://www.linkedin.com/in/wellington-moreira-santos/)

---

### **Introdução**

#### **Descrição do Problema**
O valor de um imóvel é influenciado por diversos fatores, como o número de cômodos, a composição socioeconômica da região e a infraestrutura educacional. O objetivo deste projeto foi desenvolver e avaliar diferentes modelos de regressão para prever o valor médio dos imóveis (`MEDV`) com base em características relevantes, incluindo o número médio de cômodos (`RM`), a proporção de população de baixa renda (`LSTAT`), e a razão entre alunos e professores nas escolas (`PTRATIO`).

#### **Objetivo**
O objetivo principal foi identificar o modelo de regressão que melhor prediz o valor médio dos imóveis, com base em métricas como o **coeficiente de determinação R²**, **MAE** (erro absoluto médio), **MSE** (erro quadrático médio), e **RMSE** (raiz do erro quadrático médio).

---

### **Descrição dos Dados**

O dataset contém 489 registros e 4 variáveis:

| Variável  | Descrição                                                    |
|-----------|--------------------------------------------------------------|
| `RM`      | Número médio de cômodos por casa                              |
| `LSTAT`   | Percentual de proprietários de classe baixa                   |
| `PTRATIO` | Proporção de alunos por professor                             |
| `MEDV`    | Valor médio das casas (variável dependente)                   |

---

### **Modelos Avaliados**

Vários modelos de regressão foram testados para prever o valor médio das casas. Abaixo estão os resultados de cada modelo, juntamente com as métricas de avaliação. Os modelos variam de simples regressões lineares até algoritmos mais avançados, como **XGBoost** e **CatBoost**.

#### **Modelos de Regressão Simples**

1. **Regressão Linear (RM)**
   - **R² (Treino)**: 46.36%
   - **R² (Teste)**: 54.26%
   - **MAE**: 76,063.99
   - **MSE**: 11,294,624,525.74
   - **RMSE**: 106,276.17

   A regressão linear com o número médio de cômodos (`RM`) apresentou um desempenho modesto, com um **R²** de 54.26%, indicando que 54.26% da variabilidade no preço dos imóveis pode ser explicada pela quantidade de cômodos.

2. **Regressão Linear (LSTAT)**
   - **R² (Treino)**: 56.88%
   - **R² (Teste)**: 60.06%
   - **MAE**: 76,340.55
   - **MSE**: 9,863,567,949.63
   - **RMSE**: 99,315.49

   A regressão linear com a variável `LSTAT` (percentual de classe baixa) teve um desempenho ligeiramente melhor, com um **R²** de 60.06% e erros absolutos e quadráticos menores.

#### **Modelos de Regressão Avançada**

1. **Regressão Múltipla**
   - **R² (Treino)**: 73.23%
   - **R² (Teste)**: 67.83%
   - **MAE**: 59,294.98
   - **MSE**: 6,124,867,841.06
   - **RMSE**: 78,261.53

   A regressão múltipla, que incorpora todas as variáveis preditivas (`RM`, `LSTAT`, `PTRATIO`), apresentou um desempenho significativamente melhor, com um **R²** de 67.83%, sugerindo uma boa capacidade de predição quando múltiplas variáveis são consideradas.

2. **Regressão Polinomial**
   - **R² (Treino)**: 64.66%
   - **R² (Teste)**: 59.96%
   - **MAE**: 76,354.62
   - **MSE**: 10,537,450,723.94
   - **RMSE**: 102,652.08

   Embora a regressão polinomial capture alguma não linearidade nos dados, o desempenho ainda ficou aquém da regressão múltipla.

---

### **Modelos Baseados em Árvores de Decisão e Ensemble**

1. **Decision Tree Regressor**
   - **R² (Treino)**: 90.50%
   - **R² (Teste)**: 82.56%
   - **MAE**: 52,954.00
   - **MSE**: 5,057,266,756.34
   - **RMSE**: 71,114.46

   O modelo de árvore de decisão apresentou um **R²** elevado nos dados de treino, mas uma ligeira queda no desempenho com os dados de teste, sugerindo um possível **overfitting**.

2. **Random Forest Regressor**
   - **R² (Treino)**: 91.60%
   - **R² (Teste)**: 84.65%
   - **MAE**: 49,730.29
   - **MSE**: 4,452,803,054.51
   - **RMSE**: 66,729.32

   O **Random Forest Regressor** apresentou um dos melhores desempenhos, com um **R²** de 84.65% e erros absolutos e quadráticos menores comparados ao modelo de árvore de decisão.

---

### **Modelos Baseados em Gradient Boosting**

1. **XGBoost**
   - **R² (Treino)**: 92.68%
   - **R² (Teste)**: 83.55%
   - **MAE**: 47,811.11
   - **MSE**: 4,061,975,473.18
   - **RMSE**: 63,733.62

   O **XGBoost** apresentou um desempenho excelente, com o melhor **R²** nos dados de treino e teste, além dos menores valores de **MAE** e **RMSE**.

2. **LightGBM**
   - **R² (Treino)**: 88.14%
   - **R² (Teste)**: 82.17%
   - **MAE**: 55,114.09
   - **MSE**: 5,170,544,146.43
   - **RMSE**: 71,906.49

   O **LightGBM** também apresentou bons resultados, embora com erros ligeiramente maiores comparados ao XGBoost.

3. **CatBoost**
   - **R² (Treino)**: 89.87%
   - **R² (Teste)**: 83.56%
   - **MAE**: 52,043.38
   - **MSE**: 4,768,365,379.01
   - **RMSE**: 69,053.35

   O **CatBoost** foi um dos modelos com melhor desempenho, com um **R²** elevado e métricas de erro competitivas.

---

### **Comparação de Desempenho dos Modelos**

| Modelo                    | R² (Treino) | R² (Teste) | MAE      | MSE            | RMSE      |
|---------------------------|-------------|------------|----------|----------------|-----------|
| Regressão Linear (RM)      | 46.36%      | 54.26%     | 76,063.99| 11,294,624,525.74 | 106,276.17 |
| Regressão Linear (LSTAT)   | 56.88%      | 60.06%     | 76,340.55| 9,863,567,949.63  | 99,315.49  |
| Regressão Múltipla         | 73.23%      | 67.83%     | 59,294.98| 6,124,867,841.06  | 78,261.53  |
| Regressão Polinomial       | 64.66%      | 59.96%     | 76,354.62| 10,537,450,723.94 | 102,652.08 |
| SVR                        | 86.18%      | 82.80%     | 48,813.74| 4,246,686,809.81  | 65,166.60  |
| Decision Tree              | 90.50%      | 82.56%     | 52,954.00| 5,057,266,756.34  | 71,114.46  |
| Random Forest              | 91.60%      | 84.65%     | 49,730.29| 4,452,803,054.51  | 66,729.32  |
| XGBoost                    | 92.68%      | 83.55%     | 47,811.11| 4,061,975,473.18  | 63,733.62  |
| LightGBM                   | 88.14%      | 82.17%     | 55,114.09| 5,170,544,146.43  | 71,906.49  |
| CatBoost                   | 89.87%      | 83.56%     | 52,043.38| 4,768,365,379.01  | 69,053.35  |

---

### **Conclusão**

Com base nas métricas de desempenho, os melhores modelos para a predição de preços de imóveis foram os baseados em **Random Forest**, com destaque para o **XGBoost**, que apresentou o melhor equilíbrio entre as métricas de erro (MAE, MSE, RMSE) e o **coeficiente de determinação R²**.

- O **Random Forest** é o modelo recomendado, pois apresentou o melhor desempenho, com um **R²** de 84.65% nos dados de teste e o menor **RMSE** de 66,729.32.
- Outros modelos como **CatBoost** e **XGBoost** também tiveram bons resultados, sendo alternativas viáveis dependendo do contexto e da necessidade de explicabilidade.

---

Se precisar de mais informações ou tiver perguntas, fique à vontade para entrar em contato!