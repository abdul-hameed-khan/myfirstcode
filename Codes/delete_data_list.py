# POP() METHOD

words = ['Abdul','hamedd','khan',"jadoon",'mirpur']
words.pop()
print(words) # ['Abdul', 'hamedd', 'khan', 'jadoon']

# pop() method can return the value which it remove
print(words.pop()) # jadoon

words.pop(1)
print(words) # ['Abdul', 'khan', 'jadoon']

# del OPERATOR

words = ['Abdul','hamedd','khan',"jadoon",'mirpur']
del words[3]
print(words) # ['Abdul', 'hamedd', 'khan', 'mirpur']

# REMOVE METHOD

words = ['Abdul','hamedd','khan',"jadoon",'mirpur']
words.remove('khan') # if the list has 2 items like khan then it will delete 1st khan
print(words) # ['Abdul', 'hamedd', 'jadoon', 'mirpur']

