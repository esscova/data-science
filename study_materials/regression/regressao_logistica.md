


### Aplicação da Regressão Logística em R

#### Contexto do Estudo

Este script em R demonstra a aplicação da **regressão logística** para prever a situação de candidatos em uma eleição com base em seus gastos de campanha (variável `DESPESAS`). A variável dependente `SITUACAO` é binária, indicando se o candidato foi eleito (1) ou não (0).

#### Principais Etapas

1.  **Carregamento e Exploração dos Dados**
    
    -   O dataset `Eleicao.csv` é carregado para análise. Com o comando `summary`, observa-se as estatísticas descritivas das variáveis, e o comando `dim` exibe o tamanho do dataset.
    -   O gráfico inicial (scatter plot) de `DESPESAS` versus `SITUACAO` ajuda a visualizar a relação entre os gastos e o resultado eleitoral.
    -   A correlação é calculada para medir a intensidade da relação entre as variáveis.
2.  **Criação do Modelo de Regressão Logística**
    
    -   A regressão logística é ajustada com `glm` usando `DESPESAS` como preditor da variável dependente `SITUACAO`.
    -   O parâmetro `family='binomial'` especifica que o modelo segue uma distribuição binária (logística).
    -   O comando `summary` apresenta os coeficientes do modelo, mostrando a significância estatística da variável preditora.
3.  **Visualização e Ajuste do Modelo**
    
    -   O gráfico é atualizado para incluir os valores ajustados (fitted values), representados por pontos, indicando as probabilidades previstas pelo modelo para cada despesa.
4.  **Predição e Avaliação do Modelo**
    
    -   As probabilidades previstas para cada candidato são geradas com `predict`.
    -   Um limiar de 0,5 é usado para classificar as previsões como "eleito" (1) ou "não eleito" (0).
    -   A matriz de confusão (à partir do comando `table`) avalia o desempenho do modelo, comparando previsões e resultados reais.
    -   A acurácia é calculada como a proporção de previsões corretas no total.
5.  **Aplicação para Novos Candidatos**
    
    -   Um novo dataset (`NovosCandidatos.csv`) é carregado.
    -   As probabilidades previstas são geradas e classificadas com base no mesmo limiar de 0,5.
    -   O resultado indica a probabilidade de cada novo candidato ser eleito, auxiliando na tomada de decisões.

#### Conclusão

Este script exemplifica como usar a regressão logística em problemas de classificação binária. A abordagem é particularmente útil para prever resultados binários baseados em variáveis preditoras contínuas, como os gastos eleitorais. A matriz de confusão e a acurácia são ferramentas fundamentais para validar o desempenho do modelo antes de aplicá-lo em cenários reais.
