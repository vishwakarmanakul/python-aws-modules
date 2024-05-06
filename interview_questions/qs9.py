# print the pair whose sum=6 from the list
a=[3,1,5,2,0,1,3,5,0,9]
k=6
n=len(a)
for i in range(n):
    for j in range(i+1,n):
        if (a[i]+a[j])==k:
            print(a[i],a[j])
