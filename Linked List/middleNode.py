"""
Given a Singly Linked-List, write a function to find and return the middle node of the list. Try and limit the runtime complexity to O(n) and space complexity to O(1).

Examples:
1 ==> 1

1->2 ==> 1

1->2->3->4 ==> 2

1->2->3->4->5 ==> 3

Note: Return type
of the function should be Node. Check out the Use Me section to find out it's structure.
"""


class SinglyLinkedList:
    # constructor
    def __init__(self):
        self.head = None

    # method for setting the head of the Linked List
    def setHead(self, head):
        self.head = head

    def find_middle_node(self):
        if self == None:
            return None
        p1 = self.head
        p2 = self.head

        while p1 != None and p1.getNext() != None and p1.getNext().getNext() != None:
            p1 = p1.getNext().getNext()
            p2 = p2.getNext()
        return p2