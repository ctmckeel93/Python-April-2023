from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import pizza
class Customer():
    db = "pizza_store"
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.pizzas = []
        
    # Added after class. Use for reference!!!
    @classmethod
    def get_all(cls):
        
        query = "SELECT * FROM customers;"
        
        results = connectToMySQL(cls.db).query_db(query)
        all_customers = []
        
        for row in results:
            all_customers.append(cls(row))
        return all_customers    
        
    
    
    # Added after lecture. Use for reference
    @classmethod
    def get_one(cls,data):
        
        query = """SELECT * FROM customers
                    LEFT JOIN pizzas ON 
                    pizzas.customer_id = customers.id
                    WHERE customers.id=%(id)s;"""
                    
        results = connectToMySQL(cls.db).query_db(query,data)
        
        customer = cls(results[0])
        
        for row in results:
            
            pizza_data = {
                "id": row["pizzas.id"],
                "pizza_type": row["pizza_type"],
                "pizza_crust": row["pizza_crust"],
                "pizza_size": row["pizza_size"],
                "pizza_sauce": row["pizza_sauce"],
                "amount_of_toppings": row["amount_of_toppings"],
                "created_at": row["pizzas.created_at"],
                "updated_at": row["pizzas.updated_at"]
            }
            
            customer.pizzas.append(pizza.Pizza(pizza_data)) # Pizza(pizza_data)
            
        return customer