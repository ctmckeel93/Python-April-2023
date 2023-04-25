from flask_app import app
from flask import render_template

@app.route("/<color>")
def index(color):
    users = ["Matt", "Brittany", "Sam", "Rishad", "Patrick", "Catrina", "Dana"]
    return render_template("index.html", monkey="Its a chimpanzee", print_this=False, users_list=users, color=color)
