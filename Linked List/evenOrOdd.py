"""
Given a Singly Linked-List, check whether its length is even or odd in a single pass.

Example:
1->2->3->4 ==> True

1->2->3->4->5 ==> False
"""
class SinglyLinkedList:
    # constructor
    def __init__(self):
        self.head = None

    # method for setting the head of the Linked List
    def setHead(self, head):
        self.head = head

    def is_list_even(self):
        length = 0
        curr = self.head
        while curr != None:
            length += 1
            curr = curr.getNext()

        if length % 2 == 0:
            return True
        return False