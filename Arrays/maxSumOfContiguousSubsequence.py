"""
Given a list consisting of both positive and negative integers, find the maximum sum among all the contiguous subsequences of the input list.
Write a function that takes in a list of integers and returns the maximum sum.

Examples:
largestContinuousSum([-1,-2,3,4,5]) ==> 12

largestContinuousSum([1,2,3,-2,5]) ==> 6
"""


def largestContinuousSum(arr):
    if len(arr) == 0:
        return 0
    currentSum, maxSum = arr[0], arr[0]
    for i in range(1, len(arr)):
        currentSum = max(currentSum + arr[i], arr[i])
        maxSum = max(currentSum, maxSum)
    return maxSum

