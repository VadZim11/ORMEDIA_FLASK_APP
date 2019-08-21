from password_sql import PASSWORD

class Myconfiguration(object):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://root:{PASSWORD}@localhost/my_flask_app"