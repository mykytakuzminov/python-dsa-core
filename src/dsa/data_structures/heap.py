from __future__ import annotations

from collections.abc import Iterator
from typing import Any, Protocol, TypeVar


class Comparable(Protocol):
    def __lt__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...


T = TypeVar("T", bound=Comparable)


class Heap[T: Comparable]:
    """
    Base Heap implementation using a dynamic array.

    Attributes:
        _heap: Internal list representing the heap's complete binary tree.
    """

    _heap: list[T]

    def __init__(self) -> None:
        """Initialize an empty heap."""
        self._heap = []

    def __len__(self) -> int:
        """Return the number of elements in the heap."""
        return len(self._heap)

    def __repr__(self) -> str:
        """Return a string representation of the heap for debugging."""
        return f"{self.__class__.__name__}({self._heap})"

    def __iter__(self) -> Iterator[T]:
        """Allow iteration over all items in the heap."""
        return iter(self._heap)

    @property
    def is_empty(self) -> bool:
        """Check if the heap contains no elements."""
        return len(self._heap) == 0

    # --- Modification Methods ---

    def heapify(self, arr: list[T]) -> None:
        """
        Transform a list into a valid heap in-place.

        Args:
            arr: A list of elements to be transformed into a heap.
        """
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            self._sift_down(arr, n, i)
        self._heap = list(arr)

    def push(self, value: T) -> None:
        """
        Add a new element to the heap and maintain heap property.

        Args:
            value: The element to be added to the heap.
        """
        self._heap.append(value)
        self._sift_up(self._heap, len(self._heap) - 1)

    def pop(self) -> T:
        """
        Remove and return the root element of the heap.

        Returns:
            The root element (smallest in MinHeap, largest in MaxHeap).

        Raises:
            IndexError: If the heap is empty.
        """
        if self.is_empty:
            raise IndexError("pop from an empty heap")

        root_value = self._heap[0]
        last_item = self._heap.pop()

        if not self.is_empty:
            self._heap[0] = last_item
            self._sift_down(self._heap, len(self._heap), 0)

        return root_value

    # --- Access & Utility Methods ---

    def peek(self) -> T:
        """
        Return the root element without removing it.

        Returns:
            The value at the root of the heap.

        Raises:
            IndexError: If the heap is empty.
        """
        if self.is_empty:
            raise IndexError("peek from an empty heap")
        return self._heap[0]

    def sort(self) -> list[T]:
        """
        Return all elements in sorted order without destroying the heap.

        Returns:
            A list of elements sorted according to the heap's priority.
        """
        original_state = self._heap[:]
        result: list[T] = []
        try:
            while not self.is_empty:
                result.append(self.pop())
        finally:
            self._heap = original_state
        return result

    def clear(self) -> None:
        """Remove all elements from the heap."""
        self._heap = []

    # --- Private Helpers ---

    def _is_better(self, val1: T, val2: T) -> bool:
        """
        Abstract comparison strategy to be implemented by subclasses.

        Args:
            val1: First value to compare.
            val2: Second value to compare.

        Returns:
            True if val1 has higher priority than val2.
        """
        raise NotImplementedError("Subclasses must implement _is_better")

    def _sift_down(self, arr: list[T], n: int, i: int) -> None:
        """
        Move an element down the tree to its correct position.

        Args:
            arr: The list representing the heap.
            n: Total number of elements in the array.
            i: Index of the element to sift down.
        """
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
        """
        Move an element up the tree to its correct position.

        Args:
            arr: The list representing the heap.
            i: Index of the element to sift up.
        """
        if i == 0:
            return

        parent = (i - 1) // 2
        if self._is_better(arr[i], arr[parent]):
            arr[i], arr[parent] = arr[parent], arr[i]
            self._sift_up(arr, parent)


class MaxHeap(Heap[T]):
    """Max-Heap implementation where the largest element is at the root."""

    def _is_better(self, val1: T, val2: T) -> bool:
        """Compare two values for Max-Heap priority."""
        return val1 > val2


class MinHeap(Heap[T]):
    """Min-Heap implementation where the smallest element is at the root."""

    def _is_better(self, val1: T, val2: T) -> bool:
        """Compare two values for Min-Heap priority."""
        return val1 < val2
