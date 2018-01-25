"""
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
"""
import string
class Solution:
    def titleToNumber(self, s):
        chars = list(s)
        ret = 0
        for (index, char) in enumerate(chars):
            ret += (26**(len(chars) - 1 - index))*(string.ascii_uppercase.index(char) +1)
        return ret