from tests import test


def selection_sort(A):
    """
    Selection sort.
    Time complexity, worst case: O(n^2)
    Time complexity, average case: O(n^2)
    Time complexity, best case: O(n)
    Aux. space: O(1) (in-place)
    """
    if len(A) <= 1:
        return A
    n = len(A)
    for i in range(n):
        # Find smallest value in sequence
        # At start of step, a[0...i-1] is sorted: only search A[i..n]
        min_val, min_index = A[i], i
        for j in range(i, n):
            if A[j] < min_val:
                min_val = A[j]
                min_index = j
        # Swap minimum with leftmost element in sequence, A[i]
        A[i], A[min_index] = A[min_index], A[i]
        # At end of step, a[0...i] is sorted
    return A


if __name__ == "__main__":
    test(selection_sort)
