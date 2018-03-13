"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer,
replace the number by the sum of the squares of its digits, and repeat the process until the
number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""

def isHappy(number):
    seen = set()
    while True:
        number = square_number(number)
        if number == 1:
            return True
        if number in seen:
            return False
        seen.add(number)

def square_number(number):
    digits = list(str(number))
    s = 0
    for d in digits:
        s += int(d)**2
    return s