import unittest
from datetime import datetime
import json
from flask_json import FlaskJSON, jsonify, JsonTestResponse
from app import *

class UserTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        app.response_class = JsonTestResponse
        connection.cursor().execute("CREATE TABLE User")
        logging.disable(logging.CRITICAL)

    def tearDown(self):
        os.close(self.app)
        connection.cursor().execute("DROP TABLE User")

    def test_create(self):

    def test_list(self):

    def test_get(self):

    def test_delete(self):

    def test_update(self):

if __name__ == '__main__':
    unittest.main()
