test_dict = {'c': [3], 'b': [12, 10], 'a': [19, 4]}
s=list(test_dict.keys())
s.sort()
sorted_dict={i:test_dict[i] for i in s}
# print(sorted_dict)

#sort by values
d={i: sorted(sorted_dict[i]) for i in sorted_dict.keys()}
print(d)

