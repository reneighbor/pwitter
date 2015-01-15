from datetime import datetime

from flask import g
from flask.ext.restful import reqparse, fields, marshal_with, marshal

from service import db
from service.models import Tweet
from protected_resource import ProtectedResource


fields = {
    'username': fields.String,
    'date_created': fields.DateTime(dt_format='rfc822'),
    'body': fields.String,
}

class UsersTweetsList(ProtectedResource):

    def _get(self, username):
        parser = reqparse.RequestParser()

        parser.add_argument('search')

        args = parser.parse_args()

        tweets = Tweet.query.filter_by(
            user_id = g.user.id
        ).all()


        if len(tweets) == 0:
            return {'tweets': []}

        tweet_results = []

        for tweet in tweets:
            tweet_fields = marshal({
                'username': tweet.username,
                'date_created': tweet.date_created,
                'body': tweet.body
            }, fields)

            tweet_results.append(tweet_fields)

        return {'tweets': tweet_results}


    @marshal_with(fields, envelope='tweet')
    def _post(self, username):

        parser = reqparse.RequestParser()

        parser.add_argument('body',
            required=True)

        args = parser.parse_args()

        tweet = Tweet(
            username = g.user.username,
            user_id = g.user.id,
            date_created = datetime.now(),
            date_updated = datetime.now(),
            body=args['body']
        )

        db.session.add(tweet)
        db.session.commit()

        result = {
            'username': tweet.username,
            'date_created': tweet.date_created,
            'body': tweet.body
        }

        return result, 201
        

