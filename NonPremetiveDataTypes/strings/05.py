# Python program to print even length words in a string
s = "This is a python language"
new_str=''
for i in s.split():
    if len(i)%2==0:
        new_str+=i
        new_str+=' '
# print(new_str)

a=s.split()
res=filter(lambda x:(len(x)%2==0),a)
a=list(res)
z=' '.join(a)
print(z)