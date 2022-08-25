# **kwargs

def func(**kwargs):
    for i ,j in kwargs.items():
        print(f'{i} : {j}')

func(name =  'Abdul hameed', age= 20)
d= {'name' : 'Abdul hameed', 'age': 20}
func(**d)
print()

# order for the function in awhich u use all 
#PADK

def func2(name,*args,l_name = 'khan',**kwargs):
    print(name)
    print(args)
    print(kwargs)
    print(l_name)

func2('Hameed',1,12,3,a=1,b=3)