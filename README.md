# ED AVL SOSD Benchmark

Final project for the Data Structures course.

This repository implements and benchmarks an augmented AVL tree using SOSD datasets. It also includes a simple unbalanced BST as a baseline.

---

## Group Configuration

| Parameter       | Value      |
| --------------- | ---------- |
| Dataset         | `amzn`     |
| Theta           | `0.6`      |
| Operation mix   | `60:10:30` |
| Range aggregate | `sum`      |
| Insert order    | `shuffle`  |
| Seed            | `1`        |

`range_agg(a, b)` returns the sum of keys in `[a, b]`.

---

## Goals

* Implement an augmented AVL tree.
* Maintain AVL invariants and subtree metadata (`size`, `sum`).
* Validate correctness with traces.
* Benchmark performance under different workloads.
* Compare against an unbalanced BST.

---

## Data Structure

Each node stores:

```python
key
left
right
height
size
sum
```

`height` ensures balance, `size` supports rank/select, and `sum` supports range queries.

---

## Repository Structure

```text
.
├── data/
├── prompts/
├── results/
├── scripts/
│   ├── gen_workload.py
│   └── plot_results.py
├── src/
│   ├── avl_tree.py
│   ├── bst_tree.py
│   ├── benchmark.py
│   └── run_trace.py
├── tests/
├── README.md
└── requirements.txt
```

---

## Main Components

* `avl_tree.py`: AVL implementation with insert, delete, search, rank, select, range_sum.
* `bst_tree.py`: Unbalanced BST baseline.
* `run_trace.py`: Executes workload traces.
* `benchmark.py`: Measures performance.
* `plot_results.py`: Generates graphs.

---

## Setup

```bash
python -m venv .venv
```

Activate:

```bash
# Windows
.venv\Scripts\activate

# Linux/macOS
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Suggested:

```text
numpy
pandas
matplotlib
```

---

## Running a Trace

Example trace:

```text
I 10
I 5
S 10
D 10
S 10
```

Run:

```bash
python src/run_trace.py --tree avl --trace traces/manual.trace --out results/manual.out
```

Output:

```text
10 FOUND
10 NOT_FOUND
```

---

## Workload Generation

```bash
python scripts/gen_workload.py generate \
  --keys data/books_200M_uint32 \
  --format sosd \
  --key-bytes 4 \
  --max-load 10000 \
  --out traces/g1_small \
  --ops 50000 \
  --universe 10000 \
  --mix 60:10:30 \
  --theta 0.6 \
  --seed 1
```

---

## Verification

```bash
python scripts/gen_workload.py verify \
  --expected traces/g1_small.expected \
  --candidate results/g1_small.out
```

---

## Benchmark Plan

Compare:

* AVL vs BST
* `shuffle` vs `sorted`
* Different sizes and theta values (`0.0`, `0.6`, `0.99`, `1.2`)

Suggested sizes:

```text
10k, 50k, 100k, 500k, 1M operations
```

---

## Expected Analysis

Discuss:

* AVL balance and rotations
* BST degradation with sorted inserts
* Impact of `theta`
* Differences between theory and practice

---

## Prompt Log

Store all AI prompts in `prompts/` with date, tool, goal, and result.

---

## Status

* [ ] AVL implementation
* [ ] Trace runner
* [ ] BST baseline
* [ ] Tests
* [ ] Workload generation
* [ ] Verification
* [ ] Benchmarks
* [ ] Graphs
* [ ] Report
* [ ] Presentation

---

## Authors

* Iuri da Silva Fernandes — AVL
* Lara Sarotti da Silva Rios — runner/tests/BST
*# ED AVL SOSD Benchmark

Final project for the Data Structures course.

This repository implements and benchmarks an augmented AVL tree using SOSD datasets. It also includes a simple unbalanced BST as a baseline.

---

## Group Configuration

| Parameter       | Value      |
| --------------- | ---------- |
| Dataset         | `amzn`     |
| Theta           | `0.6`      |
| Operation mix   | `60:10:30` |
| Range aggregate | `sum`      |
| Insert order    | `shuffle`  |
| Seed            | `1`        |

`range_agg(a, b)` returns the sum of keys in `[a, b]`.

---

## Goals

* Implement an augmented AVL tree.
* Maintain AVL invariants and subtree metadata (`size`, `sum`).
* Validate correctness with traces.
* Benchmark performance under different workloads.
* Compare against an unbalanced BST.

---

## Data Structure

Each node stores:

```python
key
left
right
height
size
sum
```

`height` ensures balance, `size` supports rank/select, and `sum` supports range queries.

---

## Repository Structure

```text
.
├── data/
├── prompts/
├── results/
├── scripts/
│   ├── gen_workload.py
│   └── plot_results.py
├── src/
│   ├── avl_tree.py
│   ├── bst_tree.py
│   ├── benchmark.py
│   └── run_trace.py
├── tests/
├── README.md
└── requirements.txt
```

---

## Main Components

* `avl_tree.py`: AVL implementation with insert, delete, search, rank, select, range_sum.
* `bst_tree.py`: Unbalanced BST baseline.
* `run_trace.py`: Executes workload traces.
* `benchmark.py`: Measures performance.
* `plot_results.py`: Generates graphs.

---

## Setup

```bash
python -m venv .venv
```

Activate:

```bash
# Windows
.venv\Scripts\activate

# Linux/macOS
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Suggested:

```text
numpy
pandas
matplotlib
```

---

## Running a Trace

Example trace:

```text
I 10
I 5
S 10
D 10
S 10
```

Run:

```bash
python src/run_trace.py --tree avl --trace traces/manual.trace --out results/manual.out
```

Output:

```text
10 FOUND
10 NOT_FOUND
```

---

## Workload Generation

```bash
python scripts/gen_workload.py generate \
  --keys data/books_200M_uint32 \
  --format sosd \
  --key-bytes 4 \
  --max-load 10000 \
  --out traces/g1_small \
  --ops 50000 \
  --universe 10000 \
  --mix 60:10:30 \
  --theta 0.6 \
  --seed 1
```

---

## Verification

```bash
python scripts/gen_workload.py verify \
  --expected traces/g1_small.expected \
  --candidate results/g1_small.out
```

---

## Benchmark Plan

Compare:

* AVL vs BST
* `shuffle` vs `sorted`
* Different sizes and theta values (`0.0`, `0.6`, `0.99`, `1.2`)

Suggested sizes:

```text
10k, 50k, 100k, 500k, 1M operations
```

---

## Expected Analysis

Discuss:

* AVL balance and rotations
* BST degradation with sorted inserts
* Impact of `theta`
* Differences between theory and practice

---

## Prompt Log

Store all AI prompts in `prompts/` with date, tool, goal, and result.

---

## Status

* [ ] AVL implementation
* [ ] Trace runner
* [ ] BST baseline
* [ ] Tests
* [ ] Workload generation
* [ ] Verification
* [ ] Benchmarks
* [ ] Graphs
* [ ] Report
* [ ] Presentation

---

## Authors

* Iuri da Silva Fernandes — AVL
* Lara Sarotti da Silva Rios — runner/tests/BST
* Sidnei Correa Junior — benchmarks/report

---

## License

Academic use only.
 — benchmarks/report

---

## License

Academic use only.

