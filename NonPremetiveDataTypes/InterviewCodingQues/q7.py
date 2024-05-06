data_list=[12,14,22,32,45,5,34,12,44,67]
new_list=[]
while data_list:
    maximum = data_list[0]
    for item in data_list:
        if item>maximum:
            maximum=item
    new_list.append(maximum)
    data_list.remove(maximum)
print(new_list)