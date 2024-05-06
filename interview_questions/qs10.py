def odd_filter_fun(n):
    return n%2!=0

n=[1,2,3,4,5,6,7,8,9,10]
a= filter(odd_filter_fun, n)
print(list(a))