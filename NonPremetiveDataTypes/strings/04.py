# Find the len of string, avoid the spaces
Input = 'hello world !'
i=Input.replace(' ','')
# print(len(i))
len_str=0
for ele in Input:
    if ele==' ':
        pass
    else:
        len_str+=1
print(len_str)