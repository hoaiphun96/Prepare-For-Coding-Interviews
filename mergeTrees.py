"""
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:
Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
Note: The merging process must start from the root nodes of both trees.
"""
class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """

        if t1 is not None and t2 is not None:
            t3 = TreeNode(t1.val + t2.val)
            t3.left = self.mergeTrees(t1.left, t2.left)
            t3.right = self.mergeTrees(t1.right, t2.right)
        elif t1 is not None and t2 is None:
            t3 = TreeNode(t1.val)
            t3.left = self.mergeTrees(t1.left, None)
            t3.right = self.mergeTrees(t1.right, None)
        elif t1 is None and t2 is not None:
            t3 = TreeNode(t2.val)
            t3.left = self.mergeTrees(None, t2.left)
            t3.right = self.mergeTrees(None, t2.right)
        else:  # both null
            return
        return t3