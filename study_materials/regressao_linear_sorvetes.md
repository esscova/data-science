# Explicação do exercício

### 1. **Pacotes e Dados**
```R
install.packages("ggplot2")
library(ggplot2)

dados <- data.frame(
  Temperatura = c(20, 22, 24, 26, 28, 30, 32),
  Vendas = c(50, 55, 60, 65, 70, 75, 80)
)

print(dados)
```
- O pacote `ggplot2` é instalado e carregado para criar gráficos.
- Um conjunto de dados é criado com duas variáveis: `Temperatura` e `Vendas`. Este conjunto de dados representa uma relação linear entre temperatura (em graus Celsius) e vendas de sorvete.

### 2. **Modelo de Regressão Linear**
```R
modelo <- lm(Vendas ~ Temperatura, data = dados)
summary(modelo)
```
- A função `lm()` é usada para ajustar um modelo de regressão linear, onde `Vendas` é a variável dependente e `Temperatura` é a variável independente.
- O resumo do modelo (`summary()`) fornecerá informações como os coeficientes estimados (intercepto e inclinação), erro padrão, valor $R²$, valores-p, e estatísticas F. Esses valores ajudam a avaliar a qualidade do modelo e a significância estatística da relação entre as variáveis.

### 3. **Gráfico de Dispersão e Linha de Regressão**
```R
ggplot(dados, aes(x = Temperatura, y = Vendas)) +
  geom_point() +
  geom_smooth(method = "lm", col = "blue") +
  theme_minimal() +
  labs(title = "Regressão Linear: Vendas de Sorvete vs Temperatura")
```
- O gráfico exibe os pontos de dados originais (scatter plot) e a linha de regressão ajustada.
- A linha de regressão é desenhada com a função `geom_smooth(method = "lm")`, que utiliza o modelo de regressão linear ajustado.

### 4. **Análise de Resíduos**
```R
residuos <- residuals(modelo)
plot(residuos, main = "Resíduos do Modelo", ylab = "Resíduos", xlab = "Índice")
```
- Os resíduos do modelo são calculados com `residuals(modelo)` e representados em um gráfico. 
- Este gráfico ajuda a avaliar a suposição de homocedasticidade (resíduos com variância constante) e a presença de padrões nos resíduos.

### 5. **Previsão**
```R
previsao <- predict(modelo, newdata = data.frame(Temperatura = 34))
print(previsao)
```
- O modelo é usado para prever as vendas esperadas quando a temperatura é 34°C. O resultado é impresso.

### 6. **Interpretação**
1. **Resumo do Modelo (`summary(modelo)`):**
   - Os coeficientes mostram como a variável `Temperatura` influencia `Vendas`. Por exemplo, se o coeficiente de inclinação for $5$, significa que cada aumento de 1°C na temperatura resulta em um aumento esperado de 5 unidades nas vendas.
   - O $R^2$ indica a proporção da variação em `Vendas` explicada por `Temperatura`.

2. **Gráficos:**
   - O gráfico de dispersão com a linha de regressão ajuda a visualizar a relação linear entre as variáveis.
   - O gráfico de resíduos permite identificar possíveis problemas com o modelo, como padrões nos resíduos ou variância não constante.

3. **Previsão:**
   - O valor previsto fornece uma estimativa das vendas esperadas para uma temperatura de 34°C com base no modelo ajustado.

---