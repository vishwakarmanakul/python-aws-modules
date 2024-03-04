def fibonnaci(n):
    if n==0: return 0
    elif n==1 : return 1
    else:
        return fibonnaci(n-1)+fibonnaci(n-2)
for i in range(12):
    print(fibonnaci(i))