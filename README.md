# Python DSA Core

![Python](https://img.shields.io/badge/Python-24292e?logo=python&logoColor=fff)
![Pytest](https://img.shields.io/badge/Pytest-24292e?logo=pytest&logoColor=fff)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-24292e?logo=github-actions&logoColor=fff)

> A robust, enterprise-grade educational library containing fundamental Data Structures and Algorithms implemented completely from scratch in Python. Enforces strict static type hinting and guarantees 100% test coverage.

## 🗺️ Key Highlights

| Criterion | Specification |
|---|---|
| **Code Coverage** | 🎯 **100% Test Coverage** verified via `pytest-cov` across 300+ unit tests. |
| **Type Safety** | Enforced strict static analysis via `mypy` with zero implicit type definitions. |
| **Quality Control** | Automated linting, formatting, and multi-environment validation managed via `ruff` and `tox`. |
| **Zero Dependencies** | Built using pure Python standard library to demonstrate raw algorithm design and memory layout principles. |

## 🛠️ Tech Stack

- **[Python](https://www.python.org/)** — Core language focusing on data structures design and memory layouts.
- **[Pytest](https://docs.pytest.org/)** — Advanced testing framework used to achieve and maintain 100% code coverage.
- **[GitHub Actions](https://github.com/features/actions)** — Automated CI/CD pipeline executing the verification suite on every push and pull request.
  
## 📦 Implemented Modules

### 💾 Data Structures

| Structure | Description |
|---|---|
| Dynamic Array | Growable array backed by a fixed-size list |
| Stack | LIFO — backed by dynamic array |
| Queue | FIFO — backed by doubly linked list |
| Singly Linked List | Classic node-pointer traversal |
| Doubly Linked List | Bidirectional traversal |
| Hash Map | Separate chaining collision resolution |
| Binary Search Tree | With BFS, DFS, and all traversals |
| Heap | Max and Min variants |
| Graph | Adjacency list, directed and undirected |

### ⚙️ Algorithms
| Category | Implementations |
|---|---|
| Searching | Binary Search |
| Sorting | Bubble, Insertion, Selection, Merge, Quick, Counting |
| Recursion | Factorial, Fibonacci, Sum, Max, Reverse, Nested Sum |

## 🏗️ Technical Architecture & Design Principles

Unlike typical competitive programming scripts, this core library treats computer science fundamentals with industrial code-quality standards:

1. **Strict Type Definitions:** Leveraging Python's `typing` module (`Generic`, `TypeVar`), every structure handles broad ranges of data types safely while strictly preventing type runtime issues.
2. **Deterministic Quality Pipelines:** The project setup fully abstracts testing routines into decoupled layers. This ensures that every pointer manipulation in the custom data structures is thoroughly stress-tested against edge cases (empty collections, single-element structures, overflow conditions).

## 🚀 Getting Started

### Local Setup

1. Clone the repository and navigate into the project directory:
```bash
git clone https://github.com/mykytakuzminov/python-dsa-core.git
cd python-dsa-core
```

2. Initialize your workspace using the ultra-fast Python package toolchain:
```bash
uv sync
```

## 🔧 Testing & Quality Assurance

The validation loop runs automatically inside GitHub Actions on every integration cycle. You can trigger the verification pipeline locally using the following commands:

* **Run Everything (Tox):** Enforces tests, linters, and checkers in isolated environments.
```bash
uv run tox
```

* **Unit & Integration Tests:** Driven by `pytest` with async database isolation.
```bash
uv run pytest tests/
```

* **Linter & Code Formatting:** Managed by `ruff`.
```bash
uv run ruff check
```

* **Strict Type Auditing:** Evaluated via mypy.
```bash
uv run mypy src/
```
