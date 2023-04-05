import random;

"""

Variables:

    name = value

Data Types:

    string -> "Hello"
    int    -> 10
    float  -> 3.14
    boolean -> True, False

    list
    dictionaries






Operators:

    * Math
        - +
        - -
        - *
        - /
        - // -> floor division
        - %
    * Comparison
        - <
        - >
        - <=
        - >=
        - =
        - == (is can also be used, but not when comparing strings)
    * Logical
        - or
        - and
        - not

""" # Python ignores string literals not assigned to a variable
# Numbers

integer = 4
floating_point = 3.14

print(type(integer))
print(type(floating_point))
print(type("Hello World"))
print(type(False))

print(int(floating_point)) # 3
print(int(1.7587658758756)) # 1
print(float(integer)) # 4.0

roll = random.randint(1,20)
print(roll)

num_array = []
# Create an array with 20 random numbers 1-100
for i in range(20):
    num_array.append(random.randint(1,100))

print(num_array)
print(num_array[random.randint(0,len(num_array)-1)])
# print(num_array[len(num_array)]) -> this will throw an error

# # Lists
array = [1,2,3.14,False, "Hello"]
array[3] = True
print(array)

# Tuples - Read only Array
tup = (1,2,55,4.13, True)
print(tup[1]) # Access tuples the same as arrays
# tup[3] = 44 -> You cannot change the values of a tuple
print(tup)

# Dictionaries
my_dict = {}


# Strings
first_string = "I am here to"
second_string = "PARTY!!!!"

# String concatenation
print(first_string,second_string) # The comma separation syntax only works with print()
combined_string = first_string + " " + second_string

# String Interpolation

# string.format()
formatted_string = "Welcome to {}! I am {} your instructor and I think were going to have a lot of fun together in this stack! My favorite number is {}".format("first bracket", "Second bracket", 3)
print(formatted_string)

# - f string
num = 22
new_f_string = f"{first_string} {second_string} {num}"
print("combined string:",combined_string)
print(new_f_string)

# - % formatting
percent_string = "My name is %s and I am happy to assist you. Your number is %d" % ("Corey Mckeel" ,103) # I honestly hate this lol
print(percent_string)
print(first_string + str(num));

# Split and Join

# Split - turns a string into an array creating an index out of each separator
# Join - turns an array into a string with each index separated by your choice of string
string_splitter = "777-777-0077";
split_string = string_splitter.split('-') # ["777", "777", "0077"]
print(" ".join(split_string))
print(" MARIA ".join(split_string)) # 777 MARIA 777 MARIA 0077 -> Just to show how ridiculously you could use this XD

# Accessing Strings -> strings are tuples of characters
print(string_splitter[4])
# string_splitter[2] = "F" -> This will throw an error similarly to tuples
print(string_splitter[0:3]) #gets a piece of the string from the first index, does not include right number






