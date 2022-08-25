# we are giving discount on our laptop

class Laptop:
    dis = 10
    def __init__(self , brand , model , price):
        self.brand = brand
        self.model = model
        self.price = price
        

    def discount(self):
        return (self.price - (self.price * (self.dis / 100)))
         

l1 = Laptop('hp','2018',75000)
l2 = Laptop('dell','2016',10000)
# l2.dis = 20
print(l2.discount())

print(l2.__dict__) # {'brand': 'hp', 'model': '2018', 'price': 75000, 'dis': 20}


# how many instance of class has been created

class Person:
    class_instance = 0
    def __init__(self):
        Person.class_instance += 1

p1 = Person()
p2 = Person()
p3 = Person()
print(Person.class_instance)