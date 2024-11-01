# Previsão de Vendas de Leite com Streamlit e Séries Temporais

Este projeto apresenta uma aplicação de previsão de vendas de leite, desenvolvida com [Streamlit](https://streamlit.io/) e utilizando o modelo de séries temporais SARIMA. O objetivo é permitir ao usuário carregar uma série temporal de dados históricos de vendas e, a partir disso, realizar previsões para períodos futuros, visualizando a decomposição e a projeção das vendas.

## Visão Geral

O script utiliza as bibliotecas `pandas`, `statsmodels`, `matplotlib`, e `streamlit` para:
1. Carregar e manipular dados de vendas a partir de um arquivo `.csv`.
2. Decompor a série temporal para visualizar componentes de tendência, sazonalidade e ruído.
3. Treinar um modelo de séries temporais SARIMA e fazer previsões para meses futuros, exibindo os resultados de maneira interativa e visual.

## Como Executar o Projeto

Para executar a aplicação, é necessário ter Python instalado, junto com as bibliotecas requeridas. Siga os passos abaixo:

1. Clone este repositório.
2. Instale as dependências:
   ```bash
   pip install streamlit pandas statsmodels matplotlib
   ```
3. Execute a aplicação com o comando:
   ```bash
   streamlit run app.py
   ```

A aplicação estará disponível no navegador em `http://localhost:8501`.

## Estrutura do Código

### Carregamento de Dados e Preparação da Série Temporal

- **Upload de Arquivo**: O usuário carrega um arquivo `.csv` que contém valores mensais de vendas de leite.
- **Configuração de Período e Previsão**: O usuário define a data inicial da série e o número de meses a prever (1 a 48).
  
### Decomposição e Previsão da Série Temporal

- **Função de Decomposição**: A aplicação usa `seasonal_decompose` para decompor a série em componentes de tendência, sazonalidade e ruído, facilitando a análise da série.
- **Modelo SARIMA**: Para realizar a previsão, o modelo SARIMA é ajustado aos dados carregados, com parâmetros para capturar a sazonalidade anual. Em seguida, a aplicação realiza a previsão para o número de meses escolhido.

### Interface e Funcionalidades

1. **Visualização da Decomposição**: A decomposição é exibida em gráficos que detalham a tendência e a sazonalidade dos dados históricos.
2. **Visualização da Previsão**: A previsão gerada é sobreposta ao gráfico dos dados históricos, permitindo que o usuário visualize a série temporal completa com a projeção.
3. **Exibição dos Dados Previstos**: Os valores previstos também são apresentados em uma tabela, facilitando a consulta aos dados.

## Dataset

O arquivo `data.csv` esperado deve conter uma única coluna com valores mensais das vendas de leite, como no exemplo abaixo:

```plaintext
589
561
640
656
727
697
640
599
568
577
553
...
```

## Tecnologias e Bibliotecas Utilizadas

- **[Streamlit](https://streamlit.io/)**: Framework para criar aplicações web interativas em Python.
- **[Pandas](https://pandas.pydata.org/)**: Manipulação e análise de dados.
- **[Statsmodels](https://www.statsmodels.org/)**: Modelagem estatística e séries temporais (SARIMA).
- **[Matplotlib](https://matplotlib.org/)**: Visualização gráfica dos dados e das previsões.

## Referências

- Documentação do [Streamlit](https://docs.streamlit.io/).
- Documentação do [Statsmodels](https://www.statsmodels.org/stable/index.html).
- Documentação do [Pandas](https://pandas.pydata.org/docs/).
- Documentação do [Matplotlib](https://matplotlib.org/stable/contents.html).
- Curso Udemy [Streamlit: Crie aplicações web de inteligência artificial](https://www.udemy.com/course/streamlit-aplicacoes-web-de-ia).

