import pytest

from dsa import DynamicArray

# --- Constants ---

NUM_ELEMENTS = 5
TEST_DATA = list(range(NUM_ELEMENTS))  # [0, 1, 2, 3, 4]

# --- Fixtures ---


@pytest.fixture
def empty_array() -> DynamicArray[int]:
    """Return an empty DynamicArray."""
    return DynamicArray()


@pytest.fixture
def populated_array() -> DynamicArray[int]:
    """Return a DynamicArray populated with TEST_DATA."""
    arr: DynamicArray[int] = DynamicArray()
    for val in TEST_DATA:
        arr.append(val)
    return arr


# --- Tests: Initialization ---


def test_initial_state(empty_array):
    """Array should start empty with capacity of 1."""
    assert len(empty_array) == 0
    assert empty_array.capacity == 1
    assert empty_array.is_empty


# --- Tests: Append ---


def test_append_single(empty_array):
    """Appending one element should update size and content."""
    empty_array.append(42)
    assert len(empty_array) == 1
    assert empty_array[0] == 42
    assert not empty_array.is_empty


def test_append_multiple(empty_array):
    """Appending multiple elements should preserve order."""
    for val in TEST_DATA:
        empty_array.append(val)
    assert len(empty_array) == NUM_ELEMENTS
    assert list(empty_array) == TEST_DATA


def test_append_triggers_resize(empty_array):
    """Capacity should double when array is full."""
    assert empty_array.capacity == 1
    empty_array.append(1)
    assert empty_array.capacity == 1
    empty_array.append(2)
    assert empty_array.capacity == 2
    empty_array.append(3)
    assert empty_array.capacity == 4


# --- Tests: Getitem / Setitem ---


def test_getitem(populated_array):
    """Should return correct element at each index."""
    for i, val in enumerate(TEST_DATA):
        assert populated_array[i] == val


def test_setitem(populated_array):
    """Should update element at given index."""
    populated_array[0] = 99
    assert populated_array[0] == 99


def test_getitem_out_of_bounds(populated_array, empty_array):
    """Should raise IndexError for invalid indices."""
    with pytest.raises(IndexError, match="out of bounds"):
        populated_array[NUM_ELEMENTS]
    with pytest.raises(IndexError, match="out of bounds"):
        populated_array[-1]
    with pytest.raises(IndexError, match="out of bounds"):
        empty_array[0]


def test_setitem_out_of_bounds(populated_array):
    """Should raise IndexError when setting at invalid index."""
    with pytest.raises(IndexError, match="out of bounds"):
        populated_array[NUM_ELEMENTS] = 99


# --- Tests: Insert ---


def test_insert_at_beginning(populated_array):
    """Inserting at index 0 should shift all elements right."""
    populated_array.insert(0, 99)
    assert populated_array[0] == 99
    assert populated_array[1] == TEST_DATA[0]
    assert len(populated_array) == NUM_ELEMENTS + 1


def test_insert_at_middle(populated_array):
    """Inserting at middle index should shift elements correctly."""
    middle = NUM_ELEMENTS // 2
    populated_array.insert(middle, 99)
    assert populated_array[middle] == 99
    assert len(populated_array) == NUM_ELEMENTS + 1


def test_insert_at_end(populated_array):
    """Inserting at index == size should append to the end."""
    populated_array.insert(NUM_ELEMENTS, 99)
    assert populated_array[NUM_ELEMENTS] == 99
    assert len(populated_array) == NUM_ELEMENTS + 1


def test_insert_out_of_bounds(populated_array):
    """Should raise IndexError for invalid insert index."""
    with pytest.raises(IndexError, match="out of bounds"):
        populated_array.insert(NUM_ELEMENTS + 1, 99)
    with pytest.raises(IndexError, match="out of bounds"):
        populated_array.insert(-1, 99)


# --- Tests: Remove ---


def test_remove_first(populated_array):
    """Removing first element should shift all elements left."""
    populated_array.remove(0)
    assert populated_array[0] == TEST_DATA[1]
    assert len(populated_array) == NUM_ELEMENTS - 1


def test_remove_middle(populated_array):
    """Removing middle element should shift right elements left."""
    middle = NUM_ELEMENTS // 2
    populated_array.remove(middle)
    assert populated_array[middle] == TEST_DATA[middle + 1]
    assert len(populated_array) == NUM_ELEMENTS - 1


def test_remove_last(populated_array):
    """Removing last element should decrease size by one."""
    last_val = TEST_DATA[-2]
    populated_array.remove(NUM_ELEMENTS - 1)
    assert populated_array[NUM_ELEMENTS - 2] == last_val
    assert len(populated_array) == NUM_ELEMENTS - 1


def test_remove_out_of_bounds(populated_array, empty_array):
    """Should raise IndexError for invalid remove index."""
    with pytest.raises(IndexError, match="out of bounds"):
        populated_array.remove(NUM_ELEMENTS)
    with pytest.raises(IndexError, match="out of bounds"):
        empty_array.remove(0)


# --- Tests: Pop ---


def test_pop_returns_last(populated_array):
    """Pop should return and remove the last element."""
    value = populated_array.pop()
    assert value == TEST_DATA[-1]
    assert len(populated_array) == NUM_ELEMENTS - 1


def test_pop_until_empty(populated_array):
    """Popping all elements should result in an empty array."""
    for val in reversed(TEST_DATA):
        assert populated_array.pop() == val
    assert populated_array.is_empty


def test_pop_empty_array(empty_array):
    """Should raise IndexError when popping from empty array."""
    with pytest.raises(IndexError, match="Pop from empty array"):
        empty_array.pop()


# --- Tests: Iteration ---


def test_iter(populated_array):
    """Iterating should yield all elements in order."""
    assert list(populated_array) == TEST_DATA


def test_iter_empty(empty_array):
    """Iterating over empty array should yield nothing."""
    assert list(empty_array) == []


# --- Tests: Repr / Str ---


def test_repr(populated_array):
    """repr should show class name and elements."""
    assert repr(populated_array) == f"DynamicArray({TEST_DATA})"


def test_str(populated_array):
    """str should show elements in readable format."""
    assert str(populated_array) == f"[{', '.join(str(x) for x in TEST_DATA)}]"


def test_str_empty(empty_array):
    """str of empty array should return empty brackets."""
    assert str(empty_array) == "[]"


# --- Tests: is_empty / capacity ---


def test_is_empty(empty_array, populated_array):
    """is_empty should reflect actual state."""
    assert empty_array.is_empty
    assert not populated_array.is_empty


def test_capacity_never_less_than_size(populated_array):
    """Capacity should always be >= size."""
    assert populated_array.capacity >= len(populated_array)
