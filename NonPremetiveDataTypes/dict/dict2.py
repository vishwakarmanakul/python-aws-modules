from operator import itemgetter
list_ = [{"name": "Nandini", "age": 14},
       {"name": "Manjeet", "age": 25},
       {"name": "Nikhil", "age": 11},
       {"name": "Rahul", "age": 34}]

print(sorted(list_, key=lambda x:x['age']))
print(sorted(list_, key=itemgetter('age'), reverse=True))

dict={'nakul':12,'rohit':11,'manish':45,'akshay':34}
print(sorted(dict.items(), key=lambda item:item[1]))
