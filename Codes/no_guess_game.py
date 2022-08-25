import random
win_no = random.randint(0,100)

guess_no = int(input('enter a guess number b/w 0 to 100\n'))
if guess_no == win_no:
    print('YOU WON..')
else:       #nested if else
    if guess_no > win_no:
        print('too high\n')
    else:
        print('too low\n')
