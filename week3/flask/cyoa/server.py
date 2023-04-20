from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/loner")
def loner():
    return render_template("loner.html")

@app.route("/teamwork")
def teamwork():
    return render_template("teamwork.html")

@app.route("/creature")
def creature():
    return render_template("creature.html")

@app.route("/dragon")
def dragon():
    return render_template("dragon.html")

@app.route("/party")
def party():
    return render_template("party.html")

@app.route("/end")
def end():
    return render_template("end.html")

if __name__ == '__main__':
    app.run(debug=True)