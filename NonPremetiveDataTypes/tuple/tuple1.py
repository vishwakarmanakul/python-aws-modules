test_tup = (5, 20, 3, 7, 6, 8)
print('The original tuple is :', test_tup)
K=2
test_list=list(sorted(test_tup))
new_list=[]
for idx, val in enumerate(test_list):
    if idx<K or idx>=(len(test_list)-K):
        new_list.append(val)
print(new_list)