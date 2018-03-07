"""
Given a Singly Linked-List, write a function that returns the "Nth from the end" node of the list.

Example:
1->2->3->4->5->6, n=2 ==> 5

Note: Check out Use Me section to find out Node's structure. Your solution should return the entire node, not just it's data.
"""


class SinglyLinkedList:
    # constructor
    def __init__(self):
        self.head = None

    # method for setting the head of the Linked List
    def setHead(self, head):
        self.head = head

    def find_nth_node_from_end(self, n):
        if not self.head or n < 0:
            return None
        p1 = Node()
        p2 = Node()
        p1 = self.head
        p2 = self.head
        # move forward to the n node
        for i in range(n - 1):
            if p1.getNext():
                p1 = p1.getNext()
            else:
                return None
        while p1.getNext() != None:
            p1 = p1.getNext()
            p2 = p2.getNext()
        return p2

#More elegant solution
class SinglyLinkedList:
    # constructor
    def __init__(self):
        self.head = None

    # method for setting the head of the Linked List
    def setHead(self, head):
        self.head = head

    def find_nth_node_from_end(self, n):
        if not self.head or n < 0:
            return None
        p1 = Node()
        p2 = Node()
        p1 = self.head
        p2 = self.head

        length = 0
        while p1.getNext() != None:
            p1 = p1.getNext()
            length += 1

        time = length - n + 1
        if time < 0:
            return None
        for i in range(time):
            if p2.getNext() != None:
                p2 = p2.getNext()
        return p2