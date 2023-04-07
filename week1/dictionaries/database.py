
def generate_database():

    emails = ["vacim35132@dogemn.com",
            "vpldvnkxshoqnamxmq@tpwlb.com",
            "dawan.rami@findours.com",
            "tidiane.mohamad@findours.com",
            "peterson.khalil@findours.com",
            "young.arne@findours.com",
            "aaran.berkley@findours.com",
            "norman.tryson@findours.com",
            "jeferson.kemal@findours.com",
            "alessandro.alexandro@findours.com"
            ]
    db = [] 

    for i in range(len(emails)):
        db.append({"id": i+1,
                "email": emails[i],
                "address" : {
                    "street": "123 Maple Street",
                    "zip-code": 123456,
                    "apt": "A"
                }
                })
        
    print(db)
    return db

def pretty_db(database):
    for user in database:
        for key in user:
            print(f"{key}: {user[key]}\n")

generate_database()



    
