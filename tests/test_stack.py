import pytest

from dsa import Stack

NUM_ELEMENTS = 5
TEST_DATA = list(range(NUM_ELEMENTS))


@pytest.fixture
def empty_stack() -> Stack:
    return Stack()


@pytest.fixture
def populated_stack():
    s = Stack()
    for n in TEST_DATA:
        s.push(n)
    return s


def test_is_empty(empty_stack, populated_stack):
    assert empty_stack.is_empty
    assert not populated_stack.is_empty


def test_push(empty_stack):
    empty_stack.push(1)
    empty_stack.push(2)
    empty_stack.push(3)

    assert empty_stack.peek() == 3
    assert len(empty_stack) == 3


def test_pop(populated_stack):
    assert populated_stack.pop() == TEST_DATA[-1]
    assert populated_stack.pop() == TEST_DATA[-2]
    assert populated_stack.pop() == TEST_DATA[-3]
    assert len(populated_stack) == NUM_ELEMENTS - 3


def test_pop_index_error(empty_stack):
    with pytest.raises(IndexError):
        empty_stack.pop()


def test_peek(populated_stack):
    assert populated_stack.peek() == TEST_DATA[-1]
    assert populated_stack.peek() == TEST_DATA[-1]
    assert len(populated_stack) == NUM_ELEMENTS


def test_peek_index_error(empty_stack):
    with pytest.raises(IndexError):
        empty_stack.peek()


def test_clear(empty_stack, populated_stack):
    empty_stack.clear()
    assert list(empty_stack) == []
    assert len(empty_stack) == 0

    populated_stack.clear()
    assert list(populated_stack) == []
    assert len(populated_stack) == 0


def test_traverse_is_immutable(populated_stack):
    items = list(populated_stack)
    original_len = len(populated_stack)

    items.append(999)
    items.clear()

    assert len(populated_stack) == original_len
    assert list(populated_stack) != items


def test_len(empty_stack, populated_stack):
    assert len(empty_stack) == 0
    assert len(populated_stack) == NUM_ELEMENTS


def test_repr(empty_stack, populated_stack):
    assert repr(empty_stack) == "Stack([])"
    assert repr(populated_stack) == f"Stack({TEST_DATA})"


def test_str(empty_stack, populated_stack):
    assert str(empty_stack) == "[]"
    assert str(populated_stack) == f"{TEST_DATA}"
