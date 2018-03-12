"""
Given an list of integers, write a method - max_gain - that returns the maximum gain. Maximum Gain is defined as the maximum difference between 2 elements in a list such that the larger element appears after the smaller element. If no gain is possible, return 0.

Example:
max_gain([100,40,20,10]) ==> 0
max_gain([0,50,10,100,30]) ==> 100

Since the larger element must always appear after the smaller element, this problem can be solved in a single pass. Keep a record of the maximum gain found so far, and the minimum element. When finding the maximum gain,
use the difference between the current element and the minimum element found so far.
"""


def max_gain(input_list):
    max_gain = 0
    curr_min = input_list[0]
    for i in range(1, len(input_list)):
        if input_list[i] > curr_min:
            max_gain = max(max_gain, input_list[i] - curr_min)
        else:
            curr_min = input_list[i]
    return max_gain
