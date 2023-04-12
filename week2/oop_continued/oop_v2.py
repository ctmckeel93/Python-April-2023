from __future__ import annotations

# Classes - Syntax
class class_name:
    pass

metas = []

# Lets build our first class
class Meta:
# Constructor - def  __init__()
    def __init__(self, name, alias, eye_color,powers, nemesis = None):
# member variables or properties -> Information aboput the class
        print("Creating new meta!")
        self.name = name
        self.alias = alias
        self.eye_color = eye_color
        self.powers = powers
        self.nemesis = nemesis   
        self.health = 100
        metas.append(self) # Adds instance to metas list above upon creation    
# methods -> actions a class can perform
    def get_name(self) -> str:
        print(self.name)
        return self.name
    
    def attack(self, meta: Meta) -> Meta :
        if isinstance(meta, Meta ):
            meta.health -= 5
        else:
            print("Argument must be instance of Meta class")
        return self
    
    def display_powers(self) -> None:
        print(self)
        print("Powers".center(20,"_"))
        for power in self.powers:
            print(power)
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Alias: {self.alias}")
        print(f"Eye Color: {self.eye_color}")
        self.display_powers()
        print(f"Nemesis: {self.nemesis}")
        print(f"Health: {self.health}\n")

meta1 = Meta("Guy", "Guy One", "Blue", [])
meta1.attack().attack()


# classmethod

# staticmethod


# Lets make a city class