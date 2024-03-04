mylist=['geeks','for','geeks']
temp_list=[]
for ele in mylist:
    if ele not in temp_list:
        temp_list.append(ele)
print(temp_list)