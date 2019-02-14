from app import app, db
from datetime import datetime



class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    tweet = db.Column(db.String(140))
    date_posted = db.Column(db.DateTime, default=datetime.now().date())
