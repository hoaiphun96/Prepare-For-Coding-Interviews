"""
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
Note: There are at least two nodes in this BST."""""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # in order traversal left-> root> right and keeptrack of minimum difference
        mind = float("inf")
        current = root
        s = []
        done = 0
        last = -1
        while not done:
            if current is not None:
                s.append(current)
                current = current.left
            else:
                if len(s) > 0:
                    current = s.pop()
                    if last != -1:
                        d = current.val - last
                        print(d, mind)
                        if d < mind:
                            mind = d
                    last = current.val
                    current = current.right
                else:
                    done = 1
        return mind
