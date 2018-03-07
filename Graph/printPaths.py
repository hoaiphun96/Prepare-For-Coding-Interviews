"""
You're given a 2D board which contains an m x n matrix (2D list of characters). Write a method - print_paths that prints all possible paths from the top left cell to the bottom right cell. Your method should return a list of strings, where each string represents a path with characters appended in the order of movement. You're only allowed to move down and right on the board. The order of string insertion in the list does not matter.

Example:

Input Board :
[
    [A, X],
    [D, E]
]
Output: ["ADE", "AXE"]
"""


def print_paths(board):
    if board[0] == []:
        return []
    ret = []
    target = (len(board) - 1, len(board[0]) - 1)
    helper(board, ret, "", (0, 0), target)
    return ret


def helper(board, ret, path_so_far, current_pos, target):
    # if current position is the bottom right cell, then add the path to the list
    current_letter = board[current_pos[0]][current_pos[1]]

    if current_pos == target:
        ret.append(path_so_far + current_letter)
        return

    # else keep doing dfs
    # get the right move and check if it's valid then do the recursive call
    if current_pos[1] < len(board[0]) - 1:
        helper(board, ret, path_so_far + current_letter, (current_pos[0], current_pos[1] + 1), target)
    if current_pos[0] < len(board) - 1:
        helper(board, ret, path_so_far + current_letter, (current_pos[0] + 1, current_pos[1]), target)

"""
Runtime Complexity 
O(bd)
b = Branching Factor = 2 (down and right)

d = depth = m + n where m and n are the number of rows and columns in the matrix

Space Complexity 
O(bxd)
b = Branching Factor = 2 (down and right)

d = depth = m + n where m and n are the number of rows and columns in the matrix
"""