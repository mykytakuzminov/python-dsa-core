from collections.abc import Iterator
from typing import Any


class HashMap[K, V]:
    """Hash map with separate chaining collision resolution."""

    _capacity: int
    _length: int
    _buckets: list[list[tuple[K, V]]]

    def __init__(self, capacity: int = 8) -> None:
        self._capacity = capacity
        self._length = 0
        self._buckets = [[] for _ in range(capacity)]

    def __len__(self) -> int:
        return self._length

    def __iter__(self) -> Iterator[K]:
        for bucket in self._buckets:
            for k, _ in bucket:
                yield k

    def __repr__(self) -> str:
        pairs: list[str] = []
        for bucket in self._buckets:
            for k, v in bucket:
                pairs.append(f"{k!r}: {v!r}")
        content = ", ".join(pairs)
        return f"{self.__class__.__name__}({{{content}}})"

    def __str__(self) -> str:
        if self.is_empty:
            return "{}"
        pairs: list[str] = []
        for bucket in self._buckets:
            for k, v in bucket:
                pairs.append(f"{k!r}: {v!r}")
        return "{" + ", ".join(pairs) + "}"

    def __contains__(self, key: Any) -> bool:
        index = self._hash(key)
        return self._find_index_in_bucket(index, key) is not None

    @property
    def is_empty(self) -> bool:
        return self._length == 0

    def put(self, key: K, value: V) -> None:
        index = self._hash(key)
        bucket = self._buckets[index]

        entry_index = self._find_index_in_bucket(index, key)

        if entry_index is not None:
            bucket[entry_index] = (key, value)
        else:
            bucket.append((key, value))
            self._length += 1

    def remove(self, key: K) -> bool:
        index = self._hash(key)
        entry_index = self._find_index_in_bucket(index, key)

        if entry_index is not None:
            del self._buckets[index][entry_index]
            self._length -= 1
            return True

        return False

    def clear(self) -> None:
        self._buckets = [[] for _ in range(self._capacity)]
        self._length = 0

    def get(self, key: K) -> V | None:
        index = self._hash(key)
        entry_index = self._find_index_in_bucket(index, key)

        if entry_index is not None:
            return self._buckets[index][entry_index][1]

        return None

    def keys(self) -> list[K]:
        return list(self)

    def values(self) -> list[V]:
        all_values: list[V] = []
        for bucket in self._buckets:
            for _, v in bucket:
                all_values.append(v)
        return all_values

    def _hash(self, key: Any) -> int:
        return hash(key) % self._capacity

    def _find_index_in_bucket(self, bucket_index: int, key: Any) -> int | None:
        bucket = self._buckets[bucket_index]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                return i
        return None
