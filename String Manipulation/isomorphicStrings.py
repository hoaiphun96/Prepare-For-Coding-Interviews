"""
Given two strings - input1 and input2, determine if they are isomorphic.
Two strings are isomorphic if the letters in one string can be remapped to get the second string. Remapping a letter means replacing all occurrences of it with another letter. The ordering of the letters remains unchanged. You can also think of isomorphism as it is used in chemistry - i.e. having the same form or overall shape.

Example:
Input 1 : css
Input 2 : dll
Output  : true

Input 1 : css
Input 2 : dle
Output  : false
"""
#Approach 1
def are_isomorphic(input1, input2):
    if input1 == None and input2 == None:
        return False
    if len(input1) != len(input2):
        return False

    length = len(input1)
    dic1 = dict()
    dic2 = dict()
    for i in range(length):
        if input1[i] not in dic1:
            dic1[input1[i]] = input2[i]
            if input2[i] in dic2 and dic2[input2[i]] != input1[i]:
                return False
            dic2[input2[i]] = input1[i]
        else:
            if input2[i] != dic1[input1[i]] or input1[i] != dic2[input2[i]]:
                return False
    return True

#Approach 2:
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        d = {}
        seen = set()
        for i, x in enumerate(s):
            if x not in d:
                if t[i] in seen:
                    return False
                seen.add(t[i])
                d[x] = t[i]
            elif d[x] != t[i]:
                return False
        return True