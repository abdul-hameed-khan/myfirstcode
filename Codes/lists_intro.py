numbers = [1,6,9]
print(numbers) # 1, 6, 9]

numbers[1]=5
print(numbers) # [1, 5, 9]

words = ['hamedd','khan',"jadoon",'mirpur']
print(words) # ['hamedd', 'khan', 'jadoon', 'mirpur']

words[2] = 'khan'
print(words) # ['hamedd', 'khan', 'khan', 'mirpur']

words[1:] = ['hami','c','code',5]
print(words) # ['hamedd', 'hami', 'c', 'code', 5]

mixed = [1,2,'khan',8,None]
print(mixed) # [1, 2, 'khan', 8, None]

mixed[1:]= 'four'
print(mixed) # [1, 'f', 'o', 'u', 'r']


# ANOTHER METHOD TO MAKE a LISTS WITH RANGE FUCNTION

numb = list(range(1,11))
print(numb) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# LOOPING IN LISTS

numb1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numb1:
    print(i)

i = 0
while i < len(numb1):
    print(i)
    i+= 1

# output of looping
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# PASSING LIST TO A FUNCTION

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative

print(negative_list(n)) # [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]