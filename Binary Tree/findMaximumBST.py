"""
Given a
Binary Search Tree
, return the node with the maximum data.

Example:

       4
      / \
     2   8
        / \
       5  10

Output ==> 10 (TreeNode)

Note: Each node of BinaryTree is a TreeNode.
Check out Use Me section to find out it's structure.
"""


class BinaryTree:
    def __init__(self, root_node=None):
        # Check out Use Me section to find out Node Structure
        self.root = root_node

    def find_max(self, root):
        # Return element should be of type TreeNode
        if not root:
            return None
        curr = root
        while curr.right_child != None:
            curr = curr.right_child
        return curr