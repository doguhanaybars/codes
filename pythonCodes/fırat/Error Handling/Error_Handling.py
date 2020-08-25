# error handling

while True:
    try:
        age = int(input("what is your age : "))
        10/age
    except ValueError:
        print("please enter a number.")
    except ZeroDivisionError:
        print("please enter age higher than zero.")
    else:
        print(f"your age is {age} \nthank you.")
        break
