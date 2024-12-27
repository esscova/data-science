# EXPLICAÇÃO


### **1. Carregamento dos Dados**

```r
dados <- read.csv('data/slr12.csv', sep = ";")

```

-   **Objetivo**: Carregar o arquivo `slr12.csv` contendo os dados necessários para a análise.
-   **Detalhe**: O separador utilizado no CSV é `";"`, comum em dados formatados no padrão europeu ou latino-americano.

```r
head(dados)

```

-   **Objetivo**: Visualizar as primeiras linhas do dataset para verificar a estrutura e conteúdo dos dados.

```r
dim(dados)

```

-   **Objetivo**: Verificar a dimensão do dataset (número de linhas e colunas). Útil para confirmar se os dados foram carregados corretamente.

----------

### **2. Ajuste do Modelo Linear**

```r
modelo <- lm(CusInic ~ FrqAnual, data = dados)

```

-   **Objetivo**: Ajustar um modelo de regressão linear simples para prever a variável `CusInic` (Custo Inicial) com base na variável `FrqAnual` (Frequência Anual).
-   **Função**: `lm()` realiza a modelagem linear.

```r
summary(modelo)

```

-   **Objetivo**: Obter o resumo estatístico do modelo.
    -   Inclui coeficientes estimados, significância estatística (valores p), e métricas gerais do ajuste do modelo.

```r
summary(modelo)$r.squared
summary(modelo)$adj.r.squared

```

-   **Objetivo**: Obter o **R-quadrado** (explicação da variabilidade dos dados pelo modelo) e o **R-quadrado ajustado** (corrigido para o número de preditores no modelo).

----------

### **3. Análise de Resíduos**

```r
residuos <- residuals(modelo)
plot(residuos)

```

-   **Objetivo**: Avaliar a distribuição dos resíduos do modelo.
    -   Gráfico pode indicar possíveis violações de suposições do modelo (como heterocedasticidade ou não linearidade).
    -   Resíduos devem ser aproximadamente aleatórios em torno de zero.

----------

### **4. Previsão com o Modelo**

```r
previsao <- predict(modelo, newdata = data.frame(FrqAnual=1100))
previsao

```

-   **Objetivo**: Realizar uma previsão para um novo valor de `FrqAnual` (neste caso, 1100).
    -   O resultado é o valor previsto de `CusInic` baseado no modelo ajustado.

----------

### **5. Visualização do Modelo**

```r
plot(CusInic ~ FrqAnual, data=dados)
abline(modelo)

```

-   **Objetivo**: Criar um gráfico de dispersão entre `CusInic` e `FrqAnual`, visualizando a relação linear entre as variáveis.
    -   A linha ajustada pelo modelo (`abline(modelo)`) é adicionada ao gráfico para ilustrar o ajuste.


