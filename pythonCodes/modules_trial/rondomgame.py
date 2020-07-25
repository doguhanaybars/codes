from random import randint
answer = randint(1,10)



while True:
    try:
        guess = int(input('guess a number 1-10:  '))
        if  0 < int(guess) <11:
            if int(guess) == answer:
                print('you are a genius!')
                break
        else:
            print('hey , i said 1-10')
    except ValueError:
        print('please enter a number')
        continue