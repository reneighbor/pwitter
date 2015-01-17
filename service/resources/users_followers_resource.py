from collections import OrderedDict

from flask import jsonify
from flask.ext.restful import fields, reqparse, marshal_with, marshal

from service import db
from service.models import User, Broadcaster2Follower
from protected_resource import ProtectedResource


fields = {
	'username': fields.String,
	'date_created': fields.DateTime(dt_format='rfc822'),
	'date_followed': fields.DateTime(dt_format='rfc822'),
}

class UsersFollowersList(ProtectedResource):

	def get(self, username):
		user = User.query.filter_by(
			username=username).first()

		if not user:
			raise ValueError("No user found for YOU")


		broadcaster2followers = Broadcaster2Follower.query.filter_by(
			broadcaster_id = user.id).all()

		if len(broadcaster2followers) == 0:
			return {'followers': {}}


		follower_results = []

		for b2f in broadcaster2followers:
			follower = User.query.filter_by(
				id=b2f.follower_id).first()

			if not follower:
				raise Exception("No user exists for user_id {}".format(
					b2f.follower_id))


			follower_result = marshal({
					'username': follower.username,
					'date_followed': b2f.date_created,
				}, fields)

			follower_results.append(follower_result)

		
		return {'followers': follower_results}