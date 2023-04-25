from flask_app import app
from flask import render_template

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<color>/<int:num>")
def color(color, num):
    users = ["Matt", "Brittany", "Sam", "Rishad", "Patrick", "Catrina", "Dana"]
    return render_template("index.html", num=num, monkey="Its a chimpanzee", print_this=False, users_list=users, color=color)
