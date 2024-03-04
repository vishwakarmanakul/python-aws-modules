array=[3,4,5,7,8,9,19,11]
target=173
found= False
for i in range(len(array)):
    for j in range(i+1, len(array)):
        if array[i]+array[j]==target:
            print(f'the numbers are {array[i], array[j]}')
            found = True
            break
if not found:
    print('no such pair')
