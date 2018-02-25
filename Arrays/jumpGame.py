"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""


class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        current_i = 0
        max_range = 0
        next_i = 0
        while max_range < len(nums) - 1:
            if nums[current_i] == 0:
                return False
            for k in range(1, min(len(nums) - 1 - current_i, nums[current_i]) + 1):
                r = current_i + k + nums[current_i + k]
                if r > max_range:
                    max_range = r
                    next_i = current_i + k
            if current_i == next_i:
                return False
            current_i = next_i
        return True
