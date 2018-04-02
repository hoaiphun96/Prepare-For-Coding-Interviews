"""
Given a nested list of integers representing a triangle, find the minimum path sum from top to bottom. At each step you can move to adjacent numbers on the row one level below.

Note: You can only traverse to adjacent nodes while moving downwards. The input triangle is a nested list of integers.

Example:
Input Triangle:
   1
  2 3
 4 5 6
7 8 9 10

Output : 14
"""


def min_triangle_depth(input_dict):
    if len(input_dict) == 0:
        return 0
    d = {}
    dfs(input_dict, (0, 0), d)
    return d[(0, 0)]


def dfs(input_dict, current, d):
    if current in d:
        current_min = d[current]
    else:
        current_row, current_col = current[0], current[1]

        if current_row == len(input_dict) - 1:
            current_min = input_dict[current_row][current_col]
        else:
            left, right = 0, 0
            if current_row + 1 < len(input_dict):
                left = dfs(input_dict, (current_row + 1, current_col), d)
                right = dfs(input_dict, (current_row + 1, current_col + 1), d)

            current_min = input_dict[current_row][current_col] + min(left, right)
    d[current] = current_min
    return current_min