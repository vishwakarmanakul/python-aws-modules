# max num
list_=[2,1,-1,5,3,4]
max=list_[0]
a=len(list_)
for i in range(1,a):
    if list_[i]<max:
        max=list_[i]
print(max)