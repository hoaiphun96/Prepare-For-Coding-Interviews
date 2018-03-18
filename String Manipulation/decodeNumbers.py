"""
Write a method to determine the number of ways to decode a string.

A msg string consists of letters from A-Z,
which represent numbers in the following mapping:

'A' -> 1

'B' -> 2

...

'Z' -> 26
Examples:

decodeString("521") => 2
Possible ways of decoding:
EBA, EU

decodeString("113021") => 0
Take 0 or 30, neither represent any alphabet and hence the entire string can't be decoded!
"""

#Approach 1, dfs, 2^n
def decode_string(msg):
    if msg is None:
        return 0
    counter = 0
    stack = list()
    addNext(-1, msg, stack)

    while stack:
        current = stack.pop()
        if current[1] == len(msg) - 1:
            counter += 1
            continue

        addNext(current[1], msg[current[1] + 1:], stack)
    return counter


def addNext(i_so_far, msg, stack):
    i = 1
    while i <= 2:
        if len(msg) < i:
            break
        next_s = msg[:i]
        if isValid(next_s):
            stack.append((next_s, i_so_far + i))
        i += 1


def isValid(s):
    if s[0] == "0":
        return False
    return 1 <= int(s) <= 26

#Approach 2, O(n)
def decode_string(msg):
    if len(msg) == 0:
        return 0
    previousWays = 0
    possibleWays = 1
    for i in range(0,len(msg)):
        if not msg[i].isdigit():
            return 0
        temp = 0
        if msg[i]!='0':
            temp = possibleWays
        if i>0 and int(msg[i-1:i+1])<27 and msg[i-1]!= '0':
            temp += previousWays
        previousWays = possibleWays
        possibleWays = temp
    return possibleWays