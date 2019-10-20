class BinarySearchTree():
  class Node():
    def __init__(self, value=0, left=None, right=None):
      self.value = value
      self.left = left
      self.right = right

  def __init__(self, rootNode=None):
    self.root = rootNode

  def insert(self, value):
    try:
      iter(value)
    except TypeError:
      if not self.root:
        self.root = BinarySearchTree.Node(value)
        return self.rootNode
      return BinarySearchTree.insertAt(self.root, value)

    for itm in value:
      if not self.root:
        self.root = BinarySearchTree.Node(itm)
        continue
      lastInsert = BinarySearchTree.insertAt(self.root, itm)
    return lastInsert

  def get_root(self):
      return self.root

  def __str__(self):
    return str(BinarySearchTree.in_order(self.root))

  @staticmethod
  def insertAt(root, value):
    if not root:
      return root

    if value > root.value:
      return BinarySearchTree.insertRight(root, value)
    elif value <= root.value:
      return BinarySearchTree.insertLeft(root, value)

    raise ValueError('Wtf')

  @staticmethod
  def insertRight(root, value):
    if root.right:
      return BinarySearchTree.insertAt(root.right, value)

    root.right = BinarySearchTree.Node(value)
    return root.right

  @staticmethod
  def insertLeft(root, value):
    if root.left:
      return BinarySearchTree.insertAt(root.left, value)

    root.left = BinarySearchTree.Node(value)
    return root.left

  @staticmethod
  def in_order(root, results=None):
    if not results:
      results = []

    if not root:
      return results

    results = BinarySearchTree.in_order(root.left, results)
    results.append(root.value)
    results = BinarySearchTree.in_order(root.right, results)

    return results
