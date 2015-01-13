from flask import jsonify
from flask.ext.restful import reqparse

from service import db
from service.models import User2Follower
from protected_resource import ProtectedResource

class FollowersList(ProtectedResource):


	def post(self):
		parser = reqparse.RequestParser()

		parser.add_argument('username',
							required=True,
							type=str)

		args = parser.parse_args()

		user = User(username=args['username'])

		db.session.add(user)
		db.session.commit()

		result = {'name': user.username}

		return result, 201