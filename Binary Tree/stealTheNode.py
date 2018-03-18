"""
Write a method to delete a node from a given
binary search tree
.

Example:

   4             4
  / \     del    / \
 2   8    10    2   8
    / \   =>       /
   5  10          5


Note: Each node of BinaryTree is a TreeNode. Check out Use Me section to find out it's structure.
Your solution should return the new root node. Level order representation of your new structure will be validated against our test cases.
"""


class BinaryTree:
    def __init__(self, root_node=None):
        # Check out Use Me section to find out Node Structure
        self.root = root_node

    # Helper method
    def find_min(self, root):
        if root == None:
            return None
        if root.left_child == None:
            return root
        return self.find_min(root.left_child)

    def delete(self, root, data):
        # Return the new root node of type TreeNode
        if root == None:
            return None
        elif data < root.data:
            root.left_child = self.delete(root.left_child, data)
        elif data > root.data:
            root.right_child = self.delete(root.right_child, data)
        else:
            if root.left_child != None and root.right_child != None:
                root.data = self.find_min(root.right_child).data
                root.right_child = self.delete(root.right_child, root.data)
            elif root.left_child == None and root.right_child == None:
                root = None
            elif root.left_child == None:
                root = root.right_child
            elif root.right_child == None:
                root = root.left_child

        return root