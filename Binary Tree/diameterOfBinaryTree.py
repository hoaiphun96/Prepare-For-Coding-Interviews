"""
Given a Binary Tree, write a method to return its diameter. The diameter of a Binary Tree is defined as the "Number of nodes on the longest path between two leaf nodes".

Example:
       20
      /   \
    15     30
   /  \      \  output => 7
  14  18     35
     /  \    /
  17   19  32

Note:
Each node of BinaryTree is represented by a TreeNode. Check out Use Me section to find out it's structure.
Return type of diameter method should be an integer  and it should execute in O(n) time complexity.
"""
class BinaryTree:
    def __init__(self, root_node=None):
        self.root = root_node
        self.longest_diameter = 0

    def diameter(self, root):
        self.update_longest_diameter(root)
        return self.longest_diameter

    def update_longest_diameter(self, root):
        if root == None:
            return 0
        longest_left_path = self.update_longest_diameter(root.left_child)
        longest_right_path = self.update_longest_diameter(root.right_child)

        this_diameter = 1 + longest_left_path + longest_right_path

        self.longest_diameter = max(self.longest_diameter, this_diameter)

        return max(longest_right_path, longest_left_path) + 1

#Firecode approach
class BinaryTree:
    def __init__(self, root_node=None):
        self.root = root_node

    def diameter(self, root):
        return self.diameter_helper(root, BinaryTree.Height())

    class Height:
        def __init__(self, h=0):
            self.h = h

    def diameter_helper(self, root, height):
        # left_height : Height of left subtree
        # right_height : Height of right subtree
        left_height = BinaryTree.Height()
        right_height = BinaryTree.Height()
        if root == None:
            height.h = 0
            return 0

        # ldiameter  : diameter of left subtree
        # rdiameter  : Diameter of right subtree
        # Get the heights of left and right subtrees in left height and right height
        # and store the returned values in ldiameter and rdiameter

        left_height.h += 1
        right_height.h += 1

        ldiameter = self.diameter_helper(root.left_child, left_height)
        rdiameter = self.diameter_helper(root.right_child, right_height)
        # Height of current node is max of heights of left and right subtrees plus 1
        height.h = max(left_height.h, right_height.h) + 1
        # diameter
        return max(left_height.h + right_height.h + 1, max(ldiameter, rdiameter))