class AVLTree():
    class Node():
        def __init__(self, value=0, left_child=None, right_child=None):
            self.value = value
            self.left_child = left_child
            self.right_child = right_child
            self.height = AVLTree.calculate_height(self)

        def __str__(self):
            return str(self.value)

        def __repr__(self):
            return str(self.value)

    @staticmethod
    def height(node):
        if not node:
            return 0

        return node.height

    @staticmethod
    def calculate_height(node):
        if node is None:
            raise ValueError('calculate_height parameter one must be a node')

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
        if node is None:
            raise ValueError('single_rotate_left parameter one must be a node')

        right_tree = node.right_child
        node.right_child = right_tree.left_child
        node.height = AVLTree.calculate_height(node)

        right_tree.left_child = node
        node = right_tree
        node.height = AVLTree.calculate_height(node)
        return node

    @staticmethod
    def single_rotation_right(node):
        r"""
              x                y
             / \              / \
            /   \            /   \
           y     C    ==>   A     x
          / \                    / \
         /   \                  /   \
        A     B                B     C

        Tree L   = T->left;
        T->left  = L->right;
        calculate_height(T);

        L->right = T;
        T        = L;
        calculate_height(T);
        """
        if node is None:
            raise ValueError('single_rotate_right parameter one must be a node')

        left_tree = node.left_child
        node.left_child = left_tree.right_child
        node.height = AVLTree.calculate_height(node)

        left_tree.right_child = node
        node = left_tree
        node.height = AVLTree.calculate_height(node)
        return node

    @staticmethod
    def double_rotation_left(node):
        if node is None:
            raise ValueError('double_rotate_left parameter one must be a node')

        node.right_child = AVLTree.single_rotation_right(node.right_child)
        return AVLTree.single_rotation_left(node)

    @staticmethod
    def double_rotation_right(node):
        if node is None:
            raise ValueError('double_rotate_right parameter one must be a node')

        node.left_child = AVLTree.single_rotation_left(node.left_child)
        return AVLTree.single_rotation_right(node)

    @staticmethod
    def rotate_left(node):
        if node is None:
            raise ValueError('rotate_left parameter one must be a node')

        right_child = node.right_child
        left_child_height = AVLTree.height(right_child.left_child)
        right_child_height = AVLTree.height(right_child.right_child)

        if right_child_height > left_child_height:
            return AVLTree.single_rotation_left(node)

        return AVLTree.double_rotation_left(node)

    @staticmethod
    def rotate_right(node):
        if node is None:
            raise ValueError('rotate_right parameter one must be a node')

        left_child = node.left_child
        left_child_height = AVLTree.height(left_child.left_child)
        right_child_height = AVLTree.height(left_child.right_child)

        if left_child_height > right_child_height:
            return AVLTree.single_rotation_right(node)

        return AVLTree.double_rotation_right(node)

    @staticmethod
    def rebalance(node):
        if node is None:
            raise ValueError('rebalance parameter one must be a node')

        left_child_height = AVLTree.height(node.left_child)
        right_child_height = AVLTree.height(node.right_child)

        if right_child_height > left_child_height + 1:
            return AVLTree.rotate_left(node)

        if left_child_height > right_child_height + 1:
            return AVLTree.rotate_right(node)

        node.height = AVLTree.calculate_height(node)
        return node

    @staticmethod
    def insert(value, node):
        if node is None:
            node = AVLTree.Node(value)
        elif value < node.value:
            node.left_child = AVLTree.insert(value, node.left_child)
        elif value > node.value:
            node.right_child = AVLTree.insert(value, node.right_child)

        node = AVLTree.rebalance(node)

        return node

    @staticmethod
    def insertAll(values, node=None):
        for value in values:
            node = AVLTree.insert(value, node)

        return node

    @staticmethod
    def remove_smallest(node):
        if node is None:
            raise ValueError('remove_smallest parameter one must be a node.')

        if node.left_child is None:
            value = node.value
            node = node.right_child
            result = {'value': value, 'node': node}
        else:
            result = AVLTree.remove_smallest(node.left_child)
            AVLTree.rebalance(result['node'])

        return result

    @staticmethod
    def remove(value, node):
        if node:
            if value < node.value:
                node = AVLTree.rebalance(AVLTree.remove(value, node.left_child))
            elif value > node.value:
                node = AVLTree.rebalance(AVLTree.remove(value, node.right_child))
            elif node.left_child is None:
                node = node.right_child
            elif node.right_child is None:
                node = node.left_child
            else:
                result = AVLTree.remove_smallest(node.right_child)
                node.value = result['value']
                node = AVLTree.rebalance(node)

        return node

    @staticmethod
    def in_order(node, buff: list = None):
        if node is None:
            return buff

        AVLTree.in_order(node.left_child, buff)
        buff.append(node.value)
        AVLTree.in_order(node.right_child, buff)

        return buff

    @staticmethod
    def post_order(node, buff: list = None):
        if node is None:
            return buff

        AVLTree.post_order(node.right_child, buff)
        buff.append(node.value)
        AVLTree.post_order(node.left_child, buff)

        return buff
