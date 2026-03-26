import pytest

from dsa import binary_search


@pytest.mark.parametrize(
    ("array", "to_search"),
    [
        ([-5, -3, -1, 0, 1, 2, 6, 7, 8], 2),
        ([0, 1, 2, 3, 4, 5], 5),
        (["apple", "banana", "cherry", "date"], "banana"),
    ],
)
def test_binary_search_found(array, to_search):
    assert binary_search(array, to_search)


@pytest.mark.parametrize(
    ("array", "to_search"),
    [
        ([-5, -3, -1, 0, 1, 2, 6, 7, 8], 10),
        ([0, 1, 2, 3, 4, 5], -5),
        (["apple", "banana", "cherry"], "fig"),
    ],
)
def test_binary_search_not_found(array, to_search):
    assert not binary_search(array, to_search)


def test_binary_search_empty_list():
    assert not binary_search([], 5)


def test_binary_search_single_element():
    assert binary_search([5], 5)
    assert not binary_search([5], 1)
