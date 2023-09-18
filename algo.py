class BTNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # Add a value to the BST
    def add(self, val):
        new_node = BTNode(val)

        if not self.root:
            self.root = new_node
        else:
            self._insert_node(self.root, new_node)

    def _insert_node(self, node, new_node):
        if new_node.val <= node.val:
            if not node.left:
                node.left = new_node
            else:
                self._insert_node(node.left, new_node)
        else:
            if not node.right:
                node.right = new_node
            else:
                self._insert_node(node.right, new_node)

    # Check if the BST contains a given value
    def contains(self, val):
        return self._contains(self.root, val)

    def _contains(self, node, val):
        if not node:
            return False

        if val == node.val:
            return True
        elif val < node.val:
            return self._contains(node.left, val)
        else:
            return self._contains(node.right, val)

    # Find the minimum value in the BST
    def min(self):
        if not self.root:
            return None

        current = self.root
        while current.left:
            current = current.left
        return current.val

    # Find the maximum value in the BST
    def max(self):
        if not self.root:
            return None

        current = self.root
        while current.right:
            current = current.right
        return current.val

    # Bonus: Get the number of nodes (size) in the BST
    def size(self):
        return self._get_size(self.root)

    def _get_size(self, node):
        if not node:
            return 0

        return 1 + self._get_size(node.left) + self._get_size(node.right)

    # Bonus: Check if the BST is empty
    def is_empty(self):
        return self.root is None

bst = BST()

bst.add(5)
bst.add(3)
bst.add(7)
bst.add(2)
bst.add(4)
bst.add(6)
bst.add(8)

print(bst.contains(3))
print(bst.contains(9))

print(bst.min())
print(bst.max())

print(bst.size())

print(bst.is_empty())

def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.val)
        in_order_traversal(node.right)

print("In order traversal:")
in_order_traversal(bst.root)