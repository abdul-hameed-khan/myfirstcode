# import random
# win_no = random.randint(0,100)
# i = 1
# guess_no = int(input('enter a guess number b/w 0 to 100\n'))
# if guess_no == win_no:
#     print('YOU WON..')
# else:       #nested if else
#     if guess_no > win_no:
#         print('too high')
#     else:
#         print('too low')
# while guess_no != win_no:
#     guess_again = int(input('guess again : '))
#     if guess_again == win_no:
#         print(f'YOU WON..your guess is successful after {i}th try')
#         break
#     else:      
#         if guess_again > win_no:
#             print('too high')
#         else:
#             print('too low')
#     i += 1


#the upper is my own

# import random
# win_no = random.randint(0,100)
# guess = 1
# guess_no = int(input('enter a guess number b/w 0 to 100 : '))
# game_over = True

# while game_over:
#     if guess_no == win_no :
#         print(f'YOU WIN...you guess this number in {guess} times')
#         game_over = False
#     else : 
#         if guess_no < win_no :
#             print('too low')
#             guess += 1
#             guess_no = int(input('guess again : '))
#         else :
#             print('too high')
#             guess += 1
#             guess_no = int(input('guess again : '))

import random
win_no = random.randint(0,100)
guess = 1
guess_no = int(input('enter a guess number b/w 0 to 100 : '))
game_over = True

while game_over:
    if guess_no == win_no :
        print(f'YOU WIN...you guess this number in {guess} times')
        game_over = False
    else : 
        if guess_no < win_no :
            print('too low') 
        else :
            print('too high')
        #the next two lines will work same as the upper 2nd code works and it is called DRY principle
        guess += 1
        guess_no = int(input('guess again : '))
        