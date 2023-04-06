from colorama import Fore, Style, Back

store = "Store"
print(Fore.GREEN, Back.WHITE)
print(Fore.GREEN + store.center(20,"="))
print(Style.RESET_ALL)
print("Coffee".ljust(16,"."),       "$7.00 |".rjust(3))
print("Pizza".ljust(16,"."),        "$2.00 |".rjust(3))
print("Smoothie".ljust(16,"."),     "$4.50 |".rjust(3))
print("Soda".ljust(16,"."),         "$2.00 |".rjust(3))
print("Water".ljust(16,"."),        "$7.00 |".rjust(3))
print("Milkshake".ljust(16,"."),    "$2.00 |".rjust(3))
print("Sundae".ljust(16,"."),       "$7.00 |".rjust(3))
print("Americano".ljust(16,"."),    "$2.00 |".rjust(3))
print("=====".center(20,"="))
