"""
You are given an n x n square 2D matrix that represents a monochromatic image's pixels.
Rotate it by 90 degrees in the clockwise direction.

Note: The input matrix is a nested list.

Example:
Input Matrix :

       [1 0]
       [0 1]

Output       :

       [0 1]
       [1 0]

"""

def rotate_image(matrix):
   # get matrix transpose
   n = len(matrix)

   for row in range(n):
       for col in range(row + 1, n):
           matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

   # flip matrix along vertical axis
   for row in range(n):
       for col in range(n // 2):
           matrix[row][col], matrix[row][n - col - 1] = matrix[row][n - col - 1], matrix[row][col]

   return matrix
