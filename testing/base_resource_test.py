import unittest
from flask import Flask, g

import sys
sys.path.append('/Users/renee/Projects/personal-projects/Pwitter')
from service import app
from service.resources.base_resource import verify_pw
from base_test import BaseTest





class BaseResourceTest(BaseTest):

    def test_verify_pw_success(self):

        app = Flask(__name__)
        with app.app_context():

            verified = verify_pw("USf1ffeba94bf041", "3c7dbf890b764f23")
            
            assert verified == True
            assert g.user.username == "reneighbor"







if __name__ == '__main__':
    unittest.main()