from flask import jsonify
from flask.ext.restful import Resource, reqparse

from service.models import User
from service import db


class UsersList(Resource):

	def get(self):
		users = User.query.all()

		result = {
			'users': []
		}

		for user in users:
			result['users'].append({'name':user.username})

		return jsonify(result)


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