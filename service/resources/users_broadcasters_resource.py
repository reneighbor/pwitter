from datetime import datetime

from flask import jsonify, abort
from flask.ext.restful import reqparse, fields, marshal_with, marshal

from service import db
from service.models import User, Broadcaster2Follower
from protected_resource import ProtectedResource


fields = {
    'username': fields.String,
    'date_created': fields.DateTime(dt_format='rfc822'),
    'date_followed': fields.DateTime(dt_format='rfc822'),
}

class UsersBroadcastersList(ProtectedResource):

	def _get(self, username):

		user = User.query.filter_by(
			username=username).first()

		if not user:
			raise ValueError("No user found for YOU")


		broadcaster2followers = Broadcaster2Follower.query.filter_by(
			follower_id=user.id).all()

		if len(broadcaster2followers) == 0:
			return {'broadcasters': []}


		broadcaster_results = []

		for b2f in broadcaster2followers:
			broadcaster = User.query.filter_by(
				id=b2f.broadcaster_id).first()

			if not broadcaster:
				raise Exception("No user exists for user_id {}".format(
					b2f.broadcaster_id))

			broadcaster_result = marshal({
				'username': broadcaster.username,
				'date_followed': b2f.date_created
			}, fields)

			broadcaster_results.append(broadcaster_result)


		return {'broadcasters': broadcaster_results}


	@marshal_with(fields, envelope='broadcaster')
	def _post(self, username):

		parser = reqparse.RequestParser()

		parser.add_argument('username',
			required=True,
			dest='broadcaster_name')

		args = parser.parse_args()

		

		user = User.query.filter_by(
			username=username).first()

		if not user:
			raise ValueError("No user found for YOU")
		

		broadcaster = User.query.filter_by(
			username=args['broadcaster_name']).first()

		if not broadcaster:
			raise ValueError("No user found for '{}'".format(
				args['broadcaster_name']))


		existing_follow = Broadcaster2Follower.query.filter_by(
			broadcaster_id = broadcaster.id,
			follower_id = user.id).first()

		if existing_follow:
			raise ValueError("Already following user {}".format(
				args['broadcaster_name']))



		broadcaster2follower = Broadcaster2Follower(
			broadcaster_id=broadcaster.id,
			follower_id=user.id,
			date_created=datetime.now(),
			date_updated=datetime.now(),
		)

		db.session.add(broadcaster2follower)
		db.session.commit()


		result = {	
			'username': broadcaster.username,
			'date_created': broadcaster.date_created,
			'date_followed': broadcaster2follower.date_created
		}

		return result, 201


class UsersBroadcastersInstance(ProtectedResource):

	@marshal_with(fields, envelope='broadcaster')
	def _delete(self, username, broadcaster_name):
		

		user = User.query.filter_by(
			username=username).first()

		if not user:
			raise ValueError("No user found for YOU")
		

		broadcaster = User.query.filter_by(
			username=broadcaster_name).first()

		if not broadcaster:
			raise ValueError("No user found for '{}'".format(
				args['broadcaster_name']))


		broadcaster2follower = Broadcaster2Follower.query.filter_by(
			broadcaster_id = broadcaster.id,
			follower_id = user.id).first()

		if not broadcaster2follower:
			raise ValueError("Not currently following {}".format(
				args['broadcaster_name']))



		broadcaster2follower.active = False

		db.session.add(broadcaster2follower)
		db.session.commit()


		result = {	
			'username': broadcaster.username,
			'date_created': broadcaster.date_created,
			'date_unfollowed': broadcaster2follower.date_updated
		}

		return result, 204