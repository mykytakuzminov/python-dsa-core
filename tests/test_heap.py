import pytest

from dsa import MaxHeap, MinHeap

# --- Constants ---
TEST_DATA_INPUT = [12, -3, 7, 12, -10, 0, 25, 8, 5, -2]

HEAPIFIED_MAX_EXPECTED = [25, 12, 12, 8, -2, 0, 7, -3, 5, -10]
HEAPIFIED_MIN_EXPECTED = [-10, -3, 0, 5, -2, 7, 25, 8, 12, 12]

SORTED_ASC = sorted(TEST_DATA_INPUT)
SORTED_DESC = sorted(TEST_DATA_INPUT, reverse=True)

HEAP_SIZE = len(TEST_DATA_INPUT)


# --- Fixtures ---
@pytest.fixture
def empty_max():
    """"""
    return MaxHeap()


@pytest.fixture
def empty_min():
    """"""
    return MinHeap()


@pytest.fixture
def populated_max():
    """"""
    mh = MaxHeap()
    mh.heapify(list(TEST_DATA_INPUT))
    return mh


@pytest.fixture
def populated_min():
    """"""
    mh = MinHeap()
    mh.heapify(list(TEST_DATA_INPUT))
    return mh


# --- Tests: Status & Utility ---
def test_is_empty(empty_max, empty_min, populated_max, populated_min):
    """Check is_empty() for all heap types."""
    assert empty_max.is_empty
    assert empty_min.is_empty
    assert not populated_max.is_empty
    assert not populated_min.is_empty


def test_len(empty_max, empty_min, populated_max, populated_min):
    """Verify __len__() returns correct count for both heaps."""
    assert len(empty_max) == 0
    assert len(empty_min) == 0
    assert len(populated_max) == HEAP_SIZE
    assert len(populated_min) == HEAP_SIZE


# --- Tests: Modification Methods ---
def test_heapify_logic(empty_max, empty_min):
    """Verify heapify produces the correct internal structure."""
    empty_max.heapify(list(TEST_DATA_INPUT))
    empty_min.heapify(list(TEST_DATA_INPUT))

    assert list(empty_max) == HEAPIFIED_MAX_EXPECTED
    assert list(empty_min) == HEAPIFIED_MIN_EXPECTED


def test_push_logic(empty_max, empty_min):
    """Test push maintains the correct root for both heap types."""
    # Test MaxHeap Push
    for x in [10, 20, 5]:
        empty_max.push(x)
    assert empty_max.peek() == 20

    # Test MinHeap Push
    for x in [10, 5, 20]:
        empty_min.push(x)
    assert empty_min.peek() == 5


def test_pop_logic(populated_max, populated_min):
    """Test pop returns elements in correct order (Max vs Min)."""
    # MaxHeap: should return elements from largest to smallest
    max_results = [populated_max.pop() for _ in range(HEAP_SIZE)]
    assert max_results == SORTED_DESC

    # MinHeap: should return elements from smallest to largest
    min_results = [populated_min.pop() for _ in range(HEAP_SIZE)]
    assert min_results == SORTED_ASC


def test_pop_empty_raises(empty_max, empty_min):
    """Verify pop() raises IndexError for empty heaps."""
    with pytest.raises(IndexError):
        empty_max.pop()
    with pytest.raises(IndexError):
        empty_min.pop()


# --- Tests: Access Methods ---
def test_peek(populated_max, populated_min):
    """Verify peek returns the root without removing it."""
    assert populated_max.peek() == max(TEST_DATA_INPUT)
    assert populated_min.peek() == min(TEST_DATA_INPUT)
    assert len(populated_max) == HEAP_SIZE
    assert len(populated_min) == HEAP_SIZE


def test_peek_empty_raises(empty_max, empty_min):
    """Verify peek() raises IndexError for empty heaps."""
    with pytest.raises(IndexError):
        empty_max.peek()
    with pytest.raises(IndexError):
        empty_min.peek()


# --- Tests: Sorting & Traversal & Clearing ---
def test_sort_preserves_state(populated_max, populated_min):
    """Ensure sort() returns sorted list but doesn't destroy the heap."""
    assert populated_max.sort() == SORTED_DESC
    assert list(populated_max) == HEAPIFIED_MAX_EXPECTED

    assert populated_min.sort() == SORTED_ASC
    assert list(populated_min) == HEAPIFIED_MIN_EXPECTED


def test_traverse_isolation(populated_max):
    """Check that traverse() returns a copy of the internal list."""
    t = list(populated_max)
    t.clear()
    assert not populated_max.is_empty


def test_clear(populated_max, populated_min):
    """Verify clear() resets both heap types."""
    populated_max.clear()
    populated_min.clear()
    assert len(populated_max) == 0
    assert populated_max.is_empty
    assert len(populated_min) == 0
    assert populated_min.is_empty
