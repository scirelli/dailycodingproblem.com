"""
Node for a tree
"""


class Node:
    "Node for a tree"
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def get_left(self):
        "Get's the left node."
        return self.left

    def get_right(self):
        "Get's the right node."
        return self.right

    def to_string(self):
        "Return a string"
        return self.value

    def print(self):
        "Print a string"
        print(f"\t\t{self.value}\n", end='')

        if self.left:
            print(f"{self.left.print()}\t\t", end='')
        else:
            print('\t\t\t\t\t\t')

        if self.right:
            print(f"{self.right.print()}", end='')
