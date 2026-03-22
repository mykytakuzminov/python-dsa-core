from typing import Any, Protocol, TypeVar


class Comparable(Protocol):
    """Protocol for objects that support comparison operations."""

    def __lt__(self, other: Any, /) -> bool: ...
    def __gt__(self, other: Any, /) -> bool: ...
    def __eq__(self, other: object, /) -> bool: ...


T = TypeVar("T", bound=Comparable)


def binary_search[T: Comparable](arr: list[T], value: T) -> bool:
    """
    Performs a binary search on a sorted list.

    Args:
        arr: Sorted list of comparable elements (int, str, etc.).
        val: Value to find.

    Returns:
        True if found, False otherwise.
    """
    left: int = 0
    right: int = len(arr) - 1

    while left <= right:
        m = left + ((right - left) // 2)

        if value == arr[m]:
            return True
        elif value < arr[m]:
            right = m - 1
        else:
            left = m + 1

    return False
