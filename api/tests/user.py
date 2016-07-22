import unittest
from datetime import datetime
import json
from flask_json import FlaskJSON, jsonify, JsonTestResponse
from app import *

class UserTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        app.response_class = JsonTestResponse
        database.connect()
        # database.creat_tables([User], safe=True)
        cursor = database.curser()
        cursor.execute("CREATE TABLE User")
        logging.disable(logging.CRITICAL)

    def tearDown(self):
        # database.drop_tables([User], safe=True)
        cursor().execute("DROP TABLE IF EXISTS User"
        os.close(self.app)

    def test_create(self):
        self.app.post('/users', data=dict (
            username=username,
            password=password
        ), follow_redirects=True)

    # def test_list(self):
    #
    # def test_get(self):
    #
    # def test_delete(self):
    #
    # def test_update(self):

if __name__ == '__main__':
    unittest.main()
