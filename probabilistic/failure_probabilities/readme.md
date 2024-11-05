# Probabilidade de Falhas em Equipamentos com Streamlit e Distribuição de Poisson

Este projeto apresenta uma aplicação para análise de falhas em equipamentos, desenvolvida com [Streamlit](https://streamlit.io/). Utilizando a **Distribuição de Poisson**, o projeto permite que o usuário calcule probabilidades de falhas em equipamentos em função de uma ocorrência média esperada. É uma ferramenta útil para avaliações de manutenção preditiva e confiabilidade.

## Visão Geral

O script utiliza as bibliotecas `numpy`, `matplotlib`, `scipy`, e `streamlit` para:
1. Configurar a ocorrência média de falhas e definir o tipo de probabilidade desejada.
2. Calcular as probabilidades exata, acumulada e complementar (menor que, maior que) utilizando a Distribuição de Poisson.
3. Visualizar os resultados em um gráfico de barras interativo.

## Como Executar o Projeto

Para executar a aplicação, é necessário ter Python instalado, junto com as bibliotecas requeridas. Siga os passos abaixo:

1. Clone este repositório.
2. Instale as dependências:
   ```bash
   pip install streamlit numpy matplotlib scipy
   ```
3. Execute a aplicação com o comando:
   ```bash
   streamlit run app.py
   ```

A aplicação estará disponível no navegador em `http://localhost:8501`.

## Estrutura do Código

### Configuração de Parâmetros e Seleção do Tipo de Probabilidade

- **Entrada do Usuário**:
  - **Tipo de Cálculo**: O usuário escolhe entre:
    - **Probabilidade Exata**: Calcula a probabilidade de ocorrer uma quantidade exata de falhas.
    - **Menos que**: Calcula a probabilidade de ter até um número específico de falhas.
    - **Mais que**: Calcula a probabilidade de ter mais que um determinado número de falhas.
  - **Ocorrência Média (λ)**: Define o valor médio esperado de falhas, que serve de base para os cálculos da Distribuição de Poisson.

### Cálculo e Visualização da Probabilidade

- **Distribuição de Poisson**:
  - Dependendo do tipo de cálculo, o programa usa diferentes funções da `scipy.stats.poisson`:
    - `pmf` para calcular probabilidades exatas.
    - `cdf` para probabilidades acumuladas até um ponto específico.
    - `sf` para probabilidades complementares (probabilidade de ocorrências superiores a um ponto).
- **Geração do Gráfico**:
  - O gráfico de barras mostra os valores calculados para um intervalo de valores ao redor da média escolhida.
  - As barras são rotuladas com as probabilidades calculadas e arredondadas.

### Interface e Funcionalidades

1. **Configuração do Tipo de Cálculo**: A interface permite definir o tipo de cálculo desejado e a ocorrência média de falhas.
2. **Visualização dos Resultados**: Exibe um gráfico de barras com as probabilidades calculadas para cada valor no intervalo escolhido.
3. **Rotulação**: As barras mostram etiquetas que indicam a probabilidade de cada valor no gráfico, facilitando a interpretação dos dados.

## Exemplo de Uso

1. No menu lateral, escolha o **Tipo de Cálculo** desejado (Exato, Menos que, Mais que).
2. Defina a **Ocorrência Média** para o cálculo (representando a média de falhas).
3. Clique no botão **Processar** para visualizar o gráfico das probabilidades.

## Tecnologias e Bibliotecas Utilizadas

- **[Streamlit](https://streamlit.io/)**: Framework para criar aplicações web interativas em Python.
- **[Numpy](https://numpy.org/)**: Suporte matemático para operações com arrays.
- **[SciPy](https://scipy.org/)**: Cálculo da Distribuição de Poisson.
- **[Matplotlib](https://matplotlib.org/)**: Visualização gráfica dos dados e das probabilidades.

## Referências

- Documentação do [Streamlit](https://docs.streamlit.io/).
- Documentação do [SciPy](https://docs.scipy.org/doc/scipy/).
- Documentação do [Numpy](https://numpy.org/doc/).
- Documentação do [Matplotlib](https://matplotlib.org/stable/contents.html).
- Curso Udemy [Streamlit: Crie aplicações web de inteligência artificial](https://www.udemy.com/course/streamlit-aplicacoes-web-de-ia).