# Geração de Regras de Recomendação com Streamlit e Apriori

Este projeto apresenta uma aplicação para geração de regras de recomendação, desenvolvida com [Streamlit](https://streamlit.io/) e utilizando o algoritmo Apriori para encontrar padrões em transações. O objetivo é permitir ao usuário carregar um conjunto de transações e, a partir disso, gerar e visualizar regras de associação.

## Visão Geral

O script utiliza as bibliotecas `pandas`, `mlxtend`, `matplotlib` e `streamlit` para:
1. Carregar e manipular dados de transações a partir de um arquivo `.csv`.
2. Aplicar o algoritmo Apriori para encontrar conjuntos frequentes de itens.
3. Gerar e filtrar regras de associação baseadas em suporte, confiança e lift.
4. Visualizar os resultados de maneira interativa e visual.

## Como Executar o Projeto

Para executar a aplicação, é necessário ter Python instalado, junto com as bibliotecas requeridas. Siga os passos abaixo:

1. Clone este repositório.
2. Instale as dependências:
   ```bash
   pip install streamlit pandas mlxtend matplotlib
   ```
3. Execute a aplicação com o comando:
   ```bash
   streamlit run app.py
   ```

A aplicação estará disponível no navegador em `http://localhost:8501`.

## Estrutura do Código

### Carregamento de Dados e Preparação das Transações

- **Upload de Arquivo**: O usuário carrega um arquivo `.csv` que contém transações, com itens separados por vírgulas.
- **Configuração de Parâmetros**: O usuário define os valores mínimos de suporte, confiança, lift e tamanho dos conjuntos de itens a considerar.

### Geração e Visualização das Regras de Associação

- **Algoritmo Apriori**: O algoritmo Apriori é aplicado aos dados para encontrar conjuntos frequentes de itens.
- **Regras de Associação**: As regras de associação são geradas e filtradas com base nos parâmetros definidos pelo usuário.

### Interface e Funcionalidades

1. **Visualização das Transações**: As transações carregadas são exibidas em uma tabela.
2. **Visualização das Regras Encontradas**: As regras de associação geradas são exibidas em uma tabela.
3. **Visualização Gráfica**: Um gráfico de dispersão exibe a relação entre suporte, confiança e lift das regras geradas.
4. **Resumo das Regras**: Um resumo estatístico das regras geradas é apresentado.
5. **Exportação de Dados**: As regras geradas podem ser exportadas como um arquivo `.csv`.

## Dataset

O arquivo `.csv` esperado deve conter transações, com itens separados por vírgulas, como no exemplo abaixo:

```plaintext
Leite,Pão,Ovos
Pão,Manteiga
Cerveja,Frango
Leite,Cerveja,Pão
Ovos,Manteiga
...
```

## Tecnologias e Bibliotecas Utilizadas

- **[Streamlit](https://streamlit.io/)**: Framework para criar aplicações web interativas em Python.
- **[Pandas](https://pandas.pydata.org/)**: Manipulação e análise de dados.
- **[Mlxtend](http://rasbt.github.io/mlxtend/)**: Algoritmos de aprendizado de máquina e mineração de dados (Apriori).
- **[Matplotlib](https://matplotlib.org/)**: Visualização gráfica dos dados e das associações.

## Referências

- Documentação do [Streamlit](https://docs.streamlit.io/).
- Documentação do [Pandas](https://pandas.pydata.org/docs/).
- Documentação do [Mlxtend](http://rasbt.github.io/mlxtend/).
- Documentação do [Matplotlib](https://matplotlib.org/stable/contents.html).
- Curso Udemy [Streamlit: Crie aplicações web de inteligência artificial](https://www.udemy.com/course/streamlit-aplicacoes-web-de-ia).
