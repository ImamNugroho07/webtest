from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    kelamin = db.Column(db.String(15))
    email = db.Column(db.String(100))

class Write(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tulis = db.Column(db.String(1000))
    date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
