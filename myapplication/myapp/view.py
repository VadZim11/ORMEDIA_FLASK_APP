from app import app
from flask import render_template

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contakts")
def contakt():
    return render_template("contakts.html")