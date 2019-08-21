from app import db

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    muvi_href = db.Column(db.String(250))
    muvi_image = db.Column(db.String(250))
    
    def __init__(self, *args, **kwargs):
        super(Movies, self).__init__(*args, **kwargs)