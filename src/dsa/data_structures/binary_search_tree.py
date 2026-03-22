from __future__ import annotations

from collections.abc import Iterator
from typing import Any, Protocol, TypeVar

from .queue import Queue
from .stack import Stack


class Comparable(Protocol):
    def __lt__(self, other: Any, /) -> bool: ...
    def __gt__(self, other: Any, /) -> bool: ...
    def __le__(self, other: Any, /) -> bool: ...
    def __ge__(self, other: Any, /) -> bool: ...
    def __eq__(self, other: object, /) -> bool: ...


T = TypeVar("T", bound=Comparable)


class Node[T: Comparable]:
    """
    Represents a node in a Binary Search Tree.

    Attributes:
        value: The value stored in the node.
        left: Reference to the left child node (smaller values).
        right: Reference to the right child node (larger values).
    """

    value: T
    left: Node[T] | None
    right: Node[T] | None

    def __init__(self, value: T) -> None:
        """Initialize a tree node."""
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        """Return a string representation of the node."""
        return f"Node({self.value})"


class BinarySearchTree[T: Comparable]:
    """
    Binary Search Tree (BST) implementation.

    Attributes:
        _root: The top-level node of the tree.
    """

    _root: Node[T] | None

    def __init__(self) -> None:
        """Initialize an empty Binary Search Tree."""
        self._root = None

    def __len__(self) -> int:
        """Return the total number of nodes in the tree."""
        return self._size(self._root)

    def __repr__(self) -> str:
        """Return a string representation of the tree."""
        return f"BinarySearchTree({list(self)})"

    def __iter__(self) -> Iterator[T]:
        """Iterate over elements in sorted (inorder) order."""
        stack: Stack[Node[T]] = Stack()
        current = self._root

        while current or not stack.is_empty:
            while current:
                stack.push(current)
                current = current.left

            current = stack.pop()
            yield current.value
            current = current.right

    @property
    def is_empty(self) -> bool:
        """Check if the tree contains no nodes."""
        return self._root is None

    # --- Modification Methods ---

    def insert(self, value: T) -> None:
        """
        Insert a new value into the BST.

        Args:
            value: The value to add.
        """
        if self._root is None:
            self._root = Node(value)
        else:
            self._insert_recursive(self._root, value)

    def clear(self) -> None:
        """Remove all nodes from the tree."""
        self._root = None

    # --- Query & Search Methods ---

    def search(self, value: T) -> bool:
        """
        Search for a value in the tree.

        Args:
            value: The value to find.

        Returns:
            True if found, False otherwise.
        """
        current = self._root
        while current:
            if value == current.value:
                return True
            current = current.left if value < current.value else current.right
        return False

    def height(self) -> int:
        """
        Calculate the height of the tree.

        Returns:
            The maximum number of edges from root to leaf.
        """
        return self._height(self._root)

    # --- Traversal Methods (DFS) ---

    def preorder(self) -> list[T]:
        """
        Perform iterative preorder traversal (Root -> L -> R).

        Returns:
            A list of values in preorder sequence.
        """
        if not self._root:
            return []

        stack: Stack[Node[T]] = Stack()
        stack.push(self._root)
        result: list[T] = []

        while not stack.is_empty:
            node = stack.pop()
            result.append(node.value)
            if node.right:
                stack.push(node.right)
            if node.left:
                stack.push(node.left)
        return result

    def inorder(self) -> list[T]:
        """
        Perform iterative inorder traversal (L -> Root -> R).

        Returns:
            A list of values in ascending order.
        """
        return list(self)

    def postorder(self) -> list[T]:
        """
        Perform iterative postorder traversal (L -> R -> Root).

        Returns:
            A list of values in postorder sequence.
        """
        stack: Stack[Node[T]] = Stack()
        result: list[T] = []
        current = self._root
        last_visited = None

        while current or not stack.is_empty:
            while current:
                stack.push(current)
                current = current.left

            peek_node = stack.peek()
            if not peek_node.right or last_visited == peek_node.right:
                result.append(peek_node.value)
                last_visited = stack.pop()
                current = None
            else:
                current = peek_node.right
        return result

    # --- Traversal Methods (BFS) ---

    def bfs(self) -> list[T]:
        """
        Perform Breadth-First Search (level-order traversal).

        Returns:
            List of values level by level from top to bottom.
        """
        if not self._root:
            return []

        queue: Queue[Node[T]] = Queue()
        queue.enqueue(self._root)
        result: list[T] = []

        while not queue.is_empty:
            node = queue.dequeue()
            result.append(node.value)
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return result

    # --- Private Helpers ---

    def _insert_recursive(self, node: Node[T], value: T) -> None:
        """Helper to recursively find the insertion point."""
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def _height(self, node: Node[T] | None) -> int:
        """Helper to recursively calculate the depth of the tree."""
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

    def _size(self, node: Node[T] | None) -> int:
        """Helper to recursively count nodes."""
        if node is None:
            return 0
        return 1 + self._size(node.left) + self._size(node.right)
