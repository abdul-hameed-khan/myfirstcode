

class Phone:
    def __init__(self, name , no, brand,price):
        self.name = name
        self.no = no 
        self.brand = brand
        self._price = 30000 # naming convention for private variables for other developers... can modifyeable
        self.__price = price  # for private variables ... can't modifyeable but accessible with class name as prefix

    def call(self):
        print(f'calling... {self.no}')
    
    def message(self): 
        print(f'message sent to {self.no}')


p1 = Phone('nokia', 3145916393 , 's9',15000)
# p1.call()
# p1.message()

p1._Phone__price = 12000
print(p1.__dict__) # {'name': 'nokia', 'no': 3145916393, 'brand': 's9', '_Phone__price': 20000}
# print(p1.__price) # will give u an error