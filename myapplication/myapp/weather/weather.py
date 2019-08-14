from flask import Blueprint, render_template,  request
from .parsing_openweathermap import parsing_wether

weather = Blueprint("weather", __name__, template_folder="templates")

@weather.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        city_name = request.form.get("city_name")
        return render_template("weather/weather.html", text=parsing_wether(city_name), city_name=city_name)
    return render_template("weather/weather.html")