from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.customer import Customer
from flask import flash

# data = {
#     "id": 1,
#     "pizza_type": "Italian",
#     "pizza_crust": "Thin crust"
# }
class Pizza():
    db = "pizza_store"
    def __init__(self, data):
        self.id = data["id"]
        self.pizza_type = data["pizza_type"]
        self.pizza_crust = data["pizza_crust"]
        self.pizza_sauce = data["pizza_sauce"]
        self.pizza_size = data["pizza_size"]
        self.amount_of_toppings = data["amount_of_toppings"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM pizzas;"
        
        results = connectToMySQL(cls.db).query_db(query)
        # print(results)
        pizzas = [] # This will hold all of our instances
        for pizza in results:
            new_pizza = cls(pizza) # Pizza(pizza_dict)
            pizzas.append(new_pizza)
        print(results) # List of dictionaries
        print("-------------------------------------------------------------------------------")
        print(pizzas) # List of clas objects
        return pizzas
    
    @classmethod
    def get_one(cls, data):
        # data = {"id": id_value}
        cust = Customer.get_all()
        query = "SELECT * FROM pizzas WHERE id = %(id)s;"
        
        results = connectToMySQL(cls.db).query_db(query, data)
        new_pizza = cls(results[0]) # [{our pizza}]
        
        return new_pizza
    
    @classmethod
    def create_pizza(cls, data):
        
        query = "INSERT INTO pizzas (pizza_type, pizza_crust, pizza_size, pizza_sauce, amount_of_toppings, customer_id) VALUES (%(pt)s,%(pc)s,%(psz)s,%(ps)s,%(t)s,%(customer_id)s);"
        
        results = connectToMySQL(cls.db).query_db(query, data)
        
        return results
    
    @classmethod 
    def update_pizza(cls, data):
        query = "UPDATE pizzas SET pizza_type=%(pt)s, pizza_crust=%(pc)s, pizza_size=%(psz)s, pizza_sauce=%(ps)s, amount_of_toppings=%(t)s WHERE id=%(id)s;"
        connectToMySQL(cls.db).query_db(query, data)
        
    @classmethod
    def delete_pizza(cls, data):
        query = "DELETE FROM pizzas WHERE id = %(id)s;"
        connectToMySQL(cls.db).query_db(query, data)
        
    @staticmethod
    def is_valid(pizza_dict):
        print("Pizza from controller:", pizza_dict)
        is_valid = True
        
        if len(pizza_dict["pt"]) < 3:
            is_valid = False
            flash("Pizza Type must be at least 3 characters", category="pizza")
        if len(pizza_dict["pc"]) < 3:
            is_valid = False
            flash("Pizza Crust must be at least 3 characters", category="pizza")
        if len(pizza_dict["psz"]) < 2:
            is_valid = False
            flash("Pizza Size must be at least 2 characters", category="pizza")
        if len(pizza_dict["ps"]) < 3:
            is_valid = False
            flash("Pizza Sauce must be at least 3 characters", category="pizza")
        if int(pizza_dict["t"]) < 1:
            print("Not enough toppings!")
            is_valid = False
            flash("Pizza must have at least 1 topping", category="pizza")
        return is_valid
            
        
        