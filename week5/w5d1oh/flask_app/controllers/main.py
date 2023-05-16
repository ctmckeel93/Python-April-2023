from flask_app import app
from flask import render_template, request, redirect, url_for
from flask_app.models import resume
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    print(request.form.getlist("languages"))
    data = {
        "name": request.form.get("name"),
        "age": request.form.get("age"),
        "languages": ",".join(request.form.getlist("languages"))
    }
    resume.Resume.create(data)
    return redirect(url_for("home"))

@app.route("/resumes/<int:id>")
def show_one(id):
    print(resume.Resume.get({"id": id})["languages"].split(","))
    return "Hello"