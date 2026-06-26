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

Useful entry points:

```bash
poetry run run-trace --help
poetry run benchmark --help
poetry run plot-results --help
```

## Current Status

- [x] Initial project structure
- [x] Poetry configuration
- [x] Module and CLI skeletons
- [ ] AVL implementation
- [ ] BST baseline implementation
- [ ] Trace execution logic
- [ ] Benchmarks
- [ ] Plotting logic
- [ ] Tests
