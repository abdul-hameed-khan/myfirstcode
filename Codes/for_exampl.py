num = input('enter a number to sum\n')
sum = 0
for i in range(0,len(num)):
    sum += int(num[i])
print(sum)