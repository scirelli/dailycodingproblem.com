class Node():
    def __init__(self, value=None, leftNode=None, rightNode=None):
        self.value = value
        self.left = leftNode
        self.right = rightNode
        self.duplicateCount = 0

    def __iter__(self):
        return filter(lambda x: x, [self.left, self.right])
