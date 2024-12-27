dados <- read.csv('data/slr12.csv', sep = ";")
head(dados)

dim(dados)

modelo <- lm(CusInic ~ FrqAnual, data = dados)
summary(modelo)
summary(modelo)$r.squared
summary(modelo)$adj.r.squared

residuos <- residuals(modelo)
plot(residuos)

previsao <- predict(modelo, newdata = data.frame(FrqAnual=1100))
previsao

plot(CusInic ~ FrqAnual, data=dados)
abline(modelo)
