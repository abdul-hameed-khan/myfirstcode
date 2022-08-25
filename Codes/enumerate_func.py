names = ['hameed','khan','jadoon']

for pos , name in enumerate(names):
    print(f'{pos} : {name}')

def func(l,s):
    
    for pos , name in enumerate(names):
        if s == name:
            print(pos)
    if s not in l:
        print('-1')

func(names,'hameed') 
