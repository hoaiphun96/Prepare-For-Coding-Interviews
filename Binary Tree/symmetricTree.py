"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.


"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return self.helper(root.left, root.right)

    def helper(self, treeleft, treeright):
        # if not treeleft and not treeright:
        #  return True
        sleft = [treeleft]
        sright = [treeright]

        while sleft and sright:  # may change
            nodetreeleft = sleft.pop()
            nodetreeright = sright.pop()

            if nodetreeleft is None and nodetreeright is None:
                continue
            elif nodetreeleft is None and nodetreeright:
                return False
            elif nodetreeright is None and nodetreeleft:
                return False
            if nodetreeleft.val != nodetreeright.val:
                return False
            sleft.append(nodetreeleft.left)
            sright.append(nodetreeright.right)
            sleft.append(nodetreeleft.right)
            sright.append(nodetreeright.left)
        return True




