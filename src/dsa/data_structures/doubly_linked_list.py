from __future__ import annotations

from collections.abc import Iterator
from typing import TypeVar

T = TypeVar("T")


class Node[T]:
    """
    Node class for a doubly linked list.

    Attributes:
        value: The value stored in the node.
        next: Pointer to the next node in the list.
        prev: Pointer to the previous node in the list.
    """

    value: T
    next: Node[T] | None
    prev: Node[T] | None

    def __init__(self, value: T) -> None:
        """Initialize a node with a given value."""
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self) -> str:
        """Return a string representation of the node."""
        return f"Node({self.value})"


class DoublyLinkedList[T]:
    """
    Doubly Linked List implementation.

    Attributes:
        _head: Reference to the first node in the list.
        _tail: Reference to the last node in the list.
        _length: Total number of nodes in the list.
    """

    _head: Node[T] | None
    _tail: Node[T] | None
    _length: int

    def __init__(self) -> None:
        """Initialize an empty doubly linked list."""
        self._head = None
        self._tail = None
        self._length = 0

    def __len__(self) -> int:
        """Return the number of nodes in the list."""
        return self._length

    def __repr__(self) -> str:
        """Return a string representation of the list."""
        return f"DoublyLinkedList({list(self)})"

    def __iter__(self) -> Iterator[T]:
        """Allow iteration over the list elements from head to tail."""
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
        Add an element at the end of the list (Tail).

        Args:
            value: The value to be added.
        """
        new_node = Node(value)

        if self.is_empty:
            self._head = self._tail = new_node
        else:
            if self._tail:
                self._tail.next = new_node
                new_node.prev = self._tail
                self._tail = new_node

        self._length += 1

    def prepend(self, value: T) -> None:
        """
        Add an element at the beginning of the list (Head).

        Args:
            value: The value to be added.
        """
        new_node = Node(value)

        if self.is_empty:
            self._head = self._tail = new_node
        else:
            if self._head:
                new_node.next = self._head
                self._head.prev = new_node
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
        if index == self._length:
            self.append(value)
            return

        target = self._get_node(index)
        new_node = Node(value)

        new_node.next = target
        new_node.prev = target.prev

        if target.prev:
            target.prev.next = new_node
        target.prev = new_node

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
        while current:
            if current.value == key:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self._head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self._tail = current.prev

                self._length -= 1
                return True
            current = current.next

        return False

    def pop_front(self) -> T:
        """
        Remove and return the element at the head of the list.

        Returns:
            The value of the removed node.

        Raises:
            IndexError: If the list is empty.
        """
        if self.is_empty or self._head is None:
            raise IndexError("List is empty")

        value = self._head.value
        self._head = self._head.next

        if self._head:
            self._head.prev = None
        else:
            self._tail = None

        self._length -= 1
        return value

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

    def peek_front(self) -> T:
        """
        Return the value of the head node without removing it.

        Raises:
            IndexError: If the list is empty.
        """
        if self.is_empty or self._head is None:
            raise IndexError("List is empty")
        return self._head.value

    def peek_back(self) -> T:
        """
        Return the value of the tail node without removing it.

        Raises:
            IndexError: If the list is empty.
        """
        if self.is_empty or self._tail is None:
            raise IndexError("List is empty")
        return self._tail.value

    def clear(self) -> None:
        """Remove all elements from the list."""
        self._head = None
        self._tail = None
        self._length = 0

    # --- Private Helpers ---

    def _get_node(self, index: int) -> Node[T]:
        """
        Internal helper to fetch a node at a specific index with O(n/2) optimization.

        Args:
            index: Position of the node to retrieve.

        Returns:
            The Node object at the given index.

        Raises:
            IndexError: If index is out of range.
        """
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range")

        # Optimization: Decide traversal direction (start from head or tail)
        if index <= self._length // 2:
            current = self._head
            for _ in range(index):
                if current:
                    current = current.next
        else:
            current = self._tail
            for _ in range(self._length - 1, index, -1):
                if current:
                    current = current.prev

        if current is None:
            raise IndexError("Index out of range")
        return current

    def _get_head(self) -> Node[T] | None:
        """Return the head node (for internal testing)."""
        return self._head

    def _get_tail(self) -> Node[T] | None:
        """Return the tail node (for internal testing)."""
        return self._tail
