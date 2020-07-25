#Error Handling

while True:
    try:
        age = int(input('What is your age? '))
        10/age
    except ValueError:
        print('please number!')
    except ZeroDivisionError:
        print('please enter age higher than 0')
    else:
        print('thank you')
        break