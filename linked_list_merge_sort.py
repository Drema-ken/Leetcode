from linked_list import linked_list

def merge_sort(linked_list):
    """recursively divide a singly linked list into sublist containing a single node
    -   repeatedly merge the sublist to produce a sorted sublist until one remains
    - returns a sorted linked list   
    """
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list
    
    left_half,right_half =  split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    merge(left,right)

def split(linked_list):
    """divide unsorted list at midpoint into sublinked list"""

    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None


def merge():
    pass