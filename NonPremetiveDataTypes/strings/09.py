string = "geeksforgeeks"
unique_ = ''
for ele in string:
    if ele in unique_:
        pass
    else:
        unique_+=ele
print(unique_)