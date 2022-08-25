name = input('plz enter your name\n')

temp = ''
for i in range(0,len(name)):
    if name[i] not in temp:
        temp += name[i]
        print(f'{name[i]} : {name.count(name[i])}')
    
