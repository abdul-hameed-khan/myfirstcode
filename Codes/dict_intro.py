user1 = {
    'name' : 'hamed khan',
    'age' :20,
    'adres': ['mirpur','atd']
}
print(user1)
print(user1['name'])


# nested dict

users = {
    'user2' :{
    'name' : 'hamed khan',
    'age' :20,
    'adres': ['mirpur','atd']
    },
    'user3' : {
    'name' : 'jadoon',
    'age' :20,
    'adres': ['mirpur','atd']
    },
    }
# looping in dictionaries with items metheod

for i, j in users.items():
    for k , l in j.items():
        print(str(k)+'-->'+str(l))
# print(users)
print(users['user2'])

# in keyword in dict

user1 = {
    'name' : 'hameed khan',
    'age' :20,
    'adres': ['mirpur','atd']
}

print('name' in user1)
if 'age' in user1:
    print('present')
else:
    print('not present')



# outputs
'''
{'name': 'hamed khan', 'age': 20, 'adres': ['mirpur', 'atd']}
hamed khan
name-->hamed khan
age-->20
adres-->['mirpur', 'atd']
name-->jadoon
age-->20
adres-->['mirpur', 'atd']
{'name': 'hamed khan', 'age': 20, 'adres': ['mirpur', 'atd']}
True
present
'''