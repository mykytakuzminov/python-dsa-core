from collections.abc import Iterator


class _Node[T]:
    """A single node storing a value with references to both neighbors."""

    value: T
    next: _Node[T] | None
    prev: _Node[T] | None

    def __init__(self, value: T) -> None:
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self) -> str:  # pragma: no cover
        return f"{self.__class__.__name__}({self.value})"


class DoublyLinkedList[T]:
    """Doubly linked list with bidirectional traversal."""

    _head: _Node[T] | None
    _tail: _Node[T] | None
    _length: int

    def __init__(self) -> None:
        self._head = None
        self._tail = None
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
                new_node.prev = self._tail
                self._tail = new_node

        self._length += 1

    def prepend(self, value: T) -> None:
        new_node = _Node(value)

        if self.is_empty:
            self._head = self._tail = new_node
        else:
            if self._head:
                new_node.next = self._head
                self._head.prev = new_node
                self._head = new_node

        self._length += 1

    def insert(self, index: int, value: T) -> None:
        if index < 0 or index > self._length:
            raise IndexError("Index out of range")

        if index == 0:
            self.prepend(value)
            return
        if index == self._length:
            self.append(value)
            return

        target = self._get_node(index)
        new_node = _Node(value)

        new_node.next = target
        new_node.prev = target.prev

        if target.prev:
            target.prev.next = new_node
        target.prev = new_node

        self._length += 1

    def delete(self, key: T) -> bool:
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

    def search(self, key: T) -> bool:
        return any(value == key for value in self)

    def get(self, index: int) -> T:
        return self._get_node(index).value

    def peek_front(self) -> T:
        if self.is_empty or self._head is None:
            raise IndexError("List is empty")
        return self._head.value

    def peek_back(self) -> T:
        if self.is_empty or self._tail is None:
            raise IndexError("List is empty")
        return self._tail.value

    def clear(self) -> None:
        self._head = None
        self._tail = None
        self._length = 0

    def _get_node(self, index: int) -> _Node[T]:  # pragma: no cover
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
