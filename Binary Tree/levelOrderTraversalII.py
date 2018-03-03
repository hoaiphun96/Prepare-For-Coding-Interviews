"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

"""
from collections import defaultdict


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        # recusive bfs:
        ht = defaultdict(list)
        self.bfs(root, ht, 0)
        return list(ht.values())[::-1]

    def bfs(self, root, ht, d):
        ht[d].append(root.val)
        if root.left:
            self.bfs(root.left, ht, d + 1)
        if root.right:
            self.bfs(root.right, ht, d + 1)