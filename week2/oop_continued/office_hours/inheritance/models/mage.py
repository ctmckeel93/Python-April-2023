from character import Character

class Mage(Character):
    def __init__(self,name):
        super().__init__(name, 4, 5, 80)
        self.mana = 150