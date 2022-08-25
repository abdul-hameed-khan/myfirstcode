# APPEND() method

numbers = [1,6,9]
numbers.append(10)
print(numbers) #[1, 6, 9, 10]

words = ['hamedd','khan',"jadoon",'mirpur']
words.append('abbottabad')
print(words) # ['hamedd', 'khan', 'jadoon', 'mirpur','abbottabad']

# INSERT() Method

numbers = [1,6,9]
numbers.insert(1,10)
print(numbers) #[1, 10, 6, 9]

words = ['hamedd','khan',"jadoon",'mirpur']
words.insert(0,'abbottabad')
print(words) # ['abbottabad','hamedd', 'khan', 'jadoon', 'mirpur']

# CONCATENATE TWO STRINGS

n1 = [1,2,3]
n2 = [5,6,7]
n = n1 + n2
print(n) # [1, 2, 3, 5, 6, 7]

# DIFFERENCE B/W extend() & append()

n3 = ['1','5','3']
n4 = ['5','6','7']
n3.append(n4)
print(n3) #['1', '5', '3', ['5', '6', '7']]

n5 = [1,9,3]
n6 = [5,6,7]
n5.extend(n6)
print(n5) #[1, 9, 3, 5, 6, 7]

