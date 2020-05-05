import math
from tests import test


def heap_sort(A):
    """
    Heap sort using a max-heap and sinking down.
    Time complexity, worst case: O(n*log n)
    Time complexity, average case: O(n*log n)
    Time complexity, best case: O(n*log n)
    Aux. space: O(1) (in-place)
    """
    n = len(A)
    heapify(A)
    # Invariant: A[0..heap_end] is a heap, A[heap_end+1..n] is sorted
    heap_end = n-1
    while heap_end > 0:
        # Extract root (max element) from max-heap and swap with last element of heap
        A[0], A[heap_end] = A[heap_end], A[0]
        heap_end -= 1  # Heap is now smaller, sorted section is now larger
        sink_root(A, 0, heap_end)  # Repair heap

    return A


def left_child(i):
    return 2*i + 1


def right_child(i):
    return 2*i + 2


def heapify(A):
    """Convert A into a max-heap in-place by building ever-larger subheaps from the bottom up."""
    n = len(A)
    # For more efficiency, can eliminate leaves from the loop as they already constitute heaps
    for i in range(n-1, -1, -1):
        sink_root(A, i, heap_end=n-1)


def sink_root(A, heap_start, heap_end):
    """Repair the heap at A[heap_start..heap_end] by sinking the root until the max-heap invariant is true."""
    root = heap_start
    while left_child(root) <= heap_end:  # i.e. while root has at least one child
        if right_child(root) > heap_end or A[left_child(root)] > A[right_child(root)]:
            larger_child = left_child(root)
        else:
            larger_child = right_child(root)
        if A[root] >= A[larger_child]:  # root is in correct position
            return
        else:  # swap root with larger child and continue
            A[root], A[larger_child] = A[larger_child], A[root]
            root = larger_child


if __name__ == "__main__":
    test(heap_sort)
