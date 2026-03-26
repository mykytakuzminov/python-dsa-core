import pytest

from dsa import (
    bubble_sort,
    counting_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    selection_sort,
)

STRING_TEST_CASES = [
    (["apple", "banana", "cherry", "date"], ["apple", "banana", "cherry", "date"]),
    (["date", "cherry", "banana", "apple"], ["apple", "banana", "cherry", "date"]),
    (["kiwi", "apple", "orange", "grape"], ["apple", "grape", "kiwi", "orange"]),
    (["apple", "Apricot", "APPLE", "banana"], ["APPLE", "Apricot", "apple", "banana"]),
    (["cat", "dog", "ant", "zebra"], ["ant", "cat", "dog", "zebra"]),
]

BASE_TEST_CASES = [
    ([], []),
    ([5], [5]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([4, 1, 3, 9, 7], [1, 3, 4, 7, 9]),
    ([4, 2, 4, 1, 3, 1], [1, 1, 2, 3, 4, 4]),
    ([0, -1, 5, -2, 3], [-2, -1, 0, 3, 5]),
    ([4.5, 1.1, 3.8, 9.2, 7.0], [1.1, 3.8, 4.5, 7.0, 9.2]),
    *STRING_TEST_CASES,
]

COUNTING_SORT_TEST_CASES = [
    ([], []),
    ([5], [5]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([4, 1, 3, 9, 7], [1, 3, 4, 7, 9]),
    ([4, 2, 4, 1, 3, 1], [1, 1, 2, 3, 4, 4]),
    ([0, 10, 2, 0, 5], [0, 0, 2, 5, 10]),
]


def run_sort_test(sort_func, input_list, expected):
    arr_copy = list(input_list)
    sort_func(arr_copy)
    assert arr_copy == expected


@pytest.mark.parametrize(("input_list", "expected"), BASE_TEST_CASES)
def test_bubble_sort(input_list, expected):
    run_sort_test(bubble_sort, input_list, expected)


@pytest.mark.parametrize(("input_list", "expected"), BASE_TEST_CASES)
def test_insertion_sort(input_list, expected):
    run_sort_test(insertion_sort, input_list, expected)


@pytest.mark.parametrize(("input_list", "expected"), BASE_TEST_CASES)
def test_selection_sort(input_list, expected):
    run_sort_test(selection_sort, input_list, expected)


@pytest.mark.parametrize(("input_list", "expected"), BASE_TEST_CASES)
def test_merge_sort(input_list, expected):
    run_sort_test(merge_sort, input_list, expected)


@pytest.mark.parametrize(("input_list", "expected"), BASE_TEST_CASES)
def test_quick_sort(input_list, expected):
    run_sort_test(quick_sort, input_list, expected)


@pytest.mark.parametrize(("input_list", "expected"), COUNTING_SORT_TEST_CASES)
def test_counting_sort(input_list, expected):
    run_sort_test(counting_sort, input_list, expected)
