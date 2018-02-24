"""
Implement int sqrt(int x).

Compute and return the square root of x.

x is guaranteed to be a non-negative integer.


Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we want to return an integer, the decimal part will be truncated.

"""
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if x == 1:
            return 1
        left = 2
        right = x
        while left < right:
            middle = (left + right) // 2
            mid_squared = middle*middle
            if mid_squared == x:
                return middle
            elif mid_squared < x:
                left = middle + 1
            else:
                right = middle - 1
        return left-1 if left*left > x else left