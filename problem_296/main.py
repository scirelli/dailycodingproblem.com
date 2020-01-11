#!/usr/bin/env python3
"""
Given a sorted array, convert it into a height-balanced (AVL) binary search tree.

Reference:
    http://www.cs.ecu.edu/karl/3300/spr16/Notes/DataStructure/Tree/balance.html

    https://github.com/scirelli/jsdatastructures/tree/master/avlTree
    https://github.com/scirelli/pi_asm_armv6/tree/master/avlTree
"""
from random import shuffle
from avl_tree.AVLTree import AVLTree


def main():
    values = list(range(100))
    # shuffle(values)
    node = AVLTree.insertAll(values)
    print(', '.join([ str(x) for x in AVLTree.in_order(node, [])]))
    print('')
    print(', '.join([str(x) for x in AVLTree.post_order(node, [])]))


if __name__ == '__main__':
    main()
