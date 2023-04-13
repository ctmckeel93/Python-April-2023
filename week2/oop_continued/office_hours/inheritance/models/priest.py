from character import Character

class Priest(Character):
    def __init__(self,name):
        super().__init__(name, 7, 5, 120)
        self.mana = 120