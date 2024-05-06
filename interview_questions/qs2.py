"""
palindrom number
"""
def palindrom_number(n):
    rev_n=0
    temp= n
    while temp>0:
        digit= temp%10
        rev_n= rev_n* 10 + digit
        temp= temp//10
    if rev_n== n:
        return True
    else:
        return False
n=141
print(palindrom_number(n))
