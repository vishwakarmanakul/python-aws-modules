string = 'My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of https://www.geeksforgeeks.org/'
a=string.split()
link=''
for i in a:
    if i.startswith('http:') or i.startswith('https:'):
        link+=i
print(link)