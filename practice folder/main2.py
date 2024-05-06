# Remove numbers From a String in Python
a='Geeks123For123Gee22322222ks'
alpha=''
for i in a:
    if i.isalpha():
        alpha+=i
print(alpha)