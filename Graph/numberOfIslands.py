"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.
"""


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = set()
        counter = 0
        # do dfs to get all the ones in each island, after finish a dfs, increment number of island by one
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) in visited:
                    continue
                if grid[row][col] == '0':
                    visited.add((row, col))
                else:
                    self.dfs(visited, grid, (row, col))
                    counter += 1
        return counter

    def dfs(self, visited, grid, root):
        if grid[root[0]][root[1]] != '0':
            visited.add(tuple(root))
            if self.isValid(root[0] + 1, root[1], len(grid), len(grid[0])) and (root[0] + 1, root[1]) not in visited:
                self.dfs(visited, grid, [root[0] + 1, root[1]])
            if self.isValid(root[0] - 1, root[1], len(grid), len(grid[0])) and (root[0] - 1, root[1]) not in visited:
                self.dfs(visited, grid, [root[0] - 1, root[1]])
            if self.isValid(root[0], root[1] - 1, len(grid), len(grid[0])) and (root[0], root[1] - 1) not in visited:
                self.dfs(visited, grid, [root[0], root[1] - 1])
            if self.isValid(root[0], root[1] + 1, len(grid), len(grid[0])) and (root[0], root[1] + 1) not in visited:
                self.dfs(visited, grid, [root[0], root[1] + 1])
        else:
            return

    def isValid(self, row, col, num_row, num_col):
        return 0 <= row < num_row and 0 <= col < num_col
