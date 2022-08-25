
import pdb # python debugger 

print('aoa')

pdb.set_trace() # from this point the debugging will be started

a = input('enter your age : ')
n = input('enter your name : ')

age = a + 6 # error

print(f'your age after 6 years is : {age}')

