#!/usr/bin/env python3
from binarySearchTree.BinarySearchTree import BinarySearchTree


def ceiling(treeRoot, n):
    """
    Ceiling is the lowest element in the tree greater than or equal to an integer.
    Depth first search. node >= n
            2
          1   3
    """
    result = None

    def travers(treeRoot, n):
        nonlocal result
        if not treeRoot:
            return None

        travers(treeRoot.left, n)
        travers(treeRoot.right, n)
        if result is None and treeRoot.value >= n:
            result = treeRoot.value

        return None

    travers(treeRoot, n)
    return result


def floor(treeRoot, n):
    """
    Floor is the highest element in the tree less than or equal to an integer.
    Breath first search. node <= n
    """


def run_tests():
    ceilingTests = [
        {'array': [2, 1, 3], 'num': 2.3, 'expected': 3}
    ]

    for test in ceilingTests:
        t = BinarySearchTree()
        t.insert(test['array'])
        result = ceiling(t.get_root(), test['num'])
        try:
            assert result == test['expected']
        except AssertionError:
            print('FAIL: ', result, '!=', test['expected'])


def main():
    run_tests()


if __name__ == '__main__':
    main()
