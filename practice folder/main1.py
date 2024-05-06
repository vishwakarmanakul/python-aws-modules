# reverse the string
str_="geeks quiz practice code"
split_str= str_.split()
reversed=''
while split_str:
    reversed+= split_str.pop()
    reversed += ' '
print(reversed)