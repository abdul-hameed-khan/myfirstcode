# def last_char(name):
#     return name[-1]
# name = 'hameed'
# print(last_char(name)) # will print last char of a string

def even_odd(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"
num = int(input('enter any number to check even or odd : '))
print(even_odd(num))

# the upper and lower both fuction will return the same output (line 6 & line 14)

# def even_odd(n):
#     if n % 2 == 0:
#         return "even"
#     return "odd"

# num = int(input('enter any number to check even or odd : '))
# print(even_odd(num))

# one more way

# def is_even(n):
#     return n % 2 == 0
# num = int(input('enter a number to check even : '))
# print(is_even(num)) # this will return in true or false

# def is_even(n):
#     if n % 2 == 0:
#         return True
# num = int(input('enter a number to check even : '))
# print(is_even(num)) # this will also return in true or none



# more about functions

def square(a):
    return a**2

s = square
print(s(3)) # 9

print(s.__name__) # square
print(square.__name__) # square