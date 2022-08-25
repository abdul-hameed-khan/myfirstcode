# SPLIT() METHOD

user = 'hameed 20'.split()
print(user) # ['hameed', '20']

user = 'hameed khan,20'.split(',')
print(user) # ['hameed 20']

name , age = 'hameed khan,20'.split(',')
print(name)
print(age)

# JOIN() METHOD
# opposite of split()

user = ['hameed', '20']
print(' '.join(user)) # hameed 20
print(','.join(user)) # hameed,20
