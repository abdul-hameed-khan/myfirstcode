# map object is an iterable \
num = [1,2,3,4]
def square(a):
    return a**2

s = list(map(square,num))
print(s)

names = ['hameed','khan','jadoon']
l = list(map(len,names))
print(l)

#map object is iterator

for i in l:
    print(i)