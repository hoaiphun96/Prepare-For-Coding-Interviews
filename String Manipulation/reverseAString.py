"""
Write a function that takes in a string and returns the reversed version of the string.

Examples:

reverse_string("abcde") -> "edcba"

reverse_string("1") -> "1"

reverse_string("") -> ""

reverse_string("madam") -> "madam"
"""


def reverse_string(a_string):
    a_string = list(a_string)
    slen = len(a_string)
    for i in range(slen // 2):
        a_string[i], a_string[slen - i - 1] = a_string[slen - i - 1], a_string[i]

    return "".join(a_string)