import sys
import uuid
import string
import random
from datetime import datetime
from werkzeug.security import generate_password_hash

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from service import db
from service.models import User




def random_uuid(string_length=14):

    random = str(uuid.uuid4())
    random = random.replace("-","")
    
    return random[0:string_length]


def random_string(string_length=16):

    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for i in range(string_length))



if len(sys.argv) <= 1:
	print "Username is required"
	sys.exit()

username = sys.argv[1]

existing_users = User.query.filter_by(
	username=username)

if existing_users.count() > 0:
	print "User with name {} already exists".format(username)
	sys.exit()


sid = 'US' + random_uuid()
auth_token = random_string()
hashed_token = generate_password_hash(auth_token)

user = User(username = username,
			user_sid = sid,
			hashed_token = hashed_token,
			date_created = datetime.now(),
			date_updated = datetime.now())

# creating DB session via Flask
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


db.session.add(user)
db.session.commit()

db.session.close()

print "Created user `{}`:".format(username)
print "curl -u {}:{}".format(sid, auth_token)

