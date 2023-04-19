from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello"

@app.route("/start")
def start():
    return "Start page"

@app.route("/end")
def end():
    return "This is the end page"

@app.route("/winner")
def winner():
    return "<h1>I am afraid this is game over</h1>"

if __name__ == '__main__':
    app.run(debug=True)