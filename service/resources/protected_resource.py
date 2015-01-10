from flask.ext.restful import Resource

from service import auth

# @auth.get_password
# def get_pw(username):
	


class ProtectedResource(Resource):
    # method_decorators = [auth.login_required]
    method_decorators = []