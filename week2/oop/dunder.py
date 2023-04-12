def add(a, b,*args, kwargs1="Hello World" ):
    print(kwargs1)
    if len(args) == 0:
        print(len(args))
        print("Just a and b")
        return a + b
    print(len(args))
    sum = 0
    sum += a + b
    for num in args:
        if isinstance(num, int):
            sum+= num
        else:
            print("Not a number")
    print("Sum:",sum)
    return sum

add(1,2)
add(10,20,3)
add(11,2,31)
add(111,22,3, "Hello")


print(add.__defaults__)
print(add.__kwdefaults__)

print(type(add.__name__))

if isinstance(12,int):
    print("Its a string")
    
if add.__name__ == "add":
    print("Hooray!")
    
class User:
    def __init__(self):
        self.name = "Monkey",
        self.mood = "Happy"
        
user1 = User()
print(user1.__dict__)
print(__name__)
print(__file__)
print(user1.__class__)