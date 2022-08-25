def our_map(function , L):
    # return_list = []
    # for item,exponent in L:
    #     return_list.append(function(item , exponent))
    # return return_list
    return [function(item,exponent) for item,exponent in L] # with list conprehension

def power(item , exponent):
    return item**exponent

my_list = [
    [1,2],
    [8,2],
    [5,3],
    [4,4],
    [3,9],
    [2,8],
    [2,3],
]

print(our_map(power , my_list)) # [1, 64, 125, 256, 19683, 256, 8]

# one more example

l = [1,2,3,4]

def my_map(func,l):
    return [func(i) for i in l]

print(my_map(lambda a: a**2,l)) # [1, 4, 9, 16]
