class PlayerCharacter:
    membership = True

    def __init__(self, name="anonymus", age=0):
        self.name = name
        self.age = age

    def speak(self):
        print(f"my name is {self.name} and i am {self.age} years old")


player1 = PlayerCharacter("fırat", 10)
# player2 = PlayerCharacter("berk", 26)

print(player1.speak())
