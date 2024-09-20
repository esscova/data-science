## **Relatório Final: Escolha do Algoritmo de Regressão Logística para Classificação de Câncer de Mama**

**Autor** : Wellington Moreira - Cientista de Dados

**Contatos** : wsantos08@hotmail.com | [Linkedin](https://www.linkedin.com/in/wellington-moreira-santos)

---

### **Introdução**

#### **Descrição do Problema**
A classificação precisa entre tumores malignos e benignos é crucial no diagnóstico de câncer de mama. Utilizando dados clínicos com diversas características dos tumores, podemos desenvolver um modelo preditivo robusto. A escolha do modelo correto, juntamente com a otimização de seus hiperparâmetros, é essencial para garantir alta performance e generalização em novos dados.

#### **Objetivo**
O objetivo deste relatório é justificar a escolha final do modelo de **Regressão Logística**, após a otimização de hiperparâmetros e a comparação com outros modelos de classificação. Além disso, serão apresentados os motivos pelos quais a Regressão Logística é uma escolha adequada para este problema de classificação binária.

---

### **Otimização e Avaliação de Modelos**

#### **Dados Utilizados**
Os dados foram padronizados e divididos em características preditoras (`X`) e a variável alvo (`y`), onde `y` indica se o tumor é maligno (`1`) ou benigno (`0`). A divisão entre conjunto de treino e teste foi de 70% e 30%, respectivamente, utilizando uma amostra estratificada para manter a proporção das classes.

#### **Modelos Testados**
Diversos modelos de classificação foram avaliados com o objetivo de selecionar o melhor em termos de acurácia e generalização. Os modelos incluíram:

- **Naive Bayes**
- **Support Vector Machine (SVM)**
- **Regressão Logística**
- **K-Nearest Neighbors (KNN)**
- **Árvores de Decisão**
- **Random Forest**
- **Gradient Boosting**
- **XGBoost**

#### **Métricas Utilizadas**
Os modelos foram avaliados utilizando as seguintes métricas:

- **Acurácia**
- **Precisão**
- **Recall**
- **F1-Score**
- **Matriz de Confusão**
- **Diferença de Acurácia entre Treino e Teste**
- **Validação Cruzada com 5 Folds**

---

### **Otimização de Hiperparâmetros da Regressão Logística**

A otimização de hiperparâmetros é fundamental para melhorar o desempenho do modelo. No caso da Regressão Logística, a busca por parâmetros ideais foi realizada utilizando o **GridSearchCV** com validação cruzada de 5 folds. Os hiperparâmetros ajustados foram:

- **C**: [0.001, 0.01, 0.1, 1, 10, 100] (regularização)
- **penalty**: ['l1', 'l2', 'elasticnet'] (tipo de penalização)
- **solver**: ['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga'] (algoritmo de otimização)
- **multi_class**: ['ovr', 'multinomial'] (tipo de classificação multiclasse)

#### **Melhores Hiperparâmetros Encontrados**
Após a otimização, os melhores parâmetros foram:

- **C**: 1
- **penalty**: 'l2'
- **solver**: 'sag'
- **multi_class**: 'ovr'

Esses parâmetros foram selecionados com base na métrica **ROC AUC**, e o modelo treinado com eles atingiu um excelente desempenho com a pontuação de:

- **Melhor pontuação AUC**: 99.38%

#### **Desempenho da Regressão Logística Otimizada**
Após o treinamento com os melhores hiperparâmetros, o desempenho do modelo de Regressão Logística foi avaliado no conjunto de teste:

- **Acurácia no Teste**: 99%
- **Precisão**: 99%
- **Recall**: 98%
- **F1-Score**: 99%

#### **Relatório de Classificação**
O relatório de classificação para o conjunto de teste mostra uma excelente performance:

```plaintext
              precision    recall  f1-score   support

           0       0.99      0.99      0.99       108
           1       0.98      0.98      0.98        63

    accuracy                           0.99       171
   macro avg       0.99      0.99      0.99       171
weighted avg       0.99      0.99      0.99       171
```

#### **Matriz de Confusão**
A matriz de confusão confirma o baixo número de falsos positivos e falsos negativos:

```plaintext
array([[107,   1],
       [  1,  62]])
```

Esse resultado demonstra que o modelo tem alta capacidade de distinguir corretamente entre tumores benignos e malignos, com apenas 2 erros no total.

---

### **Comparação com Outros Modelos**

Os três melhores modelos em termos de acurácia de teste e validação cruzada foram:

| Modelo                    | Acurácia Teste | Acurácia CV  | Precisão  | Recall    | F1-Score | Dif. Acurácia (Treino-Teste) |
|---------------------------|----------------|--------------|-----------|-----------|----------|------------------------------|
| **SVM Padronizado**        | 97.66%         | 97.89%       | 97.67%    | 97.66%    | 97.65%   | 0.58                          |
| **Regressão Logística Padronizada** | **99%**       | **99.38%**  | **99%**   | 98%       | **99%**  | 1.33                          |
| **Gradient Boosting**      | 97.66%         | 96.66%       | 97.66%    | 97.66%    | 97.66%   | 2.34                          |

Apesar de modelos como **Support Vector Machine** e **Gradient Boosting** também apresentarem alta acurácia, a Regressão Logística superou ambos em termos de generalização e eficiência computacional.

---

### **Justificativa para Escolha da Regressão Logística**

#### 1. **Interpretação**
A Regressão Logística oferece uma explicação clara sobre como cada variável influencia o diagnóstico de câncer de mama. Isso é especialmente importante em um contexto médico, onde a transparência do modelo é crucial para ganhar a confiança dos profissionais de saúde.

#### 2. **Desempenho Excelente**
Com a otimização dos hiperparâmetros, o modelo de Regressão Logística alcançou **99% de acurácia**, superando a maioria dos outros modelos em termos de **F1-Score**, **acurácia** e **recall**.

#### 3. **Generalização**
A diferença de acurácia entre treino e teste foi de apenas 1.33%, indicando que o modelo de Regressão Logística não está superajustado aos dados de treinamento, mantendo uma boa capacidade de generalização.

#### 4. **Eficiência Computacional**
A Regressão Logística é computacionalmente mais eficiente que modelos complexos como **Gradient Boosting** e **SVM**, permitindo um treinamento mais rápido e uso em sistemas com menor capacidade computacional.

#### 5. **Ajuste a Dados Padronizados**
Após a padronização dos dados, a Regressão Logística continuou a demonstrar excelente desempenho, tornando-a ideal para este tipo de pré-processamento.

---

### **Conclusão**

#### **Por que a Regressão Logística foi escolhida:**
- **Interpretação**: O modelo é altamente interpretável, o que facilita a explicação dos resultados para médicos e outros profissionais.
- **Desempenho Superior**: Após a otimização, a Regressão Logística superou outros modelos em métricas importantes, como F1-Score e Acurácia, atingindo **99% de acurácia no teste**.
- **Generalização**: A diferença mínima entre treino e teste demonstra a robustez do modelo.
- **Eficiência Computacional**: A Regressão Logística é leve e rápida de treinar, o que a torna adequada para cenários onde o tempo de computação é uma preocupação.
- **Simplicidade e Eficácia**: Mesmo com sua simplicidade, a Regressão Logística provou ser altamente eficaz neste problema de classificação binária.

#### **Próximos Passos**
- **Validação Externa**: Testar o modelo em um novo conjunto de dados para verificar sua robustez em diferentes cenários.
- **Implementação**: O modelo final foi salvo como `modelo_logistica.pkl` e está pronto para ser implementado em aplicações de diagnóstico.

---

Se precisar de mais informações ou detalhes sobre o processo, fique à vontade para entrar em contato!
