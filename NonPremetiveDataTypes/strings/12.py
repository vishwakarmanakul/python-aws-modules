str = "hello geeks for geeks computer science portal"
k = 4
j=[]
for ele in str.split():
    if len(ele) >k:
        j.append(ele)

lam= filter(lambda x:(len(x)>k),str.split())
list_comprehension=[i for i in str.split() if len(i)>k]
print(list_comprehension)
print(list(lam))
