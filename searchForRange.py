"""
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        left1 = -1
        right2 = -1
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                # find left most target
                if right == left:
                    return [left, right]
                left1 = left
                right1 = middle
                while left1 < right1:
                    middle1 = (left1 + right1) // 2
                    if nums[middle1] < target:
                        left1 = middle1 + 1
                    else:  # if nums[middle] == target
                        right1 = middle1
                        # find right most target
                left2 = middle
                right2 = right
                while left2 < right2:
                    middle2 = (left2 + right2) // 2 + 1
                    if nums[middle2] > target:
                        right2 = middle2 - 1
                    else:  # if nums[middle] == target
                        left2 = middle2
                return [left1, left2]

        return [-1, -1]