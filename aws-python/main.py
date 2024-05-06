a=['a','b','c',1,4,'d',1.2, '6','7']
x= filter(lambda x: x if type(x)==int, a)
print(list(x))