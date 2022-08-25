

class Phone(object):
    def __init__(self, brand , model , price):
        self.brand = brand
        self.model = model
        self._price = max(0,price) # will select 0 if price is less than 0 
        # self.complete_spec = f'{self.brand} {self.model} and price is {self._price}'

    @property
    def complete_spec(self):
        return f'{self.brand} {self.model} and price is {self._price}'

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,new_price):
        self._price = max(new_price,0)
        return self._price
    
    def make_call(self, no):
        print(f'calling ... {no}')

p1 = Phone('nokia', '1112',600)

p1.price = -9000

print(p1.price)

print(p1.__dict__) # '_price': -9000, 

print(p1.complete_spec)


# print(p1.make_call(5454))


