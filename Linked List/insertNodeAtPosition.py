"""
Given a Singly Linked-List, implement a method to insert a node at a specific position.
If the given position is greater than the list size, simply insert the node at the end.

Example:
Given 1->2->3,

insert_at_pos(data,position) :
insert_at_pos(4,2) ==> 1->4->2->3

*position=2 means 2nd node in the list
"""


class SinglyLinkedList:
    # constructor
    def __init__(self):
        self.head = None

    # method for setting the head of the Linked List
    def setHead(self, head):
        self.head = head

    # Method for inserting a new node at the start of a Linked List
    def insert_at_pos(self, data, pos):
        new_node = Node()
        new_node.setData(data)
        if not self.head or pos == 1:
            new_node.setNext(self.head)
            self.setHead(new_node)
            return

        current = self.head
        i = 1
        while current.getNext() != None:
            if i == pos - 1:
                new_node.setNext(current.getNext())
                current.setNext(new_node)
                return
            else:
                i += 1
                current = current.getNext()
        current.setNext(new_node)