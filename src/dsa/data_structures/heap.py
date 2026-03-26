from abc import ABC, abstractmethod
from collections.abc import Iterator
from typing import Any, Protocol


class Comparable(Protocol):
    def __lt__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...


class Heap[T: Comparable](ABC):
    """Abstract base heap. Subclasses define ordering via _is_better."""

    _heap: list[T]

    def __init__(self) -> None:
        self._heap = []

    def __len__(self) -> int:
        return len(self._heap)

    def __iter__(self) -> Iterator[T]:
        return iter(self._heap)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._heap})"

    def __str__(self) -> str:
        return f"{self._heap}"

    @property
    def is_empty(self) -> bool:
        return len(self._heap) == 0

    def heapify(self, arr: list[T]) -> None:
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            self._sift_down(arr, n, i)
        self._heap = list(arr)

    def push(self, value: T) -> None:
        self._heap.append(value)
        self._sift_up(self._heap, len(self._heap) - 1)

    def pop(self) -> T:
        if self.is_empty:
            raise IndexError("Pop from an empty heap")

        root_value = self._heap[0]
        last_item = self._heap.pop()

        if not self.is_empty:
            self._heap[0] = last_item
            self._sift_down(self._heap, len(self._heap), 0)

        return root_value

    def peek(self) -> T:
        if self.is_empty:
            raise IndexError("Peek from an empty heap")
        return self._heap[0]

    def sort(self) -> list[T]:
        original_state = self._heap[:]
        result: list[T] = []
        try:
            while not self.is_empty:
                result.append(self.pop())
        finally:
            self._heap = original_state
        return result

    def clear(self) -> None:
        self._heap = []

    @abstractmethod
    def _is_better(self, val1: T, val2: T) -> bool: ...

    def _sift_down(self, arr: list[T], n: int, i: int) -> None:
        better = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self._is_better(arr[left], arr[better]):
            better = left

        if right < n and self._is_better(arr[right], arr[better]):
            better = right

        if better != i:
            arr[i], arr[better] = arr[better], arr[i]
            self._sift_down(arr, n, better)

    def _sift_up(self, arr: list[T], i: int) -> None:
        if i == 0:
            return

        parent = (i - 1) // 2
        if self._is_better(arr[i], arr[parent]):
            arr[i], arr[parent] = arr[parent], arr[i]
            self._sift_up(arr, parent)


class MaxHeap[T: Comparable](Heap[T]):
    """Max-Heap: largest element is always at the root."""

    def _is_better(self, val1: T, val2: T) -> bool:
        return val1 > val2


class MinHeap[T: Comparable](Heap[T]):
    """Min-Heap: smallest element is always at the root."""

    def _is_better(self, val1: T, val2: T) -> bool:
        return val1 < val2
