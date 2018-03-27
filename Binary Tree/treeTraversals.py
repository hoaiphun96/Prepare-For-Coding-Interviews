class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

   #Recursive BFS
   def bfs(self):
       tovisit = [self]
       visited = set()

       while tovisit:
           node = tovisit.pop(0)
           print(node.val)

           if node.left and node.left.val not in visited:
               tovisit.append(node.left)

           if node.right and node.right.val not in visited:
               tovisit.append(node.right)

           visited.add(node)

   #Recursive DFS
   def dfs(self):
       tovisit = [self]
       visited = set()
       visited.add(self)

       while tovisit:
           node = tovisit.pop()
           print(node.val)

           if node.left and node.left.val not in visited:
               tovisit.append(node.left)

           if node.right and node.left.val not in visited:
               tovisit.append(node.right)

           visited.add(node)

   #Iterative Preorder
   def preOrder(self):
       if not self:
           return
       stack = [self]

       while stack:
           node = stack.pop()
           if node:
               print(node.val)
               stack.append(node.right)
               stack.append(node.left)


   #Iterative Inorder
   def inOrder(self):
       if not self:
           return
       done = False
       stack = []
       curr = self
       while not done:
           if curr:
               stack.append(curr)
               curr = curr.left
           else:
               if not stack:
                   done = True
               else:
                   curr = stack.pop()
                   print(curr.val)
                   curr = curr.right

   #Recursive Inorder
   def inOrderR(self):
       if self:
           if self.left:
               self.left.inOrderR()
           print(self.val)
           if self.right:
               self.right.inOrderR()

   #Recursive PreOrder
   def preOrderR(self):
       if self:
           print(self.val)
           if self.left:
               self.left.preOrderR()
           if self.right:
               self.right.preOrderR()

   #Recursive PostOrder
   def postOrderR(self):
       if self:
           if self.left:
               self.left.postOrderR()
           if self.right:
               self.right.postOrderR()
           print(self.val)


t8 = TreeNode(8)
t5 = TreeNode(5)
t5.left = t8
t4 = TreeNode(4)
t2 = TreeNode(2)
t2.left = t4
t2.right = t5
t6 = TreeNode(6)
t7 = TreeNode(7)
t3 = TreeNode(3)
t3.left = t6
t3.right = t7
t1 = TreeNode(1)
t1.left = t2
t1.right = t3

