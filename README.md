# Data Structures & Algorithms (Python)

[![CI Status](https://github.com/mykytakuzminov/data-structures-and-algorithms/actions/workflows/ci.yml/badge.svg)](https://github.com/mykytakuzminov/data-structures-and-algorithms/actions)
![Python Version](https://img.shields.io/badge/python-3.14-blue.svg)
![Docker: Ready](https://img.shields.io/badge/docker-ready-2496ed.svg?logo=docker&logoColor=white)
![Tests: Pytest](https://img.shields.io/badge/tests-pytest-white.svg?logo=pytest&logoColor=white&labelColor=0a9edc)
![Types: MyPy](https://img.shields.io/badge/types-mypy-blue.svg?labelColor=2f4f4f)
![Automation: Tox](https://img.shields.io/badge/automation-tox-white.svg?logo=python&logoColor=white&labelColor=ce3262)
![Linting: Ruff](https://img.shields.io/badge/linting-ruff-000000.svg?logo=python&logoColor=white)

## 📝 Overview

This repository is a high-standard educational ecosystem dedicated to the implementation of classical data structures and algorithms. The project emphasizes **modern software engineering practices**, including strict type safety, comprehensive automation, and clean code architecture.

## 🚀 Engineering Stack

* **[Python 3.14](https://www.python.org/)**: Core language utilizing the latest features and performance improvements.
* **[Docker](https://www.docker.com/)**: Containerization for environment parity and simplified deployment.
* **[Pytest](https://docs.pytest.org/)**: Advanced unit testing with heavy use of parametrization.
* **[MyPy](http://mypy-lang.org/)**: Strict static type checking to enforce architectural integrity.
* **[Ruff](https://github.com/astral-sh/ruff)**: Ultra-fast linter and formatter for PEP 8 compliance.
* **[Tox](https://tox.wiki/)**: Multi-environment orchestration for consistent testing.
* **[GitHub Actions](https://github.com/features/actions)**: CI/CD pipeline validating every commit and pull request.

## 📦 Implementations

### Data Structures
- [x] **Stack** (LIFO)
- [x] **Queue** (FIFO)
- [x] **Linked Lists** (Singly & Doubly)
- [x] **Hash Map** (with chaining for collisions)
- [x] **Binary Search Tree**
- [x] **Heap** (Max & Min)
- [x] **Graph** (Adjacency List implementation)

### Algorithms
- [x] **Binary Search** (Generic implementation)
- [x] **Recursion** (Factorial, Fibonacci, Nested Sums)
- [x] **Sorting**
    - [x] *Simple*: Bubble, Insertion, Selection
    - [x] *Efficient*: Merge Sort, Quick Sort
    - [x] *Non-Comparison*: Counting Sort

## ⚙️ Development Setup

Follow these steps to set up the project locally for development and testing. These instructions cover **macOS**, **Linux**, and **Windows**.

### 1. Clone

Start by cloning the repository to your local machine and navigating into the project directory.

```bash
git clone https://github.com/mykytakuzminov/data-structures-and-algorithms.git
cd data-structures-and-algorithms
```

### 2. Environment Setup

It is highly recommended to use a virtual environment to keep dependencies isolated. Choose the commands that match your operating system and shell.

#### Windows (PowerShell)

**Create a virtual environment**

```powershell
python -m venv .venv
```

**Activate the environment**

```powershell
.\.venv\Scripts\Activate.ps1
```

#### macOS / Linux

**Create a virtual environment**

```bash
python3 -m venv .venv
```

**Activate the environment**

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

This project follows modern Python packaging standards. Installing the package in editable mode ensures that any changes you make to the source code are instantly available without needing to reinstall.

**Upgrade pip to the latest version**

```bash
pip install --upgrade pip
```

**Install the package in editable mode with development dependencies**

```bash
pip install -e .
```

### 4. Running Tests & Quality Control

To maintain high code quality, this project uses **Tox** to automate testing and linting in isolated environments.

**Run everything at once**

```bash
tox
```

**Run only unit tests**

```bash
tox -e py314
```

**Run only linter (Ruff)**

```bash
tox -e ruff
```

**Run only type checking (MyPy)**

```bash
tox -e mypy
```
**

## 🐳 Docker Quick Start (Recommended)

The easiest way to run tests and ensure environment parity is using Docker. You don't need Python or any dependencies installed locally.

### 1. Build the image
```bash
docker build -t data-structures-and-algorithms .
```

### 2. Run the tests
```bash
docker run --rm data-structures-and-algorithms
```

