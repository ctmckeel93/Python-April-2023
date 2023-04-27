from flask_app.config.mysqlconnection import connectToMySQL

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
        print(results)
        pizzas = [] # This will hold all of our instances
        for pizza in results:
            new_pizza = cls(pizza) # Pizza(pizza_dict)
            pizzas.append(new_pizza)
        print(results) # List of dictionaries
        print("-------------------------------------------------------------------------------")
        print(pizzas) # List of clas objects
        return pizzas
        
        