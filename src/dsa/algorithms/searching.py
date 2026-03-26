from typing import Any, Protocol


class Comparable(Protocol):
    def __lt__(self, other: Any, /) -> bool: ...
    def __gt__(self, other: Any, /) -> bool: ...
    def __eq__(self, other: object, /) -> bool: ...


def binary_search[T: Comparable](arr: list[T], value: T) -> bool:
    left: int = 0
    right: int = len(arr) - 1

    while left <= right:
        # Avoids integer overflow vs (left + right) // 2
        m = left + ((right - left) // 2)

        if value == arr[m]:
            return True
        elif value < arr[m]:
            right = m - 1
        else:
            left = m + 1

    return False
