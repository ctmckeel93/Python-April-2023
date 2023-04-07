import random
# Create an empty dictionary

# come up with 5 vocabulary words as a group. It can be related to python or something separate

# Create a dictionary with the vocabulary words as keys and a nested dictionary with the definition and key 

# Make a list out of the values and pick a random question

# Use the built in input() function to get user input for the answer

# Compare the input to the key and print correct if its right, and incorrect if its wrong. 

# Wrap this all in a function called flash_cards(dictionary)

# Example
dictionary = {
    "python": {
        "definition": "A standardized interpreted programming language universally used in web development, software, data science and machine learning",
        "key": "python"
    },
    "int": {
        "definition": "Number data type",
        "key": "int"
    },
    "string": {
        "definition": "Text based value data type",
        "key": "string"
    } 
}

values = dictionary.values()
print(type(values))
random_value = random.sample(list(values), 1)[0]
print(random_value)
answer = input(random_value['definition'] + "\n")
print(answer)
if random_value['key'] == answer:
    print("Yay! Thats corect!!!")



