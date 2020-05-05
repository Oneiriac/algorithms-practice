from tests import test


def insertion_sort(A):
    """
    Insertion sort.
    Time complexity, worst case: O(n^2)
    Time complexity, average case: O(n^2)
    Time complexity, best case: O(n)
    Aux. space: O(1) (in-place)
    """
    n = len(A)
    for i in range(1, n):
        # 1. At start of step, a[0...i-1] is sorted
        current = A[i]
        j = i
        # 2. Shift current left until it's in the correct position
        while j > 0:
            if current < A[j-1]:  # out of order, swap with element to left
                A[j-1], A[j] = A[j], A[j-1]
                j -= 1
            else:
                break
        # 3. At end of step, a[0...i] is sorted
    return A


if __name__ == "__main__":
    test(insertion_sort)
