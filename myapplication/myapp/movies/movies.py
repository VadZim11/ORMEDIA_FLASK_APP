from flask import Blueprint, render_template, request
from .parsing_afisha_tut_by import parsing_afisha
from models import Movies
from app import db

movies = Blueprint("movies", __name__, template_folder="templates")

@movies.route("/")
def index():

    page = request.args.get("page")

    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    db.create_all()

    if Movies.query.all()==[]:            
        for i in parsing_afisha():
            movi = Movies(name = i["name"], muvi_href = i["muvi_href"], muvi_image = i["muvi_image"], film_genre = i["film_genre"])
            db.session.add(movi)
            db.session.commit()

        movies = Movies.query
    else:
        movies = Movies.query

    pages = movies.paginate(page=page, per_page=4)

    return render_template("movies/movies.html", movies = movies, pages=pages)