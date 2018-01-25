"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range.
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""
class Solution:
    def reverse(self, x):
        retVal = int((str(x))[::-1]) if x >= 0 else -int((str(x)[1:])[::-1])
        checkInt32 = (2 ** 32) / 2
        if -checkInt32 < retVal < checkInt32:
            return retVal
        return 0
