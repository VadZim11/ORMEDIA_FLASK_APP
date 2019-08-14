from flask import Blueprint, render_template
from .parsing_afisha_tut_by import parsing_afisha

movies = Blueprint("movies", __name__, template_folder="templates")

@movies.route("/")
def index():
    return render_template("movies/movies.html", text = parsing_afisha())