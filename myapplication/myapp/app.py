from flask import Flask
from myconfig import Myconfiguration
from flask_sqlalchemy import SQLAlchemy

from flask_admin import Admin

app = Flask(__name__)
app.config.from_object(Myconfiguration)

db = SQLAlchemy(app)

admin = Admin(app)