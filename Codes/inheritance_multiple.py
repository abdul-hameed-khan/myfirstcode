# 
# MULTIPLE INHERITANCE

class A:
    def AOA(self):
        return 'AOA from class A'
    

class B:
    def AOA(self):
        return 'AOA from class B'


class C(A,B): # multiple inheritance having more than one parent class
    pass

a = A()
b = B()
c = C()

print(c.AOA()) # AOA from class A for class C(A,B):
# print(help(C))
# print(c.AOA()) # AOA from class B for class C(B,A):

