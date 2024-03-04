input = [("akash", 10), ("gaurav", 12), ("anand", 14),
         ("suraj", 20), ("akhil", 25), ("ashish", 30)]
final={}
for i in input:
    for x,y in enumerate(input):
        final[y[0]]=[]
        final[y[0]].append(y[1])

print(final)