### Relatório de Análise Exploratória de Dados (EDA) - Dataset "Groceries"

**Objetivo**: Realizar uma análise exploratória dos dados de transações do dataset "Groceries" do Kaggle, que contém informações sobre itens comprados em uma série de transações de clientes. O objetivo da EDA é obter insights preliminares sobre o comportamento de compra dos clientes e preparar os dados para aplicação de regras de associação, utilizando o algoritmo Apriori.

---

### 1. Descrição do Dataset

O dataset "Groceries" contém os seguintes campos:

- **Member_number**: Identificador único de cada cliente.
- **Date**: Data da compra.
- **itemDescription**: Descrição do item comprado.

A base de dados tem 38.765 registros, distribuídos em três colunas (`Member_number`, `Date` e `itemDescription`).

### 2. Análise das Variáveis

#### 2.1 Estrutura do Dataset

- **Dimensões**: O dataset possui 38.765 linhas e 3 colunas.
- **Tipos de Dados**:
  - `Member_number`: Inteiro (`int64`)
  - `Date`: Objeto (`object`), convertido posteriormente para o formato de data (`datetime64[ns]`)
  - `itemDescription`: Texto (`object`)

#### 2.2 Dados Ausentes

Não foram encontrados valores ausentes em nenhuma das colunas do dataset, o que indica que a qualidade dos dados é boa e que não há necessidade de lidar com valores faltantes.

```python
# verificando valores nulos
df.isnull().sum()
# Saída:
# Member_number      0
# Date               0
# itemDescription    0
```

### 3. Análise dos Dados Temporais

Para facilitar a análise, a coluna `Date` foi convertida para o tipo `datetime`. Isso permite manipulações temporais, como a análise de sazonalidade e o agrupamento de vendas por período, embora essa análise não tenha sido aprofundada neste relatório exploratório.

### 4. Análise Descritiva das Variáveis

#### 4.1 Frequência de Itens Comprados

A variável `itemDescription` indica o tipo de item comprado em cada transação. Abaixo estão os itens mais comprados pelos clientes:

```python
# verificando quantidade de vendas por item
df['itemDescription'].value_counts().head(5)
# Saída:
# whole milk           2502
# other vegetables     1898
# rolls/buns           1716
# soda                 1514
# yogurt               1334
```

- **whole milk** (leite integral) é o item mais vendido, com 2.502 ocorrências.
- **other vegetables** (outros vegetais) vem em seguida, com 1.898 ocorrências.
- Outros itens populares incluem **rolls/buns** (pães), **soda** (refrigerantes) e **yogurt** (iogurte).

Essa distribuição sugere uma preferência por produtos de mercearia essencial, como laticínios e pães, itens de consumo diário.

#### 4.2 Análise de Compras por Cliente

A variável `Member_number` representa cada cliente. Podemos analisar quantas transações cada cliente realizou:

```python
# verificando quantidade de vendas por item e consumidor
df['Member_number'].value_counts().head(10)
# Saída:
# Member_number
# 3180    36
# 2051    33
# 3050    33
# 3737    33
# 2271    31
```

Os dados mostram que os clientes realizam compras com frequência variada:
- O cliente com o ID 3180 fez 36 compras, sendo o maior número de transações individuais.
- Outros clientes também aparecem com mais de 30 transações, sugerindo um grupo de clientes regulares.

Essa análise preliminar indica que alguns clientes são mais frequentes, o que poderia ser explorado em um programa de fidelidade ou campanhas direcionadas.

### 5. Preparação dos Dados para Análise de Associação

Para aplicar o algoritmo Apriori, precisamos transformar os dados para indicar a presença ou ausência de cada item em uma transação. Isso foi feito com os seguintes passos:

1. **Agrupamento das Transações**:
   - Agrupamos o dataset pelas colunas `Member_number` e `itemDescription`, contando o número de ocorrências de cada item para cada cliente.
   - O resultado é uma tabela com a contagem de cada item por cliente.

2. **Transformação em Formato Binário**:
   - Convertendo as contagens para um formato binário (1 para presença e 0 para ausência), obtemos uma tabela onde cada coluna representa um item, e o valor indica se ele foi comprado pelo cliente.
   - Esse formato binário é essencial para o algoritmo Apriori, que exige uma estrutura de presença/ausência para calcular as associações entre os itens.

```python
# preparando o dataframe para APRIORI
df2 = df.groupby(['Member_number', 'itemDescription'])['itemDescription'].count()
df2 = df2.unstack().fillna(0)
df2 = df2.applymap(lambda x: 1 if x > 0 else 0)
```

### 6. Conclusões da Análise Exploratória

A EDA revelou insights valiosos sobre o comportamento de compra dos clientes:

- **Itens Populares**: Produtos essenciais, como leite integral e vegetais, são os mais comprados.
- **Compras Frequentes**: Alguns clientes fazem compras frequentemente, o que pode indicar um grupo de clientes fiéis.
- **Preparação para Regras de Associação**: Os dados foram transformados em um formato binário para análise de regras de associação, o que facilitará a identificação de padrões de compra.

Esses insights servirão de base para aplicar o algoritmo Apriori e descobrir associações úteis entre produtos, que podem ser aplicadas para personalização de ofertas e otimização de campanhas de marketing.

---
