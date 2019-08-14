from flask import Flask
from myconfig import Myconfiguration
from movies.movies import movies
from weather.weather import weather
from courses.courses import courses


app = Flask(__name__)
app.config.from_object(Myconfiguration)

app.register_blueprint(movies, url_prefix="/movies")
app.register_blueprint(weather, url_prefix="/weather")
app.register_blueprint(courses, url_prefix="/courses")