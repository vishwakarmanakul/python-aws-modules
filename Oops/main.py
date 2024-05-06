# import time
from time import sleep

# def decorator(fuc):
#     def wrapper(*args):
#         try:
#             return fuc(*args)
#         except Exception :
#             print('Not divisible by 0')
#     return wrapper
# @decorator
# def main(x,y):
#     return x/y
# a=main(1,0)
# print(a)

def prime_numbers(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def main():
    i=0
    num=2
    while i<10:
        if prime_numbers(num):
            print(num)
            i+=1
        num+=1
main()