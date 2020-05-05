from tests import test


def binary_search(A, left, right, item):
    """Binary search to find position where item should be inserted in a[left..right]."""
    while left <= right:
        median = (left + right) // 2
        if item > A[median]:
            left = median + 1
        elif item < A[median]:
            right = median - 1
        else:
            return median
    # item is not in a
    return median + 1 if item > A[median] else median


def insertion_sort_binary(A):
    """
    Insertion sort with binary search implemented to reduce number of comparisons.
    Useful when comparison is more expensive than swaps (e.g. an array of strings).
    Note that number of swaps is still O(n^2) in worst case.
    Time complexity, worst case: O(n^2)
        - O(n*log n) comparisons, O(n^2) swaps
    Time complexity, average case: O(n^2)
        - O(n*log n) comparisons, O(n^2) swaps
    Time complexity, best case: O(n)
    Aux. space complexity: O(1) (in-place)
    """
    n = len(A)
    for i in range(1, n):
        # 1. At start of step, a[0...i-1] is sorted
        current = A[i]
        # 2. Because a[0...i-1] is sorted, we can do binary search
        correct_loc = binary_search(A, 0, i-1, current)
        # Move all items to right of correct_loc up one
        j = i-1
        while j >= correct_loc:
            A[j+1] = A[j]
            j -= 1
        A[correct_loc] = current
        # 3. At end of step, a[0...i] is sorted
    return A


if __name__ == "__main__":
    test(insertion_sort_binary)
