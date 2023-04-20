from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success")
def success():
    return "<h1>Success</h1>"

@app.route("/hello/<name>/<stack>")
def say_hello(name, stack):
    return f"Hello {name} Welcome to {stack}"

@app.route("/<int:num>")
def test(num):
    return str(num)

if __name__ == '__main__':
    app.run(debug=True, port=5001)