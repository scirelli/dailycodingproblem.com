#!/usr/bin/env python3
from random import shuffle

from binarySearchTree.BinarySearchTree import BinarySearchTree

def ceiling(treeRoot, n):
    """
    Ceiling is the lowest element in the tree greater than or equal to an integer.
    Depth first search. node >= n
            2
          1   3
    """
    if not treeRoot:
        return None

    ceiling(treeRoot.left, n)
    ceiling(treeRoot.right, n)
    if treeRoot.value >= n:
        return treeRoot.value

    return None

def floor(treeRoot, n):
    """
    Floor is the highest element in the tree less than or equal to an integer.
    Breath first search. node <= n
    """
    pass

def test():
    ceilingTests = [
        {'array': [2,1,3], 'num': 2, 'expected': 3}
    ]

    for test in ceilingTests:
        t = BinarySearchTree()
        t.insert(test['array'])
        result = ceiling(t.get_root(), test['num'])
        try:
            assert(result == test['expected'])
        except AssertionError:
            print('FAIL: ', result, '!=', test['expected'])

def main():
    test()


if __name__ == '__main__':
  main()
