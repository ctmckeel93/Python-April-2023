users = []

class User:
    def __init__(self,user):
        self.first_name = user["first_name"]
        self.last_name  = user["last_name"]
        self.email      = user["email"]
        self.password   = user["password"]
        users.append(self)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def display(self):
        print(f"Name - {self.full_name()}")
        print(f"Email - {self.email}")
        print(f"Password - {self.password}\n")
    
    def get_first_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name
    def get_email(self):
        return self.email
    def get_password(self):
        return self.password
    
    def set_first_name(self, val):
        self.first_name = val
    def set_last_name(self, val):
        self.last_name = val
    def set_email(self, val):
        self.email = val
    def set_password(self, val):
        self.password = val

users_list = [
    {
        "first_name": "Colby",
        "last_name": "Calip",
        "email": "ccCalip@mail.com",
        "password": "password123" 
    },
    {
        "first_name": "Mark",
        "last_name": "Wahlberg",
        "email": "markymark@mail.com",
        "password": "password123" 
    },
    {
        "first_name": "Ariana",
        "last_name": "Grande",
        "email": "ririG@mail.com",
        "password": "password123" 
    },
    {
        "first_name": "Kurt",
        "last_name": "Cobain",
        "email": "nirvana@mail.com",
        "password": "password123" 
    },
    {
        "first_name": "Rhianna",
        "last_name": "",
        "email": "rhiaGrande@mail.com",
        "password": "password123" 
    },
    {
        "first_name": "Taylor",
        "last_name": "Swift",
        "email": "SwizzyT@mail.com",
        "password": "password123" 
    }
]

for u in users_list:
    User(u)

print(len(users))
for user in users:
    user.display()