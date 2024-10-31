# Relatório da Análise Exploratória de Dados (EDA)

O relatório da EDA realizada no dataset *Mall Customers* segue abaixo. Ele descreve as etapas e observações principais feitas com base nos dados dos clientes de um shopping, incluindo análises gerais, verificações de integridade dos dados, transformações, análises estatísticas e observações de correlação.

---

## **1. Descrição do Dataset**
O dataset contém informações de clientes, incluindo:
- **CustomerID**: Identificação do cliente (não relevante para o modelo).
- **Genre**: Gênero do cliente.
- **Age**: Idade do cliente.
- **Annual Income (k$)**: Rendimento anual em milhares de dólares.
- **Spending Score (1-100)**: Pontuação de gastos atribuída a cada cliente com base no comportamento de compras.

- **Total de Entradas**: 200.
- **Total de Atributos**: 5.

---

## **2. Análise de Qualidade dos Dados**
1. **Estrutura do Dataset**: Não foram identificados valores nulos ou duplicados. O dataset está completo, com todos os 200 registros e 5 colunas preenchidas.
2. **Tipos de Dados**:
   - `CustomerID` foi removido por ser irrelevante para a análise.
   - `Genre` foi convertido de uma variável categórica para numérica (0 para 'Male' e 1 para 'Female').

---

## **3. Transformações Realizadas**
1. **Renomeação de Colunas**: Os nomes das colunas foram traduzidos e padronizados:
   - `Genre` → `genero`
   - `Age` → `idade`
   - `Annual Income (k$)` → `rendimento`
   - `Spending Score (1-100)` → `pontuacao`
   
2. **Conversão de Variável**: A variável `genero` foi convertida de categórica para numérica (0 e 1) para simplificar a análise.

---

## **4. Análise Estatística**
1. **Estatísticas Descritivas**:
   - A média de idade é **38.85 anos**, com uma variação de **13.97 anos**.
   - A renda anual média é **$60.56 mil**, com um desvio padrão de **$26.26 mil**.
   - A pontuação média de gastos é **50.2**, variando entre 1 e 99.

2. **Distribuição dos Dados**:
   - Utilizando o teste de Shapiro-Wilk, foi constatado que as variáveis `idade`, `rendimento` e `pontuacao` **não seguem uma distribuição normal** (p < 0.05 em todos os casos).

---

## **5. Identificação de Outliers**
1. **Detecção de Outliers**: Aplicando o método de Interquartil (IQR), foi identificado que:
   - `idade` e `pontuacao` **não apresentam outliers**.
   - `rendimento` possui **2 outliers**, que podem representar clientes com rendas significativamente altas.

2. **Visualização de Outliers**: Boxplots foram gerados para cada variável, confirmando a presença de outliers apenas na variável `rendimento`.

---

## **6. Análise de Dispersão**
A análise de dispersão entre `rendimento` e `pontuacao` indicou que não há uma relação visível entre a renda anual e a pontuação de gastos, sugerindo que o comportamento de consumo pode ser independente do nível de renda.

---

## **7. Análise de Correlação**
1. **Método de Correlação**: Foi utilizado o método de **Kendall**, pois as variáveis não apresentam uma distribuição normal.
2. **Resultados da Correlação**:
   - A variável `pontuacao` apresenta:
     - Correlação fraca e negativa com `idade` (-0.21).
     - Correlações muito fracas ou inexistentes com `genero` (0.03) e `rendimento` (-0.0008).

Esses resultados sugerem que a idade tem uma relação ligeiramente negativa com a pontuação de gastos, enquanto gênero e renda anual não influenciam diretamente na pontuação.

---

## **8. Salvamento dos Dados**
Os dados foram salvos em um novo arquivo `clean.csv` após as transformações realizadas. As colunas estão padronizadas, com `genero` em formato numérico e `CustomerID` removido.

---

### **Considerações Finais**
A análise exploratória revelou que o comportamento de gastos dos clientes no shopping (pontuação de gastos) não está significativamente associado ao gênero ou à renda anual. Por outro lado, clientes mais jovens tendem a ter pontuações de gastos levemente mais altas. A análise também identificou a presença de alguns outliers na variável `rendimento`, representando clientes com rendas excepcionalmente altas.
