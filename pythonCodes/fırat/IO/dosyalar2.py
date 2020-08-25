try:
    with open("happy.txt", mode="r") as my_file:
        print(my_file.read())
        # print(text)
except FileNotFoundError as err:
    print("file does not exist")
    raise err
except IOError as err:
    print("IO error ")
    raise err
