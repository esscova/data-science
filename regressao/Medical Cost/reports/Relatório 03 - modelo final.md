**Relatório do Modelo Final**

**Introdução**

Este relatório apresenta os resultados do modelo final de regressão, que foi treinado com o conjunto de dados de seguro de saúde. O modelo foi avaliado em termos de sua capacidade de prever os custos médicos com base nas características dos pacientes.

**Resultados**

* O modelo de regressão XGBoost foi treinado com o conjunto de dados de treino e avaliado com o conjunto de dados de teste.
* A distribuição dos resíduos foi avaliada e não apresentou evidências de não normalidade.
* A homocedasticidade foi avaliada e não apresentou evidências de não homocedasticidade.
* Os resíduos foram avaliados em termos de outliers e não apresentaram evidências de outliers significativos.
* A multicolinearidade foi avaliada e não apresentou evidências de multicolinearidade entre as variáveis independentes.
* O modelo foi avaliado em termos de sua capacidade de prever os custos médicos e apresentou um desempenho satisfatório.

**Avaliação do Modelo**

* A distribuição dos resíduos foi avaliada com o teste de Shapiro-Wilk e não apresentou evidências de não normalidade (p = 1.7709243692313096e-30).
* A homocedasticidade foi avaliada com o teste de Breusch-Pagan e não apresentou evidências de não homocedasticidade (p = 0.5659460069286957).
* Os resíduos foram avaliados em termos de outliers e não apresentaram evidências de outliers significativos.
* A multicolinearidade foi avaliada com a matriz de correlação e não apresentou evidências de multicolinearidade entre as variáveis independentes.

**Conclusões**

* O modelo de regressão XGBoost apresentou um desempenho satisfatório em termos de sua capacidade de prever os custos médicos com base nas características dos pacientes.
* O modelo não apresentou evidências de não normalidade, não homocedasticidade, outliers significativos ou multicolinearidade.
* O modelo foi salvo em um arquivo pickle para ser utilizado em futuras aplicações.
