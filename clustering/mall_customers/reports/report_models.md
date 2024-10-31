# Relatório de Aplicação de Modelos de Agrupamento no Dataset *Mall Customers*

Neste relatório, detalho os métodos de agrupamento (clustering) aplicados ao dataset *Mall Customers* com as variáveis previamente tratadas no arquivo `clean.csv`. Os métodos incluem o algoritmo **K-Means**, **DBSCAN**, **Hierarchical Clustering** e **MeanShift**, em versões com e sem redução de dimensionalidade utilizando **PCA** (Principal Component Analysis).

---

## 1. **Preparação dos Dados**
1. **Carregamento e Normalização**:
   - Dados carregados do arquivo `clean.csv`.
   - Aplicação de `StandardScaler` para normalizar as variáveis `idade`, `rendimento` e `pontuação`, a fim de eliminar disparidades de escala entre as variáveis.
   
2. **Redução de Dimensionalidade (PCA)**:
   - A análise com `PCA` (2 componentes principais) explica aproximadamente 89,2% da variância dos dados, sendo útil para visualização e alguns métodos de agrupamento.

---

## 2. **Modelos de Agrupamento**

### 2.1 **K-Means Clustering**
1. **K-Means com Dois Atributos (Rendimento e Pontuação)**:
   - **Elbow Method** sugere 4 clusters.
   - Resultados: `K = 4`, com dados não normalizados, criando 4 grupos visualizados em gráfico de dispersão.
   
2. **K-Means com Dois Atributos Normalizados**:
   - Normalização das variáveis melhora a distribuição e minimiza a influência de escalas diferentes.
   - Gráficos e centroides mostram 4 grupos mais equilibrados.

3. **K-Means com Todos os Atributos**:
   - `K = 5`, com todos os atributos e dados não normalizados.
   - Os clusters incluem mais variação entre os dados com a inclusão de `idade` e `gênero`.

4. **K-Means com Todos os Atributos Normalizados**:
   - Melhoria na segmentação, com o Elbow Method sugerindo `K = 8`.
   - Inclui maior precisão na distribuição dos grupos.

5. **K-Means com PCA**:
   - Utilização de `PCA` para reduzir para duas dimensões principais.
   - Resultados mostram clusters com maior visualização em duas dimensões, sugerindo `K = 4` como configuração ótima.

### 2.2 **Hierarchical Clustering**
1. **Hierarchical Clustering com Todos os Atributos**:
   - Método de ligação (linkage) `average` e distância `euclidiana`.
   - Dendrograma indica formação de **7 clusters**.
   - Resultado em gráfico, com divisões mais naturais, adequadas para dados que seguem uma hierarquia.

2. **Hierarchical Clustering com PCA**:
   - Redução dimensional com `PCA` facilita a segmentação.
   - Método `complete` sugere 3 clusters, resultado refletido em visualização de dois componentes principais.

### 2.3 **DBSCAN Clustering**
1. **DBSCAN com Todos os Atributos Normalizados**:
   - **Configurações**: `eps = 0.8`, `min_samples = 4`.
   - Identificou **6 clusters**, incluindo um grupo de ruídos `(-1)`, com 12 pontos fora dos clusters principais.
   
2. **DBSCAN com PCA**:
   - **Configurações**: `eps = 0.32`, `min_samples = 3`.
   - Formou **5 clusters** (0 a 5) e um grupo de ruídos mais amplo com 24 pontos.
   - Visualização dos clusters, com ruídos distribuídos em torno dos grupos principais.

### 2.4 **MeanShift Clustering**
1. **MeanShift com Todos os Atributos Normalizados**:
   - Bandwidth ajustada para 1.5, resultando em **5 clusters** sem ruídos.
   - Distribuição razoavelmente equilibrada, com maior concentração em torno dos clusters centrais.
   
2. **MeanShift com PCA**:
   - Redução dimensional com `PCA`.
   - Bandwidth de 1, formando **4 clusters**.
   - Distribuição de grupos em torno de centroides identificados, com balanceamento próximo e menos dispersão entre clusters.

---

## 3. **Comparação dos Modelos**
- **K-Means**: Eficaz para grupos esféricos e bem definidos, mas com limitações ao lidar com ruídos e outliers.
- **Hierarchical Clustering**: Adequado para dados com estrutura hierárquica, mais flexível na quantidade de clusters, porém com menor escalabilidade.
- **DBSCAN**: Identificação robusta de clusters com formas arbitrárias e ruídos, mas sensível a parâmetros (`eps` e `min_samples`).
- **MeanShift**: Capaz de detectar o número ideal de clusters de forma automática, mas exigente em memória e processamento, menos eficiente em grandes datasets.

---

## 4. **Conclusão e Observações**
Cada técnica de clustering revelou diferentes características nos dados. **DBSCAN** e **MeanShift** são especialmente úteis ao lidar com ruídos, enquanto **K-Means** mostrou-se adequado para clusters esféricos. **Hierarchical Clustering** é útil para interpretações hierárquicas, e o uso de **PCA** facilita a visualização em duas dimensões.