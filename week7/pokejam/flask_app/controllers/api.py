import requests
from flask_app import app
from flask import jsonify
api_url = "https://pokeapi.co/api/v2/pokemon/"

@app.route("/pokemon")
def get_pokemon():
    response = requests.get(api_url)
    return jsonify(response.json())

@app.route("/pokemon/<name>")
def get_one_pokemon(name):
    print(name)
    response = requests.get(api_url + name)
    return jsonify(response.json())