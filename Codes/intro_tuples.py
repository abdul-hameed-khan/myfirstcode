nums = (1,2,0,3,4.0)

words = ('Abdul','Hameed','Khan')
for i in words:
    print(i)

# Abdul
# Hameed
# Khan

num = (1)
print(type(num)) # <class 'int'> not a tuple

nu = (1,)
print(type(nu)) # <class 'tuple'>

# TUPLE UNPACKING

word = ('Abdul','Hameed','Khan')
fname,mname,lname = (word)
print(fname)
print(mname)
print(lname)
# Abdul
# Hameed
# Khan
# LIST INSIDE TUPLE

# You can apply list functions in list inside the tuple

wordz = ('Abdul','Hameed','Khan',[1,2,3,4])
print(wordz)
wordz[3].pop()
wordz[3].append(5)
print(wordz) # ('Abdul', 'Hameed', 'Khan', [1, 2, 3, 5])

# TUPLE METHODS

print(min(wordz[3]))
print(min(nums))
print(max(nums))
print(sum(nums))
print(len(nums))
# 1
# 0
# 4.0
# 10.0

# STR , TUPLE  , LIST

num = tuple(range(1,11))
print(num)

lis = list(range(1,11))
print(lis)
# (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nums = str(num)
print(nums)
print(type(nums))
# (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# <class 'str'>

num_list = str(lis)
print(num_list)
print(type(num_list))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# <class 'str'>
