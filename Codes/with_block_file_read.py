# OLD METHOD

# f = open('file1.txt') 

# print(f.read())

# f.close()


with open('file1.txt') as f:
    print(f.read()) 

print(f.closed) # True.... thats why no need to close the file 
