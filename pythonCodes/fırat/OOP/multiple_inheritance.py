'''
users 
'''


class User():
    def sign_in(self):
        print("logged in")

    def attack(self):
        print("do nothing")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f"attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, num_arrow):
        self.name = name
        self.num_arrow = num_arrow

    def attack(self):
        print(f"attacking with arrows:arrows left -- {self.num_arrow}")


wizard1 = Wizard("merlin", 50)
archer1 = Archer("robin", 100)

print(wizard1.attack())


# def player_attack(char):
#     char.attack()


# for char in [wizard1, archer1]:
#     char.attack()

# player_attack(wizard1)

# print(isinstance(wizard1, User))

# archer1.attack()
# wizard1.attack()
