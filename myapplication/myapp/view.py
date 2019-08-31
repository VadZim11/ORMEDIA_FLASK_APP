from app import app
from flask import render_template
import requests
import json

@app.route("/")
def home():
    url = "http://rzhunemogu.ru/RandJSON.aspx?CType=1"
    anekdot = requests.get(url).json(strict=False)["content"]
    return render_template("home.html", anekdot=anekdot)

@app.route("/contakts")
def contakts():
    return render_template("contakts.html")

@app.errorhandler(404)
def page_error(e):
    return render_template("404.html"), 404