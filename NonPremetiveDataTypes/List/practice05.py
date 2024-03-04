# Python program to find Cumulative sum of a list
list_ = [10, 20, 30, 40, 50]
cumulative_sum=[]
count=1
for ele in range(len(list_)+1):
    cumulative_sum.append(sum(list_[0:ele]))
    ele+=1
print(cumulative_sum[1:])

#---------------------------------------
#2nd approch
j=0
cum=[]
for ele in range(len(list_)):
    j+=list_[ele]
    cum.append(j)
print(cum)



