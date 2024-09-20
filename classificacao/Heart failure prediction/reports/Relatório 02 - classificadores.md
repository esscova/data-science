### Relatório Final: Escolha do XGBoost como Melhor Modelo para o Dataset
**Autor** : Wellington Moreira dos Santos - Cientista de Dados

**Contatos** : wsantos08@hotmail.com | [Linkedin](https://www.linkedin.com/in/wellington-moreira-santos/)

---
#### Introdução

Neste relatório, analisamos o desempenho de diversos modelos de aprendizado de máquina aplicados a um dataset de classificação. Os modelos avaliados incluem **K-Nearest Neighbors (KNN)**, **Naive Bayes**, **Random Forest**, **Logistic Regression**, **Support Vector Machine (SVM)**, **Decision Tree**, e **XGBoost**. O objetivo foi identificar o modelo mais eficiente com base em métricas como **acurácia de teste**, **acurácia de validação cruzada**, **F1-score**, e **diferença entre acurácia de treino e teste**.

#### Metodologia

Os modelos foram treinados e testados usando três tipos de pré-processamento de dados:
1. **Label Encoding**
2. **One-Hot Encoding**
3. **Escalonamento**

As métricas de desempenho analisadas foram:
- **Acurácia de Teste**: Indicador primário do desempenho do modelo em dados não vistos.
- **Acurácia de Validação Cruzada**: Média de acurácias em múltiplos folds para verificar a robustez.
- **F1-Score**: Combinação de precisão e recall, útil para balancear a avaliação em casos de classes desbalanceadas.
- **Diferença entre Acurácia de Treino e Teste**: Indicativo de possíveis sinais de overfitting.
- **Matriz de Confusão**: Para entender o comportamento do modelo nas classificações corretas e incorretas.

#### Top 3 Modelos com Base na Acurácia de Teste

Com base nos resultados, os três modelos com a maior acurácia de teste foram:
```python
melhores_acuracia_teste = resultados.nlargest(3, 'acuracia_teste')
print(melhores_acuracia_teste[['modelo', 'conjunto', 'acuracia_teste']])
```

#### Resultados:
```
    modelo         conjunto  acuracia_teste
18  XGBoost    label_encoded       89.13%
2       KNN       escalonado       88.77%
19  XGBoost  one_hot_encoded       88.77%
```

#### Análise dos Melhores Modelos:

1. **XGBoost (label_encoded)**
   - **Acurácia de Teste**: 89.13%
   - **Acurácia de Validação Cruzada**: 87.56%
   - **F1-Score**: 89.07%
   - **Diferença entre Acurácia de Treino e Teste**: 1.20%
   - **Matriz de Confusão**: [[101, 20], [10, 145]]

   O **XGBoost** com o conjunto `label_encoded` obteve a maior acurácia de teste entre todos os modelos, além de manter uma alta acurácia de validação cruzada, demonstrando consistência e robustez. A diferença mínima entre acurácia de treino e teste indica um bom balanceamento sem sinais de overfitting significativo.

2. **KNN (escalonado)**
   - **Acurácia de Teste**: 88.77%
   - **Acurácia de Validação Cruzada**: 86.35%
   - **F1-Score**: 88.69%
   - **Diferença entre Acurácia de Treino e Teste**: -0.62%
   - **Matriz de Confusão**: [[100, 21], [10, 145]]

   O **KNN** aplicado aos dados `escalonados` também apresentou um excelente desempenho, praticamente igualando o XGBoost em termos de acurácia de teste. No entanto, a ligeira negatividade na diferença entre treino e teste sugere uma ligeira subestimação de sua performance no treino.

3. **XGBoost (one_hot_encoded)**
   - **Acurácia de Teste**: 88.77%
   - **Acurácia de Validação Cruzada**: 87.23%
   - **F1-Score**: 88.69%
   - **Diferença entre Acurácia de Treino e Teste**: 2.18%
   - **Matriz de Confusão**: [[100, 21], [10, 145]]

   O **XGBoost** com `one_hot_encoded` também obteve uma acurácia de teste excelente, muito próxima ao XGBoost com `label_encoded`. A validação cruzada também mostrou robustez, embora com uma diferença um pouco maior entre treino e teste, indicando um potencial leve de overfitting.

#### Conclusão

Após a análise dos modelos, é evidente que o **XGBoost com `label_encoded`** se destaca como o melhor modelo para este dataset por várias razões:
- **Maior acurácia de teste** (89.13%), o que significa que foi o mais eficaz na classificação de dados não vistos.
- **Alta acurácia de validação cruzada** (87.56%), garantindo robustez e capacidade de generalização.
- **Alto F1-Score** (89.07%), indicando um ótimo equilíbrio entre precisão e recall, importante para cenários com classes desbalanceadas.
- **Baixa diferença entre acurácia de treino e teste** (1.20%), sugerindo que o modelo é bem ajustado e não sofre de overfitting.

Os resultados gerais mostram que o **XGBoost** tem a capacidade de capturar padrões complexos nos dados, mantendo uma boa generalização, tornando-se a escolha ideal para este problema de classificação. Em segundo lugar, o **KNN** com dados `escalonados` e o **XGBoost** com `one_hot_encoded` também tiveram desempenhos próximos, mas não alcançaram a mesma consistência e robustez do XGBoost com `label_encoded`.

Portanto, recomendamos o uso do **XGBoost com `label_encoded`** para futuras aplicações e implementações neste dataset.