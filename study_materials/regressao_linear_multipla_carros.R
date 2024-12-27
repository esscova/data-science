
# ---
#   regressao linear multipla
#      variaveis
#       mpg = consumo
#       hp = cavalos
#       cyl = numero de cilindros
#       disp = cilindradas
#       ...
# ---

# pacote para visualizar correlacoes
install.packages("corrgram")
library(corrgram)

# carregando dados
mtcars
dim(mtcars)

# correlações
cor(mtcars[1:4])

# matriz de correlacoes
corrgram(
  mtcars[1:11],
  order=T,
  lower.panel=panel.shade,
  upper.panel = panel.pie,
  text.panel = panel.txt,
  main='Carros')

# cilindradas x consumo
plot(
  mtcars$mpg ~ mtcars$disp,
  ylab='mpg',
  xlab='Cilindradas',
  main='Carros')

# modelo de regressao simples
modelo = lm(mpg ~disp, data=mtcars)
modelo

# resumo do modelo simples
summary(modelo)$r.squared
summary(modelo)$adj.r.squared

# plot do modelo simples
plot(mpg ~ disp,
     data=mtcars,
     ylab='mpg',
     xlab='Cilindrada',
     main='Carros')
abline(modelo)

# previsao com modelo simples
predict(modelo, data.frame(disp=200))

# modelo multiplo
modelo_multiplo = lm(mpg ~ disp + hp + cyl, data=mtcars)
modelo_multiplo

# resumo do modelo multiplo
summary(modelo_multiplo)$r.squared
summary(modelo_multiplo)$adj.r.squared

# previsao com modelo multiplo
predict(modelo_multiplo, data.frame(disp=200, hp=100, cyl=4))
