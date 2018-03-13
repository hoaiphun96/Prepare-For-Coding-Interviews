"""
Given a sorted list of integers, find partitions such that each partition denotes a range of
consecutive integers.

Note: The input list consists of sorted integers, without duplicates. Range(a,b) should be
denoted as a-b where a and b are included in the range.

Example:
Input : [1,2,3,6,7,8,10,11]
Output : [1-3, 6-8, 10-11]
"""

def find_partitions(input_list):
    if not input_list:
        return None
    ret = []
    lower_bound = input_list[0]
    upper_bound = input_list[0]
    for index in range(1, len(input_list)):
        if input_list[index] == input_list[index-1] + 1:
            upper_bound = input_list[index]
        elif input_list[index] > input_list[index-1] + 1 : #check case the last number
            if upper_bound > lower_bound:
                ret.append(str(lower_bound) + "-" + str(upper_bound))
            else:
                ret.append(str(lower_bound))
            lower_bound, upper_bound = input_list[index], input_list[index]
    if upper_bound > lower_bound:
        ret.append(str(lower_bound) + "-" + str(upper_bound))
    else:
        ret.append(str(lower_bound))
    return ret