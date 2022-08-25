
# l = [1,2,2,2,3,4,4,5,6,6,6,7]
# print(l)

# s2 = set(l)
# print(s2) # {1, 2, 3, 4, 5, 6, 7} set

# l2 = list(set(l))
# print(l2) # [1, 2, 3, 4, 5, 6, 7] list

s = {1,2,3,4}
print(s)

# s.add(5)
# s.add(6)
# s.add(5)
# print(s) # {1, 2, 3, 4, 5, 6} not included 5 again

# s.remove(4)
# print(s)

# # s.remove(5) key error 5

# s.discard(5) # WILL NOT GIVE ERROR 
# print(s)

# # s.clear() # will clear the set

# s3 = s.copy()
# print(s3)

# CHAecking item
if 2 in s:
    print('present')
else:
    print('not present')

# loop in set
for i in s:
    print(i)

# set is used for mathematical operations union and intersection
s1 = { 1,2,3,4}
s2 = {3,4,5,6}

print(s1 | s2) # {1, 2, 3, 4, 5, 6}
print(s1 & s2)  # {3, 4}

