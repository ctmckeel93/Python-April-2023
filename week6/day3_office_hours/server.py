from flask import Flask, render_template
app =  Flask(__name__)
app.secret_key = "flubbernuggets"

@app.route("/")
def index():
    fruits = ["apples", "bannanas", "oranges", "cherries", "grapes", "grapefruit"]
    return render_template("index.html", fruits = fruits, check = True)

if __name__ == "__main__":
    app.run(debug=True)