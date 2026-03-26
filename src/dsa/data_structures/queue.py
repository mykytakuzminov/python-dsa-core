from collections.abc import Iterator

from .doubly_linked_list import DoublyLinkedList


class Queue[T]:
    """FIFO data structure backed by a doubly linked list."""

    _items: DoublyLinkedList[T]

    def __init__(self) -> None:
        self._items = DoublyLinkedList()

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> Iterator[T]:
        return iter(self._items)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._items})"

    def __str__(self) -> str:
        return f"{self._items}"

    @property
    def is_empty(self) -> bool:
        return len(self) == 0

    def enqueue(self, item: T) -> None:
        self._items.append(item)

    def dequeue(self) -> T:
        self._check_emptiness()
        return self._items.pop_front()

    def clear(self) -> None:
        self._items.clear()

    def front(self) -> T:
        self._check_emptiness()
        return self._items.peek_front()

    def back(self) -> T:
        self._check_emptiness()
        return self._items.peek_back()

    def _check_emptiness(self) -> None:
        if self.is_empty:
            raise IndexError("Queue is empty")
