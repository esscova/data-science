
# Classificação de Veículos com Streamlit e Naive Bayes

Este projeto apresenta uma aplicação de classificação de veículos, desenvolvida com [Streamlit](https://streamlit.io/) e utilizando o modelo de classificação Naive Bayes categórico. O objetivo é prever a categoria de um veículo com base em características fornecidas, explorando técnicas de pré-processamento e avaliação de modelos de machine learning.

## Visão Geral

O script utiliza as bibliotecas `pandas`, `scikit-learn`, e `streamlit` para:
1. Carregar e pré-processar um conjunto de dados de veículos.
2. Treinar um modelo Naive Bayes categórico para a classificação.
3. Exibir a acurácia do modelo e fornecer uma interface interativa para que o usuário classifique novos veículos com base em características personalizadas.

## Como Executar o Projeto

Para executar a aplicação, é necessário ter Python instalado, junto com as bibliotecas requeridas. Siga os passos abaixo:

1. Clone este repositório.
2. Instale as dependências:
   ```bash
   pip install streamlit pandas scikit-learn
   ```
3. Execute a aplicação com o comando:
   ```bash
   streamlit run app.py
   ```

A aplicação estará disponível no navegador em `http://localhost:8501`.

## Estrutura do Código

### Carregamento de Dados e Treinamento do Modelo

- **Função `load_data_and_model()`**: Esta função realiza o carregamento e pré-processamento dos dados e executa o treinamento do modelo. Ela executa os seguintes passos:
  - Carrega o dataset `car.csv`, que contém colunas com características categóricas de veículos e a coluna `class` como o rótulo de classificação.
  - Codifica os dados categóricos usando `OrdinalEncoder`, convertendo-os para uma representação numérica.
  - Separa os dados em conjuntos de treinamento e teste.
  - Treina um modelo de Naive Bayes categórico (`CategoricalNB`) e avalia sua acurácia no conjunto de teste.
- **Retorna** o encoder, o modelo treinado, a acurácia do modelo, e o dataframe original carregado.

### Interface e Funcionalidades

1. **Exibição da Acurácia**: Apresenta a acurácia do modelo na página principal, oferecendo ao usuário uma ideia da eficácia do modelo.
2. **Entrada do Usuário**: Permite que o usuário selecione características para um veículo a ser classificado por meio de menus suspensos.
3. **Classificação**: Após a seleção das características e o clique no botão "Classificar", o modelo prevê a classe do veículo, que é então exibida na interface.

## Dataset

O conjunto de dados `car.csv` inclui colunas com características categóricas de veículos e uma coluna de `class` para as categorias de classificação de veículos, por exemplo:

```
buying, maint, doors, persons, lug_boot, safety, class
vhigh, med, 2, 4, big, high, unacc
high, low, 3, more, med, med, acc
...
```

## Tecnologias e Bibliotecas Utilizadas

- **[Streamlit](https://streamlit.io/)**: Framework para criar aplicações web interativas em Python.
- **[Pandas](https://pandas.pydata.org/)**: Manipulação e análise de dados.
- **[Scikit-Learn](https://scikit-learn.org/)**: Pré-processamento e treinamento do modelo Naive Bayes categórico.

## Referências

- Documentação do [Streamlit](https://docs.streamlit.io/).
- Documentação do [Scikit-Learn](https://scikit-learn.org/stable/documentation.html).
- Documentação do [Pandas](https://pandas.pydata.org/docs/).
- Curso Udemy [Streamlit: Crie aplicações web de inteligência artificial](https://www.udemy.com/course/streamlit-aplicacoes-web-de-ia).