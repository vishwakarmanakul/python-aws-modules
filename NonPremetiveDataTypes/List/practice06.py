# Python | Sum of number digits in List
test_list = [12, 67, 98, 34]
res=[]
for i in test_list:
    sum=0
    for j in str(i):
        sum+=int(j)
    res.append(sum)
# print(res)

# Reversed number and list
num=12345
n=''
for i in range(len(str(num))):
    s=num%10
    n+=str(s)
    num=num//10
# print(n)

# ------------------------------------

list_it=[1,2,3,4,5,6,7,8]
copy_data=list_it.copy()
n_list=[]
for ele in range(len(list_it)):
    n_list.append(list_it[-1])
    a=list_it.pop(-1)
print(n_list)
print(copy_data)



