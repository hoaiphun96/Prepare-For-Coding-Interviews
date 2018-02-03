"""
Given many words, words[i] has weight i.

Design a class WordFilter that supports one function, WordFilter.f(String prefix, String suffix). It will return the word with given prefix and suffix with maximum weight. If no word exists, return -1.

Examples:
Input:
WordFilter(["apple"])
WordFilter.f("a", "e") // returns 0
WordFilter.f("b", "") // returns -1
Note:
words has length in range [1, 15000].
For each test case, up to words.length queries WordFilter.f may be made.
words[i] has length in range [1, 10].
prefix, suffix have lengths in range [0, 10].
words[i] and prefix, suffix queries consist of lowercase letters only.
"""


class WordFilter:
    hashtable = {}

    def __init__(self, words):
        """
        :type words: List[str]
        """
        for i, w in enumerate(words):
            prefix = ""
            for i_p in range(-1, min(10, len(w))):
                if i_p != -1:
                    prefix += w[i_p]
                suffix = ""
                for i_s in range(-1, min(10, len(w))):
                    if i_s != -1:
                        suffix = w[-1 - i_s] + suffix
                    self.hashtable[prefix + " " + suffix] = i

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        key = prefix + " " + suffix
        if key in self.hashtable:
            return self.hashtable[key]
        return -1



        # Your WordFilter object will be instantiated and called as such:
        # obj = WordFilter(words)
        # param_1 = obj.f(prefix,suffix)