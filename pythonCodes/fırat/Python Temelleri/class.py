class Person:
    pass
    # class attributes

    # constructor (yapıcı metodlar)
    def __init__(self, name, year):

        # #object attributes
        self.name = name
        self.year = year
        print("init metodu çalıştı")

        # methods


p1 = Person("fırat", 1998)


class Circle:
    pi = 3.14

    def __init__(self, yaricap=1):
        self.yaricap = yaricap

    def cevre(self):
        return 2*self.pi*self.yaricap

    def alan(self):
        return self.pi*self.yaricap**2


c1 = Circle()

print(c1.alan())
