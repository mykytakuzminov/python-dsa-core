import pytest

from dsa import Queue

NUM_ELEMENTS = 5
TEST_DATA = list(range(NUM_ELEMENTS))


@pytest.fixture
def empty_queue():
    return Queue()


@pytest.fixture
def populated_queue():
    q = Queue()
    for n in TEST_DATA:
        q.enqueue(n)
    return q


def test_is_empty(empty_queue, populated_queue):
    assert empty_queue.is_empty
    assert not populated_queue.is_empty


def test_enqueue(empty_queue):
    empty_queue.enqueue(1)
    empty_queue.enqueue(2)
    empty_queue.enqueue(3)

    assert empty_queue.front() == 1
    assert empty_queue.back() == 3
    assert len(empty_queue) == 3


def test_dequeue(populated_queue):
    assert populated_queue.dequeue() == TEST_DATA[0]
    assert populated_queue.dequeue() == TEST_DATA[1]
    assert populated_queue.dequeue() == TEST_DATA[2]
    assert len(populated_queue) == NUM_ELEMENTS - 3


def test_dequeue_index_error(empty_queue):
    with pytest.raises(IndexError):
        empty_queue.dequeue()


def test_peek_front(populated_queue):
    assert populated_queue.front() == TEST_DATA[0]
    assert populated_queue.front() == TEST_DATA[0]
    assert len(populated_queue) == NUM_ELEMENTS


def test_peek_front_index_error(empty_queue):
    with pytest.raises(IndexError):
        empty_queue.front()


def test_peek_back(populated_queue):
    assert populated_queue.back() == TEST_DATA[-1]
    assert populated_queue.back() == TEST_DATA[-1]
    assert len(populated_queue) == NUM_ELEMENTS


def test_peek_back_index_error(empty_queue):
    with pytest.raises(IndexError):
        empty_queue.back()


def test_clear(empty_queue, populated_queue):
    empty_queue.clear()
    assert list(empty_queue) == []
    assert len(empty_queue) == 0

    populated_queue.clear()
    assert list(populated_queue) == []
    assert len(populated_queue) == 0


def test_traverse_is_immutable(populated_queue):
    items = list(populated_queue)
    original_len = len(populated_queue)

    items.append(999)
    items.clear()

    assert len(populated_queue) == original_len
    assert list(populated_queue) != items


def test_len(empty_queue, populated_queue):
    assert len(empty_queue) == 0
    assert len(populated_queue) == NUM_ELEMENTS


def test_repr(empty_queue, populated_queue):
    assert repr(empty_queue) == "Queue([])"
    assert repr(populated_queue) == f"Queue({TEST_DATA})"


def test_str(empty_queue, populated_queue):
    assert str(empty_queue) == "[]"
    assert str(populated_queue) == f"{TEST_DATA}"
