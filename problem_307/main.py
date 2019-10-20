#!/usr/bin/env python3
from random import shuffle

from binarySearchTree.BinarySearchTree import BinarySearchTree


def main():
  t = BinarySearchTree()
  a = [1,2,3]
  shuffle(a)
  t.insert(a)
  print(t)


if __name__ == '__main__':
  main()
