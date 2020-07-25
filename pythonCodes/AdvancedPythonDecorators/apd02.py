#DECARATOR pattern

def my_decarator(func):
    def wrap_func(*args,**kwargs):
        print('********')
        func(*args,**kwargs)
        print('********')
    return wrap_func

@my_decarator
def hello(greeting, emoji=':('):
    print(greeting, emoji) 

hello('hiiii')