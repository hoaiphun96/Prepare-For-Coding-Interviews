"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""
class Solution:
    def restoreIpAddresses(self,s):
        retval = list()
        if len(s)>12:
            return retval
        else:
            for pos1 in self.helper(s):
                for pos2 in self.helper(s[len(pos1):]):
                    if pos2 == []:
                        continue
                    for pos3 in self.helper(s[len(pos1+pos2):]):
                        if pos3 == []:
                            continue
                        for pos4 in self.helper(s[len(pos1+pos2+pos3):]):
                            if pos4 == []:
                                continue
                            possible =pos1 + "." + pos2 + "." + pos3 + "." + pos4
                            print(possible)
                            if len(possible) == len(s) + 3:
                                retval.append(possible)
        return retval

    def helper(self,s):
        if s == "":
            return []
        if s[:1] == "0":
            return ["0"]
        pos = set()
        for i in range(1,4):
            if self.isValid((s[:i])):
                pos.add((s[:i]))
        return pos

    def isValid(self,i):
        return 0<=int(i)<=255
