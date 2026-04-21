import pytest

from dsa import MaxHeap, MinHeap

TEST_DATA_INPUT = [12, -3, 7, 12, -10, 0, 25, 8, 5, -2]

HEAPIFIED_MAX_EXPECTED = [25, 12, 12, 8, -2, 0, 7, -3, 5, -10]
HEAPIFIED_MIN_EXPECTED = [-10, -3, 0, 5, -2, 7, 25, 8, 12, 12]

SORTED_ASC = sorted(TEST_DATA_INPUT)
SORTED_DESC = sorted(TEST_DATA_INPUT, reverse=True)

HEAP_SIZE = len(TEST_DATA_INPUT)


@pytest.fixture
def empty_max():
    return MaxHeap()


@pytest.fixture
def empty_min():
    return MinHeap()


@pytest.fixture
def populated_max():
    mh = MaxHeap()
    mh.heapify(list(TEST_DATA_INPUT))
    return mh


@pytest.fixture
def populated_min():
    mh = MinHeap()
    mh.heapify(list(TEST_DATA_INPUT))
    return mh


def test_is_empty(empty_max, empty_min, populated_max, populated_min):
    assert empty_max.is_empty
    assert empty_min.is_empty
    assert not populated_max.is_empty
    assert not populated_min.is_empty


def test_len(empty_max, empty_min, populated_max, populated_min):
    assert len(empty_max) == 0
    assert len(empty_min) == 0
    assert len(populated_max) == HEAP_SIZE
    assert len(populated_min) == HEAP_SIZE


def test_heapify_logic(empty_max, empty_min):
    empty_max.heapify(list(TEST_DATA_INPUT))
    empty_min.heapify(list(TEST_DATA_INPUT))

    assert list(empty_max) == HEAPIFIED_MAX_EXPECTED
    assert list(empty_min) == HEAPIFIED_MIN_EXPECTED


def test_push_logic(empty_max, empty_min):
    # Test MaxHeap Push
    for x in [10, 20, 5]:
        empty_max.push(x)
    assert empty_max.peek() == 20

    # Test MinHeap Push
    for x in [10, 5, 20]:
        empty_min.push(x)
    assert empty_min.peek() == 5


def test_pop_logic(populated_max, populated_min):
    # MaxHeap: should return elements from largest to smallest
    max_results = [populated_max.pop() for _ in range(HEAP_SIZE)]
    assert max_results == SORTED_DESC

    # MinHeap: should return elements from smallest to largest
    min_results = [populated_min.pop() for _ in range(HEAP_SIZE)]
    assert min_results == SORTED_ASC


def test_pop_empty_raises(empty_max, empty_min):
    with pytest.raises(IndexError):
        empty_max.pop()
    with pytest.raises(IndexError):
        empty_min.pop()


def test_peek(populated_max, populated_min):
    assert populated_max.peek() == max(TEST_DATA_INPUT)
    assert populated_min.peek() == min(TEST_DATA_INPUT)
    assert len(populated_max) == HEAP_SIZE
    assert len(populated_min) == HEAP_SIZE


def test_peek_empty_raises(empty_max, empty_min):
    with pytest.raises(IndexError):
        empty_max.peek()
    with pytest.raises(IndexError):
        empty_min.peek()


def test_sort_preserves_state(populated_max, populated_min):
    assert populated_max.sort() == SORTED_DESC
    assert list(populated_max) == HEAPIFIED_MAX_EXPECTED

    assert populated_min.sort() == SORTED_ASC
    assert list(populated_min) == HEAPIFIED_MIN_EXPECTED


def test_traverse_isolation(populated_max):
    t = list(populated_max)
    t.clear()
    assert not populated_max.is_empty


def test_clear(populated_max, populated_min):
    populated_max.clear()
    populated_min.clear()
    assert len(populated_max) == 0
    assert populated_max.is_empty
    assert len(populated_min) == 0
    assert populated_min.is_empty


def test_repr(empty_max, populated_max):
    assert repr(empty_max) == "MaxHeap([])"
    assert repr(populated_max) == "MaxHeap([25, 12, 12, 8, -2, 0, 7, -3, 5, -10])"


def test_str(empty_max, populated_max):
    assert str(empty_max) == "[]"
    assert str(populated_max) == "[25, 12, 12, 8, -2, 0, 7, -3, 5, -10]"
