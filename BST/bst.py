from BST.node import node


class BST(object):
    def __init__(self, root=None):
        self.root = None

    def add_node(self, z):
        """
        Function to add node to BST

        y and x are variables used to traverse the tree.
        y follows x with 1 step lag. Therefore, when x reaches beyond the last leaf node i.e., when x becomes None,
        y, then, is pointing at the lead node.

        :param z: BST.node: Node object to be inserted into the tree
        :return: None
        """
        y = None  # # Variable will end up being the last node
        x = self.root  # # Dummy variable that traverses through the tree.

        while x is not None:
            y = x

            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.parent = y

        if y is None:
            self.root = z  # # Tree was empty
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z


def inorder_tree_walk(root):
    if root != None:
        inorder_tree_walk(root.left)
        print(root.key)
        inorder_tree_walk(root.right)


node1 = node(10)
node2 = node(1)
node3 = node(12)
node4 = node(14)
node5 = node(19)
tree = BST()

tree.add_node(node1)
tree.add_node(node2)
tree.add_node(node3)
tree.add_node(node4)
tree.add_node(node5)

inorder_tree_walk(tree.root)