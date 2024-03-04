str1 = 'aabcddekll12@'
str2 = 'bb22ll@55k'
common_elements=''

for ele in str1:
    if ele in str2:
        common_elements+=ele
print(set(common_elements))