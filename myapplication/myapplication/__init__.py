from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello World<h1>"

@app.route("/movies ")
def movies ():
    return "<h2>This mjvies page<h2>"

@app.route("/courses ")
def courses ():
    return "<h2>This courses page<h2>"

@app.route("/weather")
def weather():
    return "<h2>This weather page<h2>"

if __name__ == "__main__":  
    app.run()