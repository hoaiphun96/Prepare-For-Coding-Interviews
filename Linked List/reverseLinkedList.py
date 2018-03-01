"""
Reverse a singly linked list.
"""
class ListNode:
    def __init__(self,v):
        self.val = v
        self.next = None

    def reverseList(self, head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev