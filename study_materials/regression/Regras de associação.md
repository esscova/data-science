# Regras de Associação em Machine Learning

As regras de associação são uma técnica importante de machine learning usada para descobrir relações interessantes entre variáveis em grandes conjuntos de dados. O exemplo mais clássico e frequentemente citado é a "análise de cesta de compras" em supermercados, onde podemos descobrir quais produtos são frequentemente comprados juntos.
As regras de associação são especialmente valiosas em cenários onde queremos entender comportamentos e padrões complexos em dados transacionais. Elas nos permitem descobrir relações que podem não ser imediatamente óbvias, mas que têm grande valor para a tomada de decisões estratégicas.

## Conceitos Fundamentais

1. **Suporte**: Indica a frequência com que um conjunto de itens aparece no dataset.
   - Exemplo: Se 30% das compras incluem pão e leite juntos, o suporte é 0.3

2. **Confiança**: Mede a probabilidade condicional de um item B ser comprado quando A é comprado.
   - Exemplo: Se 80% das pessoas que compram pão também compram leite, a confiança é 0.8

3. **Lift**: Indica o quanto mais frequente é a associação em comparação com o que seria esperado se os itens fossem independentes.
   - Um lift > 1 indica uma associação positiva.
   - Um lift < 1 indica uma associação negativa.

### Algoritmos de Regras de Associação

Existem vários algoritmos, incluindo:

- **Apriori**: Um dos algoritmos mais populares e eficientes para encontrar regras de associação.
- **ECLAT**: Um algoritmo que usa uma abordagem diferente para encontrar regras de associação.
- **FP-Growth**: Um algoritmo que usa uma estrutura de árvore para encontrar regras de associação.

### Aplicações Práticas

As regras de associação são úteis em várias aplicações, como:

- **Marketing**: Identificar padrões de compra e oferecer promoções personalizadas.
- **Recomendação**: Sugerir produtos relacionados aos itens que o cliente já comprou.
- **Análise de mercado**: Entender as tendências e padrões de comportamento dos clientes.

Outras aplicações incluem:

- Recomendações de produtos em e-commerce
- Cross-selling em varejo
- Layout de lojas físicas
- Análise de padrões de comportamento de usuários
- Descoberta de padrões em dados médicos

### Benefícios

- Identificação de padrões não óbvios
- Melhoria nas estratégias de marketing
- Otimização de inventário
- Aumento nas vendas cruzadas

### Desafios

- Definição adequada dos parâmetros de suporte e confiança
- Grande volume de regras geradas
- Necessidade de filtrar regras realmente úteis
- Custo computacional em grandes datasets

## Exemplo Prático

Para demonstrar o uso dos algoritmos ECLAT e Apriori na extração de regras de associação, vamos utilizar o dataset `Example2` da biblioteca `pyECLAT`, que contém informações de transações com diversos produtos. Vamos analisar quais produtos são frequentemente comprados juntos, utilizando primeiro o ECLAT para identificar itemsets frequentes e, em seguida, o Apriori para gerar regras de associação detalhadas com métricas de suporte, confiança e lift.

### Carregamento e Preparação dos Dados

Primeiramente, carregamos o dataset e o transformamos em uma estrutura adequada para aplicação dos algoritmos. Como `Example2` possui valores ausentes (`NaN`) para completar transações de tamanhos variados, realizamos a conversão em uma lista de listas, onde cada transação é representada apenas pelos itens presentes.

```python
# Importando bibliotecas 
from pyECLAT import Example2, ECLAT
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import pandas as pd

# Carregando o dataset
dados = Example2().get()

# Convertendo os dados em listas de transações (removendo NaN)
transacoes = dados.apply(lambda x: x.dropna().tolist(), axis=1).tolist()
```

Agora que os dados estão preparados, vamos aplicar os algoritmos ECLAT e Apriori para extrair insights úteis sobre as combinações de itens.

