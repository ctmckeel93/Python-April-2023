from character import Character

class Warrior(Character):
    def __init__(self,name):
        super().__init__(name, 10, 8, 150)
        
warrior = Warrior("Armond")

print(warrior.attack)