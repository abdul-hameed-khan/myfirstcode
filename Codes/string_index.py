name  = 'hameed'
print(name[1:5])
print('hameed'[5::-2])
print('abdul hameed khan'[::-2])
print(name[::-1])#will reverse the string
print(name[5:-6:])#will also reverse the string

n = 1234
r  = 0
while n>0:
    r = r*10 + n% 10
    n = n//10
print(r)