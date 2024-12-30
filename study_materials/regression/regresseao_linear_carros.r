# pacotes
install.packages("corrgram")
library(corrgram)

dim(cars)
cor(cars)

# gráfico de correlação
corrgram(cars, order=TRUE, lower.panel=panel.shade,
         upper.panel=panel.pie, text.panel=panel.txt,
         main="Carros")

# modelo
modelo = lm(speed ~ dist, data=cars)

# plot do modelo
plot(speed ~ dist, data=cars, ylab = "Velocidade", xlab=" Distância", main="Carros")
abline(modelo)

# coeficientes
modelo$coefficients
modelo$coefficients[1] + modelo$coefficients[2] * 22

# previsão 
predict(modelo,data.frame(dist = 22))

# resumo
summary(modelo)

# resíduos e ajustes
modelo$coefficients
modelo$residuals
hist(modelo$residuals)
modelo$fitted.values
plot(modelo$fitted.values, cars$dist)
