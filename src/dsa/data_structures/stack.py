from collections.abc import Iterator


class Stack[T]:
    """LIFO data structure backed by a dynamic array."""

    _items: list[T]

    def __init__(self) -> None:
        self._items = []

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> Iterator[T]:
        return iter(reversed(self._items))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._items})"

    def __str__(self) -> str:
        return f"{self._items}"

    @property
    def is_empty(self) -> bool:
        return len(self._items) == 0

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        self._check_emptiness()
        return self._items.pop()

    def clear(self) -> None:
        self._items.clear()

    def peek(self) -> T:
        self._check_emptiness()
        return self._items[-1]

    def _check_emptiness(self) -> None:
        if self.is_empty:
            raise IndexError("Stack is empty")
