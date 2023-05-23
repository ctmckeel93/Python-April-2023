from flask import Flask, render_template, request, redirect
from card import Card

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dash():
    return render_template("dashboard.html", cards=Card.get_all())

@app.route("/process", methods=["POST"])
def process():
    Card.save(request.form)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)