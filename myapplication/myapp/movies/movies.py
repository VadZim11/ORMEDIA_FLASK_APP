from flask import Blueprint, render_template, request
from .parsing_afisha_tut_by import parsing_afisha
from models import Movies
from app import db
import datetime

movies = Blueprint("movies", __name__, template_folder="templates")

@movies.route("/", methods=["POST", "GET"])
def index():
    db.create_all()

    if Movies.query.all()==[]:
        for i in parsing_afisha():
            movi = Movies(name = i["name"], muvi_href = i["muvi_href"], muvi_image = i["muvi_image"], film_genre = i["film_genre"])
            db.session.add(movi)
            db.session.commit()
        movies = Movies.query
    else:
        if db.session.query(Movies).filter(Movies.date == datetime.date.today()).first():
            movies = Movies.query
        else:
            for i in parsing_afisha():
                movi = Movies(name = i["name"], muvi_href = i["muvi_href"], muvi_image = i["muvi_image"], film_genre = i["film_genre"])
                db.session.add(movi)
                db.session.commit()
            movies = Movies.query    
    
    if request.method == "POST":        
        date_muvie = request.form.get("date_movie")

        page = request.args.get("page")
        if page and page.isdigit():
            page = int(page)
        else:
            page = 1 
        
        pages = movies.filter(Movies.date == date_muvie).paginate(page=page, per_page=4)

        dates = db.session.query(Movies.date).distinct().all()

        return render_template("movies/movies.html", pages=pages, dates=reversed(dates), date_muvie=date_muvie)
    
    else:
        page = request.args.get("page")
        if page and page.isdigit():
            page = int(page)
        else:
            page = 1 

        date = request.args.get("date")
        dates = db.session.query(Movies.date).distinct().all()
        dates_prev = []
        for i in dates:
            dates_prev.append(str(i.date))
        if date and date in dates_prev:
            date_muvie = date
        else:
            date_muvie =  datetime.date.today()

        pages = movies.filter(Movies.date == date_muvie).paginate(page=page, per_page=4)

        ### add date base
        # for i in movies.all():
        #    print("( \""+i.name+"\", \""+i.muvi_href+"\", \""+i.muvi_image+"\", \""+i.film_genre+"\", \""+str(i.date)+"\"), ")

        return render_template("movies/movies.html", pages=pages, dates=reversed(dates), date_muvie=date_muvie)