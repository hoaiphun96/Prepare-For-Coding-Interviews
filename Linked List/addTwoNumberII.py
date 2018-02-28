"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s = self.convert(l1) + self.convert(l2)
        return self.toLinkedList(s)

    def convert(self, l):
        s = ""
        p = l
        while p != None:
            s += str(p.val)
            p = p.next
        return int(s)

    def toLinkedList(self, s):
        p = ListNode(0)
        h = p
        arr = list(str(s))
        for c in arr:
            node = ListNode(int(c))
            p.next = node
            p = p.next
        return h.next

