import os
import unittest
from base64 import b64encode
import datetime

from flask.ext.testing import TestCase
from flask.ext.fixtures import Fixtures, loaders

from service import app, db
from service.models import User, Tweet



fixtures = Fixtures(app, db)

def auth_headers(user = 'reneighbor'):
    user_sid = ''
    auth_token = ''

    if user == 'reneighbor':
        user_sid = 'USf1ffeba94bf041'
        auth_token = '3c7dbf890b764f23'
    elif user == 'trenton':
        user_sid = 'US3d84e915339442'
        auth_token = 'e38140f35a5848f7'


    return  {
        'Authorization': 'Basic ' + 
        b64encode("{0}:{1}".format(user_sid, auth_token))
    }



class BaseTest(unittest.TestCase):

    def setUp(self):
        app.config.from_object('testing.TestConfig')
        self.app = app.test_client()

        db.create_all()

        fixtures.load_fixtures(
            loaders.load('testing/fixtures/user.json'))
        fixtures.load_fixtures(
            loaders.load('testing/fixtures/broadcaster2_follower.json'))
        fixtures.load_fixtures(
            loaders.load('testing/fixtures/tweet.json'))


        # manually setting date_created; I don't believe 
        # Flask-Fixtures supports setting dates
        renee_tweet = Tweet.query.filter_by(id=1).first()
        renee_tweet.date_created = datetime.date(2015, 1, 1)

        trenton_tweet = Tweet.query.filter_by(id=2).first()
        trenton_tweet.date_created = datetime.date(2015, 1, 2)

        db.session.add(renee_tweet)
        db.session.add(trenton_tweet)
        db.session.commit()



    def tearDown(self): 
        db.session.remove()
        db.drop_all()



    # def test_unauthorized(self):
    #     t = self.app.get(
    #             '/users/testrunner/tweets',
    #             headers= auth_headers("foo"))

    #     assert t._status_code == 401


    # def test_not_found(self):
    #     t = self.app.get(
    #             '/foo',
    #             headers= auth_headers())

    #     assert t._status_code == 404


    # def test_tweets(self):
    #     t = self.app.get(
    #             '/tweets',
    #             headers= auth_headers())

    
    #     response = json.loads(t.data)
    #     assert len(response['tweets']) == 2

    #     contents = ['marco', 'polo']
        
    #     for tweet in response['tweets']:
    #         assert tweet['body'] in contents


    # def test_users_tweets(self):
    #     t = self.app.get(
    #             '/users/testrunner/tweets',
    #             headers= auth_headers())

    #     assert t._status_code == 200
        
    #     response = json.loads(t.data)
    #     assert len(response['tweets']) == 1

    #     assert response['tweets'][0]['body'] == "marco"


    # def test_users_tweets_no_tweets(self):
    #     t = self.app.get(
    #             '/users/follower/tweets',
    #             headers= auth_headers("US00000000000002", "0000000000000002"))

    #     assert t._status_code == 200
        
    #     response = json.loads(t.data)
    #     assert len(response['tweets']) == 0





# if __name__ == '__main__':
#     unittest.main()

