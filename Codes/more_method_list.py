# COUNT() METHOD

num = [1,5,6,8,2,4,1,6,5,7,9]
print(num.count(5))

# SORT() METHOD

num = [1,5,6,8,2,4,1,6,5,7,9]
num.sort()
print(num)


# SORTED FUCTION

num = [1,5,6,8,2,4,1,6,5,7,9]
print(sorted(num))
print(num)

# CLEAR() METHOD

num = [1,5,6,8,2,4,1,6,5,7,9]
num.clear()
print(num)

# COPY() METHOD

num = [1,5,6,8,2,4,1,6,5,7,9]
n = num.copy()
print(n)

# REVERSE() METHOD

num = [1,5,6,8,2,4,1,6,5,7,9]
num.reverse()
print(num)

# INDEX() METHOD

num = [1,5,6,8,2,4,1,6,5,7,9,5,2,9,5]

print(num.index(5)) # 1
print(num.index(5,3)) # 8
print(num.index(5,9,-2)) # 11

# OUTPUTS
# 2
# [1, 1, 2, 4, 5, 5, 6, 6, 7, 8, 9]
# [1, 1, 2, 4, 5, 5, 6, 6, 7, 8, 9]
# [1, 5, 6, 8, 2, 4, 1, 6, 5, 7, 9]
# []
# [1, 5, 6, 8, 2, 4, 1, 6, 5, 7, 9]
# [9, 7, 5, 6, 1, 4, 2, 8, 6, 5, 1]

# MIN AND MAX FUNCTIONS

numb = [2,50,41,20,9,6,100]
print(min(numb))
print(max(numb))
