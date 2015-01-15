import base64
import hashlib
from functools import wraps

from flask import request, g
from flask.ext.restful import Resource, abort
from werkzeug.security import check_password_hash

from service import auth
from service.models import User


@auth.verify_password
def verify_pw(username, password):
	user = User.query.filter_by(user_sid=username).first()
	
	if check_password_hash(user.hashed_token, password):
		g.user = user
		return True

	return False   


class ProtectedResource(Resource):
	method_decorators = [auth.login_required] 


	def get(self, *args, **kwargs):
		try:
			data = self._get(*args, **kwargs)
			return data
		except ValueError as e:
			error = {
				'status': 'client error',
				'message': e.message
				}
			return error, 400
		except BaseException as e:
			error = {
				'status': 'server error',
				'message': e.message
				}
		return error, 500



	def post(self, *args, **kwargs):
		try:
			print "Anyone here?"
			data = self._post(*args, **kwargs)
			return data
		except ValueError as e:
			error = {
				'status': 'client error',
				'message': e.message
				}
			return error, 400
		except BaseException as e:
			error = {
				'status': 'server error',
				'message': e.message
				}
		return error, 500



	def delete(self, *args, **kwargs):
		try:
			data = self._delete(*args, **kwargs)
			return data
		except ValueError as e:
			error = {
				'status': 'client error',
				'message': e.message
				}
			return error, 400
		except Exception as e:
			error = {
				'status': 'server error',
				'message': e.message
				}
		return error, 500



