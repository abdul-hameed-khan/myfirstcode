# all() --- returns true if all are evens in the list num
# any() --- returns true if there exists anyeven in num2

num = [2,4,6,8]
num2  = [1,3,5,2,7]

print(all([i % 2 == 0 for i in num])) # True bcz all are even nums

print(any([i % 2 == 0 for i in num2])) # # True bcz 2 is even in num2

# func of total with error like passing string or list ...and handling it with all func

def total(*num):
    if (all([type(arg) == int or type(arg) == float for arg in num])):
        t = 0
        for i in num:
            t += i
        return t
    else: 
        return 'wrong input'

print(total(1,2,3,4,5))
# print(total(1,2,3,4,5,'hameed')) # wrong input bcz of string