from collections import Counter
input =  {'Gfg' : 1, 'is' : 2, 'Best' : 3}
a= list(input.keys())
b=list(input.values())
a.extend(b)
print(a)
