from flask.ext.restful import Api, reqparse, fields, marshal

from service import app
from users_resource import UsersList

api = Api(app)

api.add_resource(UsersList, '/users')
