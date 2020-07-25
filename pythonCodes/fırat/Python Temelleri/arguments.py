# def changeName(n):
#     n = "ada"


# name = "yiğit"

# changeName(name)

# print(name)


# def change(n):
#     n[0] = "istanbul"


# sehirler = ["ankara", "izmir"]

# change(sehirler)
# print(sehirler)

# def add(*params):
#     return sum((params))


# print(add(10, 20, 30, 40))

def displayUser(**args):
    for key, value in args.items():
        print("{} is {}".format(key, value))


displayUser(name="çınar", age=2, city="istanbul")
displayUser(name="ada", age=12, city="kocaeli", phone="1235486")
