def myFunc(func):
    def wrapper():
        print(f"{func.__name__} was called")
        func()
        print("end")
    return wrapper

@myFunc
def say_hello():
    print("Hello")
    
    
say_hello()

