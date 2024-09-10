def merge_sort(list):
    """Sort a list in ascending order
    returns a new sorted list

    Divide : find the midpoint of the list and divide into sublists
    Conqure: recursively sort the sublist created in previous step
    COMBINE: merge the sorted sublist 
    """
    if len(list) <= 1:
        return list
    
    [left_half,right_half] = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)


def split(list):
    midpoint = len(list) // 2
    return [list[0:midpoint],list[midpoint:]]


[l,r] = split([1,2,3,4])
print(l,r)