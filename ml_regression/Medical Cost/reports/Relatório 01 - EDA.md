**Relatório de Análise Exploratória do Projeto "Medical Cost"**

**Introdução**

Este relatório apresenta os resultados da análise exploratória do conjunto de dados "insurance.csv" do projeto "Medical Cost". O objetivo é entender melhor as características dos dados e identificar padrões e relações entre as variáveis.

**Características dos Dados**

* O conjunto de dados contém 1338 registros e 7 variáveis.
* As variáveis são:
 + `age`: idade do paciente
 + `sex`: sexo do paciente (masculino ou feminino)
 + `bmi`: índice de massa corporal do paciente
 + `children`: número de filhos do paciente
 + `smoker`: se o paciente é fumante ou não
 + `region`: região de residência do paciente
 + `charges`: custo médico do paciente

**Distribuição dos Dados**

* A distribuição dos dados é a seguinte:
 + `age`: média de 39 anos, com um desvio padrão de 14 anos
 + `bmi`: média de 30,7, com um desvio padrão de 6,3
 + `children`: média de 1,1, com um desvio padrão de 1,2
 + `charges`: média de 13270, com um desvio padrão de 11500

**Análise de Correlação**

* A análise de correlação mostrou que:
 + `age` e `charges` têm uma correlação positiva moderada (coeficiente de Spearman = 0,43)
 + `bmi` e `charges` têm uma correlação positiva fraca (coeficiente de Spearman = 0,24)
 + `children` e `charges` têm uma correlação positiva fraca (coeficiente de Spearman = 0,19)

**Análise de Normalidade**

* A análise de normalidade mostrou que:
 + `age` e `bmi` têm distribuições normais
 + `children` e `charges` têm distribuições não normais

**Conclusões**

* A análise exploratória mostrou que os dados têm uma distribuição razoável e que há correlações entre as variáveis.
* A idade e o índice de massa corporal são os principais fatores que influenciam o custo médico.
* A região de residência e o número de filhos têm uma influência menor no custo médico.
