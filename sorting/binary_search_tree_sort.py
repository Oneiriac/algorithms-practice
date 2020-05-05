
from __future__ import annotations
from tests import test
from typing import TypeVar, Generic, Optional, List
from abc import abstractmethod

T = TypeVar('T')


def bst_sort(A):
    """
    Tree sort using a Binary Search Tree modified to accept duplicates.
    Time complexity, worst case: O(n*^2) (use AVL sort to improve upon this)
    Time complexity, average case: O(n*log n)
    Time complexity, best case: O(n*log n)
    Aux. space: O(n)
    """
    if len(A) <= 1:
        return A
    # Create Binary Search Tree
    root = BinarySearchTree(A[0])
    for i in range(1, len(A)):
        root.insert(A[i])
    # Sort by performing in-order traversal
    result = root.in_order()
    return result


class BinaryTree(Generic[T]):
    """Binary Tree node, with the option to support duplicate values via a count."""

    def __init__(self, value: T, left: Optional[BinaryTree[T]] = None, right: Optional[BinaryTree[T]] = None):
        super().__init__()
        self.value = value
        self.left = left
        self.right = right
        self.count: int = 1

    @abstractmethod
    def insert(self, x: T):
        pass

    @property
    def values(self) -> List[T]:
        return [self.value]*self.count

    def pre_order(self) -> List[T]:
        left_values = self.left.pre_order() if self.left else []
        right_values = self.right.pre_order() if self.right else []
        return [*self.values, *left_values, *right_values]

    def in_order(self) -> List[T]:
        left_values = self.left.in_order() if self.left else []
        right_values = self.right.in_order() if self.right else []
        return [*left_values, *self.values, *right_values]

    def reverse_in_order(self) -> List[T]:
        left_values = self.left.reverse_in_order() if self.left else []
        right_values = self.right.reverse_in_order() if self.right else []
        return [*right_values, *self.values, *left_values]

    def post_order(self) -> List[T]:
        left_values = self.left.post_order() if self.left else []
        right_values = self.right.post_order() if self.right else []
        return [*left_values, *right_values, *self.values]


class BinarySearchTree(BinaryTree):
    def insert(self, x: T):
        if x == self.value:
            self.count += 1
        elif x < self.value:
            if self.left is None:
                self.left = BinarySearchTree(x)
            else:
                self.left.insert(x)
        elif x > self.value:
            if self.right is None:
                self.right = BinarySearchTree(x)
            else:
                self.right.insert(x)


if __name__ == "__main__":
    test(bst_sort)
