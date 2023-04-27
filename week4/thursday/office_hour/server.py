from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from dog import Dog
app = Flask(__name__)

@app.route("/")
def index():

    dogs = [
        Dog("Buddy", "Golden Retriever", 10, True),
        Dog("Chance", "Pitbull", 6, True),
        Dog("Mila", "Husky", 4, True),
        Dog("Bella", "Yorkie", 2, True),
        Dog("Smoky", "Husky", 15, True),
        Dog("Shadow", "Golden Retriever", 16, True),
        Dog("Buddy", "Golden Retriever", 10, True),
    ]
    return render_template("index.html", dogs=dogs)


if __name__ == "__main__":
    Bootstrap5(app)
    app.run(debug=True)