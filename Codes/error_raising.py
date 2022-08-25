# raise key word is used to raise errors


#  # def add(a,b):
# #     if(type(a) is int) and (type(b) is int):
# #         return a+b
# #     raise TypeError('OOPs you entered wrong data type')

# # print(add('2','6')) # TypeError: OOPs you entered wrong data type

# # # 

# # ERROR RAISING example 1
# #  /...ABSTRACT METHOD..../

# class Animal:
#     def __init__(self, name ):
#         self.name = name

#     def name_print(self):
#         print( self.name)

#     def sound(self): # also called abstract method... in which's body we don't write anything
#         raise NotImplementedError('you have to define a sound method for subclass')

# class dog(Animal):
#     def __init__(self, name):
#         super().__init__(name)
        

#     def sound(self):
#         print( 'bow bow')

# class cat(Animal):
#     def __init__(self, name):
#         super().__init__(name)

#     def sound(self):
#         print( 'meow meow')

# d = dog('lolo')
# d.name_print()
# d.sound()
# c = cat('lili')
# c.sound()



# ERROR RAISING example 2

class Mobile:
    def __init__(self, name):
        self.name = name
    

class Mobilestore:
    def __init__(self):
        
        self.mobiles = []

    def add_mobile(self, new_mobile):
        if isinstance(new_mobile, Mobile):
            return self.mobiles.append(new_mobile)
        else:
            raise TypeError('new mobile must be an object of Mobile class')


mob = Mobile('samsung s8')
mob2 = Mobile('sony j9')
nokia = 'nokia r5'
mobstr = Mobilestore()

# print(mobstr.mobiles) # an empty list

mobstr.add_mobile(mob)
mobstr.add_mobile(mob2)
# mobstr.add_mobile(nokia) # TypeError: new mobile must be an object of Mobile class
m = mobstr.mobiles # list
print([m[i].name for i in range(len(m))]) # printing mobiles list
