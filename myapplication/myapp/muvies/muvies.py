from flask import Blueprint, render_template

muvies = Blueprint("muvies", __name__, template_folder="templates")

@muvies.route("/")
def index():
    return render_template("muvies/muvies.html")