

print('khan')
name, age= input('enter your name and age\n').split(",")
print(name)
print(age)
n, a = 'hameed' , 23
print('Abdul' + n)
print('yorut age is ' + str(a) + '\nyuor name is Abdul hameed'+ n)
print(int(a+6))
print()

print('hello %s ' % (name))

n = 1234
r  = 0
while n>0:
    r = r*10 + n% 10
    n = n//10
print(r)