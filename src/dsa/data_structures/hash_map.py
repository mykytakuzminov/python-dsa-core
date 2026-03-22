from __future__ import annotations

from collections.abc import Iterator
from typing import Any, TypeVar

K = TypeVar("K")
V = TypeVar("V")


class HashMap[K, V]:
    """
    Hash Map implementation using chaining.

    Attributes:
        _capacity: Initial number of buckets.
        _length: Number of key-value pairs stored.
        _buckets: List of buckets, each containing (key, value) pairs.
    """

    _capacity: int
    _length: int
    _buckets: list[list[tuple[K, V]]]

    def __init__(self, capacity: int = 8) -> None:
        """Initialize an empty hash map."""
        self._capacity = capacity
        self._length = 0
        self._buckets = [[] for _ in range(capacity)]

    def __len__(self) -> int:
        """Return the total number of key-value pairs."""
        return self._length

    def __repr__(self) -> str:
        """Return a string representation for debugging."""
        pairs: list[str] = []
        for bucket in self._buckets:
            for k, v in bucket:
                pairs.append(f"{k!r}: {v!r}")
        content = ", ".join(pairs)
        return f"HashMap({{{content}}})"

    def __str__(self) -> str:
        """Return a string representation like a Python dictionary."""
        if self.is_empty:
            return "{}"
        pairs: list[str] = []
        for bucket in self._buckets:
            for k, v in bucket:
                pairs.append(f"{k!r}: {v!r}")
        return "{" + ", ".join(pairs) + "}"

    def __iter__(self) -> Iterator[K]:
        """Allow iteration over all keys in the map."""
        for bucket in self._buckets:
            for k, _ in bucket:
                yield k

    def __contains__(self, key: Any) -> bool:
        """Enable 'in' operator support."""
        index = self._hash(key)
        return self._find_index_in_bucket(index, key) is not None

    @property
    def is_empty(self) -> bool:
        """Check if the hash map contains no elements."""
        return self._length == 0

    # --- Modification Methods ---

    def put(self, key: K, value: V) -> None:
        """
        Insert or update a key-value pair in the hash map.

        Args:
            key: Key to insert or update.
            value: Value associated with the key.
        """
        index = self._hash(key)
        bucket = self._buckets[index]

        entry_index = self._find_index_in_bucket(index, key)

        if entry_index is not None:
            bucket[entry_index] = (key, value)
        else:
            bucket.append((key, value))
            self._length += 1

    def remove(self, key: K) -> bool:
        """
        Remove a key-value pair by key.

        Args:
            key: Key to remove.

        Returns:
            True if key was removed, False otherwise.
        """
        index = self._hash(key)
        entry_index = self._find_index_in_bucket(index, key)

        if entry_index is not None:
            del self._buckets[index][entry_index]
            self._length -= 1
            return True

        return False

    def clear(self) -> None:
        """Remove all key-value pairs from the map."""
        self._buckets = [[] for _ in range(self._capacity)]
        self._length = 0

    # --- Access Methods ---

    def get(self, key: K) -> V | None:
        """
        Return the value for the given key.

        Args:
            key: Key to retrieve.

        Returns:
            The associated value, or None if the key is not found.
        """
        index = self._hash(key)
        entry_index = self._find_index_in_bucket(index, key)

        if entry_index is not None:
            return self._buckets[index][entry_index][1]

        return None

    def keys(self) -> list[K]:
        """Return a list of all keys in the map."""
        return list(self)

    def values(self) -> list[V]:
        """Return a list of all values in the map."""
        all_values: list[V] = []
        for bucket in self._buckets:
            for _, v in bucket:
                all_values.append(v)
        return all_values

    # --- Private Helpers ---

    def _hash(self, key: Any) -> int:
        """Compute the bucket index for a given key."""
        return hash(key) % self._capacity

    def _find_index_in_bucket(self, bucket_index: int, key: Any) -> int | None:
        """
        Find the index of a key within a specific bucket.

        Args:
            bucket_index: The index of the bucket to search in.
            key: The key to look for.

        Returns:
            The integer index within the bucket list, or None if not found.
        """
        bucket = self._buckets[bucket_index]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                return i
        return None
