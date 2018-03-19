"""You're given a 2D Boggle Board which contains an m x n matrix (2D list) of characters, and a string - word. Write a method - boggle_search that searches the Boggle Board for the presence of the input word. Words on the board can be constructed with sequentially adjacent letters, where adjacent letters are horizontal or vertical neighbors (not diagonal). Also, each letter on the Boggle Board must be used only once.

Example:

Input Board :
[
    [A, O, L],
    [D, E, L],
    [G, H, I],
]
Word: "HELLO"
Output: True
"""
#Approach 1
def boggle_search(board, word):
    # do dfs
    rows = len(board)
    cols = len(board[0])

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == word[0]:
                # do dfs
                if dfs(board, r, c, word) == True:
                    return True
    return False


def dfs(board, r, c, word):
    to_visit = [(r, c, 0)]
    visited = set()
    visited.add((r, c, 0))

    while to_visit:
        current = to_visit.pop()
        r, c, i = current[0], current[1], current[2]
        print(r, c, i)
        if board[r][c] == word[i]:
            # add the next cells to stack
            if i == len(word) - 1:
                return True

            if isValid(r - 1, c, board) and (r - 1, c, i + 1) not in visited:
                to_visit.append((r - 1, c, i + 1))
            # r + 1, c
            if isValid(r + 1, c, board) and (r + 1, c, i + 1) not in visited:
                to_visit.append((r + 1, c, i + 1))
            # r, c- 1
            if isValid(r, c - 1, board) and (r, c - 1, i + 1) not in visited:
                to_visit.append((r, c - 1, i + 1))
            # r, c + 1
            if isValid(r, c + 1, board) and (r, c + 1, i + 1) not in visited:
                to_visit.append((r, c + 1, i + 1))
            visited.add(current)
    return False


def isValid(r, c, aboard):
    return 0 <= r < len(aboard) and 0 <= c < len(aboard[0])

#Approach 2
def boggle_search(board,word):
    rows = len(board)
    cols = len(board[0])
    out = False
    for i in xrange(rows):
        for j in xrange(cols):
            out = search(i,j,board,word,"")
            if out:
                return True

    return out


def search(r,c,board,word,predecessor):
    rows = len(board)
    cols = len(board[0])

    # Terminating Conditions
    if (r > rows -1                         # Out of Bounds
     or r < 0                               # Out of Bounds
     or c > cols-1                          # Out of Bounds
     or c < 0                               # Out of Bounds
     or predecessor not in word             # Not matching pattern
     or board[r][c] == '@'):
        return False

    ch = board[r][c]
    s = predecessor + ch
    out = False
    if s == word:
        return True
    else:
        board[r][c] = '@'                   # Mark the board node as visited
        # Check up, down, left, right
        out = search(r-1,c,board,word,s)  or search(r+1,c,board,word,s) or search(r,c-1,board,word,s) or search(r,c+1,board,word,s)
        board[r][c] = ch                    # Unmark the board node

    return out