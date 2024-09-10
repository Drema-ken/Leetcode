list =  {'data':1,'rest':{'data':2,'rest':{'data':3,'rest':None}}}

def list_to_array(list):
    current = list
    arr = []
    while current['rest'] != None:
        arr.append(current['data'])
        current = current['rest']
    arr.append(current['data'])
    arr.reverse()
    return arr

#print(list_to_array(list))

array = [1,2,3]

def array_to_list(arr):
    current = arr
    list = None
    for i in range(0,len(arr)):
        list = {'data':arr[i],'rest':list}
    return list

print(array_to_list(array))