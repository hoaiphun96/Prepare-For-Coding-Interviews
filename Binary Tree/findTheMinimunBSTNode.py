"""
Given a
Binary Search Tree
, return the node with the minimum data.

Example:

       4
      / \
     2   8
        / \
       5  10

Output ==> 2 (TreeNode)

Note: Each node of BinaryTree is a TreeNode. Check out Use Me section to find out it's structure.

"""


class BinaryTree:
    def __init__(self, root_node=None):
        # Check out Use Me section to find out Node Structure
        self.root = root_node

    def find_min(self, root):
        # Return element should be of type TreeNode
        if root:
            if root.left_child:
                return self.find_min(root.left_child)
            return root
        return None