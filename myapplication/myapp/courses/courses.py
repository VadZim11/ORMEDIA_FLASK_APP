from flask import Blueprint, render_template
from .parsing_nbrb_by import get_json


courses = Blueprint("courses", __name__, template_folder="templates")

@courses.route("/")
def index():
    return render_template("courses/courses.html", text=get_json())