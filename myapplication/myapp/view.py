from app import app
from flask import render_template

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contakts")
def contakts():
    return render_template("contakts.html")

@app.errorhandler(404)
def page_error(e):
    return render_template("404.html"), 404