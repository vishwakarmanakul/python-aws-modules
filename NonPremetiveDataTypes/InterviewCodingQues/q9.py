def palindrom(s):
    a=''.join(reversed(s))
    if s==a:
        return 'palindrom'
    return 'not palindrom'
string='nona'
a = palindrom(string)
print(a)