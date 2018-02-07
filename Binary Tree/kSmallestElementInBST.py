"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # inorder traversal ( left, root, right) with a counter
        stack = [root]
        visited = []
        while stack:
            curr = stack[-1]
            if curr.val in visited:
                stack.pop()
                continue
            if curr.left and curr.left.val not in visited:
                stack.append(curr.left)
            else:
                visited.append(curr.val)
                if len(visited) == k:
                    return visited[k - 1]
                if curr.right:
                    stack.append(curr.right)









