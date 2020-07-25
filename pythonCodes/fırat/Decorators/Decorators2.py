

def my_dec(func):
    def wrap_func():
        print("**************")
        func()
        print("**************")
    return wrap_func()


@my_dec
def hello():
    print("helloooo")


@my_dec
def bye():
    print("cya later")


hello

bye
