# Lists - enumerators, sequences, collections, arrays 
my_names1 = ["Winter", "Samuel","German","Ernest"]
my_names2 = [100, False,3.14,"Ernest"]

my_tuple = "Hello",3
# my_tuple[0] = "Stop" # We cannot change the values inside a tuple

# Combining lists - + and *
new_list = my_names1 + my_names2
print(new_list) # ["Winter","Samuel","German","Ernest", 100, False, 3.14, "Ernest"]
multi_list = my_names1 * 5 # ['Winter', 'Samuel', 'German', 'Ernest', 'Winter', 'Samuel', 'German', 'Ernest', 'Winter', 'Samuel', 'German', 'Ernest', 'Winter', 'Samuel', 'German', 'Ernest', 'Winter', 'Samuel', 'German', 'Ernest']
print(multi_list)

# The slice syntax - list[:]
my_names_ref_copy = my_names1 # This only assigns a reference back to the original array
my_names_ref_copy.append("Rishad")
print("My names array:",my_names1) # Rishad is added to the end of both lists

my_names_copy = my_names1[:] # Creates a copy of the original array and assigns it to my_names_copy
my_names_copy.append("Brandon")
print(my_names_copy) # Brandon is added to the end of the list
print("My names 1:", my_names1) # Brandon was not added to the original list

last_three = my_names1[2:] # creates a list with values from the second index to the end of the list
middle = my_names1[1:3] # creates a list with values from the first index to the 2nd index
print(my_names1[1:4]) # creates a list with values from the first index to the 2nd index
print(my_names1) # The original list has not been changed
print(my_names1[:4]) # creates a list from the beginning of the list to the 3rd index
