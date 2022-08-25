
class Person:
    
    def __init__(self, first_name, last_name, age):
        
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return self.first_name+ ' '+ self.last_name

    def is_above_18(self):  
        return self.age > 17

class University_details(Person):
    def __init__(self, first_name, last_name, age , deptt , roll , gpa):
        # Person.__init__(first_name, last_name, age) # uncommon way 
        super().__init__(first_name, last_name, age) # best way
        self.deptt = deptt
        self.roll = roll
        self.gpa = gpa
        



# p1 = Person('Abdul Hameed','Khan',20)
# p2 = Person('Abdul ','Hameed',16)

u = University_details('Abdul Hameed','Khan',20,'BS', '002', 3.32)
print(u.__dict__)
# print(p1.full_name())
# print(p1.is_above_18())
print(u.is_above_18())
print(u.full_name())

