# it increase(enhance) the functionality of an other fuction


# def decorator_func(any_func):
#     print("this is awesome function")
#     return any_func()

# @decorator_func
# def func1():
#     print("func1")

# def func2():
#     print("func2")

# var = decorator_func(func1)

# or 

def decorator_1(func):
    def wrapper_func():
        print("this is awesome function")
        func()
    return wrapper_func

@decorator_1

def func1():
    print("this is func one")
func1()

print()

@decorator_1
def func2():
    print('this is func two') 
func2()

# 3 

# def decorators(fun):
#     def inner_fun():
#         print('Hello World')
#         fun()
#     return inner_fun
# @decorators
# def func():
#     print('How are you')
# func()

# 4 

# def decorator_func(any_func):
#     print('this is awsome function')     
#     return any_func

# def func1():
#     print('this is func1')

# var = decorator_func(func1)
# var()

# 5


# def decorator(any_func):
#     print("This is your function")
#     any_func()
# @decorator
# def func():
#     print("Hy there")