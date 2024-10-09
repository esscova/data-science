**Relatório de Treinamento e Avaliação de Modelos**

**Introdução**

Este relatório apresenta os resultados do treinamento e avaliação de diferentes modelos de regressão para prever o custo médico de pacientes com base em suas características. Os modelos avaliados incluem Regressão Linear, Regressão Polinomial, Máquina de Vetores de Suporte (SVM), Árvore de Decisão, Random Forest, XGBoost, LightGBM e CatBoost.

**Resultados**

A tabela abaixo resume os resultados dos modelos avaliados:

| Modelo | MAE | MSE | RMSE | R2 Treino | R2 Teste | Validação Cruzada |
| --- | --- | --- | --- | --- | --- | --- |
| XGBoost | 2466.21 | 1.693235e+07 | 4114.89 | 0.861067 | 0.893821 | 0.856133 |
| LightGBM | 2460.35 | 1.699737e+07 | 4122.79 | 0.859830 | 0.893413 | 0.856026 |
| CatBoost | 2449.54 | 1.723974e+07 | 4152.08 | 0.869618 | 0.891893 | 0.855981 |
| Random Forest | 2511.01 | 1.730047e+07 | 4159.38 | 0.863906 | 0.891512 | 0.854473 |
| Decision Tree | 2595.10 | 1.873372e+07 | 4328.25 | 0.853007 | 0.882525 | 0.847103 |
| SVM | 2458.99 | 1.940189e+07 | 4404.76 | 0.842574 | 0.878335 | 0.834984 |
| Polynomial Regression | 2855.52 | 2.002894e+07 | 4475.37 | 0.831184 | 0.874403 | 0.775705 |
| Linear Regression | 4013.69 | 3.331136e+07 | 5771.60 | 0.730684 | 0.791111 | 0.735995 |

**Conclusões**

* Os modelos XGBoost, LightGBM e CatBoost apresentaram os melhores resultados em termos de MAE, MSE e RMSE.
* O modelo XGBoost apresentou o melhor resultado em termos de R2 no teste, com um valor de 0.893821.
* O modelo CatBoost apresentou o melhor resultado em termos de R2 no treino, com um valor de 0.869618.
* Os modelos Random Forest e Decision Tree apresentaram resultados razoáveis, mas inferiores aos modelos XGBoost, LightGBM e CatBoost.
* O modelo SVM apresentou um resultado inferior aos modelos XGBoost, LightGBM e CatBoost, mas superior ao modelo Linear Regression.
* O modelo Linear Regression apresentou o pior resultado em termos de MAE, MSE e RMSE.
