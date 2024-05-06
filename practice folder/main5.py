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
print(obj.palindrom(len(a)-1))


def palindrom(n):
    a= len(n)
    for i in range(len(n)):
        if n[i]!= n[a-i-1]:
            print(n[i],'-',n[a-i-1])
            print(i,'-',a-i-1)
    return True
x='palindrom'
print(palindrom(x))