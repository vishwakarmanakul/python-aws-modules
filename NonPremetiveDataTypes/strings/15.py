a = ['virat','mohit','sachin','rahane']
b = ['mohit','devraj','virat','kartik','himalay']
unique_names=[]
for i in a:
    if i not in b:
        unique_names.append(i)

for j in b:
    if j not in a:
        unique_names.append(j)
print(unique_names)



