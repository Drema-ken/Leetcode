def two_sums(num,target):
   n = len(num)
   for i in range(n -1):
      for j in range(i+1,n):#for next index of i to length of list but not including
         if num[i] + num[j] == target:
            return [i,j]
   return [] 

print(two_sums([1,2,3],5))