def selection_sort(list):
    sorted_list = []
    for i in range(0,len(list)):
      index_to_move = index_of_min(list)
      sorted_list.append(list.pop(index_to_move))
    return sorted_list

def index_of_min(values):
   min_index = 0 
   for i in range(1,len(values)):
      if values[i] < values[min_index]:
         min_index =  i
   return min_index


print(selection_sort([2,3,1,4]))
