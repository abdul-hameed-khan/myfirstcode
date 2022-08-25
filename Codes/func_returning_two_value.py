def twoValue(a,b):
    add = a + b
    mul = a*b
    return add, mul

print(twoValue(5,6)) # (11, 30) ...it is returning a tuple

add , mul = twoValue(5,6)
print(add, mul) # 11 30 .... not a tuple ..

