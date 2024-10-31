# Redes Neurais para Regressão com o Dataset Boston Housing

## Introdução ao Problema de Regressão

A tarefa de **regressão** é um método de aprendizado supervisionado focado na previsão de valores contínuos, sendo amplamente utilizado em cenários como precificação de imóveis, previsão de demanda e estimativas de vendas. Diferente das tarefas de classificação, em que se categorizam dados em classes, a regressão lida com uma variável dependente contínua, onde o objetivo é minimizar o erro entre as previsões do modelo e os valores reais. Neste projeto, utilizamos redes neurais para modelar um problema de regressão com o dataset **Boston Housing**, que visa estimar o valor médio das residências em diversas áreas da cidade de Boston.

<p align='center'>
    <img src='https://upload.wikimedia.org/wikipedia/commons/3/3d/Neural_network.svg' alt="neural network">
</p>

### Dataset Utilizado: Boston Housing

O dataset **Boston Housing** é um conjunto de dados clássico para estudos de regressão, contendo 506 amostras de áreas residenciais de Boston e 13 características relacionadas, como proporção de área comercial, índice de criminalidade e qualidade das escolas locais. O objetivo é prever a variável `MEDV` (Valor Médio das Casas), em milhares de dólares, com base nas características fornecidas. Este conjunto de dados é utilizado para testar a capacidade de algoritmos de regressão em capturar padrões relevantes nas variáveis e gerar previsões precisas.

### Arquitetura da Rede Neural

Para modelar o problema de regressão, construímos uma rede neural do tipo **MLPRegressor** (Multi-Layer Perceptron Regressor), com a seguinte configuração:
- **Camadas Ocultas**: 2 camadas com 6 neurônios cada.
- **Função de Ativação**: Função `relu`, que possibilita a modelagem de relações não lineares.
- **Algoritmo de Otimização**: `lbfgs`, um solver adequado para conjuntos de dados menores.
- **Iterações Máximas**: Ajustado para 1500 para melhorar a convergência.

O modelo foi treinado utilizando os dados no formato bruto e, posteriormente, com dados normalizados para verificar a diferença de performance entre as abordagens.

### Normalização dos Dados

A **normalização** das características é uma etapa essencial para o treinamento de redes neurais, pois garante que todos os dados estejam em uma escala comparável, o que facilita o aprendizado. Para tanto, aplicamos o **StandardScaler** para padronizar as variáveis independentes (`X`) e dependentes (`y`), resultando em dados com média zero e desvio padrão igual a um.

### Avaliação do Modelo

Para avaliar o desempenho do modelo, utilizamos as seguintes métricas:

1. **Mean Absolute Error (MAE)**: Mede o erro médio absoluto entre as previsões e os valores reais, fornecendo uma medida direta do erro médio.

2. **Mean Squared Error (MSE)**: Calcula a média dos erros quadráticos, penalizando grandes desvios e sendo sensível a outliers.

3. **Root Mean Squared Error (RMSE)**: A raiz quadrada do MSE, facilitando a interpretação em relação às unidades originais do target (`MEDV`).

Essas métricas foram calculadas tanto para os dados normalizados quanto para os não normalizados, permitindo uma comparação direta entre as duas abordagens e possibilitando ajustes no modelo com base nos resultados.

### Validação Cruzada

Implementamos a **validação cruzada com k-folds** para avaliar a robustez do modelo e sua capacidade de generalização. No caso dos dados normalizados, utilizamos uma **pipeline** para garantir que a normalização fosse aplicada em cada iteração de forma isolada, evitando vazamento de dados. O `KFold` foi configurado com 12 divisões para uma avaliação mais robusta dos resultados.

### Resultados

Os resultados finais das métricas para os dados normalizados e não normalizados foram os seguintes:

#### Dados Não Normalizados
- **MAE**: 50729.93
- **MSE**: 4052914666.86
- **RMSE**: 63662.51

#### Dados Normalizados
- **MAE**: 48254.22
- **MSE**: 3805143098.62
- **RMSE**: 61685.84

Em considerações finais, a análise indica que o modelo apresentou uma leve melhora ao usar os dados brutos em relação à normalização, sugerindo que o ajuste do modelo ainda pode ser aprimorado com outros métodos de regularização ou otimização.