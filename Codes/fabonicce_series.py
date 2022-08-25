# def fibonacci_series(num):
#     n1 = 0
#     n2 = 0
#     n3 = 1
#     print(n3,end="  ")
#     for i in range(0,num):
#         n1 = n2
#         n2 = n3
#         n3 = n1 + n2
#         print(n3,end="  ")   
        
# num = int(input('enter a number to which you want to print faonicce series : '))
# fibonacci_seq(num)

# OR THE ANOTHER WAY (the upper is my own)

def fibonacci_seq(num):
    a = 0
    b = 1
    if num == 1:
        print(a)
    elif num == 2:
        print(a, b)
    else:
        print(a  ,  b ,end="  ")
        for i in range(num-2): # n-2 bcz the 1st two numbers are fixed
            c = a + b
            a = b
            b = c
            print(c, end="  ")

num = int(input('enter a number to which you want to print faonicce series : '))
fibonacci_seq(num)