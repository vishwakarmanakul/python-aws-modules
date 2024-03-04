# Remove the empty lists from the dataset
test_list = [5, 6, [], 3, [], [], 9]
new_list=[]
for i in test_list:
    if i!=[]:
        new_list.append(i)
print(new_list)

# ----------
test_list = [5, 6, [], 3, [], [], 9]
a=list(map(str, test_list))
b=''.join(a)
c=b.replace('[]','')
final_list= list(map(str,c))
print(final_list)

# ----------

list_comp= [ele for ele in test_list if ele!=[]]
print(list_comp)


