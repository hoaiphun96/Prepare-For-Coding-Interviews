"""
Given a 2D array, traverse in clockwise direction and return the path
For example:
[[1,2,3],[4,5,6],[7,8,9]]
is
[ 1 2 3]
[4 5 6]
[7 8 9]

return 1 2 3 6 9 8 7 4 5
"""
def find_spiral(matrix):
    nrows = len(matrix)
    ncols = len(matrix[0])
    wall_up, wall_down, wall_left, wall_right = -1, nrows, -1, ncols
    ret = []
    current_row = 0
    current_col = 0
    current_move = "R"
    # loop until traverse through all the spots
    while True:
        if wall_up < current_row < wall_down and wall_left < current_col < wall_right:
            ret.append(matrix[current_row][current_col])
        else:
            break
        if current_move == "R":
            # go all the way to the right until hit the right wall
            if current_col < wall_right - 1:
                current_col += 1
            else:
                current_move = "D"
                current_row += 1
                wall_up += 1
        elif current_move == "D":
            # go all the way down until hit the down wall
            if current_row < wall_down - 1:
                current_row += 1
            else:
                current_move = "L"
                current_col -= 1
                wall_right -= 1
        elif current_move == "L":
            # go all the way to the left until hit the left wall
            if current_col > wall_left + 1:
                current_col -= 1
            else:
                current_move = "U"
                current_row -= 1
                wall_down -= 1
        elif current_move == "U":
            # go all the way down until hit the down wall
            if current_row > wall_up + 1:
                current_row -= 1
            else:
                current_move = "R"
                current_col += 1
                wall_left += 1

        else:
            break


find_spiral([[1, 2, 3], [4, 5, 6], [7, 8, 9]])