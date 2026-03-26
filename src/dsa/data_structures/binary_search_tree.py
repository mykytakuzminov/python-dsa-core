from collections.abc import Iterator
from typing import Any, Protocol

from .queue import Queue
from .stack import Stack


class Comparable(Protocol):
    def __lt__(self, other: Any, /) -> bool: ...
    def __gt__(self, other: Any, /) -> bool: ...
    def __le__(self, other: Any, /) -> bool: ...
    def __ge__(self, other: Any, /) -> bool: ...
    def __eq__(self, other: object, /) -> bool: ...


class Node[T: Comparable]:
    """A BST node storing a value with references to left and right children."""

    value: T
    left: Node[T] | None
    right: Node[T] | None

    def __init__(self, value: T) -> None:
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.value})"


class BinarySearchTree[T: Comparable]:
    """Binary Search Tree with BFS, DFS, and all traversals."""

    _root: Node[T] | None
    _count: int

    def __init__(self) -> None:
        self._root = None
        self._count = 0

    def __len__(self) -> int:
        return self._count

    def __iter__(self) -> Iterator[T]:
        # Iterative inorder traversal using an explicit stack
        stack: Stack[Node[T]] = Stack()
        current = self._root

        while current or not stack.is_empty:
            while current:
                stack.push(current)
                current = current.left

            current = stack.pop()
            yield current.value
            current = current.right

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({list(self)})"

    def __str__(self) -> str:
        return f"{list(self)}"

    @property
    def is_empty(self) -> bool:
        return self._root is None

    def insert(self, value: T) -> None:
        if self._root is None:
            self._root = Node(value)
            self._count += 1
        else:
            added = self._insert_recursive(self._root, value)
            if added:
                self._count += 1

    def delete(self, value: T) -> bool:
        if not self.search(value):
            return False
        self._root = self._delete_recursive(self._root, value)
        self._count -= 1
        return True

    def clear(self) -> None:
        self._root = None
        self._count = 0

    def search(self, value: T) -> bool:
        current = self._root
        while current:
            if value == current.value:
                return True
            current = current.left if value < current.value else current.right
        return False

    def height(self) -> int:
        return self._height(self._root)

    def preorder(self) -> list[T]:
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
        return list(self)

    def postorder(self) -> list[T]:
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

    def bfs(self) -> list[T]:
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

    def _insert_recursive(self, node: Node[T], value: T) -> bool:
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
                return True
            return self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
                return True
            return self._insert_recursive(node.right, value)
        return False

    def _delete_recursive(self, node: Node[T] | None, value: T) -> Node[T] | None:
        if node is None:
            return None

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if not node.left and not node.right:
                return None
            if not node.left:
                return node.right
            if not node.right:
                return node.left

            successor = node.right
            while successor.left:
                successor = successor.left
            node.value = successor.value
            node.right = self._delete_recursive(node.right, successor.value)

        return node

    def _height(self, node: Node[T] | None) -> int:
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))
