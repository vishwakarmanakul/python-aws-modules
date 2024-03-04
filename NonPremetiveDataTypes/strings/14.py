# Python program to split and join a string
list_=  ['Geeks', 'for', 'Geeks','okay','python']
a='-'.join(list_)
print(a)

b=''
s=len(list_)-1
for i in range(len(list_)):
   b+=list_[i]
   if i==s:
       break
   b += '-'
print(b)