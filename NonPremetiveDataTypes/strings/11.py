string = "Geeks$For$Geeks"
split_st= string.split()
special_char= "[@_!#$%^&*()<>?/\|}{~:]"
c=0
for ele in string:
    if ele in special_char:
        c+=1
print(c)
if c:
    print('string is not accepted')
else:
    print('str is accepted')


