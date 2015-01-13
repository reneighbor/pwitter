import base64
import hashlib
from functools import wraps

from flask import request
from flask.ext.restful import Resource, abort
from werkzeug.security import check_password_hash

from service import auth
from service.models import User


def authenticate(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        if auth_pass(
        	request.authorization.username, request.authorization.password):

            return func(*args, **kwargs)

        abort(401)
    return wrapper


def auth_pass(request_sid, request_token):

    user = User.query.filter_by(user_sid=request_sid).first()
   
    if not user:
    	return False

    if not check_password_hash(user.hashed_token, request_token):
    	return False

    return True


class ProtectedResource(Resource):
    # method_decorators = [authenticate] 
    method_decorators = [] 


    def post(self, *args, **kwargs):
    	try:
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



