#!/usr/bin/env python3
from binarySearchTree.BinarySearchTree import BinarySearchTree
import binarySearchTree.DrawTree as DrawTree


def main():
    postOrder = [2, 4, 3, 8, 7, 5]
    bst = BinarySearchTree(postOrder[::-1])
    print(bst.postOrderTraversal())
    lines = DrawTree.printTree(DrawTree.layout(DrawTree.DrawTree(bst.get_root())))
    print('\n'.join([''.join(l) for l in lines]))


if __name__ == '__main__':
    main()
