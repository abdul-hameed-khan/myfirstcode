
def square(a):
    # """this function will take a num and returns its square"""
    '''this function will take a num and returns its square''' # doc string ,,we can use both single or double quotes

    return a**2

print(square(4))

print(square.__doc__) # this function will take a num and returns its square

print(help(sum))  

# Help on built-in function sum in module builtins:

# sum(iterable, /, start=0)
#     Return the sum of a 'start' value (default: 0) plus an iterable of numbers

#     When the iterable is empty, return the start value.
#     This function is intended specifically for use with numeric values and may
#     reject non-numeric types.

# None

print(help(square))

# Help on function square in module __main__:

# square(a)
#     this function will take a num and returns its square

# None