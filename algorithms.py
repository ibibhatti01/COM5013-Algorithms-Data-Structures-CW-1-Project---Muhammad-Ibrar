# algorithms.py

from typing import List, Callable, TypeVar, Optional

T = TypeVar("T")


# Linear search performs a full scan of the list. 
# Time complexity: O(n) in all cases.
def linear_search(items: List[T], predicate: Callable[[T], bool]) -> List[T]:
    """Return all items that satisfy the predicate. O(n)."""
    matches: List[T] = []
    for item in items:
        if predicate(item):
            matches.append(item)
    return matches

# Bubble Sort repeatedly swaps adjacent elements until sorted.
# Time complexity: O(n^2) worst and average, O(n) best case when already sorted.
def bubble_sort(items: List[T], key: Callable[[T], object]) -> List[T]:
    """
    Simple bubble sort implementation. O(n^2).
    Returns a new sorted list.
    """
    result = items[:]  # make a copy
    n = len(result)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if key(result[j]) > key(result[j + 1]):
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break
    return result
