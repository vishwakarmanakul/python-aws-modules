ask= 'geeiiiksfaorguueeks'
vowels=set('aeiou')
a=''
for char in ask:
    if char in vowels:
        a+=char
if len(set(a))==len(vowels):
    print('all vowels are present')
else:
    print('not present')


