"""
Given a sorted list of integers, find all the unique triplets which sum up to the given target.

Note: Each triplet must be a tuple having elements (input[i], input[j], input[k]), such that i < j < k. The ordering of unique triplets within the output list does not matter.

Example:
Input : [1,2,3,4,5,6,7]
Target: 15
Output: [(2, 6, 7), (3, 5, 7), (4, 5, 6)]
"""

#approach 1
def triple_sum(integer_list, target_number):
    ret = set()
    length = len(integer_list)
    for i in range(length - 2):
        if i > 0 and integer_list[i] == integer_list[i-1]:
            continue
        for j in range(i + 1, length - 1):
            sum_ij = integer_list[i] + integer_list[j]
            # do binary search for number target_number - sum_ij
            k = binarysearch(integer_list, j + 1, length - 1, target_number - sum_ij)
            if k != -1:
                ret.add((integer_list[i], integer_list[j], integer_list[k]))
    return list(ret)


def binarysearch(arr, left, right, number):
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == number:
            return middle
        elif arr[middle] > number:
            right = middle - 1
        else:
            left = middle + 1
    return -1

#approach 2
def triple_sum(integer_list, target_number):
    a_set = set()
    output = []
    for i in range(0,len(integer_list)):
        if i > 0 and integer_list[i] == integer_list[i-1]:
            continue
        j = i + 1
        k = len(integer_list) - 1
        while(j < k):
            sum = integer_list[i] + integer_list[j] + integer_list[k]
            if(sum > target_number):
                k -= 1
            elif sum < target_number:
                j += 1
            elif sum == target_number:
                temp_tuple = (integer_list[i],integer_list[j],integer_list[k])
                if temp_tuple not in a_set:
                    a_set.add(temp_tuple)
                    output.append(temp_tuple)
                j += 1
                k -= 1
    return output