from collections.abc import Iterator


class _Node[T]:
    """A single node storing a value and a reference to the next node."""

    value: T
    next: _Node[T] | None

    def __init__(self, value: T) -> None:
        self.value = value
        self.next = None

    def __repr__(self) -> str:  # pragma: no cover
        return f"{self.__class__.__name__}({self.value})"


class SinglyLinkedList[T]:
    """Singly linked list with classic node-pointer traversal."""

    _head: _Node[T] | None
    _tail: _Node[T] | None
    _length: int

    def __init__(self) -> None:
        self._head = None
        self._length = 0

    def __len__(self) -> int:
        return self._length

    def __iter__(self) -> Iterator[T]:
        current = self._head
        while current:
            yield current.value
            current = current.next

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({list(self)})"

    def __str__(self) -> str:
        return f"{list(self)}"

    @property
    def is_empty(self) -> bool:
        return self._length == 0

    def append(self, value: T) -> None:
        new_node = _Node(value)

        if self.is_empty:
            self._head = self._tail = new_node
        else:
            if self._tail:
                self._tail.next = new_node
            self._tail = new_node
        self._length += 1

    def prepend(self, value: T) -> None:
        new_node = _Node(value)
        new_node.next = self._head
        self._head = new_node
        self._length += 1

    def insert(self, index: int, value: T) -> None:
        if index < 0 or index > self._length:
            raise IndexError("Index out of range")

        if index == 0:
            self.prepend(value)
            return

        prev_node = self._get_node(index - 1)
        new_node = _Node(value)

        new_node.next = prev_node.next
        prev_node.next = new_node

        self._length += 1

    def delete(self, key: T) -> bool:
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
        self._head = None
        self._tail = None
        self._length = 0

    def search(self, key: T) -> bool:
        return any(value == key for value in self)

    def get(self, index: int) -> T:
        return self._get_node(index).value

    def _get_node(self, index: int) -> _Node[T]:
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range")

        current = self._head
        for _ in range(index):
            if current:
                current = current.next

        if current is None:  # pragma: no cover
            raise RuntimeError("List integrity error")

        return current
