str_=" geeks quiz practice code"
str_split=str_.split()[::-1]
new_str=''
for ele in str_split:
    new_str+=ele
    new_str+=' '
# print(new_str)

words=str_.split()
a=' '.join(reversed(words))
# print(a)

stack=str_.split()
j=[]
while stack:
    j.append(stack.pop())
reversed_str=' '.join(j)
print(reversed_str)