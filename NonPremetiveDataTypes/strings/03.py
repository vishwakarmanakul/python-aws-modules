from collections import Counter
test_str = 'Gfg is best'
boto= test_str.split()
dict={}
for i in boto:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
# print(dict)

res={i: test_str.count(i) for i in test_str.split()}
print(res)