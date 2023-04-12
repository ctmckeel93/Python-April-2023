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
    def get_name(self):
        print(self.name)
        return self.name
    
    def attack(self,meta):
        if isinstance(meta, Meta ):
            meta.health -= 5
            return self
        else:
            print("Argument must be instance of Meta class")
            
    
    def display_powers(self):
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

# Using our classes

# Create instances
meta1 = Meta("Homelander", None, eye_color="Blue", powers=["all"])
meta2 = Meta("Stormfront", None, eye_color="Brown", powers=["all","Lightning Manipulation", "Electrokinesis"])
meta3 = Meta("A-Train", "Reginald Franklin", "Brown", ["Super speed"] )
meta4 = Meta("Chuck Norris", None, "Blue", ["God"], "Nobody")

# Print the values as a dictionary
print(meta1.__dict__)
print(meta2.__dict__)

# Assigning and updating member variables
meta1.powers.append("Super strength")
meta1.alias = "The blue blur"

# Using methods
print(type(meta1.powers)) # Should be a list

print(meta1.get_name().upper())
print(meta2.get_name().upper())

meta1.display_info()
meta2.attack(meta1)
meta2.attack("Hello") # Handled by the method with incorrect value
meta1.display_info()






