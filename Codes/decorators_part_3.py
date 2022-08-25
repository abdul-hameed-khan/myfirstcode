from functools import wraps
# we are using it because we want to print the doc string of func which we has called

def deco(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        '''this is wrapper function'''
        print("assum function")
        return func(*args,**kwargs)
    return wrapper

@deco
def add(a,b):
    '''this is add function'''
    return a+b

print(add(1,2))
# print(add.__name__) # wrapper
# print(add.__doc__) #  this is wrapper function ..defore using wraps

# the error is that ..it is not printng the doc of add func but it is printing the doc of wrapper function

# now this error has been solved with wraps

print(add.__doc__) #  this is add function
print(add.__name__) # add
print()


# decorators practice


def print_function_data(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"you are calling {function.__name__} function")
        print(f"{function.__doc__}")
        return function(*args, **kwargs)
    return wrapper

@print_function_data
def addition(a,b):
    '''This function takes two numbers as arguments and return their sum '''
    return a+b
print(addition(4,5))

