def linear_search(list,target):
    '''returns the index of target if found else none'''
    for i in range(0,len(list)):
        if list[i] == target:
            return i
    return None
    
    '''const linearSearch= (arr,target)=>{
                const index = arr.indexOf(target)
                return index !== -1 ? index : null
                }'''
    
def verify(index):
    if index is not None:
        print('Target found at ',index)
    else:
        print('Target not found in list')

numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
#print(numbers)
result = linear_search(numbers,12)
verify(result)