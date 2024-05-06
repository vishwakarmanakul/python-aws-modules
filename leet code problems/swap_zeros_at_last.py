def swaping_two_zeros(l,len_lst, prev):
    for i in range(len_lst):
        if l[i]!=0:
            l[prev], l[i]= l[i], l[prev]
            prev+=1
    return lst
lst=[1,3,6,0,2,0,5,6,8]
len_list=len(lst)
prev=0
print(swaping_two_zeros(lst, len_list, prev))

