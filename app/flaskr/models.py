from flask_login import UserMixin
from flaskr import db

class User(db.Model, UserMixin):
    def __init__(self):
        id = db.Column(db.Integer, primary_key=True)
        self.firstName = db.Column(db.String(150))
        self.lastName = db.Column(db.String(150))
        self.email = db.Column(db.String(150), unique=True)
        self.password = db.Column(db.String(150))
