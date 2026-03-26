from collections.abc import Iterator
from typing import cast


class DynamicArray[T]:
    """Growable array backed by a fixed-size list."""

    _size: int
    _capacity: int
    _list: list[T | None]

    def __init__(self) -> None:
        self._size = 0
        self._capacity = 1
        self._list = [None] * self._capacity

    def __len__(self) -> int:
        return self._size

    def __getitem__(self, index: int) -> T:
        self._check_index(index)
        return cast(T, self._list[index])

    def __setitem__(self, index: int, value: T) -> None:
        self._check_index(index)
        self._list[index] = value

    def __iter__(self) -> Iterator[T]:
        for i in range(self._size):
            yield cast(T, self._list[i])

    def __repr__(self) -> str:
        return f"DynamicArray({self._list[: self._size]})"

    def __str__(self) -> str:
        items = ", ".join(str(self._list[i]) for i in range(self._size))
        return f"[{items}]"

    @property
    def is_empty(self) -> bool:
        return self._size == 0

    @property
    def capacity(self) -> int:
        return self._capacity

    def append(self, value: T) -> None:
        if self._size == self._capacity:
            self._resize()
        self._list[self._size] = value
        self._size += 1

    def insert(self, index: int, value: T) -> None:
        self._check_insert_index(index)
        if self._size == self._capacity:
            self._resize()
        for i in range(self._size, index, -1):
            self._list[i] = self._list[i - 1]
        self._list[index] = value
        self._size += 1

    def remove(self, index: int) -> None:
        self._check_index(index)
        for i in range(index, self._size - 1):
            self._list[i] = self._list[i + 1]
        self._list[self._size - 1] = None
        self._size -= 1

    def pop(self) -> T:
        if self.is_empty:
            raise IndexError("Pop from empty array")
        value = cast(T, self._list[self._size - 1])
        self._list[self._size - 1] = None
        self._size -= 1
        return value

    def _resize(self) -> None:
        # Double the capacity to achieve amortized O(1) appends
        self._capacity *= 2
        new_list: list[T | None] = [None] * self._capacity
        new_list[: self._size] = self._list[: self._size]
        self._list = new_list

    def _check_index(self, index: int) -> None:
        if index < 0 or index >= self._size:
            raise IndexError("Index is out of bounds")

    def _check_insert_index(self, index: int) -> None:
        if index < 0 or index > self._size:
            raise IndexError("Index is out of bounds")
