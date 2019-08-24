from app import app
from app import db

from movies.movies import movies
from weather.weather import weather
from courses.courses import courses

import view

app.register_blueprint(movies, url_prefix="/movies")
app.register_blueprint(weather, url_prefix="/weather")
app.register_blueprint(courses, url_prefix="/courses")

if __name__ == "__main__":
    app.run()