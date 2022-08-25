# def decorators(fun):
#     def inner_fun(*args, **kwargs):
#         print('hello world ')
#         return  fun(*args, **kwargs)
#     return inner_fun

# def func(a):
#     print(f"how are you {a}")
# decorator = decorators(func)
# decorator(7)

# def func1(a, b):
#     return a+b
# decorator =decorators(func1)
# print(decorator(2, 5))

# 2 


def deco(func):
    def wrapper(*args,**kwargs):
        print("assum function")
        return func(*args,**kwargs)
    return wrapper

@deco
def add(a,b):
    return a+b

print(add(1,2))

@deco
def test():
    print("you are correct")

test()

