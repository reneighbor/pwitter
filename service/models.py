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


class Broadcaster2Follower(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime)
    broadcaster_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    follower_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    status = db.Column(db.Integer)

    def __repr__(self):
        return '<Broadcaster2Follower %r, %r>' % (self.user_id, self.follower_id)


class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date_created = db.Column(db.DateTime)
    body = db.Column(db.String(140))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Tweet %r>' % (self.body)

