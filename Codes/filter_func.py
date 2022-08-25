# will filter the objects according to condition

num = list(range(1,11))
print(list(filter(lambda a: a%2 == 0,num))) # [2, 4, 6, 8, 10]

print(list(filter(lambda a: a%2 != 0,num))) # [1, 3, 5, 7, 9]

