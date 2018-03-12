"""
Given the root node of a Binary Tree, write a method - validate_BST_Itr to iteratively determine if it is a Binary Search Tree.

A BST must satisfy the following conditions :
* The left subtree of a node contains nodes with data < its data.
* The right subtree of a node contains  nodes data > its data.
* A node's left and right subtrees follow the above two conditions.
"""


# Collections module has already been imported.
class BinaryTree:
    def __init__(self, root_node=None):
        self.root = root_node

    def validate_BST_Itr(self, root):
        # do inorder traversal
        curr = root
        stack = []
        prev = -float("inf")
        while True:
            if curr:
                stack.append(curr)
                curr = curr.left_child
            else:
                if not stack:
                    break
                else:
                    curr = stack.pop()
                    if curr.data <= prev:
                        return False
                    prev = curr.data
                    curr = curr.right_child
        return True
