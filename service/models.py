from passlib.apps import custom_app_context as pwd_context

from service import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime)
    username = db.Column(db.String(64), unique=True)
    user_sid = db.Column(db.String(16), unique=True)
    hashed_token = db.Column(db.String(16), unique=True)
    tweets = db.relationship('Tweet', backref='author')


    def __repr__(self):
        return '<User %r>' % (self.username)



class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date_created = db.Column(db.DateTime)
    body = db.Column(db.String(140))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Tweet %r>' % (self.body)

