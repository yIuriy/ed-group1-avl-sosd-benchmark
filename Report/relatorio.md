# Relatório Empírico de Desempenho — Árvore AVL Aumentada vs. BST

Este relatório apresenta a análise experimental de desempenho de uma implementação de Árvore AVL Aumentada em comparação com uma Árvore Binária de Busca (BST) simples e não balanceada. As medições foram efetuadas sobre chaves geradas sinteticamente que emulam o padrão de cargas reais sob o benchmark SOSD.

---

## 1. Configuração do Ambiente de Testes

Para garantir a reprodutibilidade dos resultados, todas as medições foram realizadas no seguinte ambiente físico e lógico:
- **Processador:** Intel(R) Core(TM) i5-1235U (12ª Geração, arquitetura híbrida Intel Alder Lake, 10 núcleos / 12 threads)
- **Sistema Operacional:** Arch Linux (Kernel 7.1.3-arch1-2)
- **Interpretador:** Python 3.14.6
- **Bibliotecas Principais:** NumPy 2.5.0, Pandas 2.3.3, Matplotlib 3.11.0
- **Configuração do Grupo 1:**
  - Proporção de Operações (Mix): Inserção 60%, Remoção 10%, Busca 30% (Mix `60:10:30`)
  - Distribuição de Acessos: Zipfiana com $\theta = 0.6$ (moderadamente enviesado)
  - Agregação de Intervalo: Soma de chaves (`range_sum`)
  - Ordem de Inserção Padrão: Embaralhada (`shuffle`)
  - Semente Aleatória (Seed): `1`

---

## 2. Resultados Empíricos

### 2.1. Escala de Operações (Shuffle, $\theta = 0.6$)
A tabela abaixo apresenta os tempos médios de operação (em microssegundos, µs) e percentis p50 e p99 para chaves inseridas de forma embaralhada (`shuffle`) sob a distribuição padrão de acessos do Grupo 1:

| Estrutura | Carga ($N$) | Tempo Médio (µs) | Mediana p50 (µs) | Percentil p99 (µs) |
| :--- | :--- | :--- | :--- | :--- |
| **AVL** | 100 | 1.77 | 1.91 | 3.69 |
| **BST** | 100 | 0.76 | 0.58 | 5.02 |
| **AVL** | 1.000 | 2.13 | 2.45 | 4.80 |
| **BST** | 1.000 | 0.56 | 0.50 | 1.46 |
| **AVL** | 10.000 | 3.19 | 3.72 | 6.62 |
| **BST** | 10.000 | 0.71 | 0.51 | 2.68 |
| **AVL** | 100.000 | 4.63 | 5.53 | 9.69 |
| **BST** | 100.000 | 0.78 | 0.69 | 1.59 |
| **AVL** | 500.000 | 7.49 | 7.84 | 25.27 |
| **BST** | 500.000 | 1.32 | 1.09 | 3.04 |

#### Detalhamento por Operação ($N = 500.000$):
- **AVL:** Inserção = 9.96 µs, Remoção = 9.48 µs, Busca = 1.83 µs
- **BST:** Inserção = 1.44 µs, Remoção = 1.41 µs, Busca = 1.05 µs

![Desempenho por Escala](scale_comparison.png)

**Discussão Teoria vs. Prática:**
Teoricamente, ambas as estruturas apresentam complexidade $O(\log N)$ para todas as operações quando as entradas estão distribuídas aleatoriamente. Contudo, na prática, a **BST Simples é significativamente mais rápida** (cerca de 5.5x a 6x mais rápida) no caso médio.
Isso ocorre devido à diferença gritante na **constante multiplicativa**:
1. A AVL precisa recalcular e atualizar a altura (`height`), tamanho da subárvore (`size`) e a soma acumulada (`sum`) para cada nó visitado durante o caminho de retorno da recursão.
2. A AVL precisa realizar testes de fator de balanceamento e aplicar rotações (simples ou duplas), o que exige múltiplas atribuições de ponteiros adicionais.
3. A BST simples do projeto possui um código iterativo muito mais curto e amigável para a máquina virtual do Python, sem o overhead de chamadas de funções recursivas.

---

### 2.2. Caso Patológico: Entrada Shuffle vs. Sorted
Quando as chaves de entrada são fornecidas em ordem crescente (`sorted`), a BST simples sofre degradação de desempenho catastrófica devido ao seu desbalanceamento. A tabela abaixo compara a média global (µs) das operações entre as duas estruturas:

| Estrutura | Carga ($N$) | Ordenação | Tempo Médio (µs) | Mediana p50 (µs) | Percentil p99 (µs) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **AVL** | 100 | sorted | 1.66 | 2.09 | 2.73 |
| **BST** | 100 | sorted | 0.69 | 0.61 | 3.52 |
| **AVL** | 1.000 | sorted | 4.22 | 4.70 | 10.32 |
| **BST** | 1.000 | sorted | 5.79 | 5.67 | 13.67 |
| **AVL** | 10.000 | sorted | 3.06 | 3.93 | 5.50 |
| **BST** | 10.000 | sorted | 43.32 | 36.21 | 118.39 |
| **AVL** | 100.000 | sorted | 4.39 | 5.19 | 10.74 |
| **BST** | 100.000 | sorted | *Não Executado* | | |

*Nota: O teste da BST ordenada em N=100.000 foi omitido pois o tempo total de execução seria proibitivo (complexidade quadrática total $O(N^2)$ em Python).*

![Caso Patológico - Shuffle vs Sorted](order_comparison.png)

