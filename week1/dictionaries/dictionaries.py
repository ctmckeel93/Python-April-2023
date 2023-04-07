from database import generate_database, pretty_db
db = generate_database()

# Dictionary
my_dictionary = {
    "id": 0,
    "brand": "Gibson",
    "strings": 6,
    "color" :"Mahogany",
    "extra": "stuff"
}
# adding a key/value pair
my_dictionary["color"] = "Maple"
my_dictionary["type"] = "Acoustic"
my_dictionary.setdefault("flubber", "Apple")

# # accessing dictionaries
guitar_type = my_dictionary["type"]
guitar_color= my_dictionary.get("color")
print(guitar_type)
print(guitar_color)

# removing a key
# # print(my_dictionary.pop("")) - This will throw an error if specified key not in dictionary
del my_dictionary['extra']

# # updating values
my_dictionary.update({
    "is_bass": False,
    "is_electric": True
})

# # iterating through a dictionary
for key in my_dictionary:
    print(key)
    
for value in my_dictionary.values():
    print(value)
    
for key,value in my_dictionary.items():
    print(f"{key}: {value}")
    
dict_keys = my_dictionary.keys()
dict_values = my_dictionary.values()
dict_items = my_dictionary.items()
print(dict_keys)
print(dict_values)
print(dict_items)

# Nesting dictionaries
for user in db:
    for key, value in user['address'].items():
        print(f"{key} --> {value}")