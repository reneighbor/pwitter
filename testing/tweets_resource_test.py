import os
import unittest
import json

from flask.ext.testing import TestCase

from service import app
from base_resource_test import BaseTest, auth_headers



class TweetResourceTest(BaseTest):

    def test_view_tweets_success(self):
        r = self.app.get(
            '/tweets',
            headers=auth_headers('reneighbor'),
        )

        assert r._status_code == 200

        tweets = json.loads(r.data)['tweets']
        assert len(tweets) == 2

        assert tweets[0]['username'] == 'trenton'
        assert tweets[0]['body'] == 'burning man'
        assert tweets[0]['date_created'] == "Fri, 02 Jan 2015 00:00:00 -0000"

        assert tweets[1]['username'] == 'reneighbor'
        assert tweets[1]['body'] == 'hello world'
        assert tweets[1]['date_created'] == "Thu, 01 Jan 2015 00:00:00 -0000"


    def test_view_tweets_search(self):
        r = self.app.get(
            '/tweets?search=world',
            headers=auth_headers('reneighbor'),
        )

        assert r._status_code == 200

        tweets = json.loads(r.data)['tweets']
        assert len(tweets) == 1

        assert tweets[0]['username'] == 'reneighbor'
        assert tweets[0]['body'] == 'hello world'
        assert tweets[0]['date_created'] == "Thu, 01 Jan 2015 00:00:00 -0000"


    def test_view_tweets_not_following_anyone(self):
        r = self.app.get(
            '/tweets',
            headers=auth_headers('trenton'),
        )

        assert r._status_code == 200

        tweets = json.loads(r.data)['tweets']
        assert len(tweets) == 1

        assert tweets[0]['username'] == 'trenton'
        assert tweets[0]['body'] == 'burning man'
        assert tweets[0]['date_created'] == "Fri, 02 Jan 2015 00:00:00 -0000"

        




if __name__ == '__main__':
    unittest.main()

