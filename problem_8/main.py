#!/usr/bin/env python3
'''
This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
'''

from node import Node


def is_unival(node):
    "Returns true if both child nodes have the same value. False otherwise."
    if node.left is None and node.right is None:
        return True

    if node.left is None:
        return node.right.value == node.value

    if node.right is None:
        return node.left.value == node.value

    return node.left.value == node.right.value == node.value


def travers(root):
    """
    Counts how many sub-trees are universal nodes.
    """
    count = 0

    if root is None:
        return 0

    count += travers(root.left)
    count += travers(root.right)

    if is_unival(root):
        count += 1
    return count


examples = [
    {
        'description': 'Example from email',             #       0
        'tree': Node(0,                                  #      / \
                     left=Node(1),                       #     1   0
                     right=Node(0,                       #        / \
                                left=Node(1,             #       1   0
                                          left=Node(1),  #      / \
                                          right=Node(1)  #     1   1
                                          ),
                                right=Node(0)
                                )
                     )
    },
    {
        'description': 'Test 1',
        'tree': Node(1,                                     #           1
                     left=Node(1,                           #         /   \
                               left=Node(1,                 #        1     1
                                         left=Node(1),      #       / \   / \
                                         right=Node(1)),    #      1   1 1   1
                               right=Node(1)),              #     / \   / \
                     right=Node(1,                          #    1   1 1   1
                                left=Node(1,
                                          left=Node(1),
                                          right=Node(1)
                                          ),
                                right=Node(1)
                                )
                     )
    },
]


def main():
    """
    The main function
    """
    for example in examples:
        print(travers(example['tree']))


if __name__ == '__main__':
    main()
