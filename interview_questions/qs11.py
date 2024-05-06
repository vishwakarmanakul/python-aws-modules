# sort
l=[1,3,2,5,3,1,6,8,3,4]
n=len(l)
for i in range(n):
    for j in range(i+1,n):
        if (l[i]>l[j]):
            l[i],l[j]=l[j],l[i]
print(l)