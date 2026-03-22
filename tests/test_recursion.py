import pytest

from dsa import (
    factorial,
    fibonacci,
    recursive_max,
    recursive_reverse,
    recursive_sum,
    sum_nested_list,
)


# --- Tests: Recursive Sum ---
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
    """Test recursive_sum with normal cases, single element, and empty list."""
    assert recursive_sum(input_list) == expected


def test_recursive_sum_type_error():
    """Check that recursive_sum raises TypeError for non-numeric elements."""
    with pytest.raises(TypeError):
        recursive_sum([1, "2", 3])


# --- Tests: Recursive Max ---
@pytest.mark.parametrize(
    ("input_list", "expected"),
    [
        ([-2, 4, 9, 7, 3], 9),
        ([3.5, 2.5, 6.0], 6.0),
        ([47], 47),
    ],
)
def test_recursive_max(input_list, expected):
    """Test recursive_max with normal cases and single element."""
    assert recursive_max(input_list) == expected


def test_recursive_max_value_error():
    """Check that recursive_max raises ValueError for an empty list."""
    with pytest.raises(
        ValueError, match="Expected a non-empty list, got an empty list\\."
    ):
        recursive_max([])


def test_recursive_max_element_type_error():
    """Check that recursive_max raises TypeError for non-numeric elements."""
    with pytest.raises(TypeError):
        recursive_max([1, "2", 3])


# --- Tests: Recursive Reverse ---
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
    """Test recursive_reverse with normal cases, single element, and empty list."""
    assert recursive_reverse(input_list) == expected


# --- Tests: Factorial ---
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
    """Test factorial calculation for valid inputs."""
    assert factorial(n) == expected


def test_factorial_errors():
    """Check factorial raises errors for negative numbers or floats."""
    with pytest.raises(
        ValueError, match="Factorial is not defined for negative numbers\\."
    ):
        factorial(-1)
    with pytest.raises(TypeError):
        factorial(5.5)


# --- Tests: Fibonacci ---
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
    """Test fibonacci sequence calculation."""
    assert fibonacci(n) == expected


def test_fibonacci_errors():
    """Check fibonacci raises errors for negative numbers or floats."""
    with pytest.raises(
        ValueError, match="Fibonacci is not defined for negative numbers\\."
    ):
        fibonacci(-1)
    with pytest.raises(TypeError):
        fibonacci(5.5)


# --- Tests: Nested Sum ---
def test_sum_nested_list():
    """Test sum_nested_list with deep nesting and mixed types."""
    assert sum_nested_list([1, [2], 3]) == 6
    assert sum_nested_list([1, [2, [3, 4], 5], 6]) == 21
    assert sum_nested_list([]) == 0


def test_sum_nested_list_type_error():
    """Check sum_nested_list raises TypeError for unsupported types."""
    with pytest.raises(TypeError):
        sum_nested_list([1, ["string"], 3])
