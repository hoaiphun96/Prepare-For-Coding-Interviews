"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold
additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
"""


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        p1 = m - 1
        p2 = n - 1
        p3 = m + n - 1
        while p1 >= 0 and p2 >= 0:
            print(p1, p2, p3)
            if nums1[p1] > nums2[p2]:
                nums1[p3] = nums1[p1]
                p1 -= 1
                p3 -= 1
            elif nums1[p1] < nums2[p2]:
                nums1[p3] = nums2[p2]
                p2 -= 1
                p3 -= 1
            else:  # case ==
                nums1[p3] = nums1[p1]
                nums1[p3 - 1] = nums2[p2]
                p1 -= 1
                p2 -= 1
                p3 -= 2
        if p1 < 0:
            nums1[:p2 + 1] = nums2[:p2 + 1]
