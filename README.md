# Data Science Learning Repository
Este repositório armazena meus estudos, experimentos e implementações de técnicas e algoritmos na área de Data Science. Cada projeto explora conceitos fundamentais de Machine Learning, organizados por técnicas como classificação, regressão e agrupamento, com notebooks, scripts e relatórios documentando o processo de aprendizado.
<p align='center'>
	<img src='https://revistamarina.cl/storage/app/media/uploaded-files/figura-1-2.jpg' width=800/>
</p>


## Estrutura do Repositório

Abaixo está a estrutura geral do repositório, organizada em categorias que representam os diferentes temas de aprendizado:

```plaintext
.
├── association_rules                 # Regras de associação e análise de padrões frequentes
├── classification                    # Projetos de classificação de dados
│   ...
├── clustering                        # Agrupamento e segmentação de dados
│   ...
├── datasets                          # Conjunto de dados utilizados nos projetos
├── neural_networks                   # Implementações de redes neurais
│   ├── classification                # Redes neurais para classificação
│   └── regression                    # Redes neurais para regressão
├── regression                        # Projetos de regressão
│   ...
├── shared_utils                      # Funções e utilidades compartilhadas
├── study_materials                   # Material de estudo 
├── time_series                       # Projetos de séries temporais
├── probabilistic                     # Projetos com modelagem probabilística
└── LICENSE                           # Licença do repositório
```

---

## Projetos

### Classificação
- [Classificação de Qualidade de Veículos](./classification/vehicle_classifier/)  
  Este projeto apresenta uma aplicação de classificação de veículos, desenvolvida com Streamlit e utilizando o modelo de classificação Naive Bayes categórico. O objetivo é prever a categoria de um veículo com base em características fornecidas, explorando técnicas de pré-processamento e avaliação de modelos de machine learning.

- [Classificador de Insuficiência Cardíaca](./classification/heart_failure/)  
  Mas e o coração? tá bem? ou só lembra dele nas sofrências? Este projeto é um sistema de machine learning para prever a possibilidade de insuficiência cardíaca com base em apenas 11 características de um conjunto de dados real. Com um modelo preditivo preciso, é possível detectar e tratar esses casos de forma precoce, potencialmente salvando vidas.

- [Classificador para Câncer de Mama](./classification/breast_cancer/)  
  O câncer de mama é uma das principais causas de morte entre mulheres em todo o mundo. Com este projeto, exploramos como a ciência de dados pode revolucionar o diagnóstico, usando dados e modelos para a detecção precoce e o diagnóstico correto de câncer de mama.

### Regressão
- [Previsão de Custo Inicial para Abertura de Franquia](./regression/franquia/)  
  Este projeto mostra na prática como o Streamlit pode ser usado para criar uma aplicação interativa de ciência de dados. Utilizando um modelo de Regressão Linear, a aplicação prevê o custo inicial de abrir uma franquia, levando em conta fatores como a frequência anual de operação.

- [Preditor para Preço de Imóveis](./regression/boston_housing/)  
  Neste projeto, aplicamos técnicas de aprendizado de máquina para prever o valor médio de imóveis com base em características socioeconômicas e estruturais, como o número de cômodos e a proporção de alunos por professor. Uma aplicação útil para decisões imobiliárias informadas.

- [Previsão de Custos Médicos](./regression/medical_cost/)  
  Este projeto visa prever os custos médicos, comparando diversos algoritmos e apresentando resultados detalhados em relatórios. A estrutura do projeto é organizada para facilitar a reprodução e análise dos resultados.

### Agrupamento
- [Segmentação de Grupos de Clientes](./clustering/mall_customers/)  
  Para otimizar estratégias de marketing e decisões comerciais, este projeto analisa os hábitos de compra e características demográficas dos clientes de um shopping. O objetivo é criar perfis de clientes com comportamentos semelhantes, permitindo campanhas de marketing personalizadas e ações mais eficazes.

### Regras de assossiação
- [Sistema de recomendação](./association_rules/sistema_recomendacoes/)  
  Este projeto apresenta uma aplicação para geração de regras de recomendação, desenvolvida com Streamlite utilizando o algoritmo Apriori para encontrar padrões em transações. O objetivo é permitir ao usuário carregar um conjunto de transações e, a partir disso, gerar e visualizar regras de associação.
- [Padrões de compra dos consumidores de um supermercado](./association_rules/grocieres/)  
  Este projeto aplica o algoritmo Apriori para analisar padrões de compra em um dataset de transações de um supermercado (Groceries). O objetivo é descobrir quais produtos são frequentemente comprados juntos, fornecendo insights para melhorar estratégias de vendas, otimizar o layout do estabelecimento e personalizar ofertas para os clientes, levando a uma experiência de compra mais eficiente e satisfatória.

### Séries temporais
- [Previsão de vendas de leite com séries temporais](./time_series/milk_sales/)  
  Este projeto desenvolve uma aplicação de previsão de vendas de leite utilizando Streamlit e o modelo de séries temporais SARIMA. A aplicação permite que os usuários carreguem uma série temporal de dados históricos de vendas e, com base nessa informação, realizem previsões precisas para períodos futuros. Além disso, a aplicação fornece uma visão detalhada da decomposição e da projeção das vendas, permitindo que os usuários tomem decisões informadas sobre suas estratégias de negócios.

### Modelagem probabilística
- [Probabilidade de falhas em equipamentos](./probabilistic/failure_probabilities/)  
  Explore a distribuição de falhas em equipamentos com Streamlit através da modelagem de Poisson, neste projeto é possível calcular probabilidades exatas, acumuladas e complementares, fornecendo insights valiosos sobre a confiabilidade do sistema. O projeto integra bibliotecas como NumPy, Matplotlib e SciPy para garantir precisão e eficiência nos cálculos.

---

## Conteúdos Adicionais

- **datasets/**: Armazena datasets utilizados em múltiplos projetos.
- **shared_utils/**: Funções e scripts auxiliares usados em diferentes projetos.
- **study_materials/**: Materiais de estudo sobre algoritmos específicos e técnicas avançadas de machine learning.

