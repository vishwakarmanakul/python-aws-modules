# Python3 program for removing i-th
# indexed character from a string
string='geek'
i=3
string=string.replace(string[i],'')
print(string)

str='geeksforgeeks'
n=5
s=list(str)
s.pop(n)
new_str=''.join(s)
print(new_str)
