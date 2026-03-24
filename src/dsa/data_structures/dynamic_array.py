from collections.abc import Iterator
from typing import cast


class DynamicArray[T]:
    """
    A generic dynamic array that automatically resizes as elements are added.

    Internally backed by a fixed-size list that doubles in capacity
    when full, providing amortized O(1) appends.

    Attributes:
        _size: The number of elements currently stored.
        _capacity: The current allocated size of the internal list.
        _list: The internal fixed-size list holding elements.
    """
    _size: int
    _capacity: int
    _list: list[T | None]

    def __init__(self) -> None:
        """Initialize an empty dynamic array with capacity of 1."""
        self._size = 0
        self._capacity = 1
        self._list = [None] * self._capacity

    def __len__(self) -> int:
        """Return the number of elements in the array."""
        return self._size

    def __getitem__(self, index: int) -> T:
        """
        Return the element at the given index.

        Args:
            index: Zero-based position of the element.

        Returns:
            The element at the specified index.

        Raises:
            IndexError: If the index is out of bounds.
        """
        self._check_index(index)
        return cast(T, self._list[index])

    def __setitem__(self, index: int, value: T) -> None:
        """
        Set the element at the given index.

        Args:
            index: Zero-based position to update.
            value: The new value to set.

        Raises:
            IndexError: If the index is out of bounds.
        """
        self._check_index(index)
        self._list[index] = value

    def __iter__(self) -> Iterator[T]:
        """Iterate over all elements in the array from first to last."""
        for i in range(self._size):
            yield cast(T, self._list[i])

    def __repr__(self) -> str:
        """Return a developer-friendly string representation."""
        return f"DynamicArray({self._list[:self._size]})"

    def __str__(self) -> str:
        """Return a readable string representation of the array."""
        items = ", ".join(str(self._list[i]) for i in range(self._size))
        return f"[{items}]"

    @property
    def is_empty(self) -> bool:
        """Return True if the array contains no elements."""
        return self._size == 0

    @property
    def capacity(self) -> int:
        """Return the current allocated capacity of the internal list."""
        return self._capacity

    def append(self, value: T) -> None:
        """
        Add an element to the end of the array.

        Doubles the internal capacity if the array is full.

        Args:
            value: The element to append.

        Complexity:
            Time: O(1) amortized
            Space: O(1) amortized
        """
        if self._size == self._capacity:
            self._resize()
        self._list[self._size] = value
        self._size += 1

    def insert(self, index: int, value: T) -> None:
        """
        Insert an element at the given index, shifting elements to the right.

        Args:
            index: Zero-based position to insert at. Can equal _size to insert at the end.
            value: The element to insert.

        Raises:
            IndexError: If the index is out of bounds.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        self._check_insert_index(index)
        if self._size == self._capacity:
            self._resize()
        for i in range(self._size, index, -1):
            self._list[i] = self._list[i - 1]
        self._list[index] = value
        self._size += 1

    def remove(self, index: int) -> None:
        """
        Remove the element at the given index, shifting elements to the left.

        Args:
            index: Zero-based position of the element to remove.

        Raises:
            IndexError: If the index is out of bounds.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        self._check_index(index)
        for i in range(index, self._size - 1):
            self._list[i] = self._list[i + 1]
        self._list[self._size - 1] = None
        self._size -= 1

    def pop(self) -> T:
        """
        Remove and return the last element.

        Returns:
            The last element in the array.

        Raises:
            IndexError: If the array is empty.

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        if self.is_empty:
            raise IndexError("Pop from empty array")
        value = cast(T, self._list[self._size - 1])
        self._list[self._size - 1] = None
        self._size -= 1
        return value

    def _resize(self) -> None:
        """
        Double the internal capacity and copy existing elements.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        self._capacity *= 2
        new_list: list[T | None] = [None] * self._capacity
        for i in range(self._size):
            new_list[i] = self._list[i]
        self._list = new_list

    def _check_index(self, index: int) -> None:
        """
        Validate that the index is within bounds for access operations.

        Args:
            index: The index to validate.

        Raises:
            IndexError: If the index is negative or >= _size.
        """
        if index < 0 or index >= self._size:
            raise IndexError(f"Index {index} is out of bounds for array of size {self._size}")

    def _check_insert_index(self, index: int) -> None:
        """
        Validate that the index is within bounds for insert operations.

        Allows index == _size to support appending via insert.

        Args:
            index: The index to validate.

        Raises:
            IndexError: If the index is negative or > _size.
        """
        if index < 0 or index > self._size:
            raise IndexError(f"Index {index} is out of bounds for array of size {self._size}")
