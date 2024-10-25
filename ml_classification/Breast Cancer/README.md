# Ciência de Dados e o Câncer de Mama
<p align='center'>
<img src='https://www.healthxchange.sg/sites/hexassets/Assets/women/breast-cancer-surgery-surgical-drains-exercises.jpg'>
</p>

Você sabia que o câncer de mama é uma das principais causas de morte entre as mulheres em todo o mundo? No entanto, com a detecção precoce e o diagnóstico correto, é possível salvar vidas. Nesse sentido, apresentamos um projeto inovador que combina ciência de dados e aprendizado de máquina para melhorar a precisão do diagnóstico do câncer de mama.

## O Desafio

Neste projeto de ciência de dados se concentra no conjunto de dados de câncer de mama Wisconsin (Diagnóstico), que contém informações sobre características de imagens digitalizadas de aspirações por agulha fina (FNA) de massas mamárias. O objetivo deste estudo é desenvolver modelos de aprendizado de máquina capazes de classificar corretamente se uma massa mamária é benigna ou maligna com base nessas características.

O conjunto de dados inclui 569 amostras, das quais 357 são benignas e 212 são malignas. Para cada amostra, há 30 recursos computados a partir das imagens, incluindo medidas de raio, textura, perímetro, área, suavidade, compactação, concavidade, simetria e dimensão fractal. Esses recursos capturam diferentes aspectos da morfologia das células tumorais, que podem ser usados para diferenciar tumores benignos de malignos.

O desafio deste projeto é construir modelos preditivos robustos que possam realizar essa classificação com alta precisão. Isso envolverá explorar diferentes algoritmos de aprendizado de máquina, como regressão logística, árvores de decisão, florestas aleatórias entre outros, e avaliar seu desempenho usando métricas como acurácia, precisão, revocação e F1-score.

Além disso, será importante entender quais recursos são os mais informativos para a classificação, a fim de obter insights sobre os mecanismos biológicos subjacentes ao câncer de mama. Isso pode ajudar a orientar futuras pesquisas nessa área.

No geral, este projeto visa contribuir para o avanço da detecção precoce e do diagnóstico do câncer de mama, uma questão de saúde pública crucial. Os resultados deste estudo podem ter implicações importantes para a melhoria dos cuidados de saúde e do bem-estar dos pacientes.

## Conteúdo do respositório

```plaintext
.
├── data
│   ├── cancer_clean.csv
│   ├── cancer.csv
│   ├── modelo_logistica.pkl
│   ├── preds.csv
│   ├── preds_scaled.csv
│   ├── results.csv
│   └── target.csv
├── README.md
├── reports
│   ├── Relatorio - Exploração de dados.md
│   └── Relatório - Modelo final.md
└── src
    ├── Breast Cancer - Analise exploratoria.ipynb
    ├── Breast Cancer - Modelo final.ipynb
    └── Breast Cancer - pre-processamento e treinamento.ipynb

```
- `data` : diretório com datasets e modelo finalizado do projeto.
- `src` : notebooks utilizados para projeto.
- `reports` : relatórios das análises e insights.

## Relatórios
- [Exploração de dados](./reports/Relatorio%20-%20Exploração%20de%20dados.md) : Informações gerais do dataset, análises de atributos e insights.
- [Modelo escolhido para classificação](./reports/Relatório%20-%20Modelo%20final.md) : Avaliação final de modelos, após analisar métricas e aplicar otimização de hiperparametros para escolha de algoritmo e disponibilização de modelo para produção.