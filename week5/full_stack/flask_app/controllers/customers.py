from flask_app import app 
from flask import render_template
from flask_app.models import customer

@app.route("/customers/<int:id>")
def show_customers(id):
    customer_from_db = customer.Customer.get_one({"id": id})
    return render_template("customers.html", customer = customer_from_db)