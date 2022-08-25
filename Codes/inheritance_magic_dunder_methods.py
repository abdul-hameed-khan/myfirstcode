
# DUNDER METHODS
# double underscores method
# __str__ and __repr__ both are same....but if u write both then __str__ will be called


class Phone:
    def __init__(self, brand , model , price):
        self.brand = brand 
        self.model = model
        self.price = price

    def __str__(self): # nicely formatted string... used for printing attributes/ instance variables
        return f'{self.brand} {self.model} and price is {self.price}'

    def __repr__(self): # using it for creating new object by developers
        return f"Phone('{self.brand}','{self.model}',{self.price})"

    def __len__(self):
        l= len(self.__str__()) 
        # l2 = len(self.__repr__())
        return l

    def __add__(self,other):
        return self.price + other.price

    def __name__(self): # my own defined dunder method
        return self.brand + self.model

p = Phone('nokia', '1100',2000)
p2 = Phone('nokia','1112',1000)
print(p) # nokia 1100 and price is 2000
# print(str(p)) # nokia 1100 and price is 2000...1 way
# print(format(p)) # nokia 1100 and price is 2000...2 way
print(p.__repr__()) # Phone('nokia','1100',2000) ..... 1 waY
# print(repr(p)) # Phone('nokia','1100',2000)... 2 way

print(p.__len__())

# print(p.__add__(p2)) # 1 way
print(p + p2) # 2 way
print(p.__name__())

