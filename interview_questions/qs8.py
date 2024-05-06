# sort the tuple
l=(('a',12),('b',2),('c',34),('d',23))
a=sorted(dict(l).items(), key=lambda x:x[1])
print(a)

# reverse the dictionary
x=dict(l).items()
print(list(x)[::-1])