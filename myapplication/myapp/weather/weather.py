from flask import Blueprint, render_template

weather = Blueprint("weather", __name__, template_folder="templates")

@weather.route("/")
def index():
    return render_template("weather/weather.html")