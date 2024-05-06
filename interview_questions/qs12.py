from collections import defaultdict

list1=[{'name':'Rohan', 'location':'l1'},
       {'name':'Mohan', 'location':'l2'},
       {'name':'Nitin', 'location':'l1'},
       {'name':'Arjun', 'location':'l3'},
       {'name':'Mohan', 'location':'l2'}]

d=defaultdict(list)
for item in list1:
  d[item['location']].append(item)

print(dict(d))
