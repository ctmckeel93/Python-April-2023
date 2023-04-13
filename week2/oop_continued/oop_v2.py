from __future__ import annotations

# Classes - Syntax
class class_name:
    pass


# Lets build our first class
class Meta:
    metas = []
    metas_count = 0
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
        Meta.metas.append(self) # Adds instance to metas list above upon creation
        Meta.metas_count+=1    
# instance methods -> actions a class can perform on individual instances
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
        # print(self)
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
        
# classmethod -> Method that relates to the class itself, but does not care about each individual instance
    @classmethod
    def get_all_metas(cls):
        for meta in cls.metas:
            meta.display_info()
    @classmethod
    def get_count(cls):
        print(cls.metas_count)
        return cls.metas_count
    
    @classmethod
    def from_string(cls, meta_string): # "matt murdock,daredevil,blue,[sonic hearing]"
        print("running from string")
        name, alias, eye_color, powers = meta_string.split(",")
        print(name, alias, eye_color, list(powers)) # this will turn powers into a character array ["[","s","o", "n", "i", "c"]...you get the picture
        
        # Now this will take some tricky manipulation -> If you are curious, try to piece together what I am doing here | This is not important, dont spend too much time trying to understand it
        character_array = list(powers)
        open_bracket = character_array.index("[")
        space = character_array.index(" ")
        print("Space:",space)
        close_bracket = character_array.index("]")
        sonic = "".join(character_array[open_bracket+1:space])
        hearing = "".join(character_array[space+1:close_bracket])
        print(hearing)
        print(sonic ,hearing)
        power1 = sonic + " " + hearing
        # -----------------------------------------------------------------
        
        return cls(name, alias, eye_color, [power1])
    
    @classmethod
    def from_dict(cls,meta_dict):
        name, alias, eye_color, powers = meta_dict.keys()
        return cls(meta_dict[name], meta_dict[alias], meta_dict[eye_color], meta_dict[powers])
# -----------------------------------------------------------------------------------------------------------------

# staticmethod -> Usually used for validations | Methods that can be used in relation to the class or instances, but does not interact with either
    @staticmethod
    def is_valid(meta_dict):
        is_valid = True
        if len(meta_dict["name"]) < 1:
            is_valid = False
        if len(meta_dict["alias"]) < 1:
            is_valid = False
        if len(meta_dict["eye_color"]) < 1:
            is_valid = False
        return is_valid
        
        

# This is all to show that class attributes can be accessed by both the instances and the class itself.

# meta1 = Meta("Guy", "Guy One", "Blue", [])
# # meta1.attack().attack()
# meta1.get_all_metas()
# Meta.metas_count+=1
# meta1.get_count()
# Meta.get_count()

# This is how they should be used
new_meta = Meta.from_string("matt murdock,daredevil,blue,[sonic hearing]")
new_meta.display_info()

meta_dict = {
    "name": "Mark",
    "alias": "Invincible",
    "eye_color": "Brown",
    "powers": []
}

is_valid = Meta.is_valid(meta_dict)
print(is_valid)
if is_valid:
    meta2 = Meta(meta_dict["name"], meta_dict["alias"], meta_dict["eye_color"], meta_dict["powers"])
else:
    print("Not a valid meta")

# Lets make a city class and associate it with a Meta -> use an instance of the Meta class inside of our City class
class City:
    def __init__(self, name, main_hero):
        self.name = name
        self.main_hero: Meta = main_hero
        

superman = Meta("Clark Kent", "Superman", "Blue", ["Super strength", "heat vision", "super hearing"])
metropolis = City("Metropolis", superman)

metropolis.main_hero.display_info() # main hero is an instance of the Meta class and therefore has access to its methods


print(Meta.from_dict(meta_dict).__dict__)