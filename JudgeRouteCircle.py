"""
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false
"""


class Solution:
    def judgeCircle(self, moves):
        currpos = [0, 0]
        for char in list(moves):
            if char == "U":
                currpos[1] += 1
            if char == "D":
                currpos[1] -= 1
            if char == "L":
                currpos[0] -= 1
            if char == "R":
                currpos[0] += 1
        return currpos == [0, 0]
