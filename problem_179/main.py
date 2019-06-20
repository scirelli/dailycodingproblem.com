#!/usr/bin/env python3
from BinarySearchTree import BinarySearchTree


def main():
    postOrder = [2, 4, 3, 8, 7, 5]
    bst = BinarySearchTree(postOrder[::-1])
    print(bst.postOrderTraversal())


if __name__ == '__main__':
    main()
