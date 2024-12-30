# carregando dados
eleicao <- read.csv('data/Eleicao.csv', sep = ';', header = T)
eleicao

# conhecendo os dados
dim(eleicao)
summary(eleicao)

plot(eleicao$DESPESAS, eleicao$SITUACAO)

# correlacao
cor(eleicao$DESPESAS, eleicao$SITUACAO)


# modelo de regressao logistica
modelo <- glm(SITUACAO ~ DESPESAS, data=eleicao, family='binomial')
summary(modelo)

# plot modelo aos dados
plot(eleicao$DESPESAS, eleicao$SITUACAO, col='red', pch=20)
points(eleicao$DESPESAS, modelo$fitted, pch=4)

# teste do modelo
prever <- predict(modelo, newdata=eleicao, type='response')
prever <- prever >= 0.5 #teste logico
prever

# avaliando
confusao <- table(prever, eleicao$SITUACAO) # matriz de confusao
confusao

# acuracia
taxaacerto <- (confusao[1] + confusao[4]) / sum(confusao)
taxaacerto


# aplicando modelo para novos candidatos
novos_candidatos <- read.csv('data/NovosCandidatos.csv', sep=';', header=T)
novos_candidatos


novos_candidatos$RESULT <- predict(modelo, newdata=novos_candidatos, type='response')
novos_candidatos$RESULT # probabilidades
novos_candidatos$RESULT >= 0.5 # teste logico
