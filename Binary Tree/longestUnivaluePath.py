"""
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:

2
Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output:

2
Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.


"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    maxlen = 0

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.helper(root)
        return self.maxlen

    def helper(self, root):
        if not root:
            return 0
        leftlen, rightlen = self.helper(root.left), self.helper(root.right)

        if root.left and root.left.val == root.val:
            l = 1 + leftlen
        else:
            l = 0

        if root.right and root.right.val == root.val:
            r = 1 + rightlen
        else:
            r = 0

        self.maxlen = max(self.maxlen, l + r)
        return max(l, r)



