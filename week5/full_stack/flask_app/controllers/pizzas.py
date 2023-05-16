from flask import render_template, request, redirect, url_for
from flask_app import app
from flask_app.models import pizza 
from flask_app.models import customer

@app.route("/")
def index():
    pizza_list = pizza.Pizza.get_all() # getting the return value of a list of class objects from our model
    customers = customer.Customer.get_all()
    return render_template("index.html", pizzas=pizza_list, customer_list=customers)

@app.route("/process", methods=["POST"])
def process():
    data = {
        "pt": request.form["pizza_type"],
        "pc": request.form["pizza_crust"],
        "psz": request.form["pizza_size"],
        "ps": request.form["pizza_sauce"],
        "t": request.form["amount_of_toppings"],
        "customer_id": request.form["customer_id"]
    }
    
    if request.form["which_form"] == "create":
        print("Pizza Data",data)
        if pizza.Pizza.is_valid(data):
            pizza.Pizza.create_pizza(data)
        else:
            print("Data not valid")
            return redirect("/")
    else:
        data = {
            "id": request.form["id"],
            "pt": request.form["pizza_type"],
            "pc": request.form["pizza_crust"],
            "psz": request.form["pizza_size"],
            "ps": request.form["pizza_sauce"],
            "t": request.form["amount_of_toppings"],
            "customer_id": request.form["customer_id"]
        }
        pizza.Pizza.update_pizza(data)
    return redirect(url_for("index"))

@app.route("/pizzas/<int:id>")
def edit_form(id):
    return render_template("edit.html", id=id)

@app.route("/pizzas/delete/<int:id>")
def destroy_pizza(id):
    pizza.Pizza.delete_pizza({"id": id})
    return redirect(url_for("index"))
