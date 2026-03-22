from __future__ import annotations

from collections.abc import Iterator
from typing import TypeVar

T = TypeVar("T")


class Stack[T]:
    """
    Stack data structure implemented using a dynamic array (Python list).

    Attributes:
        _items: Internal list to store stack elements.
    """

    _items: list[T]

    def __init__(self) -> None:
        """Initialize an empty stack using a dynamic array."""
        self._items = []

    def __len__(self) -> int:
        """Return the number of elements in the stack."""
        return len(self._items)

    def __repr__(self) -> str:
        """Return a string representation for debugging."""
        return f"Stack({self._items})"

    def __iter__(self) -> Iterator[T]:
        """Allow iteration over stack elements (from bottom to top)."""
        return iter(self._items)

    @property
    def is_empty(self) -> bool:
        """Check if the stack contains no elements."""
        return len(self._items) == 0

    # --- Modification Methods ---

    def push(self, item: T) -> None:
        """
        Add an element to the top of the stack.

        Args:
            item: The value to be added.
        """
        self._items.append(item)

    def pop(self) -> T:
        """
        Remove and return the element from the top of the stack.

        Returns:
            The value of the removed element.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty:
            raise IndexError("Stack is empty")
        return self._items.pop()

    def clear(self) -> None:
        """Remove all elements from the stack."""
        self._items.clear()

    # --- Access Methods ---

    def peek(self) -> T:
        """
        Return the top element of the stack without removing it.

        Returns:
            The value at the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty:
            raise IndexError("Stack is empty")
        return self._items[-1]
