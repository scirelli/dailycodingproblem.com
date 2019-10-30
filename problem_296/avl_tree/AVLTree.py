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

    @staticmethod
    def single_rotation_right(node):
        r"""

            Tree L   = T->left;
            T->left  = L->right;
            installHeight(T);

            L->right = T;
            T        = L;
            installHeight(T);
        """
        left_tree = node.left_child
        node.left_child = left_tree.right_child
        AVLTree.calculate_height(node)

        left_tree.right_child = node
        node = left_tree
        AVLTree.calculate_height(node)

        return node

    @staticmethod
    def double_rotation_left(node):
        """
        double_rotate_left(T) performs a double rotation from right to left at the root of T.

        single_rotation_right(T.right_child);
        single_rotation_left(T);
        """
        node.right_child = AVLTree.single_rotation_right(node.right_child)
        return AVLTree.single_rotation_left(node)

    @staticmethod
    def double_rotation_right(node):
        """
        doubleRotateRight(T) performs a double rotation from left to right at the root of T.

        single_rotation_left(T->left);
        single_rotation_right(T);
        """
        node.left_child = AVLTree.single_rotation_left(node.left_child)
        return AVLTree.single_rotation_right(node)

    @staticmethod
    def rotate_left(node):
        """
        rotate_left(T) performs a rotation from right to left at the root of T, choosing a single or double rotation.

        Tree r   = T->right;
        int  zag = height(r->left);
        int  zig = height(r->right);

        if(zig > zag)
        {
            singleRotateLeft(T);
        }
        else
        {
            doubleRotateLeft(T);
        }
        """
        right_tree = node.right_child
        zag = AVLTree.height(right_tree.left_child)
        zig = AVLTree.height(right_tree.right_child)

        if zig > zag:
            node = single_rotation_left(node)
        else:
            node = double_rotation_left(node)

        return node

    @staticmethod
    def rotate_right(node):
        """
        rotateRight(T) performs a rotation from left to right at the root of T, choosing a single or double rotation.

        Tree L  = T->left;
        int  zig = height(L->left);
        int  zag = height(L->right);

        if(zig > zag)
        {
        singleRotateRight(T);
        }
        else
        {
        doubleRotateRight(T);
        }
        """
        left_tree = node.left_child
        zig = AVLTree.height(left_tree.left_child)
        zag = AVLTree.height(left_tree.right_child)

        if zig > zag:
            node = single_rotation_right(node)
        else:
            node = double_rotation_right(node)

        return node

    @staticmethod
    def rebalance(node):
        """
        (1) Perform a rotation at T if required.
        (2) Set the ht field of T correctly, regardless of whether or not a rotation is done.

        Requirement: T must not be empty.

        int hl = height(T->left);
        int hr = height(T->right);

        if(hr > hl + 1)
        {
            rotateLeft(T);
        }
        else if(hl > hr + 1)
        {
            rotateRight(T);
        }
        else
        {
            installHeight(T);
        }
        """
        left_child_height = AVLTree.height(node.left_child)
        right_child_height = AVLTree.height(node.right_child)

        if right_child_height > left_child_height + 1:
            node = rotate_left(node)
        elif left_child_height > right_child_height + 1:
            node = rotate_right(node)
        else:
            node.height = AVLTree.calculate_height(node)

        return node
