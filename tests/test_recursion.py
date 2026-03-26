import pytest

from dsa import (
    factorial,
    fibonacci,
    recursive_max,
    recursive_reverse,
    recursive_sum,
    sum_nested_list,
)


@pytest.mark.parametrize(
    ("input_list", "expected"),
    [
        ([1, 2, 3, 4], 10),
        ([1.5, 2.5, 3.0], 7.0),
        ([47], 47),
        ([], 0),
    ],
)
def test_recursive_sum_basic(input_list, expected):
    assert recursive_sum(input_list) == expected


def test_recursive_sum_type_error():
    with pytest.raises(TypeError):
        recursive_sum([1, "2", 3])


@pytest.mark.parametrize(
    ("input_list", "expected"),
    [
        ([-2, 4, 9, 7, 3], 9),
        ([3.5, 2.5, 6.0], 6.0),
        ([47], 47),
    ],
)
def test_recursive_max(input_list, expected):
    assert recursive_max(input_list) == expected


def test_recursive_max_value_error():
    with pytest.raises(ValueError):  # noqa: PT011
        recursive_max([])


def test_recursive_max_element_type_error():
    with pytest.raises(TypeError):
        recursive_max([1, "2", 3])


@pytest.mark.parametrize(
    ("input_list", "expected"),
    [
        ([1, 2, 3, 4], [4, 3, 2, 1]),
        (["a", "b", "c"], ["c", "b", "a"]),
        ([47], [47]),
        ([], []),
    ],
)
def test_recursive_reverse(input_list, expected):
    assert recursive_reverse(input_list) == expected


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (0, 1),
        (1, 1),
        (5, 120),
        (10, 3628800),
    ],
)
def test_factorial(n, expected):
    assert factorial(n) == expected


def test_factorial_errors():
    with pytest.raises(ValueError):  # noqa: PT011
        factorial(-1)
    with pytest.raises(TypeError):
        factorial(5.5)


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (7, 13),
    ],
)
def test_fibonacci(n, expected):
    assert fibonacci(n) == expected


def test_fibonacci_errors():
    with pytest.raises(ValueError):  # noqa: PT011
        fibonacci(-1)
    with pytest.raises(TypeError):
        fibonacci(5.5)


def test_sum_nested_list():
    assert sum_nested_list([1, [2], 3]) == 6
    assert sum_nested_list([1, [2, [3, 4], 5], 6]) == 21
    assert sum_nested_list([]) == 0


def test_sum_nested_list_type_error():
    with pytest.raises(TypeError):
        sum_nested_list([1, ["string"], 3])
