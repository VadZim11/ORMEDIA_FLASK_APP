from flask import Blueprint, render_template

courses = Blueprint("courses", __name__, template_folder="templates")

@courses.route("/")
def index():
    return render_template("courses/courses.html")