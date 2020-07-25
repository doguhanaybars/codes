class PlayerCharacter:
    # Class Object Attributes
    membership = True

    def __init__(self, name, age):
        if (self.membership): # or PlayerCharacter.membership
            self.name = name  # attributes
            self.age = age

    def shout(self):
        print(f'my name is {self.name}') # not PlayerCharacter.name
        
    def run(self,hello):
        print(f'my name is {self.name}')

player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 25)
player2.attack = 50

print(player1.run('hello'))
print(player2.shout())
