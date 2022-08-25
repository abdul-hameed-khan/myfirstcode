class Person:
    instance_count = 0
    def __init__(self, first_name, last_name, age):
        Person.instance_count += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def instances(cls):
        return f'you have created {cls.instance_count} intance of class {cls.__name__} '

    def full_name(self):
        return self.first_name+ ' '+ self.last_name

    def is_above_18(self):
        return self.age > 17
 
p1 = Person('Abdul Hameed','Khan',20)
p2 = Person('Abdul ','Hameed',16)

print(p1.full_name())
print(p1.is_above_18())
print(Person.instances())
# print(p1.instances())
# print(p2.instances())