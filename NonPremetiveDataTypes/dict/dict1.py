from collections import Counter
dict= {'gfg': [5, 6, 7, 8], 'is': [10, 11, 7, 5], 'best': [6, 12, 10, 8], 'for': [1, 2, 5]}
unique_values=[]
# counter=Counter(dict)
for i, j in dict.items():
    unique_values.extend(j)
print(set(unique_values))
a=sorted({ele for i in dict.values() for ele in i})
print(list(a))