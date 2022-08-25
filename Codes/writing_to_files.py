
# w , a , r+ 
# w


with open('file2.txt', 'w') as f: # it has created automatically a new file
    f.write('AOA hameed\n')
    f.write('AOA hameed khan')


# a 

with open('file2.txt', 'a') as f: 
    f.write('\nAOA hameed\n') # it will append these lines in a file
    f.write('AOA hameed khan')


# r+

# with open('file3.txt', 'r+') as f: # it has created automatically a new file3
#     # f.write('AOA hameed\n')
#     # f.write('AOA jadoon khan') # it will override these lines with existing lines starting from 0 
#     # to set this from our own cursor position WE ARE USING SEEK() METHOD

#     f.seek(len(f.read())+1)
#     f.write('\nAOA hameed\n')
#     f.write('AOA jadoon khan') 


# write code file2.txt and code file3.txt

# ALSO YOU CAN WRITE FROM 1 FILE TO ANOTHER FILE

with open('file2.txt' , 'r') as rf:
    with open('file3.txt' , 'w') as wf:
        wf.write(rf.read()) # it will write the file2 in file3

