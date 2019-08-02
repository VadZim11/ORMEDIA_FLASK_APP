from flask import Flask
from myconfig import Myconfiguration
app = Flask(__name__)
app.config.from_object(Myconfiguration)