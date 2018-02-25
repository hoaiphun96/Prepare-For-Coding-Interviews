"""

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.


"""

class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right)// 2
            if (middle == 0 and nums[middle] < nums[middle+1]) or nums[middle] < nums[middle-1]:
                return nums[middle]
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle - 1
        return middle