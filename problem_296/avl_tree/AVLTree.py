class AVLTree():
    class Node():
        def __init__(self, value=0, left_child=None, right_child=None):
            self.value = value
            self.left_child = left_child
            self.right_child = right_child
            self.height = AVLTree.calculate_height(self)

    def __init__(self, root):
        self.root = root

    @staticmethod
    def height(node):
        if not node:
            return 0

        return node.height

    @staticmethod
    def calculate_height(node):
        lh = node.left_child.height if node.left_child else 0
        rh = node.right_child.height if node.right_child else 0
        return 1 + max(lh, rh)

    @staticmethod
    def single_rotation_left(node):
        r"""
            x                     y
           / \                   / \
          /   \                 /   \
         A     y       ==>     x     C
              / \             / \
             /   \           /   \
            B     C         A     B

            Tree r   = T->right;
            T->right = r->left;
            calculate_height(T);

            r->left  = T;
            T        = r;
            calculate_height(T)
        """
        right_tree = node.right_child
        node.right_child = right_tree.left_child
        AVLTree.calculate_height(node)

        right_tree.left_child = node
        node = right_tree
        AVLTree.calculate_height(node)
        return node
