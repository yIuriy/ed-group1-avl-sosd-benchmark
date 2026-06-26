# AGENTS.md

## Mission

This repository is a Data Structures final project.

The goal is to implement, validate, and benchmark an augmented AVL tree using SOSD datasets while keeping the work understandable and defensible by the group.

AI tools such as Codex and Agy may help with implementation, review, debugging, and documentation, but they must support learning, not replace reasoning.

---

## Group Configuration

* Dataset: `amzn`
* Theta: `0.6`
* Operation mix: `60:10:30`
* Range aggregate: `sum`
* Insert order: `shuffle`
* Seed: `1`

The main structure is an augmented AVL tree with:

* `insert(k)`
* `delete(k)`
* `search(k)`
* `rank(k)`
* `select(i)`
* `range_sum(a, b)`

For this group, `range_sum(a, b)` must return the sum of all keys in the interval `[a, b]`.

---

## Agent Rules

1. Read `README.md` and `AGENTS.md` before making changes.
2. Make small and focused changes.
3. Do not rewrite unrelated files.
4. Prefer simple, readable Python.
5. Do not add dependencies unless necessary.
6. Do not download SOSD datasets.
7. Do not run expensive benchmarks unless explicitly requested.
8. Do not fabricate benchmark results.
9. Do not hide AI usage.
10. Keep responses short and practical.

---

## Token Economy

Before editing, inspect only the files needed for the task.

Avoid:

* opening many unrelated files;
* pasting full files in the response;
* large explanations unless requested;
* broad refactors;
* implementing extra features outside the prompt.

After editing, report only:

* files created;
* files modified;
* summary of changes;
* how to verify manually.

---

## Prompt Logs

All meaningful AI-assisted work must be logged in `prompts/`.

Each log should include:

```markdown
# Prompt Log — Task Name

## Date

YYYY-MM-DD

## Tool

Codex / Agy / ChatGPT / Other

## Goal

Short description.

## Prompt

Original prompt.

## Result

Short summary of what changed or was decided.

## Notes

Manual corrections, assumptions, or limitations.
```

Do not store secrets, credentials, tokens, or private data.

---

## Project Structure

Expected structure:

```text
.
├── data/
├── prompts/
├── results/
├── scripts/
├── src/
├── tests/
├── README.md
├── AGENTS.md
├── pyproject.toml
└── .gitignore
```

---

## Implementation Notes

The AVL node should store:

* `key`
* `left`
* `right`
* `height`
* `size`
* `sum`

After insertions, deletions, and rotations, always update:

* `height`
* `size`
* `sum`

The unbalanced BST in `src/bst_tree.py` is only a baseline for comparison.

---

## Testing and Benchmarking

Start with small manual tests before using SOSD workloads.

Do not run heavy benchmarks as normal tests.

Benchmark results must be real measurements from the group machine.

Generated data, traces, and large result files should not be committed.

---

## Final Reminder

Correctness comes first.

The group must be able to explain every important implementation decision in the oral defense.
