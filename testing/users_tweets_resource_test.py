import os
import sys
sys.path.append('/Users/renee/Projects/personal-projects/Pwitter')
import unittest
from base64 import b64encode
import json
import datetime

from flask.ext.testing import TestCase
from flask.ext.fixtures import Fixtures, loaders

from service import app, db
from service.models import Tweet
from base_resource_test import BaseTest, auth_headers


fixtures = Fixtures(app, db)

class TweetResourceTest(BaseTest):

    def test_view_user_tweets_success(self):
        r = self.app.get(
            '/users/reneighbor/tweets',
            headers=auth_headers('reneighbor'),
        )

        assert r._status_code == 200

        tweets = json.loads(r.data)['tweets']
        assert len(tweets) == 1
     
        assert tweets[0]['username'] == 'reneighbor'
        assert tweets[0]['body'] == 'hello world'
        assert tweets[0]['date_created'] == "Thu, 01 Jan 2015 00:00:00 -0000"


    def test_view_user_tweets_no_user(self):
        r = self.app.get(
            '/users/nobody/tweets',
            headers=auth_headers('reneighbor'),
        )

        assert r._status_code == 400

        response = json.loads(r.data)
        assert response['message'] == "No user nobody"
       

    def test_view_other_user_tweets_success(self):
        r = self.app.get(
            '/users/trenton/tweets',
            headers=auth_headers('reneighbor'),
        )

        assert r._status_code == 200

        tweets = json.loads(r.data)['tweets']
        assert len(tweets) == 1
     
        assert tweets[0]['username'] == 'trenton'
        assert tweets[0]['body'] == 'burning man'
        assert tweets[0]['date_created'] == "Fri, 02 Jan 2015 00:00:00 -0000"


    def test_view_user_tweets_search_success(self):
        r = self.app.get(
            '/users/reneighbor/tweets?query=hello',
            headers=auth_headers('reneighbor'),
        )

        assert r._status_code == 200

        tweets = json.loads(r.data)['tweets']
        assert len(tweets) == 1
     
        assert tweets[0]['username'] == 'reneighbor'
        assert tweets[0]['body'] == 'hello world'
        assert tweets[0]['date_created'] == "Thu, 01 Jan 2015 00:00:00 -0000"
        

    def test_view_user_tweets_search_no_tweets(self):
        r = self.app.get(
            '/users/reneighbor/tweets?search=goodbye',
            headers=auth_headers('reneighbor'),
        )

        assert r._status_code == 200

        tweets = json.loads(r.data)['tweets']
        assert len(tweets) == 0
     


if __name__ == '__main__':
    unittest.main()