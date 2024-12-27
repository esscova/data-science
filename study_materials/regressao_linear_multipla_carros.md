# Regressão linear multipla carros
Este código fornece uma introdução a:

1.  **Correlação**: A análise de correlação inicial é útil para entender a relação entre variáveis antes de ajustar o modelo.
2.  **Regressão Linear Simples**: Começamos com uma regressão simples para uma variável independente.
3.  **Regressão Linear Múltipla**: Evoluímos para um modelo com múltiplas variáveis independentes para prever a variável dependente com mais precisão.
4.  **Previsão**: Usamos o modelo ajustado para fazer previsões baseadas em novos dados.

Essa sequência ajuda a construir uma análise  que permite verificar a precisão e a validade do modelo com a avaliação de R-quadrado e R-quadrado ajustado.

### 1. **Instalação e Carregamento de Pacotes**

```r
install.packages("corrgram")
library(corrgram)

```

-   **Objetivo**: Instalar e carregar o pacote `corrgram` para visualizar a matriz de correlação entre as variáveis.
-   O pacote `corrgram` facilita a visualização das correlações entre variáveis de forma intuitiva.

### 2. **Carregamento do Conjunto de Dados `mtcars`**

```r
mtcars
dim(mtcars)

```

-   O conjunto de dados `mtcars` é um dataframe incluído no R, que contém informações sobre características de diferentes modelos de carros.
-   `dim(mtcars)` retorna as dimensões do dataframe (número de linhas e colunas).

### 3. **Análise de Correlação**

```r
cor(mtcars[1:4])

```

-   **Objetivo**: Calcular a correlação entre as primeiras quatro variáveis numéricas do conjunto de dados `mtcars`.
-   A função `cor()` calcula a correlação entre variáveis numéricas. Valores próximos de +1 indicam forte correlação positiva, e valores próximos de -1 indicam forte correlação negativa.

### 4. **Matriz de Correlação com Visualização**

```r
corrgram(
  mtcars[1:11],
  order=T,
  lower.panel=panel.shade,
  upper.panel = panel.pie,
  text.panel = panel.txt,
  main='Carros')

```

-   **Objetivo**: Visualizar as correlações entre as variáveis do dataframe `mtcars` usando o `corrgram`.
-   A opção `order=T` reorganiza as variáveis com base na correlação, para melhor visualização.
-   O painel inferior exibe sombras representando a força da correlação, o painel superior usa gráficos de pizza para mostrar os valores de correlação, e a área de texto exibe os coeficientes de correlação numérica.

### 5. **Visualização: Cilindrada vs Consumo**

```r
plot(
  mtcars$mpg ~mtcars$disp,
  ylab='mpg',
  xlab='Cilindradas',
  main='Carros')

```

-   **Objetivo**: Plotar um gráfico de dispersão entre as variáveis `mpg` (milhas por galão, ou consumo) e `disp` (cilindrada do motor).
-   O gráfico mostra se existe uma relação visível entre essas duas variáveis. Neste caso, a expectativa é que o consumo diminua à medida que a cilindrada aumenta.

### 6. **Modelo de Regressão Linear Simples**

```r
modelo = lm(mpg ~ disp, data=mtcars)
modelo

```

-   **Objetivo**: Ajustar um modelo de regressão linear simples, onde a variável dependente (`mpg`) é prevista pela variável independente (`disp`).
-   A função `lm()` ajusta o modelo, e ao digitar `modelo` você visualiza o modelo ajustado.

### 7. **Resumo do Modelo**

```r
summary(modelo)$r.squared
summary(modelo)$adj.r.squared

```

-   **Objetivo**: Obter o valor de R-quadrado (`r.squared`) e o R-quadrado ajustado (`adj.r.squared`).
    -   **R-quadrado**: Mede a proporção da variabilidade na variável dependente que é explicada pelas variáveis independentes. Varia de 0 a 1.
    -   **R-quadrado ajustado**: Ajusta o R-quadrado levando em conta o número de preditores no modelo. Usado para comparar modelos com diferentes números de variáveis independentes.

### 8. **Visualização com a Linha de Regressão**

```r
plot(mpg ~ disp,
     data=mtcars,
     ylab='mpg',
     xlab='Cilindrada',
     main='Carros')
abline(modelo)

```

-   **Objetivo**: Adicionar a linha de regressão ao gráfico de dispersão.
-   A função `abline(modelo)` desenha a linha de regressão calculada pelo modelo no gráfico de dispersão.

### 9. **Previsões com o Modelo de Regressão Simples**

```r
predict(modelo, data.frame(disp=200))

```

-   **Objetivo**: Usar o modelo ajustado para prever o valor de `mpg` dado um valor específico para `disp` (neste caso, 200).
-   A função `predict()` calcula a previsão do modelo para os valores fornecidos em `data.frame()`.

### 10. **Modelo de Regressão Linear Múltipla**

```r
modelo_multiplo = lm(mpg ~ disp + hp + cyl, data=mtcars)
modelo_multiplo

```

-   **Objetivo**: Ajustar um modelo de regressão linear múltipla, onde a variável dependente (`mpg`) é explicada por múltiplas variáveis independentes: `disp` (cilindrada), `hp` (cavalos de potência) e `cyl` (número de cilindros).
-   A regressão múltipla tenta capturar a relação entre a variável dependente e várias variáveis independentes ao mesmo tempo.

### 11. **Resumo do Modelo Múltiplo**

```r
summary(modelo_multiplo)$r.squared
summary(modelo_multiplo)$adj.r.squared

```

-   **Objetivo**: Obter o valor de R-quadrado e R-quadrado ajustado para o modelo de regressão múltipla.
-   Novamente, esses valores indicam a qualidade do ajuste do modelo, mas agora com várias variáveis independentes.

### 12. **Previsões com o Modelo Múltiplo**

```r
predict(modelo_multiplo, data.frame(disp=200, hp=100, cyl=4))

```

-   **Objetivo**: Fazer uma previsão de `mpg` usando o modelo de regressão múltipla, para um conjunto de valores específicos de `disp`, `hp` e `cyl`.


