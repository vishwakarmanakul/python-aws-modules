def prime_number(n):
    flag=False
    if n>1:
        for i in range(2,n):
            if n%i==0:
                flag=True
                break
        if flag == False:
            print('It is a prime number')
        else:
            print('Not a prime number')
# prime_number(2)

def prime_number_range(start, end):
    for n in range(start, end):
        if n>1:
            for i in range(2,n):
                if n%i==0:
                    break
            else:
                print(n)
prime_number_range(1,50)