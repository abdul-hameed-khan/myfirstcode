class Person:
    instance_count = 0
    def __init__(self, first_name, last_name, age):
        Person.instance_count += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def with_string(cls,string):
        first_name, last_name, age = string.split(',')
        return cls(first_name, last_name, int(age))

    @classmethod
    def instances(cls):
        return f'you have created {cls.instance_count} intance of class {cls.__name__} '

    def full_name(self):
        return self.first_name+ ' '+ self.last_name

    def is_above_18(self):
        return self.age > 17
 
# p1 = Person('Abdul Hameed','Khan',20)
# p2 = Person('Abdul ','Hameed',16)

p3 = Person.with_string('hameed ,khan , 20')
print(p3.full_name())
print(p3.is_above_18())
print(p3.instances())