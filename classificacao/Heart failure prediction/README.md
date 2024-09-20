## Previsão de Insuficiência Cardíaca

<img src="heart_failure.jpg" alt="image" width="300" height="200"> 

As doenças cardiovasculares (DCVs) são a principal causa de morte em todo o mundo, resultando em aproximadamente 17,9 milhões de óbitos anualmente, o que representa 31% de todas as mortes globais. Quatro em cada cinco mortes por DCVs são atribuídas a infartos e acidentes vasculares cerebrais (AVCs), e um terço dessas mortes ocorre prematuramente em pessoas com menos de 70 anos. A insuficiência cardíaca é um evento comum causado por DCVs, e este conjunto de dados contém 11 características que podem ser utilizadas para prever a possibilidade de doenças cardíacas.

Indivíduos com doenças cardiovasculares ou que apresentam alto risco cardiovascular (devido à presença de um ou mais fatores de risco, como hipertensão, diabetes, hiperlipidemia ou doenças já estabelecidas) necessitam de detecção e manejo precoces, onde um modelo de aprendizado de máquina pode ser de grande ajuda.

## Informações sobre os Atributos do dataset

- **Age**: idade do paciente [anos]
- **Sex**: sexo do paciente [M: Masculino, F: Feminino]
- **ChestPainType**: tipo de dor no peito [TA: Angina Típica, ATA: Angina Atípica, NAP: Dor Não Anginal, ASY: Assintomática]
- **RestingBP**: pressão arterial em repouso [mm Hg]
- **Cholesterol**: colesterol sérico [mm/dl]
- **FastingBS**: glicose em jejum [1: se FastingBS > 120 mg/dl, 0: caso contrário]
- **RestingECG**: resultados do eletrocardiograma em repouso [Normal: Normal, ST: com anormalidade da onda ST-T (inversões da onda T e/ou elevação ou depressão ST > 0,05 mV), LVH: mostrando provável ou definitiva hipertrofia ventricular esquerda segundo os critérios de Estes]
- **MaxHR**: frequência cardíaca máxima alcançada [Valor numérico entre 60 e 202]
- **ExerciseAngina**: angina induzida por exercício [Y: Sim, N: Não]
- **Oldpeak**: oldpeak = ST [Valor numérico medido em depressão]
- **ST_Slope**: a inclinação do segmento ST no pico do exercício [Up: inclinação ascendente, Flat: plano, Down: inclinação descendente]
- **HeartDisease**: classe de saída [1: doença cardíaca, 0: Normal]

## Relatórios

- [Análise exploratória](reports/Relatório%2001%20-%20análise%20de%20dados.md)
- [Escolha e avaliação do modelo](reports/Relatório%2002%20-%20classificadores.md)