import os
import unittest
import json

from flask.ext.testing import TestCase

from service import app, db
from service.models import User
from base_resource_test import BaseTest, auth_headers



class UsersBroadcastersResourceTest(BaseTest):

    def test_view_user_broadcasters(self):
        r = self.app.get(
            '/users/reneighbor/broadcasters',
            headers=auth_headers('reneighbor'),
        )

        assert r._status_code == 200

        broadcasters = json.loads(r.data)['broadcasters']
        assert len(broadcasters) == 1

        assert broadcasters[0]['username'] == 'trenton'


    def test_view_other_user_broadcasters(self):
        r = self.app.get(
            '/users/reneighbor/broadcasters',
            headers=auth_headers('trenton'),
        )

        assert r._status_code == 200

        broadcasters = json.loads(r.data)['broadcasters']
        assert len(broadcasters) == 1

        assert broadcasters[0]['username'] == 'trenton'


    def test_view_user_no_user(self):
        r = self.app.get(
            '/users/nobody/broadcasters',
            headers=auth_headers('reneighbor'),
        )

        assert r._status_code == 400

        response = json.loads(r.data)
        assert response['message'] == "No user nobody"


    def test_view_user_not_following_anyone(self):
        r = self.app.get(
            '/users/trenton/broadcasters',
            headers=auth_headers('trenton'),
        )

        assert r._status_code == 200

        broadcasters = json.loads(r.data)['broadcasters']
        assert len(broadcasters) == 0


    def test_view_user_broadcaster_no_broadcaster(self):
        
        # altering the fixtures
        trenton = User.query.filter_by(
            id = 2).first()

        db.session.delete(trenton)
        db.session.commit()

        r = self.app.get(
            '/users/reneighbor/broadcasters',
            headers=auth_headers('reneighbor'),
        )

        assert r._status_code == 500

        response = json.loads(r.data)
        print response['message']
        assert response['message'] == 'No user exists for broadcaster with ID: 2'


       




if __name__ == '__main__':
    unittest.main()
