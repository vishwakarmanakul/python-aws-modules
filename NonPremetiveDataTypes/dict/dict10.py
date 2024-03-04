from collections import Counter
str = 'geeksforgeeks'
a= Counter(str)
c={i:j for i, j in a.items() if j==1}
list_ = ''.join(c.keys())
try:

    input_ = int(input('Enter the kth word:'))
    if input_ <= len(list_):
        print(list_[input_-1])
    else:
        print('index out of range')
except Exception as e:
    print(e)

