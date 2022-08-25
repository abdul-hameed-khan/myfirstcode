
# READ , OPEN , CLOSE METHOD


# l = open('file1.txt') 
# print(f'cursor position - {l.tell()}')
# print(l.read())
# print(f'cursor position - {l.tell()}')
# # print(l.read()) # it will print it only 1 time bcz it reads as the cursor moves line by line ....
# l.close()

# l = open('file1.txt') 
# print(f'cursor position - {l.tell()}\n')

# print(l.read())

# l.seek(0) # will change the position of cursor to 0

# print(f'cursor position - {l.tell()}\n')

# print(l.read()) 
# l.close()


# READLINE METHOD



l = open('file1.txt') 

# print(l.readline() , end = '') # WILL READ ONLY 1 LINE

# print(l.readline()) 

lines = l.readlines() 
print(lines) # will print the list of all lines
print(len(lines)) 

for i in lines:
    print(i, end = '')

l.close()



# DATA DESCRIPTERS for reading name of file ....AND ITERATION ON OBJECT IN WHICH OUR FILE IS STORED

# l = open('file1.txt') 

# # print(l.name)
# # print(l.closed)
# for i in l:
#     print(i , end= '')
# # for i in l.readlines()[:2]:  # for reading only first 2 lines
# #     print(i , end= '')
# l.close()



# WE CAN USE SLICING WITH readlines()

# l = open('file1.txt') 

# for line in l.readlines()[:2]:
#     print(line)

# l.close()


# TO READ A FILE FROM DIFFERNT PATH

# l = open(r"C:\Users\Zulfiqar\Desktop\file1.txt") 

# for line in l.readlines():
#     print(line)

# l.close()