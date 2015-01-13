from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from service import db
from service.models import User, Broadcaster2Follower


b2f = Broadcaster2Follower(broadcaster_id=12,
			follower_id=13)

# creating DB session via Flask
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

db.session.add(b2f)
db.session.commit()