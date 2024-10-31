# Previsão de Custo para Franquia com Streamlit

Este projeto demonstra o uso de [Streamlit](https://streamlit.io/) para construir uma aplicação interativa de ciência de dados. O objetivo da aplicação é prever o custo inicial de uma franquia com base na frequência anual de operação, utilizando um modelo de Regressão Linear.

<p align='center'>
    <img src='https://franquiademarketingdigital.com.br/images/blog/quanto-custa-uma-franquia.jpg' width=800>
</p>

## Visão Geral

O script utiliza as bibliotecas `pandas`, `scikit-learn`, `matplotlib` e `streamlit` para:
1. Ler e exibir os dados de um arquivo CSV contendo informações de frequência anual e custo inicial de franquias.
2. Treinar um modelo de Regressão Linear para prever o custo inicial da franquia com base na frequência anual.
3. Apresentar visualmente os dados e a linha de regressão do modelo.
4. Permitir que o usuário insira novos valores de frequência anual e visualize uma previsão personalizada do custo inicial.

## Como Executar o Projeto

Para executar a aplicação, você precisará de Python instalado, juntamente com as bibliotecas necessárias. Siga os passos abaixo:

1. Clone este repositório.
2. Instale as dependências:
   ```bash
   pip install streamlit pandas scikit-learn matplotlib
   ```
3. Execute a aplicação com o comando:
   ```bash
   streamlit run app.py
   ```

A aplicação estará disponível no navegador em `http://localhost:8501`.

## Estrutura do Código

- **Carregamento de Dados**: Carrega os dados do arquivo `data.csv`, que contém as colunas:
  - `FrqAnual`: Frequência anual da franquia.
  - `CusInic`: Custo inicial da franquia.

- **Treinamento do Modelo**: Utiliza Regressão Linear para ajustar um modelo de previsão do custo inicial com base na frequência anual (`FrqAnual`).

- **Visualização e Interação**: 
  - Exibe os dados carregados e os resultados do modelo treinado.
  - Fornece uma interface para o usuário inserir um novo valor de frequência anual e obter uma previsão interativa.

## Funcionalidades da Aplicação

### 1. Exibição de Dados
A aplicação exibe as primeiras 10 entradas dos dados, permitindo que o usuário observe rapidamente o conjunto de dados utilizado para o treinamento do modelo.

### 2. Modelo de Regressão Linear
Visualização gráfica dos dados e da linha de regressão do modelo, proporcionando insights sobre o ajuste do modelo e a relação entre a frequência anual e o custo inicial.

### 3. Previsão Interativa
O usuário pode inserir um novo valor de frequência anual e clicar em "Processar" para obter a previsão do custo inicial.

## Exemplo de Uso

1. Insira um valor de frequência anual no campo fornecido.
2. Clique em "Processar" para ver o custo inicial previsto para a franquia.

## Dataset

O conjunto de dados `data.csv` inclui informações de frequência anual e custo inicial de franquias:

```
FrqAnual;CusInic
1000;1050
1125;1150
1087;1213
...
```

## Tecnologias e Bibliotecas Utilizadas

- **[Streamlit](https://streamlit.io/)**: Framework para criar aplicações web interativas em Python.
- **[Pandas](https://pandas.pydata.org/)**: Manipulação e análise de dados.
- **[scikit-learn](https://scikit-learn.org/)**: Treinamento do modelo de Regressão Linear.
- **[Matplotlib](https://matplotlib.org/)**: Visualização de dados e gráficos.

## Referências

- Documentação do [Streamlit](https://docs.streamlit.io/).
- Documentação do [Scikit-Learn](https://scikit-learn.org/stable/documentation.html).
- Documentação do [Pandas](https://pandas.pydata.org/docs/).
- Curso Udemy [Streamlit: Crie aplicações web de inteligência artificial](https://www.udemy.com/course/streamlit-aplicacoes-web-de-ia).


