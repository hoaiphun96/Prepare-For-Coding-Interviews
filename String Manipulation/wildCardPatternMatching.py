"""

You are given two strings - where the first string can include regex wildcard characters (* and ?)
and other is a regular string.
Write a method to check if the two strings match.

* --> Matches with zero or more characters.

? --> Matches exactly a single character.

Examples:

match("fi*de", "firecode") ==> "True"
match("fi?de", "firecode") ==> "False"
"""


def match(first, second):
    p1, p2, starInd = 0, 0, -1

    while p2 < len(second):
        if p1 < len(first) and (first[p1] == second[p2] or first[p1] == "?"):
            p1 += 1
            p2 += 1
        elif p1 < len(first) and first[p1] == "*":
            starInd = p1
            p1 += 1
        elif starInd != -1:
            p2 += 1
            p1 = starInd + 1
        else:
            return False
    while p1 < len(first) and first[p1] == "*":
        p1 += 1
    return p1 == len(first)
