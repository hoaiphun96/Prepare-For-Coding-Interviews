# Find min, max of Binary Search Tree
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

    # Helper method
    def find_max(self, root):
        if root == None:
            return None
        if root.left_child == None:
            return root
        return self.find_max(root.right_child)