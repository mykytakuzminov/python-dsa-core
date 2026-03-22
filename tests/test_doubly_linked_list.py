import pytest

from dsa import DoublyLinkedList

# --- Constants ---
NUM_ELEMENTS = 5
TEST_DATA = list(range(5))
NEW_HEAD = 99
NEW_MIDDLE = 55
NEW_TAIL = 100
INVALID_LOW_INDEX = -1
INVALID_HIGH_INDEX = NUM_ELEMENTS + 1
NOT_EXISTING_VALUE = 999
NOT_EXISTING_VALUES = [NEW_HEAD, NEW_MIDDLE, NEW_TAIL, NOT_EXISTING_VALUE]
PARAM_DATA = [(i, val) for i, val in enumerate(TEST_DATA)]


# --- Fixtures ---
@pytest.fixture
def empty_list():
    """Return an empty doubly linked list."""
    return DoublyLinkedList()


@pytest.fixture
def populated_list():
    """Return a doubly linked list pre-populated with TEST_DATA values."""
    dll = DoublyLinkedList()
    for n in TEST_DATA:
        dll.append(n)
    return dll


# --- Tests: Emptiness ---
def test_is_empty(empty_list, populated_list):
    """Check is_empty() for empty and populated lists."""
    assert empty_list.is_empty
    assert not populated_list.is_empty


# --- Tests: Adding Elements ---
def test_append(empty_list):
    """Test append() adds elements to the end of the list."""
    empty_list.append(1)
    empty_list.append(2)
    empty_list.append(3)
    assert list(empty_list) == [1, 2, 3]
    assert len(empty_list) == 3
    assert empty_list._get_head().value == 1
    assert empty_list._get_tail().value == 3


def test_prepend(empty_list, populated_list):
    """Test prepend() adds elements to the beginning of the list."""
    empty_list.prepend(NEW_HEAD)
    assert list(empty_list) == [NEW_HEAD]
    assert len(empty_list) == 1
    assert empty_list._get_head().value == NEW_HEAD
    assert empty_list._get_tail().value == NEW_HEAD

    populated_list.prepend(NEW_HEAD)
    assert list(populated_list) == [NEW_HEAD, *TEST_DATA]
    assert len(populated_list) == NUM_ELEMENTS + 1
    assert populated_list._get_head().value == NEW_HEAD
    assert populated_list._get_tail().value == TEST_DATA[-1]


def test_insert(populated_list):
    """Test insert() at head, middle, and tail positions."""
    # Insert at head
    populated_list.insert(0, NEW_HEAD)
    assert next(iter(populated_list)) == NEW_HEAD

    # Insert at middle
    middle_index = NUM_ELEMENTS // 2
    populated_list.insert(middle_index, NEW_MIDDLE)
    assert list(populated_list)[middle_index] == NEW_MIDDLE

    # Insert at tail
    populated_list.insert(len(populated_list), NEW_TAIL)
    assert list(populated_list)[-1] == NEW_TAIL

    # Verify list length and head/tail
    assert len(populated_list) == NUM_ELEMENTS + 3
    assert populated_list._get_head().value == NEW_HEAD
    assert populated_list._get_tail().value == NEW_TAIL


def test_insert_index_error(populated_list):
    """Verify insert() raises IndexError for invalid indices."""
    with pytest.raises(IndexError):
        populated_list.insert(INVALID_LOW_INDEX, NEW_MIDDLE)
    with pytest.raises(IndexError):
        populated_list.insert(INVALID_HIGH_INDEX, NEW_MIDDLE)


# --- Tests: Removing Elements ---
def test_delete(populated_list):
    """Test delete() removes elements and handles non-existing values."""
    # Remove head
    assert populated_list.delete(TEST_DATA[0])
    assert TEST_DATA[0] not in list(populated_list)

    # Remove middle
    assert populated_list.delete(TEST_DATA[2])
    assert TEST_DATA[2] not in list(populated_list)

    # Remove tail
    assert populated_list.delete(TEST_DATA[-1])
    assert TEST_DATA[-1] not in list(populated_list)

    # Attempt to remove non-existing value
    assert not populated_list.delete(NOT_EXISTING_VALUE)

    # Verify head and tail remain consistent
    assert populated_list._get_head().value == TEST_DATA[1]
    assert populated_list._get_tail().value == TEST_DATA[-2]


