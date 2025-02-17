class Node:
    """An object for storing single node of linked list.
    Models two attributes - data and the link to the next node in the list"""
    data = None
    next_node = None

    def __init__(self,data) -> None:
       self.data = data

    def __repr__(self):
        return '<Node data: %s' %  self.data


class LinkedList:
    """singly linked list"""
    def __init__(self) -> None:
        self.head = None


    def is_empty(self):
        return self.head == None
    
    def size(self):
        """Returns number of nodes in list in linear time"""
        current = self.head
        count = 0

        while current :
            count += 1
            current = current.next_node
        return count
