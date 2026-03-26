from typing import Any, Protocol


class Comparable(Protocol):
    def __lt__(self, other: Any, /) -> bool: ...
    def __gt__(self, other: Any, /) -> bool: ...
    def __eq__(self, other: object, /) -> bool: ...
    def __le__(self, other: Any, /) -> bool: ...
    def __ge__(self, other: Any, /) -> bool: ...


def bubble_sort[T: Comparable](arr: list[T]) -> None:
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(1, n - i):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                swapped = True
        # Early exit if no swaps occurred
        if not swapped:
            break


def insertion_sort[T: Comparable](arr: list[T]) -> None:
    n = len(arr)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break


def selection_sort[T: Comparable](arr: list[T]) -> None:
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


def merge_sort[T: Comparable](arr: list[T]) -> None:
    if len(arr) <= 1:
        return
    _merge_sort_partition(arr, 0, len(arr) - 1)


def quick_sort[T: Comparable](arr: list[T]) -> None:
    if len(arr) <= 1:
        return
    _quick_sort_helper(arr, 0, len(arr) - 1)


def counting_sort(arr: list[int]) -> None:
    if len(arr) <= 1:
        return

    max_val = max(arr)
    counts = [0] * (max_val + 1)

    for x in arr:
        counts[x] += 1

    i = 0
    for val, count in enumerate(counts):
        while count > 0:
            arr[i] = val
            i += 1
            count -= 1


def _merge_sort_helper[T: Comparable](
    arr: list[T], left: int, mid: int, right: int
) -> None:
    L = arr[left : mid + 1]
    R = arr[mid + 1 : right + 1]

    li = ri = 0
    curr = left

    while li < len(L) and ri < len(R):
        if L[li] <= R[ri]:
            arr[curr] = L[li]
            li += 1
        else:
            arr[curr] = R[ri]
            ri += 1
        curr += 1

    while li < len(L):
        arr[curr] = L[li]
        li += 1
        curr += 1

    while ri < len(R):
        arr[curr] = R[ri]
        ri += 1
        curr += 1


def _merge_sort_partition[T: Comparable](arr: list[T], left: int, right: int) -> None:
    if left < right:
        mid = (left + right) // 2
        _merge_sort_partition(arr, left, mid)
        _merge_sort_partition(arr, mid + 1, right)
        _merge_sort_helper(arr, left, mid, right)


def _quick_sort_helper[T: Comparable](arr: list[T], left: int, right: int) -> None:
    if left < right:
        pi = _quick_sort_partition(arr, left, right)
        _quick_sort_helper(arr, left, pi - 1)
        _quick_sort_helper(arr, pi + 1, right)


def _quick_sort_partition[T: Comparable](arr: list[T], left: int, right: int) -> int:
    pivot = arr[right]  # Last element as pivot
    j = left - 1
    for i in range(left, right):
        if arr[i] <= pivot:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[j + 1], arr[right] = arr[right], arr[j + 1]  # Place pivot in final position
    return j + 1
