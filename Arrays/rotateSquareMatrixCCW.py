"""
You are given a square 2D image matrix (List of Lists) where each integer represents a pixel. Write a method rotate_square_image_ccw to rotate the image counterclockwise - in-place. This problem can be broken down into simpler sub-problems you've already solved earlier! Rotating an image counterclockwise can be achieved by taking the transpose of the image matrix and then flipping it on its horizontal axis.

Example:
Input image :
1 0
1 0
Modified to :
0 0
1 1
"""

def rotate_square_image_ccw(matrix):
    #inverse of matrix
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(i+1, cols):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    #flip on horizontal axis
    for i in range(rows / 2):
        matrix[i], matrix[rows-i-1] = matrix[rows-i-1], matrix[i]
    return matrix