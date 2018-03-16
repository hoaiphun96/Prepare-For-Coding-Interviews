"""
Array Quadruplet
Given an unsorted array of integers arr and a number s, write a function findArrayQuadruplet that finds four numbers (quadruplet) in arr that sum up to s. Your function should return an array of these numbers in an ascending order. If such a quadruplet doesn’t exist, return an empty array.

Note that there may be more than one quadruplet in arr whose sum is s. You’re asked to return the first one you encounter (considering the results are sorted).

Explain and code the most efficient solution possible, and analyze its time and space complexities.

Example:

input:  arr = [2, 7, 4, 0, 9, 5, 1, 3], s = 20

output: [0, 4, 7, 9] # The ordered quadruplet of (7, 4, 0, 9)
                     # whose sum is 20. Notice that there
                     # are two other quadruplets whose sum is 20:
                     # (7, 9, 1, 3) and (2, 4, 9, 5), but again you’re
                     # asked to return the just one quadruplet (in an
                     # ascending order)
Constraints:

[time limit] 5000ms

[input] array.integer arr

1 ≤ arr.length ≤ 100
[input] integer s

[output] array.integer
"""


def find_array_quadruplet(arr, s):
    # sort the array
    arr = sorted(arr)
    if len(arr) < 4:
        return []
    for i in range(len(arr) - 3):
        for j in range(i + 1, len(arr) - 2):
            current_sum = arr[i] + arr[j]
            # reduce to finding two sum of arr[j+1:]
            res = sum_of_two(arr[j + 1:], s - current_sum)
            if res != None:
                return [arr[i], arr[j], res[0], res[1]]
    return []


def sum_of_two(arr, s):
    i = 0
    j = len(arr) - 1
    while i < j:
        if arr[i] + arr[j] == s:
            return (arr[i], arr[j])
        elif arr[i] + arr[j] > s:
            j -= 1
        else:
            i += 1
    return None