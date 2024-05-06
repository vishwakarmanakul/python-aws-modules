lst = [10, 11, 12, 13, 14, 15]
reversed_list=[]
counter=len(lst)-1
for i in range(len(lst)):
    reversed_list.insert(lst[i], lst[counter])
    counter-=1
print(reversed_list)