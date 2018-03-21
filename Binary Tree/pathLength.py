# Given a root node in a Binary Tree and a target num, return the distance from root to such node
def path_length(self, root, node_data):
    if root == None:
        return 0
    else:
        out = 0
        if root.data == node_data:
            return out + 1
        out = self.path_length(root.left_child, node_data1)
        if out > 0:
            return out + 1
        out = self.path_length(root.right_child, node_data1)
        if out > 0:
            return out + 1

    return 0