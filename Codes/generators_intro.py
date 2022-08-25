# we use generators when we only need it only one time

def num(n):
    for i in range(1,n+2):
        yield i**2

k = num(9)

for i in k:
    print(i)


for i in k:
    print(i)
    # this for loop will not print the print the numbers because the generator create the numbers only when it is needed 
    # and it generate the numbers only once

# exercise 

def even(n):
    # yield [i for i in range(1,n+1)  if (i%2 == 0)] # or
    yield [i for i in range(2,n+1,2)]


p = even(10)

for i in p:
    print(i)


# list vs generators

# import time

# t = time.time()

# l = [i for i in range(100000000)]

# print(time.time()-t)

# t = time.time()

# g = (i for i in range(100000000))

# print(time.time()-t)
