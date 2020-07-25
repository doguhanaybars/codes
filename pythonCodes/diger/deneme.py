class Person:
    
    def __init__(self,name,year):
        self.name = name
        self.year = year
    
    def intro(self):
        print('Hello There ' + self.name)

    def calgulateAge(self):
        return 2020 - self.year

p1 = Person(name="mehmet",year=1930)
p2 = Person(name="selami",year=1960)

p1.intro()
p2.intro()

print(f'adım: {p1.name} yaşım: {p1.calgulateAge()} ')
print(f'adım: {p2.name} yaşım: {p2.calgulateAge()} ')
