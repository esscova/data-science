# Mall Customers Clustering Analysis
<p align='center'>
    <img src='https://www.negocioefranquia.com/wp-content/uploads/2018/01/mall-em-shopping.jpg'/>
</p>
Este projeto realiza a análise e segmentação de clientes de um shopping com base no comportamento de gastos e dados demográficos. O objetivo é identificar grupos de clientes similares para auxiliar em campanhas de marketing direcionadas e outras decisões comerciais.

## Estrutura do Projeto
A estrutura do projeto está organizada em diretórios para dados, notebooks de análise e relatórios finais:

```plaintext
.
├── data
│   ├── clean.csv               # Dados processados, prontos para modelagem
│   └── Mall_Customers.csv       # Dataset original
├── notebooks
│   ├── eda.ipynb                # Notebook de Análise Exploratória dos Dados (EDA)
│   └── models.ipynb             # Notebook de Modelagem e Agrupamento (Clustering)
└── reports
    ├── report_eda.md            # Relatório detalhado da EDA
    └── report_models.md         # Relatório detalhado dos modelos de agrupamento
```

## Conteúdo do Projeto

### 1. Dados
- **Mall_Customers.csv**: Arquivo original com informações de clientes, incluindo `CustomerID`, `Genre`, `Age`, `Annual Income (k$)` e `Spending Score (1-100)`.
- **clean.csv**: Dados processados após a EDA, com as colunas renomeadas e `CustomerID` removido, pronto para aplicação dos modelos de clustering.

### 2. Análise Exploratória de Dados (EDA)
O notebook `eda.ipynb` realiza a análise inicial dos dados, incluindo:
- Carregamento e inspeção dos dados
- Análise de valores nulos, duplicados e outliers
- Transformações nas variáveis para padronização, como conversão de gêneros e renomeação de colunas
- Visualizações de distribuições e análise de correlações

O relatório da EDA pode ser encontrado em `reports/report_eda.md`.

### 3. Modelagem de Agrupamento (Clustering)
O notebook `models.ipynb` contém a aplicação de diferentes técnicas de agrupamento nos dados:
- **K-Means**: Utilizado em dados normalizados e não normalizados, com diferentes números de clusters e análise do método `Elbow`.
- **Hierarchical Clustering**: Aplicado para avaliar a estrutura hierárquica dos dados, com visualização de dendrograma.
- **DBSCAN**: Algoritmo baseado em densidade, útil para identificar clusters de forma arbitrária e detectar pontos ruidosos.
- **MeanShift**: Algoritmo de agrupamento que detecta automaticamente o número de clusters ideal.

O relatório dos modelos está disponível em `reports/report_models.md`.

## Pré-requisitos
Para rodar este projeto, as seguintes bibliotecas são necessárias:
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `scipy`

## Resultados e Conclusão
Os modelos de clustering identificaram diferentes perfis de clientes. A segmentação resultante pode ser utilizada para personalizar campanhas de marketing e desenvolver estratégias comerciais mais eficazes.

## Referências
- Documentação do [scikit-learn](https://scikit-learn.org/stable/)
- Tutoriais de clustering com Python e análise exploratória com `pandas` e `seaborn`
- Curso Udemy : [Machine Learning com Python](https://www.udemy.com/course/machine-learning-com-python/)
---

**Autor:** Wellington Moreira | [LinkedIn](https://www.linkedin.com/in/wellington-moreira-santos/)  
**Licença:** MIT
```