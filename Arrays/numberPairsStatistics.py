"""
Given a List <Point> p, find the number of (i,j) pairs that satisfy both p[i].x + p[j].x and p[i].y + p[j].y(i < j) can be divisible by 2.

 Notice
The length of given list len <= 10000.
Have you met this question in a real interview?
Example
Given p = [[1,2],[3,4],[5,6]], return 3.

Explanation:
p[0],p[1],p[2] Pairwise Covering, the sum of their x and y can be divided by 2
Given p = [[0,3],[1,1],[3,4],[5,6]], return 1.

Explanation:
Only when p [2] and p [3] are combined, their sum of x and y can be divided by two.

"""
class Solution:
    """
    @param p: the point List
    @return: the numbers of pairs which meet the requirements
    """
    def pairNumbers(self, p):
        pair_oo = 0
        pair_ee = 0
        pair_oe = 0
        pair_eo = 0
        for pair in p:
            if pair.x % 2 == 0 and pair.y % 2 == 0:
                pair_ee += 1
            elif pair.x % 2 == 1 and pair.y % 2 == 1:
                pair_oo += 1
            elif pair.x % 2 == 1 and pair.y % 2 == 0:
                pair_oe += 1
            else:
                pair_eo += 1
        print(pair_oo, pair_ee, pair_oe, pair_eo)

        return (pair_ee*(pair_ee-1) + pair_oo*(pair_oo-1) + pair_eo*(pair_eo-1) + pair_oe*(pair_oe-1)) // 2