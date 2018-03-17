"""
Write a function - long_common_prefix to find and return the longest common prefix in a list of strings. If no common prefix is found, return an empty string.
Example:
input_list => [firecode, fireacb, fireac]

commonPrefix(input_list) ==> "fir"
"""
def longestCommonPrefix(self, input_list):
    if not input_list:
        return ""
    longest_prefix = input_list[0]

    for i in range(1, len(input_list)):
        # update the longest_prefix
        word = input_list[i]
        j = 0
        for j in range(min(len(word), len(longest_prefix))):
            if word[j] == longest_prefix[j]:
                j += 1
            else:
                break
        longest_prefix = longest_prefix[:j]

    return longest_prefix