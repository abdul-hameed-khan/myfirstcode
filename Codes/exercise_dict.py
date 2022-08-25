# # input a number and the cube from 1 to number

# def cube_finder(n):
#     d = {}
#     for i in range(1,n+1):
#         d[i] = i**3
#     return d

# n = int(input('enter a number for cube range : '))
# print(cube_finder(n))

# storing user data in dict 
user = {}
user['name'] = input('plz enter your name : ')
user['age'] = int(input('plz enter your age : '))
user['hobbies']  = input('plz enter your hobbies separated by comma : ').split(',')
user['goals'] = input('plz enter your life goals separated by comma : ').split(',')

for i,j in user.items():
    print(i +'-->'+str(j))
    print()
