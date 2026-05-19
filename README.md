# Python DSA Core

![Python](https://img.shields.io/badge/Python-376996?logo=python&logoColor=fff)
![Uv](https://img.shields.io/badge/Uv-376996?logo=uv&logoColor=fff)
![Mypy](https://img.shields.io/badge/Mypy-376996?logo=python&logoColor=fff)
![Ruff](https://img.shields.io/badge/Ruff-376996?logo=ruff&logoColor=fff)
![Tox](https://img.shields.io/badge/Tox-376996?logo=python&logoColor=fff)
![Pytest](https://img.shields.io/badge/Pytest-376996?logo=pytest&logoColor=fff)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-376996?logo=github-actions&logoColor=fff)

> Hand-crafted implementations of classical data structures and algorithms in Python — built with strict typing, clean architecture, and modern tooling.
> 
## 📦 Data Structures

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

## ⚙️ Algorithms
| Category | Implementations |
|---|---|
| Searching | Binary Search |
| Sorting | Bubble, Insertion, Selection, Merge, Quick, Counting |
| Recursion | Factorial, Fibonacci, Sum, Max, Reverse, Nested Sum |

## 🛠️ Tech Stack
Built with a production-grade Python toolchain:
- **[python](https://www.python.org/)** — core language, 3.14 with the latest features
- **[uv](https://github.com/astral-sh/uv)** — blazing fast package and environment management
- **[mypy](http://mypy-lang.org/)** — strict static type checking across the entire codebase
- **[ruff](https://github.com/astral-sh/ruff)** — linting and formatting in one tool
- **[tox](https://tox.wiki/)** — automated testing across isolated environments
- **[pytest](https://docs.pytest.org/)** — 293 tests with parametrization and fixtures
- **[github actions](https://github.com/features/actions)** — CI on every push and pull request

## 🚀 Getting Started
```bash
git clone https://github.com/mykytakuzminov/python-dsa-core.git
cd python-dsa-core
uv sync
uv run tox
```
