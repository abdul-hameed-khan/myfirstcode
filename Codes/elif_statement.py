#if elif else statement

age = input('enter your age\n')
age = int(age)

if 0<age<8:
    print('your ticket is free\n')
elif 8<age<=20:
    print('ticket price is : 200')
elif 20<age<=40:
    print('ticket price is : 300')
elif 40<age<200:
    print('ticket price : 400')
else:
    print('plz enter your correct age')
