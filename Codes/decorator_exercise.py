# calculating time for the function run

import time
from functools import wraps
def deco(f):
    print(f'executing {f}')
    @wraps(f)
    def wrapper(*args):
        t1 = time.time()
        r = f(*args)
        t2 = time.time()
        print(f'this func took {t2 - t1} sec')
        return r
    return wrapper
@deco

def square(n):
    return [i**2 for i in range(n)]
square(10000)

