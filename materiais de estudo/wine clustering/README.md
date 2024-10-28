## Introdução às Técnicas de Agrupamento

As técnicas de **agrupamento** (ou clustering) são métodos de aprendizado não supervisionado que têm como objetivo agrupar dados em subconjuntos, ou "clusters", de forma que os itens de cada grupo sejam mais semelhantes entre si do que com itens de outros grupos. Esse processo permite identificar padrões ocultos e segmentações naturais no conjunto de dados. Técnicas de agrupamento são aplicadas em várias áreas, como análise de mercado, reconhecimento de padrões e até em segmentação de clientes. Diferente da classificação, que trabalha com dados rotulados, o agrupamento lida com dados não rotulados, sendo assim uma tarefa de exploração.

<p align='center'>
    <img src='https://images.datacamp.com/image/upload/v1659712759/Customer_Segmentation_ccf4cfac94.png'>
</p>

### Dataset Utilizado: Wine

Neste estudo, utilizamos o dataset **Wine** da UCI Machine Learning Repository. Esse conjunto de dados descreve características químicas e físicas de vinhos cultivados na mesma região na Itália, porém derivados de três diferentes cultivares. O dataset contém 13 variáveis numéricas, como teor alcoólico, níveis de ácido, magnésio e fenóis, entre outras características que ajudam a distinguir entre os diferentes tipos de vinho. Ele é amplamente utilizado em tarefas de classificação e clustering devido à sua riqueza de informações e à presença de grupos naturais, o que o torna ideal para avaliar técnicas de agrupamento.

### Algoritmos de Agrupamento Utilizados

1. **K-Means**: O K-Means é um dos algoritmos de clustering mais populares, especialmente para agrupamento de grandes quantidades de dados. Ele tenta dividir o dataset em `k` clusters, onde `k` é definido previamente, minimizando a variância interna dos clusters. O algoritmo escolhe pontos iniciais (centroides) e, por meio de iterações, ajusta esses centroides para melhor representar cada grupo.

2. **Agrupamento Hierárquico**: Essa técnica organiza os dados em uma hierarquia de clusters, utilizando uma abordagem de divisão ou junção. Existem dois tipos principais: hierárquico aglomerativo, onde cada ponto começa como um cluster individual e é gradualmente agrupado, e hierárquico divisivo, que começa com todos os pontos em um cluster e os divide sucessivamente. Não requer a escolha do número de clusters inicialmente, o que permite uma análise mais exploratória.

3. **Mean Shift**: Mean Shift é um algoritmo baseado em densidade que identifica regiões de alta densidade de dados (modas) e atribui pontos aos clusters com base na proximidade com esses picos. A largura de banda (bandwidth) é um parâmetro essencial que define o raio de consideração para cada ponto e, se escolhido corretamente, pode ser eficiente para dados com distribuições complexas.

4. **DBSCAN**: O DBSCAN (Density-Based Spatial Clustering of Applications with Noise) agrupa dados com base na densidade, identificando áreas de alta densidade e classificando como "ruído" (outliers) os pontos em áreas de baixa densidade. O DBSCAN não requer a especificação do número de clusters, tornando-o útil para detectar grupos de formas variadas e separar ruídos.

### Uso do PCA (Análise de Componentes Principais)

A **Análise de Componentes Principais (PCA)** foi aplicada ao dataset como uma etapa de redução de dimensionalidade. O PCA transforma o dataset original em um novo espaço de menor dimensão, preservando a variância mais relevante dos dados. Neste caso, reduzimos para duas dimensões principais, facilitando tanto a visualização dos clusters como o desempenho dos algoritmos de agrupamento. Para algoritmos baseados em distância, como K-Means e Agrupamento Hierárquico, o PCA ajuda a reduzir ruído e redundância, possibilitando uma segmentação mais eficaz dos dados.

### Métricas de Avaliação dos Modelos de Agrupamento

Para avaliar o desempenho dos algoritmos de clustering, foram utilizadas as seguintes métricas:

1. **Silhouette Score**: Mede a qualidade dos clusters verificando o quão semelhante um ponto é ao seu próprio cluster em comparação com os outros clusters. Varia de -1 a 1, onde valores mais altos indicam clusters bem definidos e separados.

2. **Calinski-Harabasz Score**: Também conhecido como “razão da variância”, calcula a razão entre a dispersão interna dos clusters e a dispersão entre clusters. Valores mais altos indicam clusters mais densos e bem separados.

3. **Davies-Bouldin Score**: Avalia a média da similaridade entre cada cluster com o cluster mais semelhante a ele. Valores mais baixos indicam clusters com boa separação e baixa similaridade entre si.

Essas métricas oferecem diferentes perspectivas sobre a qualidade dos clusters, permitindo uma escolha fundamentada do algoritmo mais apropriado para o dataset. No estudo, selecionamos os três melhores modelos para serem armazenados e reutilizados em futuras análises, com base no desempenho dessas métricas. 

Em considerações finais percebemos que, o uso de algoritmos variados, combinado com a redução de dimensionalidade via PCA e uma avaliação abrangente de métricas, permitiu um entendimento mais completo sobre a segmentação dos dados de vinhos, destacando a eficácia e a flexibilidade das técnicas de clustering em diferentes situações e tipos de dados.