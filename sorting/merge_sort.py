from tests import test


def merge(L, R):
    """Merge arrays l and r into a sorted array."""
    result = []
    l_index, r_index = 0, 0
    while l_index < len(L) and r_index < len(R):
        # elements to the left of l_index/r_index have already been merged into the result
        if L[l_index] <= R[r_index]:
            result.append(L[l_index])
            l_index += 1
        else:
            result.append(R[r_index])
            r_index += 1
    # Add leftover elements
    if l_index < len(L):
        result += L[l_index:]
    elif r_index < len(R):
        result += R[r_index:]
    return result


def merge_sort(A):
    """
    Top-down merge sort using lists: https://en.wikipedia.org/wiki/Merge_sort#Top-down_implementation_using_lists.
    Time complexity, worst case: O(n*log n)
    Time complexity, average case: O(n*log n)
    Time complexity, best case: O(n)
    Aux. space: O(n)
    """
    if len(A) <= 1:
        return A

    middle = len(A) // 2
    L = A[:middle]
    R = A[middle:]
    left_sorted = merge_sort(L)
    right_sorted = merge_sort(R)
    result = merge(left_sorted, right_sorted)
    return result


if __name__ == "__main__":
    test(merge_sort)
