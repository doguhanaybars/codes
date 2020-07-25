# x = "global x"


# def function():
#     # x = "local x"

# function()
# print(x)

# ##############################

#     # name = "çınar"


# def changeName(new_name):
#     name = new_name
#     print(name)


# changeName("Ada")
# print(name)

##############################

name = "Global String"


def greeting():
    # name = "çınar"

    def hello():
        print("hello " + name)

    hello()


greeting()
print(name)

#############################################

x = 50


def test():
    global x
    print(f"x {x}")
    x = 100
    print(f"change x to {x} ")


test()
print(x)
