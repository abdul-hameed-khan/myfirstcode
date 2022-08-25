# REDUCE THE LENGTH OF THE CODE

l = [i**2 for i in range(1,11)] 
print(l) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

l2 = [-i for i in range(1,11)]
print(l2) # [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]

name = ['Abdul','Hameed','Khan']
print([n[0] for n in name]) # ['A', 'H', 'K']

l = ['abc','tuv','xyz']
print([i[::-1] for i in l]) # ['cba', 'vut', 'zyx']

# list comprehension with if statement

print([i for i in range(1,11) if i%2 == 0]) # [2, 4, 6, 8, 10]
print([i for i in range(1,11) if i%2 != 0]) # [1, 3, 5, 7, 9]

def num_to_string(l):
    return [str(numbers) for numbers in l if (type(numbers) == float or  type(numbers) == int)]

print(num_to_string(['false','true',[1,2,3],1,1.0,12,3.4])) # ['1', '1.0', '12', '3.4']

# list comprehension with if-else statement

print([-i if (i%2 != 0) else i*2 for i in range(1,11)]) # [-1, 4, -3, 8, -5, 12, -7, 16, -9, 20]

# creating nested list comprehension

print([[i for i in range(1,4)] for j in range(3)]) # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

lis = [[i**j for i in range(2,5)] for j in range(1,4)]
print(lis) #[[2, 3, 4], [4, 9, 16], [8, 27, 64]]

for i in range(len(lis)):
    for j in range(len(lis)):
        print(lis[j][i],end = '   ')
    print()

