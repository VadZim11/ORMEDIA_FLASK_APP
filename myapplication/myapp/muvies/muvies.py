from flask import Blueprint, render_template
from .parsing_afisha_tut_by import parsing_afisha

muvies = Blueprint("muvies", __name__, template_folder="templates")

@muvies.route("/")
def index():
    return render_template("muvies/muvies.html", text = parsing_afisha())