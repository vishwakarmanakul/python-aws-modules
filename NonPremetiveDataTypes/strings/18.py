s = "GeeksforGeeks"
print(s[-2:])
a= int(input('Enter the number:'))
rotate_input=input('Enter the direction:')
rotation=['right','left']
if rotate_input==rotation[0]:
    print(s[-a:]+s[0:-a])
    
elif rotate_input==rotation[1]:
    print(s[a:]+s[0:a])

else:
    print('N')