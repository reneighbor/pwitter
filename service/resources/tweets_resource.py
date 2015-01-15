from flask import request

from protected_resource import ProtectedResource

class TweetsList(ProtectedResource):

    def _get(self):

        print "What is the username? " + request.authorization.username
        user = User.query.filter_by(
            user_sid=request.authorization.username)



        tweets = Tweet.query.filter

        return
