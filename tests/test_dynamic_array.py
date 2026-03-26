import pytest

from dsa import DynamicArray

NUM_ELEMENTS = 5
TEST_DATA = list(range(NUM_ELEMENTS))  # [0, 1, 2, 3, 4]


@pytest.fixture
def empty_array() -> DynamicArray[int]:
    return DynamicArray()


@pytest.fixture
def populated_array() -> DynamicArray[int]:
    arr: DynamicArray[int] = DynamicArray()
    for val in TEST_DATA:
        arr.append(val)
    return arr


def test_initial_state(empty_array):
    assert len(empty_array) == 0
    assert empty_array.capacity == 1
    assert empty_array.is_empty


def test_append_single(empty_array):
    empty_array.append(42)
    assert len(empty_array) == 1
    assert empty_array[0] == 42
    assert not empty_array.is_empty


def test_append_multiple(empty_array):
    for val in TEST_DATA:
        empty_array.append(val)
    assert len(empty_array) == NUM_ELEMENTS
    assert list(empty_array) == TEST_DATA


def test_append_triggers_resize(empty_array):
    assert empty_array.capacity == 1
    empty_array.append(1)
    assert empty_array.capacity == 1
    empty_array.append(2)
    assert empty_array.capacity == 2
    empty_array.append(3)
    assert empty_array.capacity == 4


def test_getitem(populated_array):
    for i, val in enumerate(TEST_DATA):
        assert populated_array[i] == val


def test_setitem(populated_array):
    populated_array[0] = 99
    assert populated_array[0] == 99


def test_getitem_out_of_bounds(populated_array, empty_array):
    with pytest.raises(IndexError):
        populated_array[NUM_ELEMENTS]
    with pytest.raises(IndexError):
        populated_array[-1]
    with pytest.raises(IndexError):
        empty_array[0]


def test_setitem_out_of_bounds(populated_array):
    with pytest.raises(IndexError):
        populated_array[NUM_ELEMENTS] = 99


def test_insert_at_beginning(populated_array):
    populated_array.insert(0, 99)
    assert populated_array[0] == 99
    assert populated_array[1] == TEST_DATA[0]
    assert len(populated_array) == NUM_ELEMENTS + 1


def test_insert_at_middle(populated_array):
    middle = NUM_ELEMENTS // 2
    populated_array.insert(middle, 99)
    assert populated_array[middle] == 99
    assert len(populated_array) == NUM_ELEMENTS + 1


def test_insert_at_end(populated_array):
    populated_array.insert(NUM_ELEMENTS, 99)
    assert populated_array[NUM_ELEMENTS] == 99
    assert len(populated_array) == NUM_ELEMENTS + 1


def test_insert_out_of_bounds(populated_array):
    with pytest.raises(IndexError):
        populated_array.insert(NUM_ELEMENTS + 1, 99)
    with pytest.raises(IndexError):
        populated_array.insert(-1, 99)


def test_remove_first(populated_array):
    populated_array.remove(0)
    assert populated_array[0] == TEST_DATA[1]
    assert len(populated_array) == NUM_ELEMENTS - 1


def test_remove_middle(populated_array):
    middle = NUM_ELEMENTS // 2
    populated_array.remove(middle)
    assert populated_array[middle] == TEST_DATA[middle + 1]
    assert len(populated_array) == NUM_ELEMENTS - 1


def test_remove_last(populated_array):
    last_val = TEST_DATA[-2]
    populated_array.remove(NUM_ELEMENTS - 1)
    assert populated_array[NUM_ELEMENTS - 2] == last_val
    assert len(populated_array) == NUM_ELEMENTS - 1


def test_remove_out_of_bounds(populated_array, empty_array):
    with pytest.raises(IndexError):
        populated_array.remove(NUM_ELEMENTS)
    with pytest.raises(IndexError):
        empty_array.remove(0)


def test_pop_returns_last(populated_array):
    value = populated_array.pop()
    assert value == TEST_DATA[-1]
    assert len(populated_array) == NUM_ELEMENTS - 1


def test_pop_until_empty(populated_array):
    for val in reversed(TEST_DATA):
        assert populated_array.pop() == val
    assert populated_array.is_empty


def test_pop_empty_array(empty_array):
    with pytest.raises(IndexError):
        empty_array.pop()


def test_iter(populated_array):
    assert list(populated_array) == TEST_DATA


def test_iter_empty(empty_array):
    assert list(empty_array) == []


def test_repr(populated_array):
    assert repr(populated_array) == f"DynamicArray({TEST_DATA})"


def test_str(populated_array):
    assert str(populated_array) == f"[{', '.join(str(x) for x in TEST_DATA)}]"


def test_str_empty(empty_array):
    assert str(empty_array) == "[]"


def test_is_empty(empty_array, populated_array):
    assert empty_array.is_empty
    assert not populated_array.is_empty


def test_capacity_never_less_than_size(populated_array):
    assert populated_array.capacity >= len(populated_array)
