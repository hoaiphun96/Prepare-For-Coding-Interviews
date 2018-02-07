"""
Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2:
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
Note: You may assume the tree (i.e., the given root node) is not NULL.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_level = 0
        self.left_most = root
        self.helper(root, 1)
        return self.left_most.val

    def helper(self, root, level):
        if not root:
            return
        if level > self.max_level:
            self.max_level = level
            self.left_most = root
        self.helper(root.left, level + 1)
        self.helper(root.right, level + 1)
