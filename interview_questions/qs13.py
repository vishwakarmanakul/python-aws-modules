"""
output : 20a1b1c2d3e5f8
"""
s='abcdef'
fib0=[1,1,2,3,5,8]
sum=0
for i in fib0:
    sum+=i
sum=str(sum)
for i in range(len(s)):
    sum+=s[i]+str(fib0[i])
print(sum)
