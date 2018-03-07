"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.helper(root.left, True) + self.helper(root.right, False)

    def helper(self, child, isLeft):
        if not child:
            return 0
        if isLeft and not child.left and not child.right:
            return child.val
        return self.helper(child.left, True) + self.helper(child.right, False)
