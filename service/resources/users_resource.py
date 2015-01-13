from flask import jsonify
from flask.ext.restful import reqparse

from service import db
from service.models import User
from protected_resource import ProtectedResource

class UsersList(ProtectedResource):

	def get(self):
		users = User.query.all()

		result = {
			'users': []
		}

		for user in users:
			result['users'].append({
				'id':user.id,
				'name':user.username,
				'sid':user.user_sid
				})

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