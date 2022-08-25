num = input('plz enter a number more than one digit\n')
if int(num) < 0:
    print('plz enter a positive number\n')
elif len(num) > 1:
    i = 0
    sum = 0
    while i<len(num):
        sum += int(num[i]) 
        i += 1
    print(sum) 
else:
    print('plz enter a number more than one digit\n')
