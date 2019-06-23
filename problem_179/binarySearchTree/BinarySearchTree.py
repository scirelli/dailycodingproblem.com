from binarySearchTree.Node import Node


class BinarySearchTree():
    def __init__(self, values=None):
        self.root = None

        if values is not None:
            self.fill(iter(values))

    def fill(self, values):
        for itm in values:
            self.insert(itm)

        return self

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return self

        currentNode = self.root
        while currentNode:
            if value > currentNode.value:
                if currentNode.right is None:
                    currentNode.right = Node(value)
                    currentNode = None
                else:
                    currentNode = currentNode.right
            elif value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = Node(value)
                    currentNode = None
                else:
                    currentNode = currentNode.left
            else:
                currentNode.duplicateCount += 1
                currentNode = None

        return self

    def get_root(self):
        return self.root

    def preOrderTraversal(self):
        return self._preOrderTraversal(self.root)

    def _preOrderTraversal(self, node):
        result = []

        if node is None:
            return result

        result.append(node.value)
        result.extend(self._preOrderTraversal(node.left))
        result.extend(self._preOrderTraversal(node.right))

        return result

    def inOrderTraversal(self):
        return self._inOrderTraversal(self.root)

    def _inOrderTraversal(self, node):
        result = []

        if node is None:
            return result

        result.extend(self._inOrderTraversal(node.left))
        result.append(node.value)
        result.extend(self._inOrderTraversal(node.right))

        return result

    def postOrderTraversal(self):
        return self._postOrderTraversal(self.root)

    def _postOrderTraversal(self, node):
        result = []

        if node is None:
            return result

        result.extend(self._postOrderTraversal(node.left))
        result.extend(self._postOrderTraversal(node.right))
        result.append(node.value)

        return result

    def depth(self):
        return self._depth(self.root)

    def _depth(self, node, depth=0, maxDepth=0):
        if node is None:
            return depth

        depth += 1
        maxDepth = max(self._depth(node.left, depth, maxDepth), depth)
        maxDepth = max(self._depth(node.right, depth, maxDepth), depth)

        return maxDepth

    def __str__(self):
        pass
