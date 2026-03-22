import pytest

from dsa import binary_search


# --- Tests: Binary Search (Found) ---
@pytest.mark.parametrize(
    ("array", "to_search"),
    [
        ([-5, -3, -1, 0, 1, 2, 6, 7, 8], 2),
        ([0, 1, 2, 3, 4, 5], 5),
        (["apple", "banana", "cherry", "date"], "banana"),
    ],
)
def test_binary_search_found(array, to_search):
    """Tests that binary_search correctly finds existing elements."""
    assert binary_search(array, to_search)


# --- Tests: Binary Search (Not Found) ---
@pytest.mark.parametrize(
    ("array", "to_search"),
    [
        ([-5, -3, -1, 0, 1, 2, 6, 7, 8], 10),
        ([0, 1, 2, 3, 4, 5], -5),
        (["apple", "banana", "cherry"], "fig"),
    ],
)
def test_binary_search_not_found(array, to_search):
    """Tests that binary_search returns False for values not in the list."""
    assert not binary_search(array, to_search)


# --- Tests: Edge Cases ---
def test_binary_search_empty_list():
    """Tests that searching in an empty list always returns False."""
    assert not binary_search([], 5)


def test_binary_search_single_element():
    """Tests that binary_search works correctly for a list with one element."""
    assert binary_search([5], 5)
    assert not binary_search([5], 1)
