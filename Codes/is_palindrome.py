# str = input('enter a word to check whether it is palinfdrome or not\n')
# rev = str[::-1]
# if str == rev:
#     print('yes')
# else:
#     print('no')

# Another way

# def palindrome(str):
#     if str == str[::-1]:
#         return True
#     return False

def palindrome(str):
    return str == str[::-1] # the best way is this
    
str = input('enter a word to check whether it is palinfdrome or not\n')
print(palindrome(str))
