# FROMKEYS METHOD
# it will generate the keys which you desire and give the same value to each key

# d1 = dict.fromkeys(['name','age','uni'], 'unknown') 
# print(d1) # {'name': 'unknown', 'age': 'unknown', 'uni': 'unknown'}

# d2 = dict.fromkeys(('name','age','uni'), 'unknown') 
# print(d2) #  {'name': 'unknown', 'age': 'unknown', 'uni': 'unknown'}

# d3 = dict.fromkeys('abc', 'unknown') 
# print(d3) # {'a': 'unknown', 'b': 'unknown', 'c': 'unknown'}

# d4 = dict.fromkeys(range(1,6), 'unknown') 
# print(d4) # {1: 'unknown', 2: 'unknown', 3: 'unknown', 4: 'unknown', 5: 'unknown'}

# d5 = dict.fromkeys(['name','age','uni'], ['unknwn','unknown']) 
# print(d5) # {'name': ['unknwn', 'unknown'], 'age': ['unknwn', 'unknown'], 'uni': ['unknwn', 'unknown']}

# GET METHOD for accessing key

user1 = {
    'name' : 'hamed khan',
    'age' :20,
    'adres': ['mirpur','atd'],
    'age': 19
}

print(user1) # {'name': 'hamed khan', 'age': 19, 'adres': ['mirpur', 'atd']} it overright the age with last key age

print(user1.get('name'))
print(user1.get('names')) # None
print(user1.get('names','not found')) # not found

if user1.get('name'):
    print('present')
else:
    print('not present')

# CLEAR METHOD

# user1.clear() # will delete the whole dict
# print(user1)

# copy method

d = user1.copy() # will copy the dict
print(d)