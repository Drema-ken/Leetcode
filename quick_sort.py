def quick_sort(values):
    if len(values) <= 1 :
        return  values
    pivot =  values[0]
    less_than_pivot = []
    greater_than_pivot = []
    for element in values[1:]:
        if element <= pivot:
            less_than_pivot.append(element)
        else:
            greater_than_pivot.append(element)
    return quick_sort(less_than_pivot) + [pivot]+ quick_sort(greater_than_pivot)
    
sort = quick_sort([2,3,75,80,5,5])
print(sort)