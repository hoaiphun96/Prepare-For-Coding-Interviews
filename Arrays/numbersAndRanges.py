"""
Given a sorted list and an input number as inputs, write a function to return a Range object, consisting of the indices of the first and last occurrences of the input number in the list. Check out the Use Me section to examine the structure of the Range class.

Note: The List can have duplicate numbers. The indices within the Range object should be zero based.

Examples:
Input List  : [1,2,5,5,8,8,10]
Input Number : 8
Output : [4,5]

Input List  : [1,2,5,5,8,8,10]
Input Number : 2
Output : [1,1]
"""


def find_range(input_list, input_number):
    # do binary search to find the index of the an input number in list
    left, right = -1, -1
    first_index = binarySearch(input_list, input_number, 0, len(input_list) - 1)
    left = first_index
    while left > 0 and input_list[left - 1] == input_number:
        left = binarySearch(input_list, input_number, 0, left - 1)

    right = first_index
    while right < len(input_list) - 1 and input_list[right + 1] == input_number:
        right = binarySearch(input_list, input_number, right + 1, len(input_list) - 1)
    return [left, right]


def binarySearch(input_list, input_number, left, right):
    while left <= right:
        mid = (left + right) // 2
        if input_list[mid] == input_number:
            return mid
        elif input_list[mid] > input_number:
            right = mid - 1
        else:
            left = mid + 1
    return -1