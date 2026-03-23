# Python DSA Core

[![CI](https://github.com/mykytakuzminov/python-dsa-core/actions/workflows/ci.yml/badge.svg)](https://github.com/mykytakuzminov/python-dsa-core/actions)
![Python](https://img.shields.io/badge/python-3.14-3776ab?logo=python&logoColor=white)
![uv](https://img.shields.io/badge/uv-package%20manager-de5fe9)
![mypy](https://img.shields.io/badge/mypy-strict-2a6db5)
![ruff](https://img.shields.io/badge/ruff-linter-d7ff64?logoColor=black)
![tox](https://img.shields.io/badge/tox-automation-ce3262?logo=python&logoColor=white)

> Hand-crafted implementations of classical data structures and algorithms in Python — built with strict typing, clean architecture, and modern tooling.
> 
## 📦 Data Structures

| Structure | Description |
|---|---|
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
- **[pytest](https://docs.pytest.org/)** — 246 tests with parametrization and fixtures
- **[github actions](https://github.com/features/actions)** — CI on every push and pull request

## 🚀 Getting Started
```bash
git clone https://github.com/mykytakuzminov/python-dsa-core.git
cd python-dsa-core
uv sync
uv run tox
```
