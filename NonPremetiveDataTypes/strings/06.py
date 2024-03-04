_str_='okay this is a string in which we have the i alphabet'
split_str =_str_.split()
res = filter(lambda x:'i' in x,split_str)
print(list(res))

res_2=map(lambda x: x, split_str)
print(list(res_2))