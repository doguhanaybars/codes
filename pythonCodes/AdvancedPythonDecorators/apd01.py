# def hello(func):
#     func()
    
# def greet():
#     print('still here!')

# a = hello(greet)
# print(a)

#hight order function 

# def greet(func):
#     func()

# def greet2():
#     def func():
#         return 5
#     return func

#Decorator

def my_decorator(func):
    def wrap_func():
        print('********')
        func()
        print('********')
    return wrap_func
@my_decorator
def hello():
    print('helloooo')
@my_decorator
def bye():
    print('see you later')
hello()
bye()
