"""
Given an m x n matrix (2d list) filled with non-negative integers, use depth first search to find the maximum sum along a path from the top-left of the grid to the bottom-right. Return this maximum sum. The direction of movement is limited to right and down.

Example:
Input Matrix :

    1 2 3
    4 5 6
    7 8 9

Output  : 1 + 4 + 7 + 8 + 9 = 29

"""


# Collections module has already been imported.
def matrix_max_sum_dfs(grid):
    max_sum = 0

    nrows = len(grid)
    ncols = len(grid[0])

    return dfs(grid, 0, 0, nrows - 1, ncols - 1, max_sum)


def dfs(grid, current_r, current_c, goal_r, goal_c, max_sum):
    to_visit = [(current_r, current_c, 0)]
    while to_visit:
        current = to_visit.pop()
        r, c, sum_so_far = current[0], current[1], current[2]
        current_sum = grid[r][c] + sum_so_far
        if r == goal_r and c == goal_c:
            # update max_sum
            max_sum = max(max_sum, current_sum)

        if c + 1 <= goal_c:
            to_visit.append((r, c + 1, current_sum))
        if r + 1 <= goal_r:
            to_visit.append((r + 1, c, current_sum))
    return max_sum