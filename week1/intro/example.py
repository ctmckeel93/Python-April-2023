def myFunc():
    my_string = "Hello World"
    print(my_string)
    for i in range(10):
        print(i) 

my_dictionary = {
    "strength": 10,
    "speed": 15,
    "durability": 10,
    "health": 200,
}
my_list = [1,2,3,4,5]

my_dictionary["health"] -= 200

if my_dictionary["health"] <= 0:
    print(f"Health = { my_dictionary['health'] } -> Game Over, Try again!")



