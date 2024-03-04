myDict = {'ravi': 10, 'rajnish': 9,
          'sanjeev': 15, 'yash': 2, 'suraj': 32}
sort_keys=list(myDict.keys())
sort_keys.sort()
sorted_dict={}
for i in sort_keys:
    sorted_dict[i]=myDict[i]
print(sorted_dict)

a=sorted(myDict.items(), key=lambda x:x[1])
print(a)