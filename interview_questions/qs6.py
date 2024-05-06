a='aaghacsckysvsvkvksvkvskkus'
ch={}
for i in a:
    ch[i]= ch.get(i,0)+1
result= min(ch.items(), key= lambda x:x[1])
print(ch)
print(result)

#  sort by values
sorted=sorted(ch.items(), key= lambda x:x[1])
print(dict(sorted))