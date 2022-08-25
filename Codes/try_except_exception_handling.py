
# try:
#     age = int(input('enter your age : '))
        
# except ValueError:
#     print('plz enter your age in integer')
    # NameError: name 'age' is not defined

while True:
    try:
        age = int(input('enter your age : '))
        break
    except ValueError:
        print('plz enter your age in integer')

    except:
        print('invalid input')


if (age > 17):
    print('you can apply for CNIC')
else:
    print('you cannot apply for CNIC')
