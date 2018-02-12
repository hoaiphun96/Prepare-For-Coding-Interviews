"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
"""
from collections import Counter
class Solution:
    def intersect(self, nums1, nums2):
        ret =[]
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        if len(c1) <= len(c2):
            smallerlist,biggerlist = c1,c2
        else:
            smallerlist,biggerlist = c2,c1
        for elem in smallerlist.keys():
            if elem in biggerlist.keys():
                t = c1[elem] if c1[elem] <= c2[elem] else c2[elem]
                ret += [elem] * t
        return ret

"""
O(n+m) time, cleaner version
"""
    def intersect2(self, nums1, nums2):
        ret = dict()
        if len(nums1) <= len(nums2):
            smallnums, bignums = nums1, nums2
        else:
            smallnums, bignums = nums2, nums1
        for n in smallnums:
            if n not in ret:
                ret[n] = 1
            else:
                ret[n] += 1
        retList = []
        for n in bignums:
            if n in ret and ret[n] > 0:
                ret[n] -= 1
                retList.append(n)

        return retList