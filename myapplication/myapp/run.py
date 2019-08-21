from app import app, db
import view

from movies.movies import movies
from weather.weather import weather
from courses.courses import courses

app.register_blueprint(movies, url_prefix="/movies")
app.register_blueprint(weather, url_prefix="/weather")
app.register_blueprint(courses, url_prefix="/courses")

if __name__ == "__main__":
    app.run()