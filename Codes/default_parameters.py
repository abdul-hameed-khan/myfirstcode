def printing(f_name,l_name,age):
    print(f'your first name is {f_name}')
    print(f'your last name is {l_name}')
    print(f'your age is {age}')

printing('hameed','khan',20)

# the upper program will work correctly

# def printing(f_name,l_name,age):
#     print(f'your first name is {f_name}')
#     print(f'your last name is {l_name}')
#     print(f'your age is {age}')

# printing('hameed','khan') #TypeError: printing() missing 1 required positional argument: 'age'

# def printing(f_name,l_name,age = 20):
#     print(f'your first name is {f_name}')
#     print(f'your last name is {l_name}')
#     print(f'your age is {age}')

# printing('hameed','khan') # now age is default 20

# def printing(f_name,l_name = 'unknown',age = 20):
#     print(f'your first name is {f_name}')
#     print(f'your last name is {l_name}')
#     print(f'your age is {age}')

# printing('hameed') # will run corrctly 

# def printing(f_name,l_name='unknown' ,age):
#     print(f'your first name is {f_name}')
#     print(f'your last name is {l_name}')
#     print(f'your age is {age}')

# printing('hameed',20) #SyntaxError: non-default argument follows default argument

# def printing(f_name = 'unknown',l_name='unknown' ,age = None):
#     print(f'your first name is {f_name}')
#     print(f'your last name is {l_name}')
#     print(f'your age is {age}')

# printing() # Will run correctly