from __future__ import annotations

from collections.abc import Iterator
from typing import TypeVar

from .doubly_linked_list import DoublyLinkedList

T = TypeVar("T")


class Queue[T]:
    """
    Queue data structure implemented using a doubly linked list.

    Attributes:
        _items: Internal doubly linked list to store queue elements.
    """

    _items: DoublyLinkedList[T]

    def __init__(self) -> None:
        """Initialize an empty queue."""
        self._items = DoublyLinkedList()

    def __len__(self) -> int:
        """Return the number of elements in the queue."""
        return len(self._items)

    def __repr__(self) -> str:
        """Return a string representation for debugging."""
        return f"Queue({list(self)})"

    def __iter__(self) -> Iterator[T]:
        """Allow iteration over queue elements."""
        return iter(self._items)

    @property
    def is_empty(self) -> bool:
        """Check if the queue contains no elements."""
        return len(self) == 0

    # --- Modification Methods ---

    def enqueue(self, item: T) -> None:
        """
        Add an element to the end of the queue.

        Args:
            item: The value to be added.
        """
        self._items.append(item)

    def dequeue(self) -> T:
        """
        Remove and return the element from the front of the queue.

        Returns:
            The value of the removed element.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty:
            raise IndexError("Queue is empty")
        return self._items.pop_front()

    def clear(self) -> None:
        """Remove all elements from the queue."""
        self._items.clear()

    # --- Access Methods ---

    def front(self) -> T:
        """
        Return the first element without removing it.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty:
            raise IndexError("Queue is empty")
        return self._items.peek_front()

    def back(self) -> T:
        """
        Return the last element without removing it.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty:
            raise IndexError("Queue is empty")
        return self._items.peek_back()
