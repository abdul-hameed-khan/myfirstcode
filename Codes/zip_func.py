user_id = ['user1','user2','user3']
names = ['Abdul','hameed','khan']

print(dict(zip(user_id,names))) # {'user1': 'Abdul', 'user2': 'hameed', 'user3': 'khan'}

# will converting again to 2 different lists
l = list(zip(user_id,names))

l1,l2 = zip(*l) # * will unpack the list
print(list(l1)) # ['user1', 'user2', 'user3']
print(list(l2)) # ['Abdul', 'hameed', 'khan']

n1 = list(range(1,6))
n2 = list(range(6,11))

# finding max numbers in both lists
n = []
for i in zip(n1,n2):
    n.append(max(i))

print(n) # [6, 7, 8, 9, 10] bcz it compares the largest element in both lists

# zip with lambda to find average of numbers 

li1 = [1,2,3]
li2 = [4,5,6]

fun = lambda *args : [sum(i)/len(i) for i in zip(*args)] 
print(fun(li1,li2,[7,8,9]))