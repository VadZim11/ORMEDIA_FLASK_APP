from password_sql import PASSWORD, HOST, DATABASE, USER

class Myconfiguration(object):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}/{DATABASE}"