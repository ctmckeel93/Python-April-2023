from flask import render_template, request, redirect, url_for
from flask_app import app
from flask_app.models.pizza import Pizza

@app.route("/")
def index():
    pizza_list = Pizza.get_all() # getting the return value of a list of class objects from our model
    return render_template("index.html", pizzas=pizza_list)

@app.route("/process", methods=["POST"])
def process():
    data = {
        "pt": request.form["pizza_type"],
        "pc": request.form["pizza_crust"],
        "psz": request.form["pizza_size"],
        "ps": request.form["pizza_sauce"],
        "t": request.form["amount_of_toppings"]
    }
    if request.form["which_form"] == "create":
        Pizza.create_pizza(data)
    else:
        data = {
            "id": request.form["id"],
            "pt": request.form["pizza_type"],
            "pc": request.form["pizza_crust"],
            "psz": request.form["pizza_size"],
            "ps": request.form["pizza_sauce"],
            "t": request.form["amount_of_toppings"]
        }
        Pizza.update_pizza(data)
    return redirect(url_for("index"))

@app.route("/pizzas/<int:id>")
def edit_form(id):
    return render_template("edit.html", id=id)

@app.route("/pizzas/delete/<int:id>")
def destroy_pizza(id):
    Pizza.delete_pizza({"id": id})
    return redirect(url_for("index"))
