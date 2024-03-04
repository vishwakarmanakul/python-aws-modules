# Clonning of list
def cloning_list(input):
    li2 = li1[:]
    return li2
li1 = [4,4, 8, 2,2, 10, 15, 18]
print(cloning_list(li1))

# --------------------
import copy
list2=li1.copy()
a=f'This is clonning of list {list2}' #fstring
b='This is clonning of list :{}'.format(list2) #string format
print(a)
print(b)