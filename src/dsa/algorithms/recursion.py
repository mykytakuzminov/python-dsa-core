from collections.abc import Sequence
from typing import Any


def recursive_sum(arr: list[Any]) -> int | float:
    """
    Recursively calculates the sum of all numeric elements in a list.

    Args:
        arr: A list of integers or floats.

    Returns:
        The sum of all elements. Returns 0 if the list is empty.

    Raises:
        TypeError: If any element in the list is not numeric.
    """
    if not arr:
        return 0

    if not isinstance(arr[0], (int, float)):
        raise TypeError(f"Expected number, got {type(arr[0]).__name__}.")

    return arr[0] + recursive_sum(arr[1:])


def recursive_max(arr: list[int | float]) -> int | float:
    """
    Recursively determines the maximum element in a list.

    Args:
        arr: A list of integers or floats.

    Returns:
        The maximum element in the list.

    Raises:
        ValueError: If the list is empty.
        TypeError: If any element in the list is not numeric.
    """
    if not arr:
        raise ValueError("Expected a non-empty list, got an empty list.")

    if not isinstance(arr[0], (int, float)):  # type: ignore
        raise TypeError(f"Expected number, got {type(arr[0]).__name__}.")

    if len(arr) == 1:
        return arr[0]

    rest_max = recursive_max(arr[1:])
    return arr[0] if arr[0] > rest_max else rest_max


def recursive_reverse(arr: list[Any]) -> list[Any]:
    """
    Recursively returns a new list with elements in reverse order.

    Args:
        arr: A list of any elements.

    Returns:
        A new list containing the elements in reverse order.
    """
    if not arr:
        return []

    return [arr[-1], *recursive_reverse(arr[:-1])]


def factorial(n: int) -> int:
    """
    Compute the factorial of a number recursively.

    Args:
        n: Non-negative integer.

    Returns:
        Factorial of n.

    Raises:
        TypeError: If `n` is not an integer.
        ValueError: If `n` is negative.
    """
    if not isinstance(n, int):  # type: ignore
        raise TypeError(f"Expected integer, got {type(n).__name__}.")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n in (0, 1):
        return 1

    return n * factorial(n - 1)


def fibonacci(n: int) -> int:
    """
    Compute the n-th Fibonacci number recursively.

    Args:
        n: Index (non-negative) of the Fibonacci sequence.

    Returns:
        The n-th Fibonacci number.

    Raises:
        TypeError: If `n` is not an integer.
        ValueError: If `n` is negative.
    """
    if not isinstance(n, int):  # type: ignore
        raise TypeError(f"Expected integer, got {type(n).__name__}.")
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


def sum_nested_list(arr: Sequence[int | float | Sequence[int | float]]) -> int | float:
    """
    Recursively compute the sum of all numbers in a nested list.

    Args:
        arr: List that may contain integers, floats, or other nested lists.

    Returns:
        The total sum of all numeric elements.

    Raises:
        TypeError: If an element is neither a number nor a list.
    """
    result: int | float = 0
    for el in arr:
        if isinstance(el, list):
            result += sum_nested_list(el)
        elif isinstance(el, (int, float)):  # type: ignore
            result += el
        else:
            raise TypeError(f"Unsupported element type: {type(el).__name__}")
    return result
