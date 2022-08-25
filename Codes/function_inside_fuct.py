def great_num(n1,n2,n3):
    # big = greater(n1,n2)
    return greater(greater(n1,n2),n3)
     

def greater(n1,n2):
    if n1 > n2:
        return n1
    return n2

n1 = int(input('enter first number :'))
n2 = int(input('enter 2nd number :'))
n3 = int(input('enter 3rd number :'))
print(f'{great_num(n1,n2,n3)} is bigger')