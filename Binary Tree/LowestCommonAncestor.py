"""
Find lowest common ancestor of two node in a binary Tree
       1
      / \
     2   3
      \   \
       4   5

find_lca(2,5) => 1
find_lca(4,2) => 2
"""
def find_lca(self, root, node_data1, node_data2):
    if root != None:
        if root.data == node_data1 or root.data == node_data2:
            return root
        left = self.find_lca(root.left_child, node_data1, node_data2)
        right = self.find_lca(root.right_child, node_data1, node_data2)

        if left != None and right != None:
            return root

        return left if left != None else right

    return None