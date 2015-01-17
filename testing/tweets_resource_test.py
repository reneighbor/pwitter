import sys
sys.path.append('/Users/renee/Projects/personal-projects/Pwitter')
import unittest
import requests
from requests.auth import HTTPBasicAuth
from werkzeug.security import generate_password_hash

from flask.ext.testing import TestCase

from service import app, db
from service.models import User
import testing
from testing import testing_client

usersid = "US9888d60335c34"
auth_token = "c6ca447dcd104907"


class PwitterTest():
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def setUp(self):
        db.create_all()

        hashed_token = generate_password_hash(auth_token)

        user = User(user_sid=usersid,
                    username="testrunner",
                    hashed_token=hashed_token)

        db.session.add(user)
        db.session.commit()

    def tearDown(self): 
        db.session.remove()
        db.drop_all()


def test_foo():

    t = testing_client.post(
        'http://127.0.0.1:5000/users/testrunner/tweets', 
        [usersid, auth_token])

    print vars(t)



def main():
    pt = PwitterTest()

    pt.setUp()
    test_foo()


if __name__ == '__main__':
    main()



