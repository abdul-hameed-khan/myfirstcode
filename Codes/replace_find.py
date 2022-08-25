string = 'my name is abdul Hameed khan and i am a student and is'
print(string.replace(' ','_'))

print(string.replace('is', 'was'))
print(string.replace('is', 'was', 1))#only first is will replace
print(string.replace('is', 'was', 2))#both is will replace and if write write 3 instead of 3
#then nothing go wrong
print()
#find
print(string.find('is'))
print(string.find('is',9))#will find the last is

is_pos1= string.find('is')#wil find first is
print(string.find('is', is_pos1 + 1))#will find the last is 