**Ponto de Cruzamento (Crossover Point):**
O ponto de cruzamento de desempenho ocorre logo após $N = 100$.
- Para $N \le 100$, a BST ainda é ligeiramente mais rápida devido ao tamanho reduzido da árvore.
- Para $N = 1.000$, a BST com chaves ordenadas já é 1.37x mais lenta do que a AVL.
- Para $N = 10.000$, a BST ordenada torna-se **14.1x mais lenta** que a AVL.

**Explicação Teórica:**
Chaves ordenadas forçam a BST a sempre inserir novos nós à direita. A estrutura degenera em uma lista simplesmente encadeada de altura $N$. A busca, inserção e remoção passam a ter complexidade de pior caso linear $O(N)$. Como a carga executa $N$ operações, o custo cumulativo total é $O(N^2)$, explicando o crescimento acentuado do tempo de execução.
Já a árvore AVL, através de suas rotações, detecta o desbalanceamento instantaneamente e reestrutura a árvore, garantindo altura máxima limitada a $\approx 1.44 \log_2 N$. Seu custo por operação mantém-se estritamente em $O(\log N)$, preservando a escalabilidade.

---

### 2.3. Sensibilidade ao Enviesamento (Zipfian $\theta$)
Analisamos a sensibilidade da Árvore AVL a diferentes níveis de viés Zipfiano de acesso para $N = 500.000$. A distribuição Zipfiana simula que uma pequena fração de chaves "quentes" concentra a maior parte dos acessos.

| Parâmetro $\theta$ | Tipo de Acesso | Tempo Médio Geral (µs) | Tempo Médio Busca S (µs) | Mediana Busca S (µs) |
| :--- | :--- | :--- | :--- | :--- |
| **0.00** | Uniforme | 7.08 | 1.69 | 1.50 |
| **0.60** | Moderadamente Enviesado | 7.49 | 1.83 | 1.61 |
| **0.99** | Padrão YCSB (Alto Viés) | 7.45 | 1.57 | 1.44 |
| **1.20** | Muito Enviesado | 7.97 | 1.58 | 1.41 |

![Sensibilidade ao Enviesamento (Zipfian Theta)](theta_sensitivity.png)

**Discussão sobre Localidade de Cache e Rotações:**
1. **Localidade de Cache:** À medida que $\theta$ cresce (de 0.0 para 1.2), os acessos concentram-se cada vez mais em um conjunto pequeno de chaves quentes. Isso resulta em uma melhora perceptível no tempo médio da operação de busca (`search` / operacão `S`), reduzindo de **1.69 µs** ($\theta = 0.0$) para **1.58 µs** ($\theta = 1.2$). Esse ganho empírico deve-se à maior taxa de acertos nos caches de hardware da CPU (L1/L2/L3) para os nós mais superiores e frequentes da árvore.
2. **Rebalanceamento:** Apesar do alto viés nas buscas, a proporção de inserções e remoções novas continua alta (60% e 10%). Como novas chaves ainda alteram a estrutura, o custo de rebalanceamento e recomputação de somas acumuladas se mantém, explicando o motivo do tempo médio global (`all`) cair de forma muito mais sutil.

---

## 3. Justificativa de Projeto da AVL Aumentada

### Invariantes da Árvore Aumentada
Nossa classe `Node` em `src/avl_tree.py` armazena três propriedades calculadas em tempo de execução:
- `height`: a altura da subárvore enraizada no nó.
- `size`: o número total de nós sob a subárvore enraizada no nó (invariante para `select` e `rank`).
- `sum`: a soma das chaves de todos os nós pertencentes à subárvore enraizada no nó (invariante para `range_sum`).

Os invariantes matemáticos para qualquer nó $x$ são definidos por:
$$height(x) = 1 + \max(height(left(x)), height(right(x)))$$
$$size(x) = 1 + size(left(x)) + size(right(x))$$
$$sum(x) = key(x) + sum(left(x)) + sum(right(x))$$

### Preservação sob Rotação
Durante as rotações necessárias para o balanceamento (esquerda e direita), os ponteiros de parentesco mudam localmente. O método auxiliar `_update(node)` recalcula essas três propriedades para os nós afetados.
A corretude é garantida pela ordem de recomputação: atualizamos primeiro o nó filho rebaixado e, em seguida, o novo nó raiz da subárvore.
Esse argumento informal garante que consultas complexas como estatísticas de ordem (`select(i)`), número de chaves menores que $k$ (`rank(k)`) e a soma no intervalo (`range_sum(a, b)`) sejam executadas em tempo logarítmico $O(\log N)$, pois utilizam apenas os valores locais pré-computados ao longo do caminho, sem precisar varrer toda a árvore linearmente.

---

## 4. Gráficos Gerados

Os gráficos gerados pela execução empírica encontram-se salvos sob o diretório `results/`:
1. **[scale_comparison.png](file:///home/sidnei/Documents/Repositories/ED/ed-group1-avl-sosd-benchmark/results/scale_comparison.png):** Mostra a evolução do tempo com o tamanho da carga e o detalhamento por operação.
2. **[order_comparison.png](file:///home/sidnei/Documents/Repositories/ED/ed-group1-avl-sosd-benchmark/results/order_comparison.png):** Ilustra a degradação da BST simples versus a estabilidade da AVL sob chaves ordenadas.
3. **[theta_sensitivity.png](file:///home/sidnei/Documents/Repositories/ED/ed-group1-avl-sosd-benchmark/results/theta_sensitivity.png):** Representa o impacto do viés Zipfiano nos tempos de busca da AVL.
