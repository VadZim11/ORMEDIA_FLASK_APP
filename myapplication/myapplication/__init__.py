from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/movies")
def movies ():
    return render_template("movies.html")

@app.route("/courses")
def courses ():
    return render_template("courses.html")

@app.route("/weather")
def weather():
    return render_template("weather.html")

if __name__ == "__main__":
    app.run()