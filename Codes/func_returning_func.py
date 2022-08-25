# they are also called closures or first class function

def outer_f2(msg):
    def inner_f2():
        print(f"I am inner functiion dude! {msg} ")
    return inner_f2

outer_f2('hi hello')()

# or

# def func(msg):
#     print (f"{msg} how are you")


# a = func("Hello")
# print(a)

 
# doing cube and square with same function using closures

def to_power(x):
    def cal_power(n):
        return n**x
    return cal_power

cube = to_power(3)
print(cube(2)) # 8

square = to_power(2)
print(square(7)) # 49

