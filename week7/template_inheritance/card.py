from mysqlconnection import connectToMySQL

class Card:
    def __init__(self, data):
        self.id = data["id"]
        self.category = data["category"]
        self.price = data["category"]
        self.created_at = data["created_at"]
        
    @classmethod
    def get_all(cls):
        
        query = "SELECT * FROM cards;"
        
        results = connectToMySQL("card_shop").query_db(query)
        all_cards = []
        for row in results:
            all_cards.append(cls(row))
            
        return all_cards

    @classmethod
    def save(cls, data):
        
        query = "INSERT INTO cards (category, price) VALUES (%(category)s, %(price)s)"
        return connectToMySQL("card_shop").query_db(query, data)

    def get_keys(self):
        return vars(self).keys()
        
            