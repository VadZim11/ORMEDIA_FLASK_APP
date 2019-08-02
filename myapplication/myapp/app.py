from flask import Flask
from myconfig import Myconfiguration
from muvies.muvies import muvies
from weather.weather import weather
from courses.courses import courses

app = Flask(__name__)
app.config.from_object(Myconfiguration)

app.register_blueprint(muvies, url_prefix="/muvies")
app.register_blueprint(weather, url_prefix="/weather")
app.register_blueprint(courses, url_prefix="/courses")