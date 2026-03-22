import pytest

from dsa import Queue

# --- Constants ---
NUM_ELEMENTS = 5
TEST_DATA = list(range(NUM_ELEMENTS))


# --- Fixtures ---
@pytest.fixture
def empty_queue():
    """Return an empty Queue."""
    return Queue()


@pytest.fixture
def populated_queue():
    """Return a queue filled with TEST_DATA values."""
    q = Queue()
    for n in TEST_DATA:
        q.enqueue(n)
    return q


# --- Tests: Emptiness ---
def test_is_empty(empty_queue, populated_queue):
    """Check is_empty() for empty and populated Queue."""
    assert empty_queue.is_empty
    assert not populated_queue.is_empty


# --- Tests: Adding Elements ---
def test_enqueue(empty_queue):
    """Test enqueue() adds elements to the end of the queue."""
    empty_queue.enqueue(1)
    empty_queue.enqueue(2)
    empty_queue.enqueue(3)

    assert empty_queue.front() == 1
    assert empty_queue.back() == 3
    assert len(empty_queue) == 3


# --- Tests: Removing Elements ---
def test_dequeue(populated_queue):
    """Test dequeue() removes elements from the front (FIFO)."""
    assert populated_queue.dequeue() == TEST_DATA[0]
    assert populated_queue.dequeue() == TEST_DATA[1]
    assert populated_queue.dequeue() == TEST_DATA[2]
    assert len(populated_queue) == NUM_ELEMENTS - 3


def test_dequeue_index_error(empty_queue):
    """Test dequeue() raises IndexError when the queue is empty."""
    with pytest.raises(IndexError):
        empty_queue.dequeue()


# --- Tests: Accessing Elements ---
def test_peek_front(populated_queue):
    """Test front() returns the first element without removing it."""
    assert populated_queue.front() == TEST_DATA[0]
    assert populated_queue.front() == TEST_DATA[0]
    assert len(populated_queue) == NUM_ELEMENTS


def test_peek_front_index_error(empty_queue):
    """Test front() raises IndexError when the queue is empty."""
    with pytest.raises(IndexError):
        empty_queue.front()


def test_peek_back(populated_queue):
    """Test back() returns the last element without removing it."""
    assert populated_queue.back() == TEST_DATA[-1]
    assert populated_queue.back() == TEST_DATA[-1]
    assert len(populated_queue) == NUM_ELEMENTS


def test_peek_back_index_error(empty_queue):
    """Test back() raises IndexError when the queue is empty."""
    with pytest.raises(IndexError):
        empty_queue.back()


# --- Tests: Clearing the Queue ---
def test_clear(empty_queue, populated_queue):
    """Check clear() empties the queue and resets length."""
    empty_queue.clear()
    assert list(empty_queue) == []
    assert len(empty_queue) == 0

    populated_queue.clear()
    assert list(populated_queue) == []
    assert len(populated_queue) == 0


# --- Tests: Immutability ---
def test_traverse_is_immutable(populated_queue):
    """
    Ensure traverse() returns a copy, so modifying the result
    does not affect the internal queue state.
    """
    items = list(populated_queue)
    original_len = len(populated_queue)

    items.append(999)
    items.clear()

    assert len(populated_queue) == original_len
    assert list(populated_queue) != items


# --- Tests: Length & String Representation ---
def test_len(empty_queue, populated_queue):
    """Verify __len__() returns correct number of elements."""
    assert len(empty_queue) == 0
    assert len(populated_queue) == NUM_ELEMENTS


def test_str(empty_queue, populated_queue):
    """Check __str__ returns correct string representation of the Queue."""
    assert str(empty_queue) == "Queue([])"
    assert str(populated_queue) == f"Queue({TEST_DATA})"
