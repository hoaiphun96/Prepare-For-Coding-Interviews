class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def bfs(self):
        tovisit = [self]
        visited = []
        while tovisit:
            node = tovisit.pop(0)
            if node.left:
                tovisit.append(node.left)
            if node.right:
                tovisit.append(node.right)
            visited.append(node.val)

        return visited

    def dfs(self):
        tovisit = [self]
        visited = []
        while tovisit:
            node = tovisit.pop()
            print(node.val)
            if node.left and node.left.val not in visited:
                tovisit.append(node.left)
            elif node.right and node.right.val not in visited:
                tovisit.append(node.right)
            visited.append(node.val)

        return visited
