list1 = [1, 2, 5, 6]
tuple_list=[(i,i**3)for i in list1]
map_fun=list(map(lambda x: (x,x**3),list1))
print(map_fun)