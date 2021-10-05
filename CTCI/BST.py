class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


class BST(object):
    def __init__(self, root=None):
        self.root = root

    def find_position(self, parent, child):
        if parent.data < child.data:
            if parent.left is None:
                parent.left = child
            else:
                self.find_position(parent.left, child)
        else:
            if parent.right is None:
                parent.right = child
            else:
                self.find_position(parent.right, child)

    def insert(self, node):
        if self.root is None:
            self.root = node
        else:
            self.find_position(self.root, node)

    def min_value_node(self, node):
        current = node

        # loop down to find the leftmost leaf
        while current.left is not None:
            current = current.left

        return current

    def remove(self, root, num):
        if root is None:
            return root

        # search left subtree
        if num > root.data:
            root.left = self.remove(root.left, num)

        # search right subtree
        elif num < root.data:
            root.right = self.remove(root.right, num)

        # found node to delete
        else:
            # one/no child
            if root.left is None:
                temp = root.right
                root = None
                return temp

            # two children, get biggest small of right
            temp = self.min_value_node(root.right)

            # copy successors contents
            root.data = temp.data

            # delete in-order successor
            root.right = self.remove(root.right, temp.data)

        return root

    def in_order(self, node):
        if node is not None:
            self.inOrder(node.left)
            print(node.data)
            self.inOrder(node.right)

    def pre_order(self, node):
        if node is not None:
            print(node.data)
            self.preOrder(node.left)
            self.preOrder(node.right)

    def post_order(self, node):
        if node is not None:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print(node)
