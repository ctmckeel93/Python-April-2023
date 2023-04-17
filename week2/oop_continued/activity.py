# Worldy wacky shop of wonders!!!!

# Together as a group, come up with an idea for a shop that sells anything you want. 
# Think about what a shop might have as attributes, maybe a name, address, list of items etc
# Associate that Shop with another class called Inventory 
# Give the inventory a name and a price.

# Create the items first and then create the Shop and add the items to the shops inventory
# Make a method to loop through the inventory and display the info of each item - think about how you can simplify that code in the class

# Bonus: create a staticmethod to check and make sure in the Item class: the name is not an empty string and the price is greater than 0
# Bonus: Validate the values before creating the Item and print "Not valid" if it fails
# Bonus: Add some more methods together and embrace your creativity!

class Guitar_Store:
    def __init__(self, name, address, inventory):
        self.name = name
        self.address = address
        self.inventory = inventory

    def in_stock(self):
        for item in self.inventory:
            item.display_info()

    def add_to_inventory(self, item):
        self.inventory.append(item)


class Stock:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        print(f"{self.name} - ${round(self.price, 2)}")

    @staticmethod
    def is_valid(item):
        is_valid = True
        if len(item["name"]) < 1:
            is_valid = False
        if item["price"] < 0.01:
            is_valid = False
        return is_valid
    
    @staticmethod
    def validate_items(item_list):
        result = []
        for item in item_list:
            if Stock.is_valid(item):
                new_item = Stock(item["name"], item["price"])
                result.append(new_item)
            else:
                print("Item not valid, instance not created")
        return result



item1 = {
    "name": "6 pack of strings",
    "price": 10.99
}
item2 = {
    "name": "TUNER",
    "price": 9.99
}
item3 = {
    "name": "Pack of picks",
    "price": 2.99
}
item4 = {
    "name": "Small amplifier",
    "price": 199.99
}
item5 = {
    "name": "Schecter C1 Special",
    "price": 399.99
}
item6 = {
    "name": "",
    "price": 0
}

stock_list = Stock.validate_items([item1,item2,item3,item4,item5,item6])

guitar_store = Guitar_Store("Perfect Pitch Guitars", {"street": "123 Main st", "city": "Appleton", "state": "Colorado", "zip": "237890"}, stock_list)

guitar_store.in_stock()
