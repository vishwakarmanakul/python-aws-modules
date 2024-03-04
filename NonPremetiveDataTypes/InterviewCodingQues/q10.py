string=['a','b','x','x','z','w','q','b','a','t','t']
a=[]
dupliacates=[]
for i in string:
    if i not in a:
        a.append(i)
    else:
        dupliacates.append(i)
print(a)
print(dupliacates)
