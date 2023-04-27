from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    Bootstrap5(app)
    app.run(debug=True)