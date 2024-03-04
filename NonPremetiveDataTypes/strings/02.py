# Remove numbers From a String in Python
a='Geeks123For123Gee22322222ks'
new_str=''
for ele in a:
    if not ele.isdigit():
        new_str+=ele
print(new_str)