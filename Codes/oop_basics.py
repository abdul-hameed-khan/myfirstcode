

class Person:
    def __init__(self, first_name, last_name, age):
        # instace variables 
        # print('init method  called')
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
 
 
p1 = Person('Harshit', 'Vashistha', 24)
p2 = Person('Mohit', 'Vashistha', 19)
 
print(p1.first_name)
print(p2.first_name)


# class User_info:
#     def __init__(self,n,a,w):
#         self.name = n
#         self.age = a
#         self.weight = w
    
#     def intro(self):
#         print('my name is ' + self.name)
#         print('my age is ' + str(self.age))
#         print('my weight is ' + str(self.weight))


# me = User_info('Abdul Hameed Khan',20,75)
# me.intro()
# print(me.age)
# print(User_info.intro(me)) # we can also use this .... actually this work is being done in the background



# STATIC METHOD

class Person2:
    
    def __init__(self, first_name, last_name, age):
      
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @staticmethod
    def hello(k):
        print(5+k)
        return "hello, hameed , static method"
        

    def full_name(self):
        return self.first_name+ ' '+ self.last_name

    def is_above_18(self):
        return self.age > 17
 
p1 = Person2('Abdul Hameed','Khan',20)
p2 = Person2('Abdul ','Hameed',16)

print(p1.hello(3))