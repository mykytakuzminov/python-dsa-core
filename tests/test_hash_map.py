import pytest

from dsa import HashMap

# --- Constants ---
NUM_ELEMENTS = 10
KEY_5 = 5
KEY_10 = 10
NEW_VALUE = 100

TEST_PAIRS = [
    (0, 0),
    (8, 8),
    (1, 1),
    (9, 9),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
]

# Set is used because HashMap order is not guaranteed
SET_OF_TEST_PAIRS = {f"{k}: {v}" for k, v in TEST_PAIRS}


# --- Fixtures ---
@pytest.fixture
def empty_hash_map():
    """Return an empty HashMap."""
    return HashMap()


@pytest.fixture
def populated_hash_map():
    """Return a HashMap filled with TEST_PAIRS."""
    hm = HashMap()
    for k, v in TEST_PAIRS:
        hm.put(k, v)
    return hm


# --- Tests: Emptiness ---
def test_is_empty(empty_hash_map, populated_hash_map):
    """Check is_empty() for empty and populated HashMap."""
    assert empty_hash_map.is_empty
    assert not populated_hash_map.is_empty


# --- Tests: Adding & Updating Keys ---
def test_put_not_existing_key(populated_hash_map):
    """Check inserting a new key increases length and stores value."""
    populated_hash_map.put(KEY_10, NEW_VALUE)
    assert populated_hash_map.get(KEY_10) == NEW_VALUE
    assert len(populated_hash_map) == NUM_ELEMENTS + 1


def test_put_existing_key(populated_hash_map):
    """Check updating an existing key keeps length same and updates value."""
    populated_hash_map.put(KEY_5, NEW_VALUE)
    assert populated_hash_map.get(KEY_5) == NEW_VALUE
    assert len(populated_hash_map) == NUM_ELEMENTS


def test_put_collision(empty_hash_map):
    """
    Test collisions: multiple keys hashing to the same bucket.
    For capacity=8, keys 0, 8, 16 hash to the same index (0).
    """
    empty_hash_map.put(0, 0)
    empty_hash_map.put(8, 8)
    empty_hash_map.put(16, 16)

    assert empty_hash_map.get(0) == 0
    assert empty_hash_map.get(8) == 8
    assert empty_hash_map.get(16) == 16
    assert len(empty_hash_map) == 3


# --- Tests: Retrieving Values ---
@pytest.mark.parametrize(("key", "value"), TEST_PAIRS)
def test_get_existing(populated_hash_map, key, value):
    """Check get() returns correct value for existing keys."""
    assert populated_hash_map.get(key) == value


def test_get_missing(empty_hash_map):
    """Check get() returns None for missing keys."""
    assert empty_hash_map.get(999) is None


# --- Tests: Contains (in operator) ---
def test_contains(populated_hash_map):
    """Check __contains__ implementation (the 'in' operator)."""
    assert 5 in populated_hash_map
    assert 999 not in populated_hash_map


# --- Tests: Keys and Values ---
def test_keys(populated_hash_map):
    """Check keys() returns a list of all keys."""
    keys = populated_hash_map.keys()
    assert len(keys) == NUM_ELEMENTS
    assert set(keys) == {k for k, _ in TEST_PAIRS}


def test_values(populated_hash_map):
    """Check values() returns a list of all values."""
    values = populated_hash_map.values()
    assert len(values) == NUM_ELEMENTS
    assert set(values) == {v for _, v in TEST_PAIRS}


# --- Tests: Removing Keys ---
def test_remove_existing_key(populated_hash_map):
    """Check removing an existing key decreases length and removes value."""
    assert populated_hash_map.remove(KEY_5)
    assert len(populated_hash_map) == NUM_ELEMENTS - 1
    assert populated_hash_map.get(KEY_5) is None


def test_remove_not_existing_key(populated_hash_map):
    """Check removing a non-existing key returns False and length stays same."""
    assert not populated_hash_map.remove(KEY_10)
    assert len(populated_hash_map) == NUM_ELEMENTS


# --- Tests: Clearing ---
def test_clear(populated_hash_map):
    """Check clear() removes all items."""
    populated_hash_map.clear()
    assert len(populated_hash_map) == 0
    assert populated_hash_map.is_empty
    assert populated_hash_map.keys() == []


# --- Tests: Length & String Representation ---
def test_len(empty_hash_map, populated_hash_map):
    """Check __len__ returns correct number of elements."""
    assert len(empty_hash_map) == 0
    assert len(populated_hash_map) == NUM_ELEMENTS


def test_str(empty_hash_map, populated_hash_map):
    """Check __str__ returns correct string representation."""
    assert str(empty_hash_map) == "{}"

    # Parse string back to set of strings to verify content regardless of order
    result_str = str(populated_hash_map).strip("{}")
    actual_pairs = set(result_str.split(", ")) if result_str else set()

    assert actual_pairs == SET_OF_TEST_PAIRS
