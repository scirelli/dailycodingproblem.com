#!/usr/bin/env python3
from binarySearchTree.BinarySearchTree import BinarySearchTree


def ceiling(treeRoot, n):
    """
    Ceiling is the lowest element in the tree greater than or equal to an integer.
    Depth first search. node >= n
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
    queue = [treeRoot]

    while queue:
        node = queue.pop(0)

        if node.value <= n:
            return node.value

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return None


def runTest(testFuncName, test):
    t = BinarySearchTree()
    t.insert(test['array'])
    result = globals()[testFuncName](t.get_root(), test['num'])
    try:
        assert result == test['expected']
    except AssertionError:
        print(testFuncName, 'FAIL: ', result, '!=', test['expected'])


def run_tests():
    tests = {
        'floor': [
            {'array': [2, 1, 3], 'num': 2.3, 'expected': 2}
        ],
        'ceiling': [
            {'array': [2, 1, 3], 'num': 2.3, 'expected': 3}
        ]
    }

    for testFuncName, tests in tests.items():
        for test in tests:
            runTest(testFuncName, test)


def main():
    run_tests()


if __name__ == '__main__':
    main()
