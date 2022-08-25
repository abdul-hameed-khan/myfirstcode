# it takes multiple arguments

def total(*args):
    sum = 0 
    for i in args:
        sum += i
    return sum

print(total(1,3,2,4))

# with normal argument

# def total2(num,*args):
#     sum = 0 
#     print(num) # 3 
#     for i in args:
#         sum += i
#     return sum
# # but if you write num after *args then it will give error
# print(total2(3,3,2,4))


# list as an parameter to *args 

def total3(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

nums = [3,3,2,4]
print(total3(*nums)) # * will unpack the list and also tuple

