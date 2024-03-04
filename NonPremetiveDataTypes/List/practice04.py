# Python | Program to print duplicates from a list of integers
from collections import Counter
list_ = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

unique=[]
duplicate=[]
for i in list_:
    if i not in unique:
        unique.append(i)
    elif i not in duplicate:
        duplicate.append(i)

# print(unique)
# print(duplicate)

u=[]
d=[]
for j in list_:
    if list_.count(j)==1:
        u.append(j)
    else:
        d.append(j)
# print(u)
# print(set(d))


enumerate_=set([x for z,x in enumerate(list_) if list_.count(x)>1])
print(list(enumerate_))