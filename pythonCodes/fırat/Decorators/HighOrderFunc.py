# High Order Function HOC

def greet(func):
    func()


def greet2():
    def func():
        return 5
    return func

# high order func bir def fonksiyonunun parametre olarak bir fonskiyon alması ya da direk fonksiyon döndürmesi demek
