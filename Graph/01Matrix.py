"""

Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
Example 1:
Input:

0 0 0
0 1 0
0 0 0
Output:
0 0 0
0 1 0
0 0 0
Example 2:
Input:

0 0 0
0 1 0
1 1 1
Output:
0 0 0
0 1 0
1 2 1
Note:
The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
"""
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return matrix
        nrows = len(matrix)
        ncols = len(matrix[0])

        for r in xrange(nrows):
            for c in xrange(ncols):
                if matrix[r][c] == 1:
                    matrix[r][c] = self.bfs(matrix, r, c, 0)
        return matrix

    def bfs(self, matrix, r, c, b):
        tovisit = [(r, c, 0)]
        visited = set()
        visited.add((r, c, 0))

        while tovisit:
            cell = tovisit.pop(0)
            if matrix[cell[0]][cell[1]] == 0:
                return cell[2]

            for neighbor in self.getNeighbors(matrix, cell[0], cell[1], cell[2]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    tovisit.append(neighbor)

    def getNeighbors(self, matrix, r, c, b):
        ret = []
        if r > 0:
            ret.append((r - 1, c, b + 1))
        if r < len(matrix) - 1:
            ret.append((r + 1, c, b + 1))
        if c > 0:
            ret.append((r, c - 1, b + 1))
        if c < len(matrix[0]) - 1:
            ret.append((r, c + 1, b + 1))

        return ret
