from collections.abc import Sequence
from typing import Any


def recursive_sum(arr: list[Any]) -> int | float:
    if not arr:
        return 0

    if not isinstance(arr[0], (int, float)):
        raise TypeError("Number expected")

    return arr[0] + recursive_sum(arr[1:])


def recursive_max(arr: list[int | float]) -> int | float:
    if not arr:
        raise ValueError("List is empty")

    if not isinstance(arr[0], (int, float)):  # type: ignore
        raise TypeError("Number expected")

    if len(arr) == 1:
        return arr[0]

    rest_max = recursive_max(arr[1:])
    return arr[0] if arr[0] > rest_max else rest_max


def recursive_reverse(arr: list[Any]) -> list[Any]:
    if not arr:
        return []

    return [arr[-1], *recursive_reverse(arr[:-1])]


def factorial(n: int) -> int:
    if not isinstance(n, int):  # type: ignore
        raise TypeError("Integer expected")
    if n < 0:
        raise ValueError("Negative input")
    if n in (0, 1):
        return 1

    return n * factorial(n - 1)


def fibonacci(n: int) -> int:
    if not isinstance(n, int):  # type: ignore
        raise TypeError("Integer expected")
    if n < 0:
        raise ValueError("Negative input")
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


def sum_nested_list(arr: Sequence[int | float | Sequence[int | float]]) -> int | float:
    result: int | float = 0
    for el in arr:
        if isinstance(el, list):
            result += sum_nested_list(el)
        elif isinstance(el, (int, float)):  # type: ignore
            result += el
        else:
            raise TypeError("Unsupported type")
    return result
