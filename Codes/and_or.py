name = input('plz enter your name\n')
age = input('enter your age\n')
age = int(age)
n = name[0] # you can also change the user name into small letters using lower method
if (n == 'a' or n == 'A') and age > 10:
    print('you can watch this movie')
else:
    print('you can\'t watch this movie\n')
