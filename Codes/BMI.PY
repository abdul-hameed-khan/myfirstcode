# class bmi:
#     def __init__(self, weight, height):
#         self.weight = weight
#         self.height = height
        

#     def calculate(self):
#         return (self.weight / (self.height * self.height))

# b1 = bmi(75,2)
# print(b1.calculate())

# x = input()
# i = x[::-1]
# if (x==i):
#     print('the number is palindrome')
# else:
#     print('the number is not a palindrome')

num=int(input("Enter a number:  "))
temp=num
rev=0
while(num>0):
    dig=num%10
    
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")