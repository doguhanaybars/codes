class User(object):
    def __init__(self,email):
        self.email = email

    def sing_in(self):
        print('logged in')

class Wizard(User):
    def __init__(self,name,power,email): #emaili eklemeyi unutma
        super().__init__(email) #user classından çektik
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f'attacking with power of {self.power}')
       

wizard1 = Wizard('Merlin',60,'merlin@gmail.com')
print(wizard1.email)
#print(dir(wizard1))