"""
Given the root of a Binary Tree  and 2 integers that represent the data values of any two TreeNodes present in the tree, write a method - get_node_distance that returns the distance between the nodes. You can assume that the given keys exist in the tree. The distance between two nodes is defined as the minimum number of edges that must be traversed to travel between the two nodes.

Example:
       1
      / \
     2   3
      \   \
       4   5

get_node_distance(2,5) => 3
"""

#Approach 1, dfs and storing paths
class BinaryTree:
    def __init__(self, root_node=None):
        self.root = root_node

    def get_node_distance(self, root, node_data1, node_data2):
        if not root:
            return 0
        path_to_node1 = self.distance(root, node_data1)  # (distance, path)
        path_to_node2 = self.distance(root, node_data2)  # (distance, path)
        path_to_lca_ab = self.lca(path_to_node1[1], path_to_node2[1])

        return path_to_node1[0] + path_to_node2[0] - 2 * self.distance(root, path_to_lca_ab)[0]

    def distance(self, root, node_data):
        if not root:
            return 0
        # do dfs to find distance
        paths = {root.data: [root.data]}
        to_visit = [(root, 0)]

        while to_visit:
            current = to_visit.pop()
            node, distance_so_far = current[0], current[1]

            if node.data == node_data:
                return (distance_so_far, paths[node_data])
            else:
                if node.left_child:
                    to_visit.append((node.left_child, distance_so_far + 1))
                    paths[node.left_child.data] = paths[node.data] + [node.left_child.data]
                if node.right_child:
                    to_visit.append((node.right_child, distance_so_far + 1))
                    paths[node.right_child.data] = paths[node.data] + [node.right_child.data]

        return (-1, None)

    def lca(self, path1, path2):
        for i in range(1, min(len(path1), len(path2))):
            if path1[i] != path2[i]:
                return path1[i - 1]
        if len(path1) < len(path2):
            return path1[-1]
        return path2[-1]

#Approach 2 recursion
class BinaryTree:
    def __init__(self, root_node=None):
        self.root = root_node

    def get_node_distance(self, root, node_data1, node_data2):
        dist_n1 = self.path_length(root, node_data1) - 1
        dist_n2 = self.path_length(root, node_data2) - 1
        lca_data = self.find_lca(root, node_data1, node_data2).data
        lca_distance = self.path_length(root, lca_data) - 1
        return (dist_n1 + dist_n2) - 2 * lca_distance

    def path_length(self, root, node_data1):
        if root == None:
            return 0
        else:
            out = 0
            if root.data == node_data1:
                return out + 1
            out = self.path_length(root.left_child, node_data1)
            if out > 0:
                return out + 1
            out = self.path_length(root.right_child, node_data1)
            if out > 0:
                return out + 1

        return 0

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