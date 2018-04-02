"""
iven a sorted list of integers and an integer target, find all the unique quadruplets which sum up to the given target.

Note: Each quadruplet must be a tuple having elements (input[i], input[j], input[k], input[l]), such that i < j < k < l. The ordering of unique quadruplets within the output list does not matter.

Examples:
Input : [1,2,3,4,5,6,7,8]
Target: 10
Output: [(1, 2, 3, 4])]

Input : [1,2,3,4,5,6,7]
Target: 20
Output: [(2, 5, 6, 7), (3, 4, 6, 7)]
"""


def quadruple_sum(integer_list, target_number):
    ret = []
    for i in range(len(integer_list) - 3):
        for j in range(i + 1, len(integer_list) - 2):
            sum_so_far = integer_list[i] + integer_list[j]
            indexes_of_kl = sum_of_two(integer_list, target_number - sum_so_far, j + 1)
            if indexes_of_kl != []:
                for pair in indexes_of_kl:
                    k, l = pair[0], pair[1]
                    ret.append((integer_list[i], integer_list[j], integer_list[k], integer_list[l]))
    return ret


def sum_of_two(integer_list, target_number, k):
    ret = []
    l = len(integer_list) - 1

    while k < l < len(integer_list):
        s = integer_list[k] + integer_list[l]

        if s < target_number:
            k += 1
        elif s == target_number:
            ret.append((k, l))
            k += 1
            l -= 1
        else:
            l -= 1
    return ret