"""
Given a Singly Linked-List, implement a method to check if the list has cycles.
The Space complexity should be O(1).
If there is a cycle, return true. Otherwise, return false.
Empty lists should be considered non-cyclic.
Be sure to click Use Me to check Node's structure.

Examples:
1->2->3->4->1 ==> True

1->2->3->4 ==> False

Requirement: O(1) space complexity
"""

class SinglyLinkedList:
    # constructor
    def __init__(self):
        self.head = None

    # method for setting the head of the Linked List
    def setHead(self, head):
        self.head = head

    def is_cyclic(self):

        p1 = self.head
        while p1 != None:
            p2 = p1
            for i in range(2):
                if p2.getNext() != None:
                    p2 = p2.getNext()
                else:
                    return False
            while p2 != None:
                if p1.getData() == p2.getData():
                    return True
                p2 = p2.getNext()
            p1 = p1.getNext()

        return False