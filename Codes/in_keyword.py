name = 'hameed khan'
chk = input('enter the word to check in the string\n')
# c = chk.lower() #if you don't want case sensitive then use this
if chk in name: # case sensitive
    print('yes present')
else:
    print('not present')


n  = '1215'
# chck = input('enter a number to check\n')
# chck = int(chck)
if '2' in n: 
    print('yes present')
else:
    print('not present')