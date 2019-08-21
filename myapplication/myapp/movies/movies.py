from flask import Blueprint, render_template
from .parsing_afisha_tut_by import parsing_afisha
from models import Movies
from app import db

movies = Blueprint("movies", __name__, template_folder="templates")

@movies.route("/")
def index():
    
    db.create_all()
    for i in parsing_afisha():
        movi = Movies(name = i["name"], muvi_href = i["muvi_href"], muvi_image = i["muvi_image"])
        db.session.add(movi)
        db.session.commit()

    

    return render_template("movies/movies.html", text = parsing_afisha())