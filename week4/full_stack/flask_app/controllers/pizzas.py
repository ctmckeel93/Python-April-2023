from flask import render_template
from flask_app import app
from flask_app.models.pizza import Pizza

@app.route("/")
def index():
    pizza_list = Pizza.get_all() # getting the return value of a list of class objects from our model
    return render_template("index.html", pizzas=pizza_list)
