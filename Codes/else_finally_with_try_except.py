while True:
    try:
        age = int(input('enter your age : '))
        
    except ValueError:
        print('plz enter your age in integer')

    except:
        print('invalid input')

    else: # this block will run if try statement will run correctly...you can write logic of your program here
        if (age > 17):
            print('you can apply for CNIC')
        else:
            print('you cannot apply for CNIC')
        break

    finally: # this block will always run whether the error comes or not
        print('finally block...')