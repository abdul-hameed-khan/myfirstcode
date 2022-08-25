
from functools import wraps

def allow_string_only(func_name):
    @wraps(func_name)
    def wrapper_func(*args,**kwargs):
        return func_name(*args,**kwargs)
    return wrapper_func

@allow_string_only
def add_str(*args):
    string=''
    for i in args:
        if type(i)==str:
            string+=i
        # else:
        #     return "invalid input" # add or remove these two lines of else statement
    return string
      
print(add_str('abc','def')) # output is abcdef removing the else statement
print(add_str('abc','def',8,[1,2])) # output is still abcdef removing the else statement
print(add_str('abc','def',8,[1,2,3])) # output is 'invalid input' adding the else statement