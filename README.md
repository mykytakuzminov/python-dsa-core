<div align="center">

# 🚀 Python DSA Core
Data structures and algorithms library from scratch

[![CI](https://github.com/mykytakuzminov/python-dsa-core/actions/workflows/ci.yml/badge.svg)](https://github.com/mykytakuzminov/python-dsa-core/actions/workflows/ci.yml)
[![Python Version](https://img.shields.io/badge/Python-3.14-3776AB?logo=python&logoColor=fff)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

</div>

---

## Features

- **Dynamic Array** - growable array backed by a fixed-size list
- **Stack** - LIFO, backed by dynamic array
- **Queue** - FIFO, backed by doubly linked list
- **Singly Linked List** - classic node-pointer traversal
- **Doubly Linked List** - bidirectional traversal
- **Hash Map** - separate chaining collision resolution
- **Binary Search Tree** - with BFS, DFS, and all traversals
- **Heap** - max and min variants
- **Graph** - adjacency list, directed and undirected
- **Algorithms** - searching, sorting, and recursion implementations

## Tech Highlights

- **Modern Generics** - strict static typing
- **Test Coverage** - full test suite
- **Zero Dependencies** - built using pure Python standard library
- **CI** - automated linting, type checking, and testing

## Getting Started

### Prerequisites

- `uv`

### Installation

```bash
git clone https://github.com/mykytakuzminov/python-dsa-core.git
cd python-dsa-core
uv sync
```

### Development

```bash
uv run tox          # run tests, linter and type checks
uv run pytest tests/
uv run ruff check
uv run mypy src/
```

## Tech Stack

### Core
- `Python`, `GitHub Actions`

### Dev Tools
- `pytest`, `pytest-cov`, `ruff`, `mypy`, `tox`
