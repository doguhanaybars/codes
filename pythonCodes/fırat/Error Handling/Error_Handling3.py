# error handling

while True:
    try:
        age = int(input("what is your age : "))
        10/age
    except ValueError:
        print("please enter a number.")
        continue
    except ZeroDivisionError:
        print("please enter age higher than zero.")
        break
    else:
        print(f"your age is {age} \nthank you.")

    finally:
        print("ok i am finnaly done.")
    print("can you hear me")
    break
