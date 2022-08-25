def to_power(n,*args):
    if args:
        return [i**n for i in args]
    else:
        return 'you didnot pass any args'

print(to_power(2,*[2,3,4]))

# taking list as an input from the user

# 1

# n = int(input("Enter number of elements : ")) 
  
# # Below line read inputs from user using map() function  
# a = list(map(int,input("\nEnter the numbers : ").split()))[:n] 
  
# print("\nList is - ", a)

# 2

# For list of integers 
# lst1 = [] 


# lst1 = [int(item) for item in input("Enter the list items : ").split()] 

# print(lst1) 

string  = ['hameed','jadoon']

def reverse(l,**kwargs):
    if kwargs.get('reverse_str') == True:
        return [i[::-1].title() for i in l]
    return [i.title() for i in l]
print(reverse(string))
# print(reverse(string,reverse_str = True))