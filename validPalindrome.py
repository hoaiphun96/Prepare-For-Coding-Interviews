"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
Dynamic programming
"""


class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(0, len(s) // 2):
            if s[i] != s[len(s) - 1 - i]:
                return self.helper(s[i + 1:len(s) - i]) or self.helper(s[i:len(s) - i - 1])
        return True

    def helper(self, s):
        for i in range(0, len(s) // 2):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True
