from flask import g
from flask.ext.restful import fields, reqparse, marshal
from sqlalchemy import or_

from service.models import Broadcaster2Follower, Tweet
from protected_resource import ProtectedResource


fields = {
    'username': fields.String,
    'date_created': fields.DateTime(dt_format='rfc822'),
    'body': fields.String,
}

class TweetsList(ProtectedResource):

    def _get(self):
        parser = reqparse.RequestParser()

        parser.add_argument('search')

        args = parser.parse_args()
    

        broadcaster2followers = Broadcaster2Follower.query.filter_by(
            follower_id=g.user.id
        ).all()

        if len(broadcaster2followers) == 0:
            return {'tweets':[]}


        broadcasters = [g.user.id]

        for b2f in broadcaster2followers:
            broadcasters.append(b2f.broadcaster_id)


        if args.get('search'):
            tweets = Tweet.query.filter(or_(
                Tweet.body.like(args['search']),
                Tweet.user_id.in_(broadcasters)
            )).all()
        
        else:
            tweets = Tweet.query.filter_by(
                Tweet.user_id.in_(broadcasters)
            ).all()

        
        tweet_results = []

        for tweet in tweets:
            tweet_result = marshal({
                'username': tweet.username,
                'date_created': tweet.date_created,
                'body': tweet.body
            }, fields)

            tweet_results.append(tweet_result)

        return {'tweets': tweet_results}
        