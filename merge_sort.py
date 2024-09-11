#divide and conquer 
def merge_sort(list):
    """Sort a list in ascending order
    returns a new sorted list

    Divide : find the midpoint of the list and divide into sublists
    Conquer : recursively sort the sublist created in previous step
    COMBINE: merge the sorted sublist 
    """ 
    if len(list) <= 1 :
        return list
    
    [left_half,right_half] = split(list)
   
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    return merge(left,right)
     

def split(list):
    """Divides an unsorted list at midppoint and returns  a sublist - left and rigth"""
    midpoint = len(list) // 2
    return [list[0:midpoint],list[midpoint:]]


def merge(left,right):
    """Merges  two lists and returns a new list
        returns a new merged list"""
    l= []
    i= 0
    j= 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1
    
    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l
sort = merge_sort([5,4,3,2])
alist = [3,5,2,1]

def verify_sorted(list):
    n = len(list)
    if n == 1:
        return True
    return list[0] < list[1] and verify_sorted(list[1:])

print(verify_sorted(alist))