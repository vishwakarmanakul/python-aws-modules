arr = [1, 2, 3, 4, 5, 6, 7]
first= 0
last= len(arr)-1
for i in range(len(arr)):
    if first < last:
        temp= arr[first]
        arr[first]= arr[last]
        arr[last]= temp
        first+=1
        last-=1
print(arr)