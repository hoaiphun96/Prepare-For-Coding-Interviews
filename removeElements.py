"""
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        while head is not None and head.val is val:
            head = head.next
        if head is None:
            return
        curr = head
        while curr.next is not None:
            if curr.next.val != val:
                curr = curr.next
            else:
                curr.next = curr.next.next
        return head