def sum(numbers):
    if not len(numbers):
        return 0
    remaining_sum = sum(numbers[1:])
    return  numbers[0] + remaining_sum 
print(sum([1,2,3]))