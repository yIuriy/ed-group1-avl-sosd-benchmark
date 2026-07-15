# ED AVL SOSD Benchmark

Final project for the Data Structures course focused on an augmented AVL tree with SOSD-based workloads.

## Group 1 Configuration

| Parameter | Value |
| --- | --- |
| Dataset | `amzn` |
| Theta | `0.6` |
| Operation mix | `60:10:30` |
| Range aggregate | `sum` |
| Insert order | `shuffle` |
| Seed | `1` |

For this project, `range_sum(a, b)` must return the sum of all keys in `[a, b]`.

## Repository Guidance

Project workflow and AI usage rules are documented in `AGENTS.md`.

## Setup with Poetry

```bash
poetry install
```

Running the Project

You can run the benchmarks, trace execution, and plotting using either the registered Poetry shortcuts or by invoking Python modules directly.

### 1. Benchmarking (AVL vs BST)

To run the complete parameter sweep:
- **Using Poetry shortcut:**
  ```bash
  poetry run benchmark --sweep
  ```
- **Using Python module:**
  ```bash
  poetry run python3 -m src.benchmark --sweep
  ```
- **Using Python script path:**
  ```bash
  poetry run python3 src/benchmark.py --sweep
  ```

### 2. Executing Workload Traces

To run a single workload trace file:
- **Using Poetry shortcut:**
  ```bash
  poetry run run-trace --tree avl --trace <path_to_trace> --out <path_to_out>
  ```
- **Using Python module:**
  ```bash
  poetry run python3 -m src.run_trace --tree avl --trace <path_to_trace> --out <path_to_out>
  ```

### 3. Plotting Results

To generate comparative graphs:
- **Using Poetry shortcut:**
  ```bash
  poetry run plot-results
  ```
- **Using Python module:**
  ```bash
  poetry run python3 -m scripts.plot_results
  ```

### 4. Running Tests

To run the project's unit tests:
```bash
poetry run pytest
```

## Current Status

- [x] Initial project structure
- [x] Poetry configuration
- [x] Module and CLI skeletons
- [x] AVL implementation
- [x] BST baseline implementation
- [x] Trace execution logic
- [x] Benchmarks
- [x] Plotting logic
- [x] Tests
