"""
palindrom string
"""

class Palindrom:
    def __init__(self, str_):
        self.str_= str_

    def palindrom(self, c):
        palindrom_str=''
        for i in range(len(self.str_)):
            palindrom_str+=self.str_[c]
            c-=1

        if self.str_== palindrom_str:
            return 'Yes!! it is a palindrom string'
        else:
            return 'not a palindrom string'
a= 'lool'
obj= Palindrom(a)
# print(obj.palindrom(len(a)-1))

# -----------------------------------------------------------------------------------------------------

def palindrom(n):
    a= len(n)
    for i in range(len(n)):
        if n[i]!= n[a-i-1]:
            break
        print('not a palindrom string')
    else:
        print('palindrom')
x='looll'
print(palindrom(x))

# -----------------------------------------------------------------------------------------------------

def palindrom_string(string):
    left=0
    right=len(string)-1
    st= True
    for i in range(len(string)//2):
        if string[left]!= string[right]:
            st=False
            left+=1
            right-=1
    if st:
        print('palindrom')
    else:
        print('not a palindrom')
number= 'cooc'
palindrom_string(number)