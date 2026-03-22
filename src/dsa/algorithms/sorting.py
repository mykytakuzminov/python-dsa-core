from typing import Any, Protocol, TypeVar


class Comparable(Protocol):
    """Protocol for objects that support comparison operations."""

    def __lt__(self, other: Any, /) -> bool: ...
    def __gt__(self, other: Any, /) -> bool: ...
    def __eq__(self, other: object, /) -> bool: ...
    def __le__(self, other: Any, /) -> bool: ...
    def __ge__(self, other: Any, /) -> bool: ...


T = TypeVar("T", bound=Comparable)


# --- Comparison Based Sorting Algorithms ---


def bubble_sort[T: Comparable](arr: list[T]) -> None:
    """
    Sorts a list in ascending order using the optimized Bubble Sort algorithm.

    Bubble Sort repeatedly steps through the list, compares adjacent elements,
    and swaps them if they are in the wrong order. This implementation includes
    an optimization to stop early if a pass completes without any swaps.
    It is an in-place sorting algorithm.

    Complexity:
        - Best Case (already sorted): O(n)
        - Average Case: O(n^2)
        - Worst Case (reverse sorted): O(n^2)

    Args:
        arr: A list of elements that supports comparison operations (e.g., int, float).
             The sort is performed in-place.
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(1, n - i):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                swapped = True
        if not swapped:
            break


def insertion_sort[T: Comparable](arr: list[T]) -> None:
    """
    Sorts a list in ascending order using the Insertion Sort algorithm.

    Insertion Sort builds the final sorted list one item at a time. It iterates
    through the input elements and inserts each element into its correct position
    in the already-sorted part of the array.
    It is an in-place sorting algorithm.

    Complexity:
        - Best Case (already sorted): O(n)
        - Average Case: O(n^2)
        - Worst Case (reverse sorted): O(n^2)

    Args:
        arr: A list of elements that supports comparison operations (e.g., int, float).
             The sort is performed in-place.
    """
    n = len(arr)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break


def selection_sort[T: Comparable](arr: list[T]) -> None:
    """
    Sorts a list in ascending order using the Selection Sort algorithm.

    Selection Sort divides the input list into two sublists: a sorted sublist
    built up from the front and the remaining unsorted sublist. It repeatedly
    finds the minimum element from the unsorted sublist and swaps it with the
    first element of the unsorted sublist (which is also the element at the
    boundary of the sorted sublist). It is an in-place sorting algorithm.

    Complexity:
        - Best Case (already sorted): O(n^2)
        - Average Case: O(n^2)
        - Worst Case (reverse sorted): O(n^2)

    Args:
        arr: A list of elements that supports comparison operations (e.g., int, float).
             The sort is performed in-place.
    """
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


def merge_sort[T: Comparable](arr: list[T]) -> None:
    """
    Sorts a list in ascending order using the Merge Sort algorithm (Divide and Conquer).

    Merge Sort is a stable, comparison-based algorithm that recursively divides
    the list into halves until single-element sublists are obtained. It then
    merges these sublists in a way that results in a sorted list.
    The time complexity relies on using O(n) auxiliary space for the merge step.

    Complexity:
        - Best Case (already sorted): O(n log n)
        - Average Case: O(n log n)
        - Worst Case (reverse sorted): O(n log n)
        - Space Complexity: O(n) (due to auxiliary arrays in merge)

    Args:
        arr: A list of elements that supports comparison operations (e.g., int, float).
             The sort is performed in-place (with O(n) auxiliary space).
    """
    if len(arr) <= 1:
        return
    _merge_sort_partition(arr, 0, len(arr) - 1)


def quick_sort[T: Comparable](arr: list[T]) -> None:
    """
    Sorts a list in ascending order using the Quick Sort algorithm (Divide and Conquer).

    Quick Sort is an in-place, comparison-based algorithm that picks an element
    as a pivot and partitions the list around the picked pivot. The partitioning
    places the pivot in its correct sorted position, with all smaller elements
    to its left and all greater elements to its right. It then recursively
    sorts the sub-lists.

    It is generally one of the fastest sorting algorithms in practice.
    The space complexity is O(log n) due to the recursive call stack.

    Complexity:
        - Best Case (good pivot selection): O(n log n)
        - Average Case: O(n log n)
        - Worst Case (bad pivot selection, e.g., already sorted): O(n^2)
        - Space Complexity: O(log n) (due to recursion stack)

    Args:
        arr: A list of elements that supports comparison operations (e.g., int, float).
             The sort is performed in-place.
    """
    if len(arr) <= 1:
        return
    _quick_sort_helper(arr, 0, len(arr) - 1)


# --- Non-Comparison Based Sorting Algorithms ---


def counting_sort(arr: list[int]) -> None:
    """
    Sorts a list of non-negative integers using the Counting Sort algorithm.

    Counting Sort is a non-comparison-based integer sorting algorithm. It works
    by counting the number of occurrences of each distinct element in the input
    array and then calculating the position of each element in the output sequence.

    Constraints:
        - The input must consist of non-negative integers.
        - The algorithm is most efficient when the range of input numbers (k)
          is not significantly larger than the number of elements (n).

    Complexity:
        - Time Complexity: O(n + k), where n is the number of elements
          and k is the range of non-negative input values (max(arr) + 1).
        - Space Complexity: O(k)

    Args:
        arr: A list of non-negative integers to be sorted.
             The sort is performed in-place in this implementation.
    """
    if len(arr) <= 1:
        return

    max_val = max(arr)
    counts = [0] * (max_val + 1)

    for x in arr:
        counts[x] += 1

    i = 0
    for val, count in enumerate(counts):
        while count > 0:
            arr[i] = val
            i += 1
            count -= 1


# --- Private Helpers ---


def _merge_sort_helper[T: Comparable](
    arr: list[T], left: int, mid: int, right: int
) -> None:
    """
    Combines two already sorted sub-arrays into a single sorted sub-array.

    This function performs the merging step of the Merge Sort algorithm, combining
    the sorted left sub-array (arr[left...mid]) and the sorted right sub-array
    (arr[mid+1...right]) back into the original array.

    It uses auxiliary space (O(n)) to store the sub-arrays for comparison,
    which is essential for maintaining the O(n log n) time complexity.

    Args:
        arr: The list containing the sub-arrays to be merged. The merge is
             performed in-place within the boundaries [left, right].
        left: The starting index of the first (left) sorted sub-array.
        mid: The ending index of the first (left) sorted sub-array.
        right: The ending index of the second (right) sorted sub-array.
    """
    L = arr[left : mid + 1]
    R = arr[mid + 1 : right + 1]

    li = ri = 0
    curr = left

    while li < len(L) and ri < len(R):
        if L[li] <= R[ri]:
            arr[curr] = L[li]
            li += 1
        else:
            arr[curr] = R[ri]
            ri += 1
        curr += 1

    while li < len(L):
        arr[curr] = L[li]
        li += 1
        curr += 1

    while ri < len(R):
        arr[curr] = R[ri]
        ri += 1
        curr += 1


def _merge_sort_partition[T: Comparable](arr: list[T], left: int, right: int) -> None:
    """
    The recursive core function for the Merge Sort algorithm (Divide step).

    This function recursively divides the array into two halves until the sub-arrays
    contain at most one element (base case). Once the base case is reached, it
    calls the _merge function to combine the sorted halves.

    Complexity:
        - Time: The recursive calls define the O(log n) depth of the algorithm.

    Args:
        arr: The list being sorted.
        left: The starting index of the current partition.
        right: The ending index of the current partition.
    """
    if left < right:
        mid = (left + right) // 2
        _merge_sort_partition(arr, left, mid)
        _merge_sort_partition(arr, mid + 1, right)
        _merge_sort_helper(arr, left, mid, right)


def _quick_sort_helper[T: Comparable](arr: list[T], left: int, right: int) -> None:
    """
    The recursive core function for the Quick Sort algorithm.

    This function recursively calls itself on the sub-arrays created by the
    partition step, effectively implementing the Divide and Conquer strategy.

    Args:
        arr: The list being sorted.
        left: The starting index of the current partition.
        right: The ending index of the current partition.
    """
    if left < right:
        pi = _quick_sort_partition(arr, left, right)
        _quick_sort_helper(arr, left, pi - 1)
        _quick_sort_helper(arr, pi + 1, right)


def _quick_sort_partition[T: Comparable](arr: list[T], left: int, right: int) -> int:
    """
    Partitions the sub-array arr[l...r] around a pivot element.

    This function selects the last element as the **pivot** (pivot). It rearranges
    the sub-array such that all elements less than or equal to the pivot are
    placed before it, and all elements greater than the pivot are placed after it.
    It then places the pivot in its correct sorted position and returns its index.

    Args:
        arr: The list containing the sub-array to be partitioned.
        left: The starting index of the sub-array.
        right: The ending index of the sub-array (the pivot is chosen as arr[r]).

    Returns:
        The index of the pivot element after partitioning (its final sorted position).
    """
    pivot = arr[right]
    j = left - 1
    for i in range(left, right):
        if arr[i] <= pivot:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[j + 1], arr[right] = arr[right], arr[j + 1]
    return j + 1
