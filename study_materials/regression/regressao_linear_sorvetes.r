# pacotes
install.packages("ggplot2")
library(ggplot2)

# dados
dados <- data.frame(
  Temperatura = c(20, 22, 24, 26, 28, 30, 32),
  Vendas = c(50, 55, 60, 65, 70, 75, 80)
)

print(dados)

# modelo de regressão linear
modelo <- lm(Vendas ~ Temperatura, data = dados)

# resumo do modelo
summary(modelo)

# plot de dispersão e linha de regressão
ggplot(dados, aes(x = Temperatura, y = Vendas)) +
  geom_point() +
  geom_smooth(method = "lm", col = "blue") +
  theme_minimal() +
  labs(title = "Regressão Linear: Vendas de Sorvete vs Temperatura")

# plot dos resíduos
residuos <- residuals(modelo)
plot(residuos, main = "Resíduos do Modelo", ylab = "Resíduos", xlab = "Índice")

# testando modelo com uma previsão para 34°C
previsao <- predict(modelo, newdata = data.frame(Temperatura = 34))
print(previsao)
