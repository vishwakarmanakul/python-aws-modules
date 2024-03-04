"""
Write a python program to convert two lists into a dictionary
"""
list1=['Naina','Kimi','Sheena']
list2=[53653,52762,65267]
a=0
dicts={}
for i in list1:
    dicts[i]=list2[a]
    a+=1
print(dicts)
for i in dicts.items():
    print(i)