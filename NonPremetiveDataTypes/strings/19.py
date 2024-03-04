a= 'geeksforgeeeks'
duplicate_elements= set()
for i in a:
    if a.count(i)>1:
        duplicate_elements.add(i)
print(duplicate_elements)