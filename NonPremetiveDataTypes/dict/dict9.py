input = ['cat', 'dog', 'tac', 'god', 'act']
d={}
for i in input:
    key=''.join(sorted(i))
    if key in d.keys():
        d[key].append(i)
    else:
        d[key]=[]
        d[key].append(i)
z = [x for i, j in d.items() for x in j]
final_output=' '.join(z)

print(final_output)