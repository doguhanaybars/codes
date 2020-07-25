
def my_dec(func):
    def wrap_func(x):
        print("**************")
        func(x)
        print("**************")
    return wrap_func


@my_dec
def hello(greeting):
    print(greeting)


hello("hiiii")
