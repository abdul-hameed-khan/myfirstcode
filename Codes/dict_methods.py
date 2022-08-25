user1 = {
    'name' : 'hamed khan',
    'age' :20,
    'adres': ['mirpur','atd']
}

# VALUES() METHOD

if 'hameed khan' in user1.values():
    print('present')
else:
    print('not present')

# print('hameed khan' in user1.values())

user_values = user1.values()
print(user_values) # dict_values(['hamed khan', 20, ['mirpur', 'atd']])

#checking of key exists in dict or not
# if 20 in user1.values():
#     print('present')
# else:
#     print('not present')

#checking of key existr in dict or not

if 'name' in user1:
    print('present')
else:
    print('not present')

# keys method

if 'age' in user1.keys():
    print('present')
else:
    print('not present')

user_keys = user1.keys()
print(user_keys) # dict_keys(['name', 'age', 'adres'])

# ITEMS METHOD
# loop for printing items kine by line

for i, j in user1.items():
    print( str(i) +"->"+str(j))
    # print(f'key is {i} and the value is {j}') # another way 
print()

user_items = user1.items()
print(user_items) # dict_items([('name', 'hamed khan'), ('age', 20), ('adres', ['mirpur', 'atd'])])

