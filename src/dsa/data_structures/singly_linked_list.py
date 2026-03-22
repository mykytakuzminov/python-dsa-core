from __future__ import annotations

from collections.abc import Iterator
from typing import TypeVar

T = TypeVar("T")


class Node[T]:
    """
    Node class for a singly linked list.

    Attributes:
        value: The data stored in the node.
        next: Pointer to the next node in the list.
    """

    value: T
    next: Node[T] | None

    def __init__(self, value: T) -> None:
        """Initialize a node with a given value.."""
        self.value = value
        self.next = None

    def __repr__(self) -> str:
        """Return a string representation of the node."""
        return f"Node({self.value})"


class SinglyLinkedList[T]:
    """
    Singly Linked List implementation.

    Attributes:
        _head: Reference to the first node in the list.
        _length: Total number of nodes in the list.
    """

    _head: Node[T] | None
    _length: int

    def __init__(self) -> None:
        """Initialize an empty singly linked list."""
        self._head = None
        self._length = 0

    def __len__(self) -> int:
        """Return the number of nodes in the list."""
        return self._length

    def __repr__(self) -> str:
        """Return a string representation of the list."""
        return f"SinglyLinkedList({list(self)})"

    def __iter__(self) -> Iterator[T]:
        """
        Allow iteration over the list elements from head to end.

        Yields:
            The values of the nodes in order.
        """
        current = self._head
        while current:
            yield current.value
            current = current.next

    @property
    def is_empty(self) -> bool:
        """Check if the list contains no elements."""
        return self._length == 0

    # --- Modification Methods (Insertion) ---

    def append(self, value: T) -> None:
        """
        Add an element at the end of the list.

        Args:
            value: Value to append to the list.
        """
        new_node = Node(value)

        if self.is_empty:
            self._head = new_node
        else:
            current = self._head
            while current and current.next:
                current = current.next
            if current:
                current.next = new_node

        self._length += 1

    def prepend(self, value: T) -> None:
        """
        Add an element at the beginning of the list.

        Args:
            value: The value to be added.
        """
        new_node = Node(value)
        new_node.next = self._head
        self._head = new_node
        self._length += 1

    def insert(self, index: int, value: T) -> None:
        """
        Insert a new element at a specific index.

        Args:
            index: Position at which to insert the element.
            value: The value to be added.

        Raises:
            IndexError: If index is out of range.
        """
        if index < 0 or index > self._length:
            raise IndexError("Index out of range")

        if index == 0:
            self.prepend(value)
            return

        prev_node = self._get_node(index - 1)
        new_node = Node(value)

        new_node.next = prev_node.next
        prev_node.next = new_node

        self._length += 1

    # --- Modification Methods (Deletion) ---

    def delete(self, key: T) -> bool:
        """
        Delete the first element with the given value.

        Args:
            key: Value to delete.

        Returns:
            True if an element was deleted, False otherwise.
        """
        current = self._head
        prev = None

        while current:
            if current.value == key:
                if prev:
                    prev.next = current.next
                else:
                    self._head = current.next

                self._length -= 1
                return True

            prev = current
            current = current.next

        return False

    def clear(self) -> None:
        """Remove all elements from the list."""
        self._head = None
        self._length = 0

    # --- Access & Search Methods ---

    def search(self, key: T) -> bool:
        """
        Search for an element by value.

        Args:
            key: Value to search for.

        Returns:
            True if the element is found, False otherwise.
        """
        return any(value == key for value in self)

    def get(self, index: int) -> T:
        """
        Return the value of the node at a specific index.

        Args:
            index: Position of the element to retrieve.

        Returns:
            Value at the specified index.
        """
        return self._get_node(index).value

    # --- Private Helpers ---

    def _get_node(self, index: int) -> Node[T]:
        """
        Internal helper to fetch a node at a specific index.

        Args:
            index: Position of the node to retrieve.

        Returns:
            The Node object at the given index.

        Raises:
            IndexError: If index is out of range.
        """
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range")

        current = self._head
        for _ in range(index):
            if current:
                current = current.next

        if current is None:
            raise IndexError("Index out of range")
        return current
