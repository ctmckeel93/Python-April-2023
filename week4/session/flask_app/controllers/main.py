from flask import render_template, request, url_for, redirect, session
from flask_app import app

@app.route("/")
def index():
    session["logged_in"] = "yes"
    return render_template("index.html")
@app.route("/process" , methods=["GET", "POST"])
def process():
    session["gundam_name"] = request.form["gundam_name"]
    session["model_number"] =request.form["model_number"]
    session["hobbies"] =request.form["hobbies"]
    session["color"] =request.form["color"]
    return redirect(url_for("display"))

@app.route("/display")
def display():
    if "logged_in" in session:
        print("Good to go")
    else:
        session["error"] = "You are not logged in"
        return redirect(url_for("index"))
    return render_template("display.html")

@app.route("/display2")
def display2():
    session.clear()
    return render_template("display.html")

@app.route("/start/<foo>")
def start(foo):
    return redirect(url_for("some_route", bar=foo, stuff="stuff", things="things" ))

@app.route("/route/<bar>/<stuff>/<things>")
def some_route(bar, stuff, things):
    print(stuff)
    print(things)
    return bar
