# POLYMOROHISM...

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


    def full_name(self):
        return self.first_name+ ' '+ self.last_name +' '+ self.deptt +' '+ self.roll

class Sports(University_details):
    def __init__(self, first_name, last_name, age , deptt , roll , gpa, football_match, cricket_match, hockey_matches):
        super().__init__(first_name, last_name, age , deptt , roll , gpa)
        self.football_match = football_match
        self.cricket_match = cricket_match
        self.hockey_matches = hockey_matches    

    def full_name(self):
        return self.first_name+ ' '+ self.last_name +' '+ self.deptt +' '+ self.roll +' '+ str(self.football_match) +' '+ str(self.cricket_match)
    
    def full_details_player(self,k):
        for i,j in k.items():
            print(f'{i} : {j}')



 
p1 = Person('Abdul Hameed','Khan',20)
p2 = Person('Abdul ','Hameed',16)

u = University_details('Abdul Hameed','Khan',20,'BS', '002', 3.32)

s = Sports('Abdul Hameed','Khan',20,'BS', '002', 3.32,5,6,15)
p = s.__dict__
# s.full_details_player(p)
# print(u.__dict__)
print(p1.full_name())
print(u.full_name())
print(s.full_name())
# print(p1.is_above_18())

print(help(Sports)) # MRO... method resolution order.... 1st method

# print(University_details.__mro__) # MRO 2nd method

# print(Person.mro()) # MRO ... 3rd method
