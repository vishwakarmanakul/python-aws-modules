#swap elements
list=[23,65,19,90]
pos1=1
pos2=3
# list[pos1], list[pos2] = list[pos2],list[pos1]
# print(list)

first_ele= list.pop(pos1)
second_ele= list.pop(pos2-1)
list.insert(pos1,second_ele)
list.insert(pos2,first_ele)
print(list)