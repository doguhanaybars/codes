
from time import time


def performance(fn):
    def wrapper(*args, **kawrgs):
        t1 = time()
        result = fn(*args, **kawrgs)
        t2 = time()
        print(f"took {t2 - t1} ms")
        return result
    return wrapper


@performance
def long_time():
    for i in range(1000):  # numara arttıkça işlenme hızı da artacaktır...
        i*5


long_time()
