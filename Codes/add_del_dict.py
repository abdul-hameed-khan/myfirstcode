user = {
    'name' : 'hamed khan',
    'age' :20,
    'adres': ['mirpur','atd'],
}

# ADD DATA

user['uni'] = 'comsats'
user['dept'] = ['BS','CS','IT']
print(user)

# DEL DATA

# d = user.pop('adres') # it returns the value of deletd key
# print(user)
# print(d) # ['mirpur', 'atd']

# DELETING LAST ITEM

p  = user.popitem() 
print(p) # ('dept', ['BS', 'CS', 'IT'])
print(user) 

# UPDATE METHOD

user2= {'subj': 'CS','lang': 'python','level': 'intermediate'}
# user2= {'name': 'A.HAMEED KHAN','subj': 'CS','lang': 'python','level': 'intermediate'} # this will replace the this name with other name
user.update(user2)
# user.update({}) # this will add nothing to other dict and doesnot change the other dict
print(user) # this will add the other dict to it

