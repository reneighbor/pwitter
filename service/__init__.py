from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restful import Api

from flask.ext.httpauth import HTTPBasicAuth


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
api = Api(app)
auth = HTTPBasicAuth()


# Importing resources after SqlAlchemy object is 
# created to avoid circular imports
from resources.users_resource import UsersList
from resources.broadcasters_resource import BroadcastersList, BroadcastersInstance
from resources.followers_resource import FollowersList
from resources.tweets_resource import TweetsList


api.add_resource(UsersList, 
    '/users')

api.add_resource(BroadcastersList, 
    '/users/<string:username>/broadcasters')
api.add_resource(BroadcastersInstance, 
    '/users/<string:username>/broadcasters/<string:broadcaster_name>')

api.add_resource(FollowersList, 
    '/users/<string:username>/followers')

api.add_resource(TweetsList, 
    '/tweets')