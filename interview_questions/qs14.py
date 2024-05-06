"""
Find the three sum : A = [1, 4, 45, 6, 10, 8]
sum = 22
output = Triplet is 4, 10, 8
"""
a = [1, 4, 45, 6, 10, 8]
s=22
len_arr=len(a)
match_found=False
for i in range(len_arr):
    for j in range(i+1, len_arr):
        for k in range(j+1, len_arr):
            if a[i]+a[j]+a[k]==s:
                print(a[i],a[j], a[k])
                match_found =True
                break
if not match_found:
    print('not found')