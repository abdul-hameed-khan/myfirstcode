# import random
# coin1 = 1
# coin2 = 2
# count,count2 = 0,0
# for i in range(10):
#     win = random.randint(coin1,coin2)
#     print(win,end = ' ')
#     if win == 1:
#         count += 1
#     else:
#         count2 += 1
# print()
# print(count,count2)

import random
def coinToss(number):
    recordList, heads, tails = [], 0, 0 # multiple assignment
    for i in range(number): # do this 'number' amount of times
         flip = random.randint(0, 1)
         if (flip == 0):
              print("Heads")
              recordList.append("Heads")
         else:
              print("Tails")
              recordList.append("Tails")
    print(str(recordList))
    print('Heads = '+str(recordList.count("Heads")) +'  '+ 'Tails = '+str(recordList.count("Tails")))
number = int(input('enter a number to flip the coin : '))
coinToss(number)