# --- Tests: Front/Back Access Methods ---
def test_pop_front_one_element(empty_list):
    """Test pop_front() on a list with a single element."""
    empty_list.append(0)

    assert empty_list.pop_front() == 0
    assert len(empty_list) == 0
    assert empty_list._get_head() is None
    assert empty_list._get_tail() is None


def test_pop_front_many_elements(populated_list):
    """Test pop_front() on a list with multiple elements."""
    assert populated_list.pop_front() == TEST_DATA[0]
    assert len(populated_list) == NUM_ELEMENTS - 1
    assert populated_list._get_head().value == TEST_DATA[1]
    assert populated_list._get_head().prev is None
    assert populated_list._get_tail().value == TEST_DATA[-1]

    assert populated_list.pop_front() == TEST_DATA[1]
    assert len(populated_list) == NUM_ELEMENTS - 2
    assert populated_list._get_head().value == TEST_DATA[2]
    assert populated_list._get_head().prev is None
    assert populated_list._get_tail().value == TEST_DATA[-1]


def test_pop_front_index_error(empty_list):
    """Test pop_front() raises IndexError for an empty list."""
    with pytest.raises(IndexError):
        empty_list.pop_front()


def test_peek_front(populated_list):
    """Test peek_front() returns the first element without removing it."""
    first_element = TEST_DATA[0]
    for _ in range(2):
        assert populated_list.peek_front() == first_element
    assert len(populated_list) == NUM_ELEMENTS


def test_peek_front_index_error(empty_list):
    """Test peek_front() raises IndexError for an empty list."""
    with pytest.raises(IndexError):
        empty_list.peek_front()


def test_peek_back(populated_list):
    """Test peek_back() returns the last element without removing it."""
    last_element = TEST_DATA[-1]
    for _ in range(2):
        assert populated_list.peek_back() == last_element
    assert len(populated_list) == NUM_ELEMENTS


def test_peek_back_index_error(empty_list):
    """Test peek_back() raises IndexError for an empty list."""
    with pytest.raises(IndexError):
        empty_list.peek_back()


# --- Tests: Accessing Elements ---
@pytest.mark.parametrize(("index", "expected"), PARAM_DATA)
def test_get(populated_list, index, expected):
    """Test get() returns correct element for valid indices."""
    assert populated_list.get(index) == expected


def test_get_index_error(populated_list):
    """Test get() raises IndexError for invalid indices."""
    with pytest.raises(IndexError):
        populated_list.get(INVALID_LOW_INDEX)
    with pytest.raises(IndexError):
        populated_list.get(INVALID_HIGH_INDEX)


# --- Tests: Searching Elements ---
@pytest.mark.parametrize("value", TEST_DATA)
def test_search_existing(populated_list, value):
    """Verify search() finds existing elements."""
    assert populated_list.search(value)


@pytest.mark.parametrize("value", NOT_EXISTING_VALUES)
def test_search_not_existing(populated_list, value):
    """Verify search() returns False for non-existing elements."""
    assert not populated_list.search(value)


# --- Tests: Traversal ---
def test_traverse_empty(empty_list):
    """Check traverse() returns empty list for empty linked list."""
    assert list(empty_list) == []


def test_traverse_populated(populated_list):
    """Check traverse() returns all elements in correct order."""
    assert list(populated_list) == TEST_DATA


# --- Tests: Links Integrity ---
def test_links_integrity(populated_list):
    """Ensure all 'next' and 'prev' pointers are consistent."""
    current = populated_list._get_head()
    while current.next:
        assert current.next.prev == current
        current = current.next


# --- Tests: Clearing the List ---
def test_clear(empty_list, populated_list):
    """Check clear() empties the list and resets length, head, and tail."""
    empty_list.clear()
    assert list(empty_list) == []
    assert len(empty_list) == 0
    assert empty_list._get_head() is None
    assert empty_list._get_tail() is None

    populated_list.clear()
    assert list(populated_list) == []
    assert len(populated_list) == 0
    assert populated_list._get_head() is None
    assert populated_list._get_tail() is None


# --- Tests: Length & String Representation ---
def test_len(empty_list, populated_list):
    """Verify __len__() returns correct number of elements."""
    assert len(empty_list) == 0
    assert len(populated_list) == NUM_ELEMENTS


def test_str(empty_list, populated_list):
    """Verify __str__() returns correct string representation."""
    assert str(empty_list) == "DoublyLinkedList([])"
    assert str(populated_list) == f"DoublyLinkedList({TEST_DATA})"
