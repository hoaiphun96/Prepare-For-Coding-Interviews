"""

Rotate an array to the left by k positions without using extra space.k can be greater than the size of the array.

Example:
rotate_left([1,2,3,4,5],2) --> [3,4,5,1,2]
"""

def rotate_left(list_numbers,k):
    k = k % len(list_numbers)
    #reverse list_numbers
    reverse(list_numbers, 0, len(list_numbers) - 1)
    #reverse left side
    reverse(list_numbers, 0, len(list_numbers) - k - 1)
    #reverse right side
    reverse(list_numbers, len(list_numbers) - k, len(list_numbers) - 1)
    return list_numbers
def reverse(list_numbers, left, right):
    if not list_numbers:
        return None
    while left < right:
        list_numbers[left], list_numbers[right] = list_numbers[right], list_numbers[left]
        left += 1
        right -= 1