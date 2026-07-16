# Prompt Log — Benchmarks, Gráficos e Relatório

## Date

2026-07-12

## Tool

Antigravity (Gemini)

## Goal

Desenvolver a infraestrutura de medição de desempenho, gerar gráficos comparativos e elaborar o relatório empírico para o projeto de Estruturas de Dados (Pessoa 3).

## Prompt

```text
take a look into @[gm-sidnei/projeto_final_estruturas_de_dados.pdf] and @[gm-sidnei/gen_workload_1.py] , and the repository @[ed-group1-avl-sosd-benchmark] . We must do this part (is in portuguese but keep the pattern of the project) ## Pessoa 3 — Benchmarks, Gráficos e Relatório

*Responsabilidade:* medir desempenho, gerar gráficos e escrever a análise.

### Tarefas

* Criar script de benchmark.
* Medir:

  * tempo médio por operação;
  * p50;
  * p99;
  * tempo de insert;
  * tempo de delete;
  * tempo de search.
* Comparar:

  * AVL vs BST simples;
  * entrada shuffle vs sorted;
  * diferentes valores de theta.
* Gerar gráficos dos resultados.
* Escrever o relatório empírico.
* Organizar os prompts usados com IA.
* Preparar a apresentação oral.

### Arquivos principais

text
src/benchmark.py
scripts/plot_results.py
results/
relatorio.md
prompts/
```

## Result

1. Criado o script `src/benchmark.py` com suporte para execução de traces individuais e sweeps completos dos parâmetros de tamanho, árvore, ordem de inserção e theta.
2. Criado o script `scripts/plot_results.py` para gerar os três gráficos de análise utilizando `pandas` e `matplotlib`:
   - `results/scale_comparison.png`: Escala AVL vs BST em tempo médio geral e detalhado por operação.
   - `results/order_comparison.png`: Comparação de caso patológico com chaves ordenadas.
   - `results/theta_sensitivity.png`: Sensibilidade ao viés Zipfiano na AVL.
3. Executado o sweep de benchmarks completo gerando `results/benchmark_results.csv` e plotados os gráficos correspondentes.
4. Elaborado o relatório empírico completo `relatorio.md` em português, integrando as medições físicas e a teoria correspondente.

## Notes

- As chaves reais do SOSD não foram baixadas devido à restrição do projeto, utilizando-se a geração de chaves sintéticas integrada do `gen_workload_1.py` para a simulação empírica.
- O tempo máximo para o sweep da BST com ordenação `sorted` foi limitado a $N = 10000$ para evitar execuções excessivamente longas (complexidade quadrática $O(N^2)$).
