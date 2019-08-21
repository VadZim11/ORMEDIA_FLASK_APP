from flask import Flask
from myconfig import Myconfiguration
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Myconfiguration)

db = SQLAlchemy(app)