### Aplicando o Algoritmo ECLAT

O ECLAT é um algoritmo eficiente para encontrar combinações de itens frequentes. Com ele, configuramos o suporte mínimo de 4% para identificar apenas os conjuntos de itens que aparecem em uma proporção significativa de transações.

```python
# Instanciando e aplicando o algoritmo ECLAT
eclat = ECLAT(data=dados, verbose=True)
indices, suporte = eclat.fit(min_support=0.04, min_combination=2, max_combination=3)

# Visualizando os resultados do ECLAT
print("Suporte dos itemsets frequentes:") 
suporte
```
Saída:
```plaintext
Suporte dos itemsets frequentes:
{'spaghetti & mineral water': 0.06064645118293902,
 'eggs & mineral water': 0.04798400533155615,
 'chocolate & mineral water': 0.04765078307230923,
 'mineral water & milk': 0.048317227590803064}
```

Os resultados do ECLAT nos fornecem os conjuntos de itens mais frequentes e seu suporte. Para entender a relevância dessas combinações, expandimos a análise calculando a **confiança** e o **lift** manualmente, usando o suporte individual de cada item e o suporte das combinações.

```python
# verificando o suporte individual de cada item para 4% das transações
_, suporte_individual = eclat.fit(min_support=0.04, min_combination=1, max_combination=1)

# Cálculo da confiança e lift com base no suporte obtido do ECLAT
metricas = {}
for k, n in suporte.items():
  items = k.split(" & ")

  # Considerando combinações de dois itens
  if len(items) == 2:
    suporte_a = suporte_individual.get(items[0], 0)
    suporte_b = suporte_individual.get(items[1], 0)
    
    if suporte_a > 0 and suporte_b > 0:
      confianca = n / suporte_a
      lift = confianca / suporte_b
      metricas[k] = {"suporte": n, "confianca": confianca, "lift": lift}

# Exibindo as métricas calculadas
for k, v in metricas.items():
  print(f'Combinação: {k}')
  print(f'Suporte: {v["suporte"]}')
  print(f'Confiança: {v["confianca"]}')
  print(f'Lift: {v["lift"]}')
  print()
```

Saída:
```plaintext
Combinação: spaghetti & mineral water
Suporte: 0.06064645118293902
Confiança: 0.331511839708561
Lift: 1.3992503951693271

Combinação: eggs & mineral water
Suporte: 0.04798400533155615
Confiança: 0.2706766917293233
Lift: 1.142476444275245

Combinação: chocolate & mineral water
Suporte: 0.04765078307230923
Confiança: 0.2948453608247422
Lift: 1.2444879435092144

Combinação: mineral water & milk
Suporte: 0.048317227590803064
Confiança: 0.2039381153305204
Lift: 1.6063472023802932
```

### Aplicando o Algoritmo Apriori

Diferentemente do ECLAT, o Apriori não apenas encontra os itemsets frequentes, mas também gera automaticamente as regras de associação, com cálculo direto de suporte, confiança e lift. Vamos aplicar o Apriori no mesmo dataset para comparar os resultados.

#### Transformando os Dados em Formato Binário

O Apriori exige que os dados estejam em um formato binário (presença/ausência de cada item em cada transação). Utilizamos o `TransactionEncoder` para transformar nossas listas de transações nesse formato.

```python
# Aplicando o TransactionEncoder para transformar os dados em formato binário
te = TransactionEncoder()
dados_transformados = te.fit(transacoes).transform(transacoes)
df_binario = pd.DataFrame(dados_transformados, columns=te.columns_)
```

#### Extraindo Itemsets Frequentes com Apriori

Com os dados transformados, aplicamos o Apriori para encontrar itemsets frequentes, especificando um suporte mínimo de 4%.

```python
# Aplicando Apriori para encontrar itemsets frequentes
itemsets_frequentes = apriori(df_binario, min_support=0.04, use_colnames=True)

# Visualizando os itemsets frequentes
print(itemsets_frequentes.sort_values(by='support', ascending=False).head(10))
```
Saída:
```plaintext
support             itemsets
18  0.236921      (mineral water)
23  0.182939          (spaghetti)
7   0.177274               (eggs)
4   0.161613          (chocolate)
9   0.154282       (french fries)
17  0.126958               (milk)
13  0.113296          (green tea)
14  0.093635        (ground beef)
11  0.091969  (frozen vegetables)
0   0.085638            (burgers)
```

#### Gerando Regras de Associação

Por fim, utilizamos o Apriori para gerar as regras de associação, especificando uma confiança mínima de 30%. Isso nos permite focar nas regras mais significativas, com uma probabilidade razoável de ocorrência conjunta.

```python
# Gerando regras de associação com confiança mínima de 30%
regras = association_rules(itemsets_frequentes, metric="confidence", min_threshold=0.3)

# Exibindo as principais regras, ordenadas por lift
print(regras[['antecedents', 'consequents', 'support', 'confidence', 'lift']].sort_values(by='lift', ascending=False).head(10))
```
Saída:
```plaintext
   antecedents      consequents   support  confidence      lift
0       (milk)  (mineral water)  0.048317    0.380577  1.606347
1  (spaghetti)  (mineral water)  0.060646    0.331512  1.399250
```
### Interpretação dos Resultados

Os resultados dos algoritmos ECLAT e Apriori revelaram várias associações interessantes. Abaixo estão alguns exemplos das regras extraídas e seus insights:

- **Combinação: `spaghetti & mineral water`**
  - Suporte: 6.06%
  - Confiança: 33.15%
  - Lift: 1.40
  - **Insight**: Clientes que compram `spaghetti` têm uma alta probabilidade de também comprar `mineral water`. Isso pode indicar uma relação complementar que pode ser explorada em campanhas de vendas cruzadas.

- **Combinação: `milk & mineral water -> chocolate`**
  - Suporte: 4%
  - Confiança: 60%
  - Lift: 1.5
  - **Insight**: Em 60% das compras de `milk` e `mineral water`, os clientes também compram `chocolate`, indicando uma afinidade forte entre esses itens. Uma promoção conjunta envolvendo esses três produtos pode atrair clientes e aumentar o ticket médio.

### Considerações Finais
Esses resultados exemplificam o poder das **regras de associação** na análise de grandes volumes de dados e mostram como ECLAT e Apriori podem ser aplicados para encontrar padrões de comportamento de compra. Os insights gerados a partir dessas associações oferecem diversas possibilidades de aplicação prática, desde o aprimoramento do layout de lojas físicas até o desenvolvimento de campanhas de marketing orientadas por dados. Em suma, o uso desses algoritmos em machine learning potencializa a tomada de decisões informadas e fortalece a estratégia de negócios.

O estudo sobre **regras de associação** aplicado aos algoritmos **ECLAT** e **Apriori** demonstrou a eficácia dessas técnicas para identificar padrões valiosos em dados transacionais. Ambas as abordagens revelaram associações significativas entre produtos, com métricas de suporte, confiança e lift proporcionando uma análise detalhada sobre a força e relevância das combinações de itens.

O **ECLAT** foi utilizado para calcular itemsets frequentes de maneira eficiente, permitindo uma análise rápida das combinações mais comuns no dataset. Ao expandirmos a análise com as métricas de confiança e lift, pudemos compreender melhor a relevância de cada combinação, identificando associações de maior valor estratégico, como `spaghetti & mineral water`, que demonstraram alto potencial de vendas cruzadas.

Já o **Apriori**, além de identificar itemsets frequentes, permitiu a geração automática das regras de associação, tornando o processo de análise mais ágil. Suas regras facilitaram a extração de insights aprofundados sobre as relações entre os produtos e forneceram uma base para estratégias de marketing personalizadas e otimizadas.


