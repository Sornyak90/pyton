import unittest


class TreeNode:
    """Binary Search Tree Node"""
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'


class BinarySearchTree:
    
    def __init__(self, tree_data):
        self.root = None
        for item in tree_data:
            self.insert(item)

    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            current = self.root
            while True:
                if data <= current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = TreeNode(data)
                        break
                else:
                    if current.right:
                        current = current.right
                    else:
                        current.right = TreeNode(data)
                        break

    def data(self):
        return self.root

    def _inorder_traversal(self, node):
        result = []
        if node:
            result.extend(self._inorder_traversal(node.left))   # Traverse left subtree first
            result.append(node.data)                            # Visit current node
            result.extend(self._inorder_traversal(node.right))  # Then traverse right subtree
        return result

    def sorted_data(self):
        return self._inorder_traversal(self.root)

print(BinarySearchTree(["4", "2", "6", "1", "3", "5", "7"]).data())