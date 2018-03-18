"""
You're given a list of integers, where each element represents the maximum number of jumps forward that can be made from that element.
You are located at the starting index of the array.
Write a method to return the minimum number of jumps required to reach the end of the array. If an element is 0, you cannot move over that element.
Examples:

min_jumps([2, 5, 7, 8, 9, 12]) => 2
min_jumps([2, 1, 1, 1, 1, 12, 15]) => 5
"""

def min_jumps(arr):
    current_i = 0
    counter = 0
    while current_i < len(arr) - 1:
        if arr[current_i] == 0:
            return 0
        next_optimal_i, highest_range = current_i + 1, 1
        for j in range(1, arr[current_i] + 1):
            if j + arr[min(current_i + j, len(arr) -1)] > highest_range:
                next_optimal_i, highest_range = min(current_i + j, len(arr) -1), j + arr[min(current_i + j, len(arr) -1)]
        current_i = next_optimal_i
        counter += 1
    return counter

#approach 2
def min_jumps(arr):
    i=0
    count=0
    end =0
    minDist=0
    while minDist >= i and i < len(arr):
        if end < i:
            count += 1
            end = minDist
        minDist = max(minDist,arr[i]+i)
        i += 1
    if minDist < len(arr)-1:
        return 0
    else:
        return count