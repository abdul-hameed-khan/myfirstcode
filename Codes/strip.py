# name1 , c=input('enter your name and a character separated by comma\n').split(',')
# print(len(name1))
# print(name1.strip().lower().count(c.strip().lower())) 
#the upper code will show the length of name including spaces

name1 , c=input('enter your name and a character separated by comma\n').split(',')  
rep = name1.replace(" ","")
print(len(rep))
print(name1.strip().lower().count(c.strip().lower())) 

# now this upper code will show the length of name only not including spaces
