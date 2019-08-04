from flask import Blueprint, render_template, request
from .parsing_nbrb_by import parsing_cours, parsing_cours_all

courses = Blueprint("courses", __name__, template_folder="templates")


@courses.route("/", methods=["POST", "GET"])
def index():
    cur_abbreviation = "USD"
    if request.method == "POST":
        cur_abbreviation = request.form.get("cur_abbreviation")
        if cur_abbreviation == "ALL":
            return render_template("courses/courses.html", text=parsing_cours_all())
        return render_template("courses/courses.html", text=parsing_cours(cur_abbreviation))
    return render_template("courses/courses.